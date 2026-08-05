---
{
  "metadata": {
    "author": "Jeff Langdon",
    "documentName": "Vampire Framework Terminology & Glossary",
    "targetRuleset": "Vampire TTRPG Framework",
    "version": "2608.57.0-bs",
    "parent_ruleset_file": "vampire.md"
  }
}
---

# Vampire Framework Official Terminology & Taxonomy v2608.57.0-bs

This document outlines the official, normalized terminology standard for the **Vampire TTRPG Framework v2608**. All core rulesets, supplements, datasets, and audit workflows MUST adhere strictly to the definitions, units, and conventions codified herein.

---

## 1. Action Economy & Temporal Units

| Standard Term | Definition & Scope | Canonical Usage Rules | Disallowed Variant(s) |
| :--- | :--- | :--- | :--- |
| **Combat Action** | A single tactical maneuver executed during a turn (e.g. attack, sprint, ritual start). | Use when referring to turn choices. | *"turn action"*, *"move"* |
| **Turn** | A single participant's initiative step within a combat round. | Single actor's step. | *"phase"*, *"sub-round"* |
| **Combat Round** | Standard tactical time unit (~6 seconds) in which all combatants execute 1 turn. | Use in combat duration headers: `Duration: 1 Combat Round`. | *"round"*, *"battle turn"* |
| **Scene** | Standard narrative time unit (~10–15 minutes) covering a single encounter or location stay. | Use in narrative duration headers: `Duration: 1 Scene`. | *"encounter"*, *"event"* |
| **Slumber** | Mandatory 12-hour daytime period of unconsciousness (sunrise to sunset). | Use when referencing daytime sleep. | *"day-sleep"*, *"rest"* |
| **Night** | Full 12-hour active period between sunset and sunrise. | Use in night duration headers: `Duration: 1 Entire Night`. | *"evening"*, *"dark hours"* |
| **Window** | Operational duration of a ritual, condition, or transformation (e.g., 24-Hour Transmutation Window). | Use when defining temporary state lifespans. | *"timer"*, *"uptime"* |

---

## 2. Resource & Capacity Terminology

| Standard Term | Definition & Scope | Canonical Usage Rules | Disallowed Variant(s) |
| :--- | :--- | :--- | :--- |
| **Blood Reserve** | Discrete unit of stored vitae (~250ml living mortal blood equivalent). | Always capitalized as **Blood Reserve** (or **Blood Reserves** in plural). | *"blood point"*, *"vitae point"*, *"mana"* |
| **Heart Reservoir** | Undead heart organ acting as the biological/magical vault for Blood Reserves. | Base pool 10 Reserves; expands by Age Tier. | *"blood tank"*, *"stomach"* |
| **Per-Round Expenditure Cap** | Hard limit on Blood Reserves spent across all actions in 1 combat round (Neonate: 2; Elder: 3; Ancient: 4). | Governs combat spending. | *"spend limit"*, *"max burn"* |
| **Blood Surge** | Expending 1 Blood Reserve for a temporary +2 bonus to physical attributes/Initiative for 1 round. | Capitalized as **Blood Surge**. | *"boost"*, *"blood pump"* |
| **Over-Push Strain** | Damage/strain suffered when attempting to spend blood at 0 Reserves (1 Core Health Damage or frenzy check). | Capitalized as **Over-Push Strain**. | *"push strain"*, *"burnout"* |

---

## 3. Checks, Tests, & Resolution Mechanics

| Standard Term | Definition & Scope | Canonical Usage Rules | Disallowed Variant(s) |
| :--- | :--- | :--- | :--- |
| **Self-Control Check** | Mental/emotional test to resist frenzy, pain, terror, or maintain concentration. | Always use **Self-Control check**. | *"will check"*, *"mind roll"*, *"sanity check"* |
| **Fortitude Check** | Physical/biological endurance test to resist curses, poisons, or displacement. | Always use **Fortitude check**. | *"stamina test"*, *"body roll"* |
| **Constitution Check** | Base biological resilience test against viral mutagens / contagions (e.g. Reaper virus). | Always use **Constitution check**. | *"con roll"*, *"health test"* |
| **Bloodline Duel** | Contested Self-Control check between two vampires, scaled by Age Tier Superiority ($\Delta$). | Always use **Bloodline Duel**. | *"mental clash"*, *"psi-duel"* |
| **Difficulty Class (DC)** | Target number required to pass a check (Easy = DC 9, Medium = DC 12, Hard = DC 15, Near-Impossible = DC 18+). | Format as **DC [X] ([Difficulty Level])**. | *"target number"*, *"diff"* |
| **Age Tier Superiority ($\Delta$)** | Bonus awarded in contested checks based on Age Tier difference (+1 Elder, +2 Ancient). | Always format with symbol $\Delta$. | *"tier bonus"*, *"age mod"* |

---

## 4. Health, Damage & Banes

