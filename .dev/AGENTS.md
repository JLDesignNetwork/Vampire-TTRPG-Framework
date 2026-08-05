---
{
    "metadata": {
        "author": "Jeff Langdon",
        "version": "2608.0.0-a",
        "scope": "Vampire TTRPG Framework",
        "location": ".dev/AGENTS.md (gitignored - internal use only)",
        "governed_by": "2608/todo.json"
    }
}
---

# Vampire TTRPG Framework — Agent Rules & Audit Protocol

---

## SECTION 1: Cross-Reference Protocol (Immutable)

### Rule 1.1 — Supplement Audits
When auditing or fixing supplement documents (`2608/supplements/*.md`):
- ALWAYS cross-reference `vampire.md` as the **Source of Truth** before proposing any fix.
- Verify the proposed rule against `vampire.md` to ensure ZERO contradictions.
- Supplements use BOTH internal cross-references (within the supplement) AND external cross-references (to `vampire.md` sections via relative anchor links).
- Supplements MUST NEVER redefine a mechanic already governed by `vampire.md`. Defer and cite instead.
- If `vampire.md` already covers a mechanic (caps, synergy, expenditure, etc.), the supplement must cross-reference it — not duplicate or override it.

### Rule 1.2 — Core Ruleset Audits
When auditing or fixing the core ruleset (`2608/vampire.md`):
- Use ONLY internal cross-references (sections within `vampire.md` itself).
- Do NOT pull rules, data, or definitions from supplement documents back into `vampire.md`.
- `vampire.md` is self-contained and self-authoritative.
- Supplements are downstream consumers of the ruleset. Data flows one way: ruleset → supplements. Never the reverse.

---

## SECTION 2: Audit Workflow (Strict Order — No Skipping Steps)

### Rule 2.1 — Present Before You Fix
NEVER write a fix to any document without first:
1. Presenting the **finding** (what the issue is and why it is a problem).
2. Presenting the **proposed fix** (exact text to be added/changed).
3. Awaiting explicit user approval ("agreed", "approved", "yes", "proceed").

### Rule 2.2 — One TODO at a Time
- Work through TODO tasks sequentially by ID (ascending order).
- Present one fix at a time. Do not batch multiple fixes in a single proposal.
- After writing a fix: mark the TODO as `completed` + `protected`, commit, push — then present the next task.

### Rule 2.3 — Contradiction Check is Mandatory
Before proposing any fix:
- For supplement fixes: search `vampire.md` for the relevant mechanic. Confirm no contradiction exists.
- For ruleset fixes: search the surrounding sections of `vampire.md` for related rules. Confirm internal consistency.
- If a contradiction is discovered during the check, report the finding to the user BEFORE proposing a fix.

### Rule 2.4 — No Assumptions
- Never assume a mechanic is undefined without searching the document first.
- Use `grep_search` against the target document before declaring a gap.
- If a mechanic exists in `vampire.md` under a different name, cross-reference it — do not create a duplicate.

### Rule 2.5 — Mandatory Task Presentation Format
When presenting a TODO task for user review, ALWAYS include all four of the following fields:

```
**Section:** [Document section path the issue lives in]
**Issue:** [Clear explanation of what the problem is and why it matters]
**Severity:** [priority level + type — e.g., 🔴 Critical Exploit / 🟠 High Gap / 🟡 Medium Contradiction]
**Proposed Fix:** [Exact text or rule change to be written into the document]
```

Never present just a fix without context. The user must be able to understand what is being changed and why before approving.

### Rule 2.6 — Mandatory Devil's Advocate & Deep Cross-Reference Comparison
Whenever the user proposes an idea, asks to cross-reference two mechanics, or questions a design choice:
- **ALWAYS play Devil's Advocate:** Stress-test the idea for edge cases, exploits, mechanical redundancy, and complexity overhead.
- **Provide a Comprehensive Comparison:** Clearly contrast the proposed mechanics (e.g. core power vs supplement ritual).
- **Evaluate Structural Options:** Detail the benefits and drawbacks of:
  1. Keeping both mechanics separate with distinct niches.
  2. Deferring/cross-referencing one to the other.
  3. Completely redesigning or replacing the supplement mechanic.

---

## SECTION 3: Version Management Rules

### Rule 3.1 — JLDN Generational Version Schema (GVS)
Authoritative source: `/Volumes/Kingston-256/Documents/Generational Version Schema/2607/gvs.md`

