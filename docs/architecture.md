# Vampire TTRPG Framework — Ruleset Architecture & Mechanics Topology

> **Document:** `docs/architecture.md`  
> **Author:** Jeff Langdon (JL Design Network)  
> **Generation:** `2608`  

---

## 1. The 8-Chapter Source of Truth Structure

The core ruleset (`docs/2608/vampire.md`) is structured into eight distinct canonical chapters:

1. **Chapter 1: The Curse & The Blood** — Fundamental nature of vampirism, Vitae pools, generation tiers, and metabolic baseline.
2. **Chapter 2: Hunger, Feeding & Starvation** — Vitae consumption, hunting dynamics, feeding vessels, blood potency, and progressive starvation stages.
3. **Chapter 3: Physical Physiology & Supernatural Traits** — Accelerated healing, supernatural resilience, sensory enhancement, sunlight vulnerability, and thermal inversion.
4. **Chapter 4: The Frenzy & Humanity** — The Beast Within, panic/rage frenzy triggers, moral tethering, and degenerate deterioration.
5. **Chapter 5: Torpor & Immortality** — Unconsciousness, stake paralysis, centuries-long slumber, and resurrection rituals.
6. **Chapter 6: Bloodline Hierarchies & Powers** — Ancestral archetypes, innate disciplines, power tier trees, and master abilities.
7. **Chapter 7: Social Structures & Coven Law** — Elder dominion, territory claim rites, blood bonding, and diplomatic protocols.
8. **Chapter 8: Multi-Genre Adaptation** — Cross-genre scaling rules for High Fantasy, Dark Age Gothic, Cyberpunk/Sci-Fi, and Modern Horror.

---

## 2. Ruleset Supplements Layer (`docs/2608/supplements/`)

- **Bloodline Magic (`bloodline_magic.md`):** Sorcerous disciplines, Thaumaturgical blood rites, and sacrificial alchemy.
- **Coven Law & Protocols (`coven_law_protocols.md`):** Feudal vampire law, trial by combat, and sovereign court proceedings.
- **Modern & Sci-Fi UV Arsenal (`uv_arsenal_handbook.md`):** Directed UV light weaponry, silver nitrate munitions, synth-vitae formulas, and battery-powered combat exosuits.

---

## 3. Books & Compilation Pipeline

Rules and mechanics in `docs/` are translated into book layouts via the Books Layer (`books/` or `.books/`):
- HTML master templates: `books/2608/html/`
- Rendered PDF rulebooks: `books/2608/pdf/`
- Shared CSS and vector graphics: `books/2608/assets/`
