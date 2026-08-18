# AI Agent & Copilot Development Guidelines

> [!IMPORTANT]
> **Authoritative Rules:** Universal JLDN rules apply. Workspace-specific guidelines:
> - **Local Rules:** `.agents/AGENTS.md`
> - **Generational Hub:** `.dev/` (Active Gen: `2608`)
> - **Source of Truth:** `docs/2608/vampire.md`

## Key Invariants
1. **Mechanical Integrity:** Never alter game balance, statistics, or formulas without explicit user approval.
2. **Generational Backlog:** Keep `.dev/2608/backlog.json` synchronized on every task resolution.
3. **Books Separation:** The Books layer (`books/`) is presentation-only and must never introduce new mechanics.