**Format:**
```
[YYMM].[SUBVERSION].[REVISION]-[TAG]
```
- **`[YYMM]`** — Epoch: two-digit year + two-digit zero-padded month of core architecture birth. Only resets on full architectural rewrite.
- **`[SUBVERSION]`** — Incrementing integer: backward-compatible feature additions or architectural expansions.
- **`[REVISION]`** — Incrementing integer: bug fixes, patches, minor adjustments without new functionality.
- **`-[TAG]`** — Compound lifecycle + support status string.

**Validation Regex:**
```regex
^(\d{2}(?:0[1-9]|1[0-2]))\.(\d+)\.(\d+)-(a|as|b|bs|l|s|ts|z)$
```

**Complete Lifecycle Tag Table:**

| Phase | Tag | Meaning & Support Status |
| :--- | :---: | :--- |
| **Alpha (Internal)** | `-a` | **Genesis Build:** First testable build, kept strictly in-house. No external support. |
| **Alpha (Public)** | `-as` | **Genesis Build:** Released for early external/live testing. Actively supported. |
| **Beta (Internal)** | `-b` | **Crucible Build:** Feature complete, focused on bug hunting, kept in-house. No external support. |
| **Beta (Public)** | `-bs` | **Crucible Build:** Released for wider real-world testing. Supported. |
| **Lambda** | `-l` | **The Lock (RC):** Release Candidate. Code freeze active. Under review, no support yet. |
| **Stable** | `-s` | **Production:** Official stable production release. Fully supported. |
| **Theta** | `-ts` | **Twilight:** Deprecation warning. Users encouraged to migrate, but still supported. |
| **Zeta** | `-z` | **Zero-Hour (EOL):** End of Life. Final update ever. Completely unsupported. |

### Rule 3.2 — Version Bump Triggers
- **`[SUBVERSION]` bump** (e.g., `2608.48.0` → `2608.49.0`): Any new content, fix, or registered audit finding.
- **`[TAG]` change** (e.g., `-as` → `-bs`): Lifecycle phase transition (e.g., all audit rounds complete).
- **Supplements**: Versions are independent from the core ruleset version. Supplements may be `-as` while the core ruleset is `-bs`.
- **`2608/todo.json` version** must always reflect the current active working version across the generation.

### Rule 3.3 — Supplement Version Alignment
- All supplement frontmatter version strings must match `2608/todo.json` version at all times.
- If `2608/todo.json` is bumped, all supplement frontmatter and title headers must be updated in the same commit or the following commit.

---

## SECTION 4: Separation of Concerns (SoC) Protocol

### Rule 4.1 — Core Ruleset is the Source of Truth
- `vampire.md` owns all base mechanical definitions: Blood Reserve math, expenditure caps, Age Tier Superiority, Torpor, creation, powers, and damage tracks.
- No supplement may introduce a new base mechanic that changes core math. Supplements may only *apply* or *reference* existing core mechanics in new contexts.

### Rule 4.2 — Supplement Scope
- Supplements expand on specific domains (magic systems, legal codes, equipment) without altering core rules.
- Supplements must include a Mode 2 frontmatter header with `parent_ruleset_file: "../vampire.md"`.
- All supplement mechanics must consume standard Blood Reserves and scale using core Age Tier rules — not invent alternative resource systems.

### Rule 4.3 — No Circular Dependencies
- Supplement A must not reference Supplement B as a governing authority. Supplements may reference each other for narrative context only.
- Mechanical authority always flows: `vampire.md` → supplements.

### Rule 4.4 — The Three Pillars of Bloodline Magic Rituals
All rituals authored or audited in blood magic supplements must adhere strictly to three architectural pillars:
1. **Pillar 1 — Power Amplification:** Rituals amplify, expand, or elevate existing supernatural/behavioral powers beyond their base single-caster limits (e.g. expanding range, scope, duration, or breaking base power restrictions).
2. **Pillar 2 — Dual-Layer Benefits:** Every ritual provides a **singular standalone benefit** that revolves around the amplified power domain. This ensures vampires who do NOT possess the underlying base power still receive a distinct, meaningful mechanical benefit from casting the ritual, while possessors gain a **+2 Power Synergy Bonus**.
3. **Pillar 3 — Mandatory Caps & Boundaries:** Every ritual MUST have defined, explicit caps and limits (Age Tier capacity caps, range boundaries, expenditure caps, duration limits, or target limits) to prevent exploits and infinite stacking loops.

---

## SECTION 5: TODO Dataset Rules (JLDN Todo Schema)

Authoritative source: `/Volumes/Kingston-256/Documents/Todo Schema/2608/todo.md`

### Rule 5.1 — Task Object Required Fields
Every task object MUST include these required fields:

