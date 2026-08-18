# Vampire TTRPG Framework — Game Master & Usage Guide

> **Document:** `docs/usage.md`  
> **Author:** Jeff Langdon (JL Design Network)  

---

## 1. Running Games with the Framework

The **Vampire TTRPG Framework** is designed to drop seamlessly into existing campaign engines.

### Step 1: Establish Resolution Engine
Choose your core resolution mechanic (e.g. d20 roll-over, 2d6 target-number, or d10 dice pool). The ruleset provides standardized DC mappings across all checks:
- **Trivial:** DC 5 / 1 Success
- **Standard:** DC 10 / 2 Successes
- **Challenging:** DC 15 / 3 Successes
- **Heroic:** DC 20 / 4 Successes
- **Supernatural:** DC 25+ / 5+ Successes

### Step 2: Set Starting Generation & Vitae Pool
- **Fledgling:** 10 Vitae max (Expend 1/turn)
- **Ancilla:** 20 Vitae max (Expend 2/turn)
- **Elder:** 40 Vitae max (Expend 4/turn)
- **Methuselah:** 80 Vitae max (Expend 8/turn)

---

## 2. Compiling Rulebooks to PDF

Book layouts are rendered from HTML templates using WeasyPrint or headless browser rendering:

```bash
# Example compilation pipeline
weasyprint books/2608/html/vampire.html books/2608/pdf/vampire.pdf
```
