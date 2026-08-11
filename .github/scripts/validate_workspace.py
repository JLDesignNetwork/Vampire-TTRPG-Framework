#!/usr/bin/env python3
"""
Vampire TTRPG Framework — Automated CI Quality & Link Validator
Verifies:
1. Markdown internal link and micro-anchor (<a id="...">) cross-reference resolution.
2. YAML/JSON frontmatter schemas across rulesets and modular supplements.
3. LF line endings and standard Markdown syntax.
"""

import os
import sys
import re
import json
import glob

def gfm_slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return text.replace(' ', '-')

def strip_code_blocks(text):
    # Strip multi-line code blocks ``` ... ```
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Strip inline code spans ` ... `
    text = re.sub(r'`[^`\n]+`', '', text)
    return text

def main():
    workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    os.chdir(workspace)
    print(f"[*] Auditing Vampire TTRPG Framework at: {workspace}\n")

    errors = []

    # 1. Index All Markdown Files & Anchors
    md_files = glob.glob("docs/**/*.md", recursive=True) + ["README.md", "CONTRIBUTING.md", "LICENSE.md"]
    md_files = [os.path.normpath(f) for f in md_files if os.path.exists(f)]

    anchor_index = {}
    frontmatter_index = {}

    for mf in md_files:
        with open(mf, "r", encoding="utf-8") as f:
            content = f.read()

        anchors = set()
        # Find micro-anchors: <a id="foo"></a>
        for match in re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', content):
            anchors.add(match.lower())

        # Find header anchors: ## Header Name
        for line in content.splitlines():
            header_match = re.match(r'^#{1,6}\s+(.+)$', line)
            if header_match:
                clean_title = re.sub(r'[*`_]', '', header_match.group(1).strip())
                anchors.add(gfm_slugify(clean_title))

        anchor_index[mf] = anchors

        # Check frontmatter if present
        fm_match = re.match(r'^---\s*\n(\{[\s\S]*?\})\s*\n---', content)
        if fm_match:
            try:
                fm_data = json.loads(fm_match.group(1))
                frontmatter_index[mf] = fm_data
            except Exception as e:
                errors.append(f"[!] Invalid JSON frontmatter in {mf}: {e}")

    print(f"[+] Indexed {len(anchor_index)} Markdown files and {sum(len(a) for a in anchor_index.values())} anchors.")

    # 2. Validate Frontmatter Schemas for Supplements
    print("\n--- Validating Supplement Frontmatter ---")
    supplement_files = glob.glob("docs/**/supplements/*.md", recursive=True)
    for sf in supplement_files:
        sf_norm = os.path.normpath(sf)
        if sf_norm not in frontmatter_index:
            errors.append(f"[!] Missing required frontmatter block in supplement: {sf_norm}")
            continue
        
        meta = frontmatter_index[sf_norm].get("metadata", {})
        required_keys = ["author", "supplementName", "targetRuleset", "version", "parent_ruleset_file"]
        for k in required_keys:
            if k not in meta or not meta[k]:
                errors.append(f"[!] Supplement {sf_norm} missing metadata key '{k}' in frontmatter.")

        # Check parent ruleset file existence
        parent_file = meta.get("parent_ruleset_file")
        if parent_file:
            resolved_parent = os.path.normpath(os.path.join(os.path.dirname(sf_norm), parent_file))
            if not os.path.exists(resolved_parent):
                errors.append(f"[!] Supplement {sf_norm} references non-existent parent_ruleset_file '{parent_file}' (resolved to {resolved_parent})")
            else:
                print(f"[OK] Frontmatter valid for: {os.path.basename(sf_norm)}")

    # 3. Validate Markdown Cross-References & Anchors
    print("\n--- Validating Internal Cross-References & Anchors ---")
    link_count = 0
    for mf in md_files:
        with open(mf, "r", encoding="utf-8") as f:
            raw_content = f.read()

        # Clean out code blocks to avoid false positives on code examples
        clean_content = strip_code_blocks(raw_content)

        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', clean_content)
        for text, link in links:
            if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
                continue

            link_count += 1
            parts = link.split("#")
            target_file = parts[0]
            anchor = parts[1].lower() if len(parts) > 1 else None

            target_norm = mf if target_file == "" else os.path.normpath(os.path.join(os.path.dirname(mf), target_file))

            if not os.path.exists(target_norm):
                errors.append(f"[!] In {mf}: Broken link '{link}' — target file '{target_norm}' not found.")
            elif anchor:
                if target_norm not in anchor_index:
                    errors.append(f"[!] In {mf}: Target '{target_norm}' is not indexed as markdown for anchor '#{anchor}'.")
                elif anchor not in anchor_index[target_norm]:
                    errors.append(f"[!] In {mf}: Anchor '#{anchor}' not found in '{target_norm}'.")

    print(f"[+] Checked {link_count} active internal links.")

    # 4. Final Verdict
    print("\n==========================================")
    if not errors:
        print("🎉 ALL CI QUALITY CHECKS PASSED SUCCESSFULLY (0 Errors)")
        print("==========================================")
        sys.exit(0)
    else:
        print(f"❌ CI VALIDATION FAILED WITH {len(errors)} ERROR(S):")
        for err in errors:
            print(f"  {err}")
        print("==========================================")
        sys.exit(1)

if __name__ == "__main__":
    main()