| Field | Type | Rule |
| :--- | :--- | :--- |
| `id` | String | Unique. Format: `TODO-\d{2,4}` or sub-task `TODO-01.1a`. Sequential, never reused. |
| `section` | String | Target document heading path (min 5 chars). e.g. `## Section -> Sub-Section` |
| `title` | String | Short imperative summary (min 5 chars, single line, not vague). |
| `status` | String | Valid lifecycle slug (see State Matrix below). |
| `priority` | String | One of: `critical`, `high`, `medium`, `low`. |
| `details` | String | Comprehensive technical description (min 15 chars, no placeholder text). |
| `existed_since` | String | Exact version string when task was created. Immutable once set. |

Optional fields: `owner`, `reason` (mandatory if `blocked`/`deprecated`), `child_of`, `prerequisite`, `relates_to`, `target_*` metadata keys.

### Rule 5.2 — The 11-State Task Lifecycle Matrix

| Phase | Status Slug | Meaning |
| :--- | :---: | :--- |
| Initial Work | `pending` | Created, drafting not started. |
| | `in-progress` | Initial implementation underway. |
| Surface Review | `pending:review` | Queued for formatting/aesthetic review. |
| | `in-progress:review` | Surface review actively underway. |
| Deep Audit | `pending:audit` | Queued for mechanical/edge-case audit. |
| | `in-progress:audit` | Red Team audit actively underway. |
| Refactor | `pending:refactor` | Flagged for structural cleanup. |
| | `in-progress:refactor` | Active refactoring underway. |
| Terminal | `completed` | Done, verified, locked. Re-opening is prohibited. |
| | `blocked` | Cannot proceed — external dependency or missing decision. |
| | `deprecated` | Cancelled or rendered obsolete. |

**Status Validation Regex:**
```regex
^(pending|in-progress|pending:review|in-progress:review|pending:audit|in-progress:audit|pending:refactor|in-progress:refactor|completed|blocked|deprecated)$
```

### Rule 5.3 — Priority Rank Order
`critical` (Rank 4) > `high` (Rank 3) > `medium` (Rank 2) > `low` (Rank 1)

Priority is **mutable** and MUST be escalated immediately if an audit uncovers critical flaws.

### Rule 5.4 — Protection Field
- `protection` is **only applicable to `completed` tasks**. Do NOT set it on pending or active tasks.
- Valid values: `"protected"` or `"open"` (default if omitted).
- `"protected"`: Locked system element. Any future task that conflicts MUST refactor around it, not alter it.
- `"open"`: Completed but open to future refactoring if architecture requires it.
- Once `"protected"`, the task's `status`, `protection`, and `details` fields are immutable.
- Do NOT re-open a protected task. New work requires a new TODO with a `"child_of"` key.

**Protection Validation Regex:**
```regex
^(protected|open)$
```

### Rule 5.5 — Details Field Tense Rule
- **Pending/active tasks:** `details` describes what needs to be done (imperative/future tense).
- **Completed tasks:** `details` describes what was codified (past tense). Must be precise enough for a future reader to understand what changed without reading the commit diff.

### Rule 5.6 — Trivial vs. Complex Pathway
- **Trivial Fast-Track:** Typos, formatting, date fixes may go directly `in-progress` → `completed`.
- **Complex/Structural:** Rule mechanics, math, schema definitions MUST pass through `pending:audit` or `pending:review` before `completed`.

---

## SECTION 6: Git Commit Conventions

- Commit message format: `Fix TODO-XX: [Short description of what was codified]`
- For audit registration commits: `[PROJ-XX] Red Team Audit: [Document Name] — [N] findings (TODO-XX through TODO-YY) registered`
- For version corrections: `Correct [file(s)] version from [old] to [new] — [reason]`
- Always commit `todo.json` changes in the same commit as the document changes they correspond to.
- Always push to `origin main` immediately after commit.

---

## SECTION 7: Internal Ideas Tracking (.dev/ideas.json)

The `.dev/ideas.json` file tracks raw design concepts, proposed mechanical ideas, and preliminary proposals before they become formal TODO tasks.

### Schema Structure:
```json
{
  "ideas": [
    {
      "id": "IDEA-01",
      "status": "pending",
      "details": "Description of the design idea or mechanical proposal.",
      "resolution": ""
    }
  ]
}
```

### Rules:
- **`id`:** Format `IDEA-\d{1,4}` (sequential, starting at `IDEA-01`).
- **`status`:** Must use standard lifecycle status slugs from JLDN Todo Schema (`pending`, `pending:audit`, `in_progress`, `completed`, `cancelled`, etc.).
- **`details`:** Comprehensive description of the proposed idea or concept.
- **`resolution`:** Updated strictly when `status` reaches `completed` (or `cancelled`). Describes what action was taken regarding the idea (e.g. codified into `vampire.md`, converted to `TODO-XX`, or rejected).


