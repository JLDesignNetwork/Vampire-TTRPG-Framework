---
{
  "metadata": {
    "author": "Jeff Langdon",
    "supplementName": "Bloodline Magic Compendium",
    "targetRuleset": "Vampire TTRPG Framework",
    "version": "2608.49.0-as",
    "parent_ruleset_file": "../vampire.md"
  }
}
---

# Bloodline Magic Compendium v2608.49.0-as
- [Overview & System-Agnostic Adaptation](#overview--system-agnostic-adaptation)
- [Foundational Ritual Mechanics](#foundational-ritual-mechanics)
  - [Ritual Action Economy & Casting Windows](#ritual-action-economy--casting-windows)
  - [Blood Reserve Cost & Sacrificial Upkeep](#blood-reserve-cost--sacrificial-upkeep)
  - [Coven Circle Chants & Age Tier Synergy](#coven-circle-chants--age-tier-synergy)
  - [Ritual Interruption & Backfire Trauma](#ritual-interruption--backfire-trauma)
- [Tier 1 Blood Rituals (Neonate Arcana)](#tier-1-blood-rituals-neonate-arcana)
  - [Sanguine Scrying Mirror](#sanguine-scrying-mirror)
  - [Ritual of the Crimson Ward](#ritual-of-the-crimson-ward)
  - [Vitae Purification Filter](#vitae-purification-filter)
- [Tier 2 Blood Sorcery (Elder Arcana)](#tier-2-blood-sorcery-elder-arcana)
  - [Rhythm of the Ancestral Lineage](#rhythm-of-the-ancestral-lineage)
  - [Hematic Curse of Inertia](#hematic-curse-of-inertia)
  - [Sanguine Transfusion Lock](#sanguine-transfusion-lock)
- [Tier 3 Primordial Rites (Ancient Arcana)](#tier-3-primordial-rites-ancient-arcana)
  - [Grand Rite of Hematic Transmutation](#grand-rite-of-hematic-transmutation)
  - [Eclipse of the Sanguine Tide](#eclipse-of-the-sanguine-tide)
- [Integration & Compatibility](#integration--compatibility)

---

## Overview & System-Agnostic Adaptation

The **Bloodline Magic Compendium** is an official, opt-in supplement for the [Vampire TTRPG Framework](../vampire.md). It expands vampiric blood powers into structured sorcery incantations, sacrificial rituals, and ancestral bloodline rites.

Following [Separation of Concerns](../vampire.md#system-agnostic--multi-genre-framework), this supplement does not alter core ruleset mechanics. All rituals consume standard [Blood Reserves](../vampire.md#blood-reserve-math--expenditure-caps) and scale using [Universal Age Tier Superiority Modifiers](../vampire.md#age-tier-superiority-modifier-system).

### Genre Translation Matrix

| Concept | 🗡️ High Fantasy (*Mytharios*) | 🚀 Sci-Fi / Modern (*The Multiverse*) |
| :--- | :--- | :--- |
| **Sorcery Catalyst** | Runal obsidian chalices, alchemical silver bowls, sacrificial incantation altars | Bio-synthetic blood centrifuges, laser-carved micro-fluidic chips, neural vitae frequency coders |
| **Blood Medium** | Spilled mortal/vampiric blood, consecrated grave soil, ancient scrolls | Oxygenated Synth-Vitae phials, cybernetic transfusion tubes, encrypted genetic bio-code |
| **Scrying Optics** | Obsidian scrying pools, silver-backed blood mirrors, raven eyes | Encrypted bio-comm feeds, thermal satellite overlays, optic cyber-drones |

---

## Foundational Ritual Mechanics

### Ritual Action Economy & Casting Windows
Unlike instantaneous [Activated Powers](../vampire.md#formalized-turn-architecture) cast during combat turns, Blood Rituals are complex incantations requiring extended concentration:
* **Tier 1 Rituals:** Require **1 Minute (10 Combat Rounds)** of continuous chanting and blood tracing.
* **Tier 2 Rituals:** Require **10 Minutes** of unbroken concentration.
* **Tier 3 Primordial Rites:** Require **1 Hour (60 Minutes)** of ritual channeling and coven alignment.

### Blood Reserve Cost & Sacrificial Upkeep
* **Casting Cost:** Rituals expend stored [Blood Reserves](../vampire.md#blood-reserve-math--expenditure-caps) upon initiation (Tier 1 = 1 Reserve; Tier 2 = 2 Reserves; Tier 3 = 3 Reserves).
* **Sacrificial Substitution:** A caster may substitute stored Blood Reserves by draining a living creature during the ritual. Blood source eligibility and potency vary by type:

  | Blood Source | Volume Required per Reserve | Notes |
  | :--- | :--- | :--- |
  | **Living mortal / Thrall** | 250ml | Standard potency. Full living vitae resonance. |
  | **Vampire vitae** | 100ml | Concentrated potency. Donor must consent or be restrained. Counts as partial feeding — subject to Coven feeding laws. |
  | **Living animal blood** | 500ml | Diminished potency. Lacks full sapient vitae resonance. |
  | **Synth-Vitae phials** | 1 full pouch (500ml) | Reduced potency. Lacks living essence; accepted by blood magic but at half efficiency. |
  | **Fresh corpse blood** (< 1 hour post-death) | 500ml | Diminished potency. Vitae resonance fading rapidly. |
  | **Stale corpse blood** (≥ 1 hour post-death) | **Ineligible** | Inert. Blood resonance fully dissipated. Cannot fulfill Sacrificial Substitution. |

### Coven Circle Chants & Age Tier Synergy
* **Coven Circle Bonus:** Each secondary vampire participating in a ritual circle grants a **+1 bonus to Ritual Fortitude checks** and reduces total casting time by **10%** (max 50% reduction). Participant counts, stacking limits, and bonus caps are governed by the [Coven Power Ritual Nexus](../vampire.md#coven-power-ritual-nexus-multi-caster-stacking--sequential-rotation) rules — including Age Tier Caster Caps: Neonate-led circles max at **+2 Fortitude bonus** (3 casters); Elder-led circles max at **+4** (5 casters); Ancient-led circles max at **+6** (7 casters).
* **Age Tier Scaling:** Ritual save DCs and potency scale using [Age Tier Superiority Math ($\Delta$)](../vampire.md#combust-vitae): Neonate = Base DC; Elder = +1 DC / +1 Area; Ancient = +2 DC / Double Duration.

### Ritual Interruption & Backfire Trauma
If a ritual caster suffers physical damage, knockback, or psychic attack during casting:
* **Concentration Test:** The caster MUST pass a **Hard Self-Control check** (DC 15).
* **Backfire Trauma:** On failure, the ritual collapses violently: spent Blood Reserves are lost, and the caster suffers **1 Direct Core Health Damage** from uncontained blood backfire.

---

## Tier 1 Blood Rituals (Neonate Arcana)

### Sanguine Scrying Mirror
* **Cost & Duration:** `1 Reserve | Duration: 10 Minutes Scrying`
* **Mechanic:** The caster pours 1 draft of blood into a silver bowl or dark obsidian pool, whispering the target's true name or gazing upon an object owned by them. The blood surface dissolves into a crystal-clear visual feed of the target's current surroundings within a **5-mile radius**.
* **Counterplay:** Targets possessing [Psychic Fortress](../vampire.md#supernatural-powers) automatically sense the scrying probe and display static.

### Ritual of the Crimson Ward
* **Cost & Duration:** `1 Reserve | Duration: 24 Hours (1 Night)`
* **Mechanic:** The caster paints intricate blood sigils across a doorway, vault, or window frame. Any uninvited mortal or rival vampire attempting to cross the threshold triggers a sudden searing blood burn, inflicting **1 Fire/Thermal Damage** and sounding a psychic alarm to the caster.

### Vitae Purification Filter
* **Cost & Duration:** `1 Reserve | Duration: Instantaneous`
* **Mechanic:** The caster draws a draft of harvested blood through their palms, channeling bloodline purity magic to instantly neutralize alchemical poisons, silver traces, holy water taints, or Reaper virus contagions present in the blood before ingestion.

---

## Tier 2 Blood Sorcery (Elder Arcana)

### Rhythm of the Ancestral Lineage
* **Cost & Duration:** `2 Reserves | Duration: 1 Scene (Communion)`
* **Mechanic:** By burning blood in an ancient bronze censor or bio-centrifuge, the caster opens a telepathic link across the bloodline, communing with the residual echo of their Sire or ancestral Elders. Grants a **+2 bonus to Lore, Strategy, and Arcane Perception checks** for 1 Scene.

### Hematic Curse of Inertia
* **Cost & Duration:** `2 Reserves | Duration: 1 Scene`
* **Mechanic:** Target enemy within line of sight feels their internal blood thicken to cold sludge. The victim's movement speed is halved (**0.5x speed**), and their Initiative is reduced by **-2** for 1 Scene.
* **Resistance:** Target may attempt a **Hard Fortitude check** at the start of each turn to break the curse.

### Sanguine Transfusion Lock
* **Cost & Duration:** `2 Reserves | Duration: Instantaneous (Action Lock)`
* **Mechanic:** Target wounded enemy bleeding exposed vitae has their blood flow violently locked in place mid-stream. Forces the target to drop held weapons and locks their physical limbs for **1 combat round**.

---

## Tier 3 Primordial Rites (Ancient Arcana)

### Grand Rite of Hematic Transmutation
* **Cost & Duration:** `3 Reserves | Duration: 24 Hours (then reverts to water)`
* **Mechanic:** An Ancient caster conducts a 1-hour ritual over a body of water (well, fountain, reservoir). Transmutes up to **1,000 gallons of water into dark, blood-infused vitae**. Rival vampires drinking the liquid regenerate 1 Blood Reserve per gallon (subject to Regeneration Cap below).
* **Thrall Susceptibility (Not Auto-Bond):** Mortals drinking the transmuted water gain the **Susceptibility** condition — a temporary state making them 50% easier to enthrall via a deliberate blood bond feeding act. Drinking transmuted water does **NOT** automatically create a Thrall bond. A vampire must still perform an intentional feeding enthrallment to establish the bond. Standard [Thrall Cap rules](../vampire.md#secrecy-covens-and-thralls) and [Thrall Cap Overage Strain](../vampire.md#secrecy-covens-and-thralls) penalties apply if the caster bonds mortals beyond their cap.
* **Susceptibility Duration:** The Susceptibility condition persists for **24 hours** (aligned with the transmutation window). After the water reverts to its natural state, no new Susceptibility conditions can be granted — but existing Susceptibility conditions on mortals who already drank persist until their 24-hour window expires.
* **Regeneration Cap:** A vampire may not regenerate more Blood Reserves from transmuted water in a single feeding session than their standard per-night Reserve pool cap (see [Blood Reserve Math](../vampire.md#blood-reserve-math--expenditure-caps)). Excess transmuted water beyond that cap yields no further regeneration benefit for that vampire until the following night.
* **Duration Clarification:** The transmutation lasts **24 hours** before all remaining water reverts to its natural state. Any Thrall bonds deliberately established during the window remain in effect after reversion.

### Eclipse of the Sanguine Tide
* **Cost & Duration:** `3 Reserves | Duration: 1 Entire Night`
* **Mechanic:** The Ancient channels an explosive crimson beacon into the night sky. A thick, oppressive crimson fog rolls across a **1-mile radius**.
* **Effects:**
  * Completely blocks moonlight and star guidance.
  * Extends [Daywalker's Grace](../vampire.md#immunities--resistances) timers by **+1 minute** for all allied vampires inside the fog zone.
  * All blood-based powers cast within the eclipse zone receive a **+1 damage/potency bonus**.

---

## Integration & Compatibility

This supplement is 100% compatible with **Vampire TTRPG Framework v2608.48.0-bs**. All ritual rules interact cleanly with [Coven Governance Law](../vampire.md#social), [Torpor Recovery Track](../vampire.md#torpor), and [Age Tier Superiority Mechanics](../vampire.md#age-tier-superiority-modifier-system).
