# Changelog - Vampire TTRPG Framework

All notable changes to the Vampire Ruleset framework are documented in this file.

The versioning follows the [JLDN Generational Versioning Schema](https://github.com/JLDesignNetwork/Generational-Versioning-Schema) format (`[YYMM].[SUBVERSION].[REVISION]-[TAG]`).

---

## Generation 2608

### 2608.26.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 18 Red Team Audit fixes and codifying the Combined Power Usage & Synergistic Scaling Matrix.**

#### Added
- **Combined Power Usage & Synergistic Scaling Matrix:** Codified rules for invoking combined powers, including per-round expenditure cap enforcement, +1 Synergistic Pair Bonus for complementary powers, Age Tier Synergy Scaling multipliers (+50% range for Elders, 2x range / +2 bonus for Ancients), and Opposing Power Elemental Cancellation.
- **Blood Surge Single-Stat Overwrite Cap:** Codified rule specifying that executing a new Blood Surge overwrites previous surge stat bonuses, maintaining a single +2 stat bonus (+2 Strength OR +2 Speed OR +2 Initiative) at any given moment under per-round expenditure caps.
- **Visage Fear Stun Immunity & Age Tier Superiority:** Codified rule specifying that Visage checks are modified by Age Tier Superiority (+1 vs Neonates, +2 vs Elders); targets successfully affected gain a 1-Scene immunity window against subsequent fear stuns.
- **Nerve Lightning Bio-Neural Target Scope vs Force Barriers:** Clarified that Kinetic Barrier deflects solid projectiles, but non-physical bio-electrical attacks (Nerve Lightning) pass through telekinetic barriers.
- **Chameleon Facade Thermal FLIR Signature Lock:** Clarified that Chameleon Facade alters physical facial features and voice pitch like wet clay, but does not generate body heat, remaining visible as a cold blue/violet silhouette under FLIR thermal optics.
- **Soul Bind Incorporeal Daylight Anchor Protection:** Clarified that bound spirits retreat inside their physical anchor object during daylight hours.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.26.0-as`.
- Completed tasks `TODO-22` through `TODO-26` in frontmatter and registered Round 19 audit tasks `TODO-27` through `TODO-31` in `in-progress:audit` status.

---

### 2608.25.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 17 Red Team Audit fixes: Phantasm Cybernetic Optic Interaction, Corpse Siphon Undead Head Interrogation Scope, Law of the Sanguine Tithe Hardship Deferral, Daywalker Solar Swarm Transference Timer, and Sub-Auditory Tremor Echo Airborne Blind Spot.**

#### Added
- **Phantasm Cybernetic Optic Interaction:** Codified rule specifying that while Phantasm affects the organic visual cortex, raw digital HUD overlays display un-distorted feeds, inflicting a -2 perceptual disorientation penalty.
- **Corpse Siphon Undead Head Interrogation Scope:** Codified restriction specifying that Corpse Siphon targets ONLY deceased mortal/host corpses; living or torpid decapitated vampire heads are immune and require Mind Tear.
- **Sanguine Tithe Hardship Deferral:** Codified 1-week deferral for neonates harvesting 0 blood due to injury or stasis; unpaid tithes after 2 consecutive weeks allow Apex Elder forced vein draining (2 reserves) or punitive labor.
- **Daywalker Solar Swarm Transference Timer:** Codified rule specifying that sunlight shining on a manifested swarm transfers 100% solar radiation into the Pocket-Realm body, continuously burning the 3-minute Daywalker timer until forced Stage 4 Torpor.
- **Sub-Auditory Tremor Echo Airborne Blind Spot:** Clarified that airborne or levitating targets (Abyssal Levitation, Vesper Canopy) do not touch solid surfaces and are completely invisible to Tremor Echo.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.25.0-as`.
- Completed tasks `TODO-17` through `TODO-21` in frontmatter and registered Round 18 audit tasks `TODO-22` through `TODO-26` in `in-progress:audit` status.

---

### 2608.24.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 16 Red Team Audit fixes: Sci-Fi Native Soil Structural Containment & Sabotage, Re-Rooting Interruption Tiers, Millennial Scaling Override Clarification, and Unified Torpor Stasis Scope.**

#### Added
- **Sci-Fi Native Soil Containment & Sabotage:** Codified rule specifying that shattering glass or breaking valves on high-tech Native Soil containers (cryo-capsules, hydroponic terrariums) breaches soil containment, causing soil micro-ecosystem death and initiating [The Bleed] after 48 hours.
- **Re-Rooting Interruption Tiers:** Standardized Re-Rooting interruption consequences: Brief ($\le$1 hour) = pauses progress without penalty; Moderate (1-24 hours) = +1 day (24hr) static penalty; Prolonged (>24 hours) = resets current stage progress back to Day 0.
- **Millennial Scaling Override Clarification:** Explicitly confirmed that after 2,000 years post-change, Millennial Scaling replaces previous 250yr/500yr cycles with a single flat rate (+2 Reserves every 250 years; no 500yr milestone bonus).
- **Unified Torpor Stasis Scope:** Unified metabolic Torpor Stasis to cover ALL forms of Torpor (Stage 3 Catatonic Torpor, Stage 4 Petrified Slumber, and Starvation Desiccation Torpor), suspending [The Bleed] decay while in Torpor.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.24.0-as`.

---

### 2608.23.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 15 Red Team Audit fixes: Structural Intactness Requirement for Creation, Wooden Stake Cardiac Lock & Torpor Paralysis, Anchor Empathy Shielding Rule, Post-Feeding Animal Reaction, and Artificial UV Light Immunity under Daywalker's Grace.**

#### Added
- **Structural Intactness Requirement for Creation:** Codified rule requiring the victim's body to be structurally intact (head attached, heart undamaged) during the 3-minute transfusion window; transfusing a decapitated/heart-destroyed body fails automatically.
- **Wooden Stake Cardiac Lock & Torpor Paralysis:** Clarified that cardiac staking inflicts immediate **Catatonic Torpor (Paralysis)**; staking only causes True Death (Ash Disintegration) if combined with decapitation, solar exposure, or fire.
- **Anchor Empathy Shielding Rule:** Codified that maintaining an active, intact Pre-Change Anchor shields Elders and Ancients from automatic Empathy Decay.
- **Post-Feeding Animal Reaction:** Specified that Post-Feeding Camouflage (1–2 hrs post-meal) reduces the Animal Panic Radius from 30 feet down to 5 feet, enabling interaction with trained animals.
- **Artificial UV Immunity under Daywalker's Grace:** Clarified that vampires actively using *Daywalker's Grace* are completely immune to artificial UV light weapons without consuming their 3-minute daily solar shield timer.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.23.0-as`.

---

### 2608.22.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release adding Archiver Immunity to Blood Archive sensory overload penalties.**

#### Added
- **Archiver Immunity to Sensory Flood:** Codified rule granting Arch-Chroniclers and Blood Scribes (*Archivers*) full immunity to sensory flood and combat concentration penalties when ingesting Blood Archive phials.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.22.0-as`.

---

### 2608.21.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 14 Red Team Audit fixes: Dual-Master Bloodline Duel, Thrall Reaper Contagion Resistance, Blood Archive Action Economy & Overload Penalty, Primary Spliced Reaper Lifespan, and Tabula Rasa Discipline Tiers.**

#### Added
- **Dual-Master Bloodline Duel System:** Codified rule resolving second-bloodline Thrall enthrallment as a direct Bloodline Duel between Original Master and Intruder Vampire using Age Tier Superiority modifiers (Master Win = intruder blood purged; Intruder Win = master bond shattered + Thrall takes 2 Direct Core Damage on Brink of Death).
- **Thrall Reaper Contagion Response:** Specified that Thralls receive a +2 Resistance bonus against Reaper contagion due to master vitae; however, because human blood remains susceptible to viral taint, a failed check transforms the Thrall into a Secondary Reaper/Husk.
- **Blood Archive Action Economy & Overload Penalty:** Standardized Archive phial drinking to 1 Action with effects taking effect on the following round; codified a -2 concentration penalty for 1 round when ingesting Archive phials mid-combat due to sensory overload.
- **Primary Spliced Reaper Lifespan:** Clarified that the original Primary Spliced Reaper (Patient Zero) possesses a laboratory-stabilized bloodline and does NOT suffer cellular breakdown, unlike Secondary contagions.
- **Tabula Rasa Discipline Tiers:** Standardized Coven penalties for Tabula Rasa violations: Minor/Accidental = 30-Day Power Lockout + 50% Reserve Drain; Major/Intentional = Forced Stage 3 Torpor for 1 Year + destruction of all records.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.21.0-as`.

---

### 2608.20.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 13 Red Team Audit fixes: Native Soil Torpor Stasis, Stage 4 Torpor petrification clarification, Nyctophilous Apex Sight in Omni-Sensory Primacy, Trailing Minion Boundary Rules, Natural Critical Success Luck Guarantee, and Digital Shroud thermal counter-power cross-reference fix.**

#### Added
- **Native Soil Torpor Stasis:** Codified rule suspending [The Bleed] regression track while a vampire is in Stage 3 or Stage 4 Torpor (Petrified Slumber), preventing unrecoverable Bleed death while calcified.
- **Stage 4 Torpor Petrification Clarification:** Clarified that Stage 4 Torpor is a petrified granite state; turning to ash represents absolute, unrecoverable True Death.
- **Omni-Sensory Primacy Trait Update:** Included *Nyctophilous Apex Sight* in *Omni-Sensory Primacy* composite traits, granting flashbang blinding flare immunity to Master perception hosts.
- **Trailing Minion Boundary Rules:** Specified that re-animated corpses falling outside a moving *Aura of the Slumbering Legion* sphere remain active for the 1-scene duration up to the active minion cap `ROUND(VAMPIRE_AGE / 100)`.
- **Natural Critical Success Luck Guarantee:** Codified that all defender targets in mental/social tests retain a minimum 1-in-20 Natural Critical Success chance to resist or break free against superior odds, ensuring a defender can never be completely counted out regardless of modifier gaps.

#### Fixed
- **The Digital Shroud Sensor Cross-Reference:** Corrected sensor counter-power cross-reference from *Thermal Vitae Vision* (a sight power) to *Crimson Mist* or *Veil Flicker*.

#### Modified
- Updated H1 title in `vampire-2608.md` to `# Vampire Ruleset v2608.20.0-as`.

---

### 2608.19.0-as (2026-08-03) - Public Alpha Release

**Public Alpha release applying Round 12 Red Team Audit fixes: Mind Grip mass caps by Age Tier, Soul Bind sentry caps, Puppet Master motor vs mental power scope, Chameleon Facade bio-testing limits, Lineage Harmonization modifier stacking, and Nerve Lightning bio-neural target scope.**

#### Added
- **Mind Grip Mass Caps:** Codified lifting/hurling weight limits based on Age Tier: Neonates (<500 yrs) = 250kg (550lbs); Elders (500-1,199 yrs) = 500kg (1,100lbs); Ancients (1,200+ yrs) = 1,000kg (1 Ton).
- **Soul Bind Active Sentry Cap:** Hard-capped active bound spirits at `ROUND(VAMPIRE_AGE / 100)` (minimum 1); codified incorporeal warning-only sentry status (no physical attack damage).
- **Puppet Master Motor Scope:** Clarified that Puppet Master controls physical motor muscles only, without granting access to the victim's brain thoughts, blood reserves, or supernatural power activations.
- **Chameleon Facade Bio-Limits:** Clarified that Chameleon Facade alters physical dermal contours and fingerprints, but deep biological markers (blood DNA sequencing, non-circulating blood) are revealed by lab tests.
- **Lineage & Age Tier Modifier Stacking:** Codified that Lineage Harmonization (+2 bonus against direct bloodline) explicitly STACKS with Universal Age Tier Superiority modifiers (+1 or +2).
- **Nerve Lightning Target Scope:** Specified that Nerve Lightning targets biological neural networks exclusively; non-biological mechanical entities (drones, computer mainframes) are unaffected.

#### Modified
- Updated H1 title in `vampire-2608.md` to `Vampire Ruleset v2608.19.0-as`.

#### Fixed
- Eliminated unlimited telekinetic weight lifting exploits.
- Resolved infinite necromantic spirit surveillance army exploits.
- Standardized mind-control modifier stacking and bio-electrical target scope.

---

### 2608.18.0-as (2026-08-03) - Public Alpha

**Public Alpha release introducing the Formal Action Economy Framework and Tiered Blood Reserve Expenditure Caps scaling by Age Tiers.**

#### Added
- **Formal Action Economy Framework:** Codified combat turn structure consisting of 1 Main Action (attack, activated power, skill check), 1 Movement/Minor Action (move, draw item, toggle innate power), Continuous Upkeep (sustained powers upkeep at start of turn), and 1 Off-Turn Reaction/Defense (dodge, reactive teleport).
- **Tiered Blood Reserve Expenditure Caps:** Replaced flat 2-reserve cap with Age-Tiered spending limits per combat round: Neonates (<500 yrs) = 2 Reserves/Round; Elders (500-1,199 yrs) = 3 Reserves/Round; Ancients (1,200+ yrs) = 4 Reserves/Round.
- **Action Economy Perks:** Codified Blood Surge bonuses (+2 Strength/Speed OR +1 Extra Minor Action) and Master Power 0-Cost initial activation advantages.

#### Modified
- Updated Categorized Per-Round Expenditure Caps under Mechanics to scale with Age Tiers.
- Updated H1 title in `vampire-2608.md` to `Vampire Ruleset v2608.18.0-as`.

#### Fixed
- Eliminated the Ancient Expenditure Bottleneck exploit, allowing Elders and Ancients to utilize expanded blood pools effectively in combat.

---

### 2608.17.0-as (2026-08-03) - Public Alpha

**Public Alpha release applying Round 10 Red Team Audit fixes: Combust Vitae Age Tier Scaling Table, Petrified Slumber Hibernation Scale, Centenary Compulsion command mediums, Weaver's Eclipse web counterplay, and Sanguine Spike/Umbral Blade structural damage math.**

#### Added
- **Combust Vitae Age Tier Scaling Table:** Delta=+2: Total Incineration & instant Round 2 Flesh Ignition; Delta=+1: Severe Combustive Burst (+2 bonus damage); Delta=0: Standard Internal Flame; Delta=-1: Resisted Fizzle (0 wounds); Delta=-2: Complete Immunity (spell smothers completely).
- **Petrified Slumber Hibernation Scale:** Bare minimum 30-Day lock-in duration (with optional 1-Year or 100-Year Centenary Slumber tiers). Detailed early awakening rituals (3 drafts of vampire blood onto statue lips or >50 structural shock damage) and Native Soil maintenance requirements for vampires without Earthbreaker.
- **Centenary Compulsion Command Mediums:** Codified that Centenary Compulsion forces obedience to a Sire's explicit intent regardless of medium (spoken, written letter, or third-party messenger).
- **Weaver's Eclipse Web Counterplay:** Codified Hard Strength check to break free from web traps; fire (Pyromancy/Pyre Aura) or Kinetic Blasts destroy webs instantly.
- **Structural Barrier Damage Math:** Clarified that Sanguine Spikes and Umbral Blades deal standard physical damage against Structural Integrity HP on heavy barriers (vault doors, tank hulls).

#### Modified
- Updated H1 title in `vampire-2608.md` to `Vampire Ruleset v2608.17.0-as`.

#### Fixed
- Eliminated quick combat-shield exploits on Petrified Slumber.
- Resolved Pyromancy damage scaling disputes against Ancient targets.
- Standardized web trap escape checks and structural barrier damage math.

---

### 2608.16.0-as (2026-08-03) - Public Alpha

**Public Alpha release applying Round 9 Red Team Audit fixes: Low-Reserve Shatter Degradation System, strict self-only Healing scope, Blood Archive phial zero-nutrition & crystallization, Kinetic Barrier evocation deflection, Primal Shift solar tissue combustion, and Grave Rot relic immunity.**

#### Added
- **Low-Reserve Shatter Degradation System:** Codified escalating penalties for Shatter Attempts at half reserves or less (>50% reserves: 50% reserve burn; <=50% reserves: 1 major consequence; <=2 reserves: 2 severe consequences; 0 reserves: 3 catastrophic consequences including permanent power loss, 3 core health damage, and immediate Torpor).
- **Blood Archive Phial & Crystallization Rules:** Codified that Blood Archive phials yield 0 Blood Reserves (zero nutrition) and naturally crystallize into red glass over centuries while retaining 100% psychic history.
- **Strict Self-Only Healing Scope:** Codified that Sanguine Knit and Grand Harmonization of Vitae heal ONLY the invoking vampire; Anti-Healing (Necrotic Vitae) affects rival vampires.
- **Primal Shift Physical Solar Combustion:** Classified Primal Shift as direct physical tissue transformation (not a Swarm Pocket-Realm), causing sunlight shining on wolf/bat forms to directly ignite flesh.
- **Grave Rot Relic & Anchor Immunity:** Exempted sacred relics, blood archives, and supernatural artifacts from passive Grave Rot decay.

#### Modified
- Updated Kinetic Barrier to confirm complete deflection of Sanguine Spikes and Umbral Blades.
- Updated H1 title in `vampire-2608.md` to `Vampire Ruleset v2608.16.0-as`.

#### Fixed
- Eliminated 0-reserve Shatter Attempt bypass exploits.
- Resolved healing target scope ambiguities across self and allies.
- Standardized Blood Archive nutritional zero-value and crystallization properties.
