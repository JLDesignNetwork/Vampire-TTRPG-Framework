#!/opt/homebrew/bin/python3
import os
import shutil
import subprocess
import sys

# Core configuration
WORKSPACE_DIR = "/Volumes/Kingston-256/Gaming/Vampire-Ruleset"

def get_books_dirs():
    # Dynamic resolution: .books/2608 (staging) or books/2608 (released)
    for root_name in [".books", "books"]:
        gen_dir = os.path.join(WORKSPACE_DIR, root_name, "2608")
        if os.path.isdir(gen_dir):
            html_dir = os.path.join(gen_dir, "html")
            pdf_dir = os.path.join(gen_dir, "pdf")
            os.makedirs(pdf_dir, exist_ok=True)
            return html_dir, pdf_dir
    return None, None

# Hand-authored book HTML files to render to PDF.
BOOKS = [
    "vampire.html",
    "bloodline_magic.html",
    "coven_law_protocols.html",
    "uv_arsenal_handbook.html",
]

def find_pagedjs():
    return shutil.which("pagedjs-cli")

def find_chrome():
    """pagedjs-cli's bundled puppeteer-core expects a specific old Chromium
    revision that `pnpm add -g` won't fetch (global installs skip postinstall
    scripts). `pnpm dlx puppeteer browsers install chrome` instead downloads a
    current Chrome for Testing build under a different path, so point
    PUPPETEER_EXECUTABLE_PATH at whatever build is actually on disk."""
    chrome_root = os.path.expanduser("~/.cache/puppeteer/chrome")
    if not os.path.isdir(chrome_root):
        return None
    for build in sorted(os.listdir(chrome_root), reverse=True):
        candidate = os.path.join(
            chrome_root, build, "chrome-mac-arm64", "Google Chrome for Testing.app",
            "Contents", "MacOS", "Google Chrome for Testing",
        )
        if os.path.exists(candidate):
            return candidate
    return None

def render_pdf(pagedjs_bin, html_dir, pdf_dir, filename):
    input_path = os.path.join(html_dir, filename)
    output_path = os.path.join(pdf_dir, filename.replace(".html", ".pdf"))

    if not os.path.exists(input_path):
        print(f"[-] Error: Input file not found: {input_path}")
        return False

    cmd = [pagedjs_bin, input_path, "-o", output_path]
    print(f"[*] Rendering: {filename} -> {os.path.basename(output_path)}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"[+] Success: Created {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during rendering of {filename}:")
        print(e.stderr.decode("utf-8", errors="ignore"))
        return False

def main():
    os.chdir(WORKSPACE_DIR)

    html_dir, pdf_dir = get_books_dirs()
    if not html_dir:
        print("[-] Error: Books directory not found (.books/2608 or books/2608).")
        sys.exit(1)

    pagedjs_bin = find_pagedjs()
    if not pagedjs_bin:
        print("[-] Error: pagedjs-cli not found. Install it first:")
        print("    pnpm add -g --allow-build=puppeteer pagedjs-cli")
        sys.exit(1)
    print(f"[+] Found pagedjs-cli at: {pagedjs_bin}")

    chrome_bin = find_chrome()
    if not chrome_bin:
        print("[-] Error: No Chrome for Testing build found. Install one first:")
        print("    pnpm dlx puppeteer browsers install chrome")
        sys.exit(1)
    print(f"[+] Found Chrome at: {chrome_bin}")
    os.environ["PUPPETEER_EXECUTABLE_PATH"] = chrome_bin

    success_count = 0
    for filename in BOOKS:
        if render_pdf(pagedjs_bin, html_dir, pdf_dir, filename):
            success_count += 1

    print("\n--- Summary ---")
    print(f"Successfully rendered {success_count}/{len(BOOKS)} PDFs.")
    if success_count != len(BOOKS):
        print("[!] Some renders failed. Check the errors above.")

if __name__ == "__main__":
    main()
