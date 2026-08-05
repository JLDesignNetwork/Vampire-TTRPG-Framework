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
* **No Pause & Resume:** Blood rituals require continuous, unbroken channeling of vitae. A ritual **cannot be paused and resumed** under any circumstances.
* **Voluntary Cancellation (50% Refund):** If a caster voluntarily aborts a ritual prior to completion, **50% of the spent Blood Reserves are forfeited** (dissipated into ambient space), while the remaining 50% are retained in the caster's reservoir. Restarting an aborted ritual requires starting a fresh full-duration casting and paying the full Blood Reserve cost.

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
* **Coven Circle Timing & Upkeep:** Coven Circle Chants require a 1-minute pre-ritual alignment phase to establish the circle. Assisting secondary casters **must remain inside the circle and continue chanting throughout the entire casting window** to sustain circle bonuses. If a secondary member moves away or is disrupted, their contribution immediately ends.
* **Circle Ritual Bonuses:** Each secondary vampire in the circle grants:
  * **Casting Time Reduction:** -10% casting time per secondary member (max 50% reduction).
  * **Concentration Shielding:** +1 bonus per secondary member to the Lead Caster's [Concentration tests](#ritual-interruption--backfire-trauma) if disturbed during casting.
  * **DC / Potency Stacking:** +1 Coven Stacking Bonus per secondary member to the ritual's save DC or spell check (governed by [Coven Power Ritual Nexus](../vampire.md#coven-power-ritual-nexus-multi-caster-stacking--sequential-rotation)).
* **Lead Caster Tier Requirements:** Secondary casters of any Age Tier may assist in any circle, but the Lead Caster initiating the ritual MUST meet the minimum Age Tier requirement for the arcana tier:
  * **Tier 1 Neonate Arcana:** Lead Caster must be **Neonate (<500 yrs) or higher**.
  * **Tier 2 Elder Arcana:** Lead Caster MUST be an **Elder (500–1,199 yrs)** or Ancient.
  * **Tier 3 Primordial Rites:** Lead Caster MUST be an **Ancient (1,200+ yrs)**.
