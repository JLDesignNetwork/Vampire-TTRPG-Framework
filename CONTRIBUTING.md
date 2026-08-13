# Contributing to the Vampire TTRPG Framework

Thank you for your interest in contributing to the **Vampire TTRPG Framework**! We welcome community contributions, balance stress-testing, bug reports, and new modular supplements.

This document outlines the architecture, standards, and submission guidelines for contributing to this repository.

---

## 1. Guiding Philosophy & Architecture

The Vampire TTRPG Framework is engineered around two non-negotiable principles:

1. **System-Agnostic Adaptation:** The core ruleset is designed to function across multiple genres (high fantasy, urban fantasy, modern horror, cyberpunk/sci-fi) without altering core mathematical equations.
2. **Separation of Concerns (SoC):**
   * **Core Ruleset (`docs/[GEN]/vampire.md`):** The authoritative Source of Truth for base math (Blood Reserves, Age Tier Superiority, Torpor, Action Economy, Disciplines). **Protected from setting-specific lore or ad-hoc rule mutations.**
   * **Modular Supplements (`docs/[GEN]/supplements/*.md`):** Opt-in, downstream expansions (e.g., Blood Sorcery, Coven Judicial Protocols, Tactical Gear). All custom powers, rituals, weapons, and campaign-specific variants belong in supplements.

---

## 2. Contribution Pathways

We accept four primary types of contributions via GitHub:

### Pathway A: Mechanical Bug & Contradiction Reports
* **How to Submit:** Open a [GitHub Issue](https://github.com/JLDesignNetwork/Vampire-TTRPG-Framework/issues).
* **Scope:** Unintended action economy exploits, mathematical loopholes, contradictory wording between rules, or broken anchor links.
* **Format:** Clearly cite the document, section header, the specific mechanical loophole, and a suggested fix.

### Pathway B: Core Balance & Errata Fixes
* **How to Submit:** Open a [Pull Request (PR)](https://github.com/JLDesignNetwork/Vampire-TTRPG-Framework/pulls).
* **Scope:** Typo corrections, clarity refactors, and minor balance tunings to `vampire.md` or `terminology.md`.
* **Requirement:** Must not break existing Blood Reserve expenditure caps or Age Tier Superiority tables.

### Pathway C: New Modular Supplements
* **How to Submit:** Open a [Pull Request (PR)](https://github.com/JLDesignNetwork/Vampire-TTRPG-Framework/pulls) adding a new `.md` file to `docs/[GEN]/supplements/` (e.g., `docs/2608/supplements/blood_alchemy_potions.md`).
* **Requirements:**
  * Must include the mandatory frontmatter schema (see Section 3 below).
  * Must consume standard Blood Reserves and respect core expenditure caps.
  * Must never redefine or override core rules from `vampire.md`.

### Pathway D: Blood Magic Ritual Contributions
If authoring new blood rituals for `bloodline_magic.md` or a custom magic supplement, rituals **must strictly obey the Three Pillars of Blood Sorcery**:
1. **Pillar 1 (Amplification):** Must elevate an existing discipline power beyond base single-caster limits.
2. **Pillar 2 (Dual-Layer Benefit):** Must provide a unique secondary utility centered on that power domain.
3. **Pillar 3 (Mandatory Caps):** Must include explicit numerical bounds, duration limits, and action economy costs.

---

## 3. Mandatory Editorial & Formatting Standards

All pull requests must adhere to the following technical formatting rules:

### A. Markdown Standards
* Use standard **GitHub Flavored Markdown (GFM)**.
* Format data tables cleanly using standard markdown table syntax (`| Header | Header |`).
* Ensure all files use **LF (Unix)** line endings (enforced by `.gitattributes`).

### B. Frontmatter Schema for Supplements
Every supplement file must begin with a standardized JSON frontmatter block:

```markdown
---
{
  "metadata": {
    "author": "Your Name or Handle",
    "supplementName": "Descriptive Supplement Title",
    "targetRuleset": "Vampire TTRPG Framework",
    "version": "2608.64.0-bs",
    "parent_ruleset_file": "../vampire.md"
  }
}
---
```

### C. Direct Line-Level Micro-Anchoring
To enable precise, deep cross-referencing without polluting PDF bookmark drawers or altering visual styling, every new power, ritual, item, or protocol **must include an invisible HTML micro-anchor** directly above or alongside its heading/bullet:

```markdown
* <a id="custom-power-name"></a>**Custom Power Name [Cost: 2 BP]:** Description of the power...
```
Cross-references should point directly to these anchors: `[Custom Power Name](docs/2608/supplements/my_supplement.md#custom-power-name)`.

### D. JLDN Generational Versioning Schema (GVS)
All ruleset documents, supplements, and metadata adhere to the **[JLDN Generational Versioning Schema](https://github.com/JLDesignNetwork/Generational-Versioning-Schema)**:
* **Version Format:** `[YYMM].[SUBVERSION].[REVISION]-[TAG]` (e.g., `2608.64.0-bs`).
* **Generation Epoch (`[GEN]`):** Represents the major architectural edition / release era (e.g., `2608` for August 2026).
* **Active Directory Alignment:** All new supplements must be placed within the active generation directory (`docs/2608/supplements/`) and match the active generation version tag (`2608.64.0-bs`) in their frontmatter.

---

## 4. Pull Request & Review Workflow

Every pull request submitted to this repository undergoes a formal **Red Team Audit** prior to merging:

1. **Fork & Branch:** Create a fork of the repository and branch from `main` (e.g., `feature/blood-alchemy` or `fix/feeding-clarity`).
2. **Commit Hygiene:** Keep commits atomic with descriptive messages:
   * `Fix DOCS-TODO-XX: Clarify Daywalker's Grace sunlight immunity duration`
   * `feat: add Blood Alchemy & Toxins supplement`
3. **Automated Audit Review:** The repository maintainer and AI review agents will audit your PR for:
   * Mechanical game-balance and exploit potential.
   * Internal anchor cross-reference validity.
   * GFM markdown rendering and table formatting.
4. **Resolution:** You may receive feedback requesting minor adjustments before the maintainer approves and merges your PR into `main`.

---

## 5. Licensing & Copyright

By submitting a Pull Request or contributing material to the Vampire TTRPG Framework repository, you agree that your contributions will be licensed under the terms of the project's [LICENSE.md](LICENSE.md).

You retain moral attribution for your original contributions, while granting Jeff Langdon and JL Design Network the non-exclusive, worldwide, royalty-free license to publish, adapt, balance, and distribute your contribution as part of the official Vampire TTRPG Framework and its compiled publications.