| Standard Term | Definition & Scope | Canonical Usage Rules | Disallowed Variant(s) |
| :--- | :--- | :--- | :--- |
| **Direct Core Health Damage** | Physical/magical wound inflicted directly to core vitality, bypassing superficial armor. | Format as **[N] Direct Core Health Damage**. | *"direct health damage"*, *"hp loss"* |
| **Fire/Thermal Damage** | Damage inflicted by extreme heat, hellfire, or blood burns. | Format as **[N] Fire/Thermal Damage**. | *"flame dmg"*, *"burns"* |
| **Solar Exposure** | Fatal radiation damage inflicted by unshielded sunlight (drains reserves/causes flesh ignition). | Capitalized as **Solar Exposure**. | *"sunburn"*, *"daylight damage"* |
| **Torpor** | Deep, near-death coma (Stage 1 Lethargic to Stage 4 Catatonic). | Capitalized as **Torpor**. | *"vampire coma"*, *"deep sleep"* |

---

## 5. Conditions & Status Slugs

| Standard Term | Definition & Scope | Canonical Usage Rules | Disallowed Variant(s) |
| :--- | :--- | :--- | :--- |
| **Susceptibility** | Condition (24hrs) making a mortal 50% easier to enthrall via blood bond. | Capitalized as **Susceptibility**. | *"vulnerable"*, *"thrall-ready"* |
| **Action Lock** | Physical limb immobilization lasting 1 combat round. | Format as **Duration: 1 Combat Round (Action Lock)**. | *"stun"*, *"paralyze"* |
| **Feral State** | Mindless predatory frenzy driven by hunger, pain, or atrocities. | Capitalized as **Feral State**. | *"frenzy mode"*, *"beast out"* |

---

## 6. Age Tier Hierarchy

| Standard Term | Age Threshold | Base Reserve Pool | Per-Round Cap |
| :--- | :--- | :---: | :---: |
| **Neonate** | New World (< 500 years) | 10 Reserves | 2 Reserves/Round |
| **Elder** | Old World (500–1,199 years) | 13+ Reserves | 3 Reserves/Round |
| **Ancient** | Primordial (1,200+ years) | 17+ Reserves | 4 Reserves/Round |

---

## 7. Supernatural & Ritual Disciplines (-mancy Taxonomy)

| Canonical Discipline | Domain & Scope | Core Assigned Powers / Rituals |
| :--- | :--- | :--- |
| **Hemomancy** | Blood Magic, Vitae Arts, Transmutation, & Bloodline Scrying | *Sanguine Scrying Mirror*, *Ritual of the Crimson Ward*, *Vitae Purification Filter*, *Hematic Curse*, *Grand Rite* |
| **Necromancy** | Death, Soul Harvesting, Post-Mortem Interrogation, & Undead Animation | *Corpse Siphon*, *Soul Bind*, *Rise of the Slumbering*, *Aura of the Slumbering Legion*, *Grave Rot* |
| **Osteomancy** | Skeletal Manipulation, Bone Darts, Calcification, & Bone Armor | *Bone Shards*, *Skeletal Calcification*, *Bone Armor Plating* |
| **Pyromancy** | Fire, Thermal Energy, Hellfire, & Pyromantic Combustion | *Hellfire Orb*, *Pyre Aura*, *Thermal Ignition* |
| **Gravimancy** | Gravity Control, Mass Defiance, Localized Force Shields, & Pressure Implosion | *Gravity Shield*, *Grav-Crush*, *Abyssal Drift*, *Spider's Grace* |
| **Astromancy** | Spatial Continuum Folding, Teleportation, & Spatial Portals/Anchors | *Astral Step*, *Astral Rift*, *Astral Anchor Ritual* |
| **Umbramancy** | Shadow Traversal, Void Manipulation, & Light-Absorbing Void Webs | *Umbral Crossing*, *Silk & Shadow* |
| **Psychomancy** | Telepathy, Emotion Manipulation, Mind Probes, Illusions, & Psychokinesis | *Psychic Grip*, *Mind Tear*, *Lethe's Touch*, *Nightmare Visage*, *Phantasm*, *Puppet Master* |
| **Cognimancy** | Heightened Perception, Retinal FLIR, Ultrasonic Bio-Sonar, & EM Spectrum Gaze | *Thermal Vision*, *Bio-Sonar*, *EM Gaze*, *Apex Sight*, *Tremor Sense*, *Resounding Beat* |
| **Morphomancy** | Biological Body Shifting, Swarm Realms, Beast Shifting, & Dermal Clay Alteration | *Mist Form*, *Bat Swarm*, *Rat Tide*, *Weaver Swarm*, *Beast Shift*, *Arachnid Shift*, *Chameleon Clay* |
| **Immunomancy** | Solar Shielding, Holy Symbol Resistance, Toxin Assimilation, & Native Soil Severance | *Daywalker's Grace*, *Unholy Primacy*, *Anointed Flesh*, *Alchemical Assimilation*, *Earthbreaker* |
| **Biomancy** | Biological Regeneration, Cellular Healing, Suppressed Mending, & Limb Regrowth | *Sanguine Knit*, *Mortal Mask*, *Gangrene Touch*, *Grand Harmonization of Vitae* |