* **Age Tier Scaling:** Ritual save DCs and potency scale using [Age Tier Superiority Math ($\Delta$)](../vampire.md#combust-vitae): Neonate = Base DC; Elder = +1 DC / +1 Area; Ancient = +2 DC / Double Duration.

### Ritual Interruption & Backfire Trauma
If a ritual caster suffers physical damage, knockback, or psychic attack during casting:
* **Concentration Test:** The caster MUST pass a **Self-Control check** with difficulty scaled by Age Tier:
  * **Neonate (< 500 yrs):** DC 15 (Hard)
  * **Elder (500–1,199 yrs):** DC 12 (Medium)
  * **Ancient (1,200+ yrs):** DC 9 (Easy)
* **Backfire Trauma:** On failure, the ritual collapses violently: spent Blood Reserves are lost, and the caster suffers **1 Direct Core Health Damage** from uncontained blood backfire.

---

## Tier 1 Blood Rituals (Neonate Arcana)

### Sanguine Scrying Mirror
* **Cost & Duration:** `1 Reserve | Duration: 10 Minutes Scrying`
* **Pillar 1 (Power Amplification):** Amplifies sensory powers ([*Thermal Vitae Vision*](../vampire.md#sensory), [*Crimson Scent*](../vampire.md#sensory)). By pouring blood into a silver bowl or obsidian pool, the caster projects their physical/vitae senses into a remote scrying feed.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** The blood surface dissolves into a crystal-clear visual feed of the target's current surroundings for 10 minutes.
  * **Power Synergy Bonus:** Casters who natively possess sensory powers ([*Thermal Vitae Vision*](../vampire.md#sensory), [*Crimson Scent*](../vampire.md#sensory), or [*EM Shroud Gaze*](../vampire.md#sensory)) receive a **+2 Power Synergy Bonus** to all Bloodline Duel checks during scrying probes.
* **Pillar 3 (Defined Caps & Age Tier Range Scaling):** The maximum scrying radius measured from the caster's physical location scales by Age Tier:
  * **Neonate Caster (< 500 yrs):** 5-Mile Radius
  * **Elder Caster (500–1,199 yrs):** 15-Mile Radius
  * **Ancient Caster (1,200+ yrs):** 50-Mile Radius
* **Caster Trance State:** Maintaining the 10-minute scrying feed requires focused concentration. The caster may converse normally and hear their immediate physical surroundings, but moving more than 5 feet away from the bowl or taking combat/defensive actions immediately breaks concentration and ends the scrying feed.
* **Bloodline Duel Counterplay:** When targeting a vampire possessing mental defenses or a rival blood magic caster, an immediate **Bloodline Duel** (contested Self-Control check) is triggered between the scrying caster and the target:
  * **Age Tier Scaling ($\Delta$):** Participants gain **+1 to their contested check per Age Tier difference** above their opponent (Elder vs Neonate = +1; Ancient vs Neonate = +2).
  * **Caster Victory:** The probe pierces the defense and establishes the 10-minute visual feed, but the target senses the breach.
  * **Defender Victory:** The blood pool clouds with static, blocking the vision. The defender senses the probe and receives a psychic trace of the caster's general cardinal direction.
  * **Tie:** The vision is blocked by static, but neither party acquires a psychic trace.

### Ritual of the Crimson Ward
* **Cost & Duration:** `1 Reserve | Duration: 24 Hours (1 Night)`
* **Pillar 1 (Power Amplification):** Amplifies protection and repulsion powers ([*Sacred Repulsion Aura*](../vampire.md#banes--weaknesses), [*Dermal Armor*](../vampire.md#immunities--resistances)), projecting bloodline defensive tethers onto physical architectural entryways.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** The caster paints blood sigils across a threshold. Any uninvited mortal or rival vampire attempting to cross the threshold triggers a sudden searing blood burn, inflicting **1 Fire/Thermal Damage** and sounding a psychic alarm to the caster.
  * **Power Synergy Bonus:** Casters who natively possess protection or defensive powers ([*Dermal Armor*](../vampire.md#immunities--resistances) or [*Thermal Insulation*](../vampire.md#immunities--resistances)) receive a **+2 Power Synergy Bonus** to the ward's blood burn damage (inflicting **3 Fire/Thermal Damage** total).
* **Pillar 3 (Defined Caps & Age Tier Boundary Caps):** The maximum number of physical thresholds warded in a single casting scales by Age Tier:
  * **Neonate Caster (< 500 yrs):** 1 Threshold max (single doorway or window frame)
  * **Elder Caster (500–1,199 yrs):** Up to 3 Thresholds max within the same haven
  * **Ancient Caster (1,200+ yrs):** Up to 7 Thresholds max within the same haven
* **Invitation Protocol:** The caster is always permanently self-invited to their own warded threshold. Additional guests may be verbally designated as invited at any time during the ward's active 24-hour duration. Invitations are revoked by the caster's explicit verbal or written decree, or automatically upon the caster's entry into Torpor or True Death. **Exile Edge-Case:** A Coven Council exile ruling does not override the caster's personal invitation authority over their own private haven ward — however, a Coven-sanctioned forced entry override may be requested as a formal Tribunal dispensation (see [Coven Law Court Protocols](./coven_law_protocols.md)).

### Vitae Purification Filter
* **Cost & Duration:** `1 Reserve (Pre-Ingestion) / 2 Reserves (Emergency Post-Ingestion Purge) | Duration: Instantaneous`
* **Pillar 1 (Power Amplification):** Amplifies internal blood control powers ([*Necrotic Vitae*](../vampire.md#supernatural-powers), [*Grand Harmonization of Vitae*](../vampire.md#supernatural-powers)), projecting biological blood purity magic onto external or ingested blood.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** Drawing a draft (~250ml) of harvested blood through palms instantly neutralizes all alchemical poisons, holy water taints, synthetic neurotoxins, or [Reaper virus contagions](../vampire.md#mutations) present in that draft for 1 Reserve.
  * **Power Synergy Bonus:** Casters who natively possess blood control powers ([*Necrotic Vitae*](../vampire.md#supernatural-powers) or [*Grand Harmonization of Vitae*](../vampire.md#supernatural-powers)) receive a **+2 Power Synergy Bonus** to all [Fortitude/Constitution checks](../vampire.md#creation) against lingering systemic toxins or contagions.
* **Pillar 3 (Defined Caps & Boundaries):**
  * **Volume Cap:** Pre-ingestion purification is capped at **1 draft (~250ml) per casting**.
  * **Emergency Purge Cap:** Emergency post-ingestion purge (2 Reserves) must occur within **60 seconds** of ingestion and is capped at **max 1 Emergency Purge per Scene**.
*(Note: Silver is omitted as it poses no supernatural toxicity to vampires; see [Silver (Mythic Misconception)](../vampire.md#banes--weaknesses).)*

---

## Tier 2 Blood Sorcery (Elder Arcana)

### Rhythm of the Ancestral Lineage
* **Cost & Duration:** `2 Reserves | Duration: 1 Scene (Communion)`
* **Power Amplification:** Amplifies [Bloodline Memory](../vampire.md#behavioral-powers). By burning blood in an ancient censer or bio-centrifuge, the caster breaks the core *Historical Scope Lock* of *Bloodline Memory*, opening a **live real-time telepathic communion feed** across the blood tether between Sire and progeny.
* **Standalone Benefit (All Casters):** Burning the blood censer grants a **+2 bonus to Cognition, Perception, and Historical Lore checks** for 1 Scene to the caster and all allied bloodline members in the room (whether they possess *Bloodline Memory* or not).
* **Power Synergy Bonus:** Casters who natively possess [Bloodline Memory](../vampire.md#behavioral-powers) receive a **+2 Power Synergy Bonus** to all Bloodline Duel checks during live communion.
* **Age Tier Progeny Capacity Cap:** The number of bloodline progeny a Sire can monitor simultaneously in a single casting scales by Age Tier: Neonate Caster = **1 Target max**; Elder Caster = **Up to 3 Progeny max**; Ancient Caster = **Up to 7 Progeny max**.
* **Bloodline Duel & Detection Limits:** The caster rolls **1 Bloodline Duel check** against target(s):
  * **Sire Probing Downward:** Progeny do not automatically notice the probe — requires a **Perception check (DC 14)** to detect. Detected progeny roll Self-Control against the caster's result to sever their link.
  * **Progeny Probing Upward:** Higher-tier ancestors **automatically detect** the probe instantly. If the ancestor wins the Bloodline Duel, they sever the link, inflict **1 Direct Core Health Damage** (psychic feedback) on the caster, and collapse the ritual.
* **Torpor/Deceased Cap:** Probing a Sire or progeny in Torpor or True Death hard-caps back to baseline past memories only, adhering strictly to [Bloodline Memory](../vampire.md#behavioral-powers) scope.

### Hematic Curse of Inertia
* **Cost & Duration:** `2 Reserves | Duration: 1 Scene`
* **Pillar 1 (Power Amplification):** Amplifies thermal and slowing powers ([*Grave Chill*](../vampire.md#supernatural-powers)), projecting cryogenic blood thickening magic into an enemy's circulatory system.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** Target enemy within line of sight has their blood thickened to cold sludge. Movement speed is halved (**0.5x speed**), and Initiative is reduced by **-2** for 1 Scene. Target may attempt a **Hard Fortitude check** at the start of each turn to break the curse.
  * **Power Synergy Bonus:** Casters who natively possess cold/thermal powers ([*Grave Chill*](../vampire.md#supernatural-powers)) receive a **+2 Power Synergy Bonus** to the curse's Fortitude resistance DC.
* **Pillar 3 (Defined Caps & Age Tier Target Caps):** The maximum number of targets cursed in a single casting scales by Age Tier:
  * **Neonate Caster (< 500 yrs):** 1 Target max
  * **Elder Caster (500–1,199 yrs):** Up to 2 Targets max within line of sight
  * **Ancient Caster (1,200+ yrs):** Up to 3 Targets max within line of sight
* **Caster Dependence & Early Termination:** The curse requires ongoing metaphysical tethering. If the caster is incapacitated, knocked unconscious, plunged into Torpor, or perishes, the curse immediately collapses and all targets' speed and Initiative are restored.

### Sanguine Transfusion Lock
* **Cost & Duration:** `2 Reserves | Duration: 1 Combat Round (Action Lock)`
* **Pillar 1 (Power Amplification):** Amplifies blood-arresting and kinetic powers ([*Instant Cardiac Lock*](../vampire.md#torpor), [*Kinetic Blast*](../vampire.md#supernatural-powers)), manipulating exposed external blood flow to freeze an enemy's motor nervous system.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** Target wounded enemy bleeding exposed vitae has their blood flow violently locked in place. Forces target to drop held weapons and locks physical limbs for **1 combat round**.
  * **Power Synergy Bonus:** Casters who natively possess blood control powers ([*Instant Cardiac Lock*](../vampire.md#torpor) or [*Necrotic Vitae*](../vampire.md#supernatural-powers)) receive a **+2 Power Synergy Bonus** to the lock check / Fortitude resistance DC.
* **Pillar 3 (Defined Caps & Stunlock Immunity Cap):**
  * **Physical Lock Scope:** While locked, the target cannot perform physical movement, attacks, or gesture-based casting, but retains full consciousness and may speak or invoke purely mental/telepathic powers ([*Mind Tear*](../vampire.md#behavioral-powers)).
  * **Stunlock Immunity Cap:** A target affected by Transfusion Lock gains temporary vascular immunity and **cannot be targeted by Sanguine Transfusion Lock again for the remainder of the Scene** (preventing continuous stunlock loops).

---

## Tier 3 Primordial Rites (Ancient Arcana)

### Grand Rite of Hematic Transmutation
* **Cost & Duration:** `3 Reserves | Duration: 24 Hours (then reverts to water)`
* **Pillar 1 (Power Amplification):** Amplifies alchemical blood powers ([*Necrotic Vitae*](../vampire.md#supernatural-powers), [*Grand Harmonization of Vitae*](../vampire.md#supernatural-powers)), projecting biological transmutation magic across macro environmental water reservoirs.
* **Pillar 2 (Dual-Layer Benefits & Synergy):**
  * **Standalone Benefit (All Casters):** Conducts a 1-hour ritual over a body of water (well, fountain, reservoir), transmuting up to **1,000 gallons into dark, blood-infused vitae**. Vampires drinking it regenerate 1 Reserve per gallon (subject to Regeneration Cap). Mortals drinking it gain the **Susceptibility** condition (50% easier to enthrall for 24 hours).
  * **Power Synergy Bonus:** Casters who natively possess alchemical blood powers ([*Necrotic Vitae*](../vampire.md#supernatural-powers) or [*Grand Harmonization of Vitae*](../vampire.md#supernatural-powers)) receive a **+2 Power Synergy Bonus** to the 1-hour ritual completion check and a **+2 bonus to Concentration tests** if disturbed during casting.
* **Pillar 3 (Defined Caps & Boundaries):**
  * **Volume Cap:** Transmutes up to 1,000 Gallons max per casting.
  * **Duration Cap:** Transmutation lasts strictly **24 hours** before all remaining water reverts to its natural state. Thrall bonds established during the window remain in effect post-reversion.
  * **Regeneration Cap:** A vampire cannot regenerate more Blood Reserves from transmuted water in a single feeding session than their standard per-night Reserve pool cap (see [Blood Reserve Math](../vampire.md#blood-reserve-math--expenditure-caps)).
* **Thrall Susceptibility Protocol:** Mortals drinking the transmuted water gain **Susceptibility** (50% easier to enthrall via deliberate blood bond feeding). Drinking transmuted water does **NOT** automatically create a Thrall bond — an intentional feeding enthrallment is still required. Standard [Thrall Cap rules](../vampire.md#secrecy-covens-and-thralls) and overage penalties apply.

### Eclipse of the Sanguine Tide
* **Cost & Duration:** `3 Reserves | Duration: 1 Entire Night`
* **Mechanic:** The Ancient channels an explosive crimson beacon into the night sky. A thick, oppressive crimson fog rolls across a **1-mile radius**.
* **Effects:**
  * Completely blocks moonlight and star guidance. All allied vampires inside the fog zone gain **+1 to all Perception and Tracking checks** for the Eclipse duration — vitae-sense sharpens as natural light is suppressed while rivals and mortals are blinded.
  * All blood-based powers cast within the eclipse zone receive a **+1 damage/potency bonus**.
  * **Eclipse Overcap:** Allied vampires inside the fog zone may temporarily exceed their personal [Blood Reserve](../vampire.md#blood-reserve-math--expenditure-caps) cap by an amount scaled to Age Tier:

    | Age Tier | Eclipse Overcap |
    | :--- | :--- |
    | **Neonate** (< 500 yrs) | +2 Reserves above personal cap |
    | **Elder** (500–1,199 yrs) | +3 Reserves above personal cap |
    | **Ancient** (1,200+ yrs) | +4 Reserves above personal cap |

    Overcap reserves are expended before standard reserves and drain at **double the passive rate** after Eclipse ends at dawn. A vampire may harvest multiple times during the Eclipse night, returning to tithe after each 5-reserve harvest threshold. Standard [Law of the Sanguine Tithe](../vampire.md#social) obligations apply to all reserves *harvested* during the Eclipse window. **No Over-Tithe Credit:** Because the Law of the Sanguine Tithe sets no minimum donation floor, donating more than the obligated amount does not generate tithe credit toward future obligations. Each tithe period is settled independently.

---

## Integration & Compatibility

This supplement is 100% compatible with **Vampire TTRPG Framework v2608.48.0-bs**. All ritual rules interact cleanly with [Coven Governance Law](../vampire.md#social), [Torpor Recovery Track](../vampire.md#torpor), and [Age Tier Superiority Mechanics](../vampire.md#age-tier-superiority-modifier-system).
