---
{
  "metadata": {
    "author": "Jeff Langdon",
    "rulesetName": "Vampire",
    "version": "2608.48.0-bs",
    "todo_file": "todo.json",
    "changelog_file": "CHANGELOG.md"
  }
}
---


# Vampire Ruleset v2608.48.0-bs
- [System Agnostic & Multi-Genre Framework](#system-agnostic--multi-genre-framework)
- [Behavior](#behavior)
  - [Physical Attributes & Speed](#physical-attributes--speed)
- [Creation](#creation)
- [Death](#death)
  - [Sunlight Lethality Baseline](#sunlight-lethality-baseline)
  - [Banes & Weaknesses](#banes--weaknesses)
  - [The Dying Echo](#the-dying-echo)
  - [The Native Soil Dependency](#the-native-soil-dependency)
    - [Weaponizing & Sabotaging Native Soil](#weaponizing--sabotaging-native-soil)
    - [The Home Sickness Regression Track (The Bleed)](#the-home-sickness-regression-track-the-bleed)
      - [Native Soil Recovery (Re-Rooting)](#native-soil-recovery-re-rooting-track)
  - [Dismemberment & Decapitation](#dismemberment--decapitation)
- [Life](#life)
  - [Pre-Change](#pre-change)
  - [Post-Change](#post-change)
- [Mechanics](#mechanics)
  - [Draining](#draining)
  - [Drinking & Sustenance Rules](#drinking--sustenance-rules)
    - [Sustenance & Blood Starvation Rules](#sustenance--blood-starvation-rules)
  - [Feeding](#feeding)
- [Powers](#powers)
  - [Behavioral Powers](#behavioral-powers)
  - [Supernatural Powers](#supernatural-powers)
- [Social](#social)
- [Types](#types)
  - [Mutations](#mutations)
  - [New World](#new-world)
  - [Old World](#old-world)

## System Agnostic & Multi-Genre Framework

This document is designed as a system-agnostic template that seamlessly adapts to different genres and game systems (such as high-fantasy settings like *Mytharios* or sci-fi/modern settings like *The Multiverse*). Core rules translate across genres as follows:

| Core Concept | 🗡️ High Fantasy (*Mytharios*) | 🚀 Sci-Fi / Modern (*The Multiverse*) |
| :--- | :--- | :--- |
| **Detection & Distortion** | Silver-backed mirror distortions, blurred water reflections, scrying pool static | High-res camera pixelation, digital video corruption, AI tracking anomalies |
| **Banes & Countermeasures** | Consecrated holy water, alchemical garlic/wolfsbane, solar incantations | UV laser suppressors, thermal motion trackers, chemical bio-toxins |
| **Feeding & Creation** | Direct wrist-biting, goblet blood exchange, blood rituals | Syringe cardiac injection, synthetic blood filters, bio-cybernetic tethers |
| **Native Soil Preservation** | Living earth in clay urns, earthworms, enchanted soil boxes | Cryo-stabilized soil capsules, oxygenated hydroponic terrariums |
| **Dietary Substitutes** | Mana-infused blood, alchemical blood phials, sacrificial chalices | Synthetic blood pouches (Synth-Vitae), bio-engineered plasma packs, cybernetic transfusion cartridges |
| **Haunts & Havens** | Underground gothic crypts, stone catacombs, sunless mountain fortresses, obsidian towers | Subterranean bunker vaults, shielded orbital space stations, radiation-proof safehouses, cyber-labs |
| **Communication & Tech** | Telepathic bloodline resonance, scrying pools, whispered raven messengers | Encrypted bio-comm channels, infrared optical overlays, sub-space neural frequency transmitters |

## Behavior & Physiology

A vampire’s behavior is largely dictated by the struggle between their lingering humanity and their new predatory instincts. The "Hunger" forces them to view mortals inherently as prey, requiring constant mental fortitude. They are fiercely territorial, mapping out distinct hunting grounds, and their nocturnal isolation often leads to a detachment from the daylight mortal world.

### Default Biological & Physical Traits
Unless actively utilizing powers or recent blood reserves to mimic life, all vampires share core apex predatory characteristics:

* **Retractable Fangs:** Fangs are naturally concealed flush against the gums during normal speech and social interaction. They automatically extend into razor-sharp, hollow feeding fangs whenever the vampire feeds, enters a frenzy, or invokes blood powers.
* **Cold Dermis & Post-Feeding Flush:** A vampire's skin is naturally cold to the touch (matching ambient room temperature) and lacks a pulse or spontaneous respiration. Immediately after consuming a full draft (~250ml) of living blood, the vampire's body flushes warm and human-like for **1–2 hours**, restoring artificial body heat and involuntary breathing.
* **Unnatural Locomotion & Statue-Like Stillness:** Vampires move with silent, fluid grace. When standing still, they exhibit complete statue-like immobility—showing zero involuntary blinking, no chest rise/fall, and no micro-fidgeting.
* **Low-Light Eye Glint:** In dim light or pitch darkness, a vampire's eyes emit a faint crimson or amber reflection (*tapetum lucidum* glint), betraying their nocturnal night vision.

### The Predatory Aura & Uncanny Valley
A vampire's supernatural apex nature destabilizes living beings in their immediate proximity:

* **Animal Instinct (30-Foot Panic Radius):** Domesticated animals (dogs, horses, cats, livestock) smell the absence of living pheromones and notice the unnatural, silent locomotion. Animals become violently hostile or flee in terror when an unmasked vampire enters within **30 feet**.
* **The Uncanny Valley Effect on Mortals:** Living humans rarely recognize a vampire as undead on sight, but their subconscious mind senses the lack of breathing and statue-like stillness. This creates an unexplainable skin chill and subconscious dread, imposing a **+1 difficulty penalty** on mundane social/persuasion checks against un-enthralled mortals.
* **Post-Feeding Camouflage (1–2 Hours):** During the 1–2 hours immediately following a living blood meal, the warm skin flush and reflex breathing eliminate the Uncanny Valley social penalty AND reduce the Animal Panic Radius from 30 feet down to **5 feet**, allowing the vampire to blend flawlessly into mortal crowds and briefly interact with trained animals.

### Night-Stalking & Hunting Psychology
* **Cardiac Hyper-Focus:** When actively stalking prey, the vampire's cognitive focus filters out ambient city noise to lock onto the target's heartbeat pulse, lung movement, and blood volume.
* **Sanguine Tracking Bonus:** A hunting vampire receives a **+1 bonus** to all Perception and Tracking rolls when pursuing injured, bleeding, or terrified targets.

### Territorial Sanguine Boundaries
Vampires mark their hunting grounds by leaving microscopic vitae scents on architectural landmarks or establishing feeding perimeters. Invading a rival Coven's established hunting grounds without a formal Blood Treaty imposes a **-1 penalty on stealth rolls** inside the rival's marked territory.

### Nocturnal Detachment (The Daylight Rift)
As decades turn to centuries, vampires experience profound psychological alienation from sunlit mortal society:
* **Empathy Decay:** Living human routines (careers, money, mortal romance) come to resemble a fleeting "Mayfly Theater," causing Old World vampires to treat mortals as temporary livestock.
* **The Daylight Void:** Centuries of enforced daylight slumber distort time perception. Decades feel like passing months, and mortal generations bloom and wither like autumn leaves.
* **Anchor Empathy Shielding Rule:** Maintaining an active, intact Pre-Change Anchor (a living descendant, cherished heirloom, or sacred oath) **shields** the vampire from automatic Empathy Decay, allowing Elders and Ancients to retain human empathy for as long as their Anchor remains uncorrupted.

### Physical Attributes & Speed
Vampires automatically possess supernatural physical enhancements compared to mortals, scaling as their blood matures:
* **New World Vampires (0–499 years):** Receive a **+1 bonus to Initiative** and **1.5x base movement speed**.
* **Old World Vampires (500+ years):** Upgrade to a **+2 bonus to Initiative**, **2x base movement speed**, **doubled vertical/horizontal jump distance**, **1 free positioning action** in the first round of combat, and an **extra bonus action** during surprise rounds.
* **Supernatural Kinetic Crash Impact & Wall Collision Recoil Math:** A vampire sprinting at supernatural velocity (1.5x speed or active *Blood Surge Speed*) who collides directly with a solid, unyielding obstacle (concrete wall, vehicle, steel bulkhead) inflicts **1 Blunt Impact Damage** onto the obstacle's Structural HP. If the barrier's structural integrity is unbreached, the unyielding surface reflects the kinetic shockwave back into the vampire's body, inflicting **1 Blunt Recoil Damage** on the vampire. Wall collision recoil damage is completely absorbed if the vampire is actively shielded by *Kinetic Barrier* or possessing Ancient *Sovereign Temperament*.

## Creation

A vampire can only be created by another vampire through a precise, perilous metabolic transformation. The creation of a neonate requires two mandatory actions: [draining](#draining) the victim to the brink of death and immediately [feeding](#feeding) the victim a draft of the Sire's own supernatural vitae. 

Metaphysically and biologically, transformation progresses through three distinct, terrifying phases:

### Phase 1: The Death Threshold
Before new immortal life can take root, the victim's mortal vessel must undergo true biological death.
* **Biological Shutdown:** As mortal blood volume drops to zero during draining, the heart seizes, respiration halts, body temperature plunges to match ambient room temperature, and brain activity ceases.
* **The 3-Minute Window:** Transformation requires entering complete brain death without incurring cellular necrosis. The Sire has a strict **3-minute biological window** from the moment the victim's heart stops to administer Sire vitae. If blood is not supplied within 3 minutes, irreversible brain rot sets in and the victim dies permanently as a mundane corpse. *Structural Intactness Requirement:* The victim's body MUST be structurally intact (head connected to torso, heart undamaged) during the 3-minute transfusion window. Transfusing vitae into a decapitated or heart-destroyed corpse fails automatically, producing a dead, inanimate corpse.

### Phase 2: The Sanguine Transfusion
Once Sire vitae enters the deceased body, it acts as superheated, dark biological mercury—igniting dead nervous tissue, liquefying bone marrow, and violently rewriting the victim's genetic essence across seconds.

* **Dual-Genre Delivery Rituals:**
  * **High Fantasy (*Mytharios*):** Administered directly by slicing the Sire's wrist over the victim's dead lips or pouring concentrated vitae from a consecrated obsidian/gold chalice during a blood ritual.
  * **Sci-Fi / Modern (*The Multiverse*):** Delivered via pneumatic cardiac syringe directly into the left ventricle or through an automated vascular filtration and transfusion rig.
* **Physiological Metamorphosis:** The corpse's blood vessels turn obsidian-black as Sire blood diffuses. Organ functions permanently cease, skin tightens into porcelain pale smoothness, and the heart transforms from a pump into a dormant reservoir for stored blood reserves.

### Phase 3: The First Awakening
Within seconds of transfusion, the neonate experiences a violent, agonizing resurrection.

* **The Oxygen Reflex:** The neonate violently gasps for air—a terrifying instinctual muscle spasm from their former mortal life, despite their lungs no longer requiring oxygen.
* **Sensory Explosion:** The neonate's eyes flood with hyper-focused night vision, while their auditory nerve explodes with every surrounding heartbeat, dripping faucet, or electric hum within a hundred yards.
* **Sensory Disorientation & The First Hunger:** The overwhelming sensory shock inflicts a temporary **+2 difficulty penalty** on all complex mental tasks for the neonate's first hour. The neonate experiences an unquenchable, burning throat and **MUST feed on living blood within 1 hour of awakening**. Failure to feed within 1 hour plunges the neonate into an immediate, indiscriminate [Feral State](#post-change).

### Creation Limitations & Anti-Mass Siring Rules

To prevent vampires from rapidly creating armies of neonates overnight, the siring process imposes heavy physical, metaphysical, and psychological tolls upon the Sire:

* **Blood Reserve Cost (5 Blood Reserves):** Siring a fledgling requires draining **5 Blood Reserves** (50% of the Sire's heart reservoir capacity) directly into the victim during Phase 2 (Sanguine Transfusion).
* **30-Day Bloodline Cooldown (Sanguine Exhaustion):** Siring a fledgling temporarily drains the ancestral magic in the Sire's blood. For **30 days** post-creation, the Sire's blood loses its igniting potency. Attempting to sire another fledgling during this 30-day window automatically botches the transformation, producing a [Feral Husk](#mutations).
* **3-Year Psychic Rebound & Emotional Echoes:** 
  * *Acclimatization Period:* For **3 years** post-creation, the Sire's mind must acclimate to the newly formed blood tether.
  * *Emotional Static Bleed:* During these 3 years, the fledgling's raw emotions (intense hunger, terror, rage, panic) bleed backward through the bond into the Sire's subconscious. The Sire suffers a **+1 difficulty penalty** on Self-Control checks whenever their fledgling is starving or in distress.
  * *Psychic Overload Hazard:* If a Sire attempts to sire a new fledgling while still experiencing Mental Rebound (within 3 years), the dual blood tethers create a violent psychic overload. The Sire must pass a **Hard Self-Control check**; failure inflicts a **permanent -1 penalty to Cognition** and causes the new fledgling to botch into a [Feral Husk](#mutations).
* **Progeny Capacity Cap (Simultaneous Sire Bond Limit):** A Sire can only maintain a maximum number of bound fledglings undergoing their 100-year Centenary Compulsion simultaneously based on their age tier:
  * **Neonates (<500 yrs):** 1 simultaneous fledgling max.
  * **Elders (500–1,199 yrs):** 3 simultaneous fledglings max.
  * **Ancients (1,200+ yrs):** 5 simultaneous fledglings max.
  * *Exceeding Cap:* Attempting to sire beyond this cap forces the oldest fledgling's bond to shatter prematurely or causes a [Power Fade Collapse Mutation](#mutations).

### Sunlight Lethality Baseline

Direct, unfiltered solar radiation is the ultimate bane of vampiric existence. The curse of the undead reacts violently to sunlight, causing solar energy to ignite the corrupted vitae within a vampire's tissue.

#### The 3-Stage Solar Disintegration Track
Upon exposure to direct, unfiltered sunlight, a standard vampire without specialized protections undergoes rapid cellular collapse across three distinct combat rounds (roughly 18 seconds total):

* **Round 1 (1–6 seconds / Dermal Vaporization):** 
  * *Sensory & Physical Effect:* Skin immediately blackens, boils, and emits hiss/crimson steam. Eyes burn out in their sockets.
  * *Mechanical Penalty:* Inflicts blinding pain and severe disorientation (-2 penalty to all physical actions and rolls).
* **Round 2 (7–12 seconds / Flesh Ignition):** 
  * *Sensory & Physical Effect:* Muscle tissue combusts into white-hot, unholy flame. 
  * *Mechanical Penalty:* All active [Supernatural Powers](#supernatural-powers) instantly collapse and shut down. The vampire burns **1 stored blood reserve per second**.
* **Round 3 (13–18 seconds / Ash Collapse):** 
  * *Sensory & Physical Effect:* Internal organs char to cinder; bone structure calcifies and shatters into light grey ash.
  * *Mechanical Outcome:* Results in permanent **True Death**.

*(Note: Vampires possessing the [**Daywalker's Grace**](#supernatural-powers) power can withstand direct sunlight for brief, agonizing minutes before ash conversion begins.)*

#### Environmental Filtering & Shade Survival
Solar lethality depends directly upon the intensity and filtering of ambient light:

* **Direct Unfiltered Sunlight:** Triggers the full 3-Stage Solar Disintegration Track above.
* **Heavy Cloud Cover / Torrential Storms:** Water vapor filters solar intensity. Lethality drops to dermal steam burns, draining **1 blood reserve per 10 minutes** of exposure without triggering white flame combustion.
  * **Thermal Insulation Collapse (0 Reserves):** Stored blood reserves act as a biological cooling insulation against filtered solar radiation. The moment a vampire's blood reserves hit **0** while exposed to cloud-filtered sunlight, thermal insulation fails completely. The vampire's tissue immediately combusts, advancing directly into **Round 2 (Flesh Ignition)** and progressing to **Round 3 (Ash Collapse / True Death)** within 12 seconds unless shade is reached.
* **Tinted / UV-Shielded Windows:** Modern UV-blocking glass or heavy architectural tinting suppresses solar ignition, reducing damage to a mild fever and non-lethal skin reddening.
* **Shade & Full Shadow:** Stepping beneath dense archways, thick umbrellas, or building shadows **instantly pauses the disintegration track**. The burning ceases immediately, though accumulated burn injuries must be healed through blood expenditure or undisturbed rest.

#### Artificial UV Light Weapons (Dual-Genre)
High-intensity artificial ultraviolet light sources operate differently from natural solar radiation:
* **Hunter UV Spotlights / Military UV Lasers / UV Flashbangs:** Trigger **Round 1 (Dermal Vaporization)** upon impact, causing steam burns and -2 action penalties while exposed. However, artificial UV light does **not** trigger Round 2 combustion or Round 3 ash collapse unless enhanced by solar incantations (*Mytharios*) or orbital UV focal lenses (*The Multiverse*). *Daywalker's Grace Immunity:* Vampires actively invoking [*Daywalker's Grace*](#supernatural-powers) are completely **immune** to artificial UV light weapons without consuming their 3-minute daily solar shield timer.

### Banes & Weaknesses

Vampires are vulnerable to specific ancient banes, sacred symbols, and botanical toxins that disrupt their supernatural biology:

#### 1. Wooden Stake (Cardiac Lock & Torpor)
Driving a wooden stake (crafted from oak, rowan, hawthorn, or ash wood) directly through the cardiac chamber of a vampire inflicts instant paralysis.
* **Instant Cardiac Lock (Catatonic Torpor):** The moment a wooden stake pierces the cardiac chamber, the vampire's blood flow and power transmission instantly freeze. The vampire collapses into an immediate **Catatonic Torpor (Paralysis)**, remaining conscious but completely immobilized and unable to invoke powers or burn blood reserves until the stake is physically extracted.
* **True Death Conditions:** Staking inflicts catatonic torpor paralysis. Staking only causes **True Death (Ash Disintegration)** if combined with decapitation, direct solar exposure, or burning the staked heart in fire.

#### 2. Garlic & Allium Toxicity (Botanical Repulsion)
Garlic contains concentrated botanical compounds that act as a volatile poison against vampiric biology.
* **Sensory Disruption Aura (50 Feet):** The pungent odor of raw or burned garlic overwhelms vampiric senses. Olfactory tracking powers (such as [*Crimson Scent*](#behavioral-powers)) are completely disabled within 50 feet of a heavy garlic source.
* **Ingestion Toxicity:** Ingesting garlic causes violent stomach convulsions, esophageal blistering, and severe nausea. The vampire suffers a temporary **lockout of physical blood expenditure** for 1 hour, rendering blood healing and physical stat boosts unusable.

#### 3. Holy Water & Consecrated Liquids (Scared Wounds)
Holy water and blessed liquids react like concentrated sulfuric acid against vampiric flesh.
* **Acidic Skin Melting:** Splash contact melts outer dermis and tissue on contact, dealing agonizing burn damage that bypasses mundane physical armor.
* **Mechanical Weight (Scared Wound):** Leaves severe holy burns that inflict a persistent **-2 debuff** on all physical actions and Self-Control checks while unhealed.
* **Suppressed Regeneration:** Holy water burns **cannot** be rapidly healed in combat using [*Sanguine Knit*](#supernatural-powers). Healing localized holy burns requires **1 full night of undisturbed slumber in Native Soil** and expending **2 Blood Reserves per holy wound** (double the standard baseline cost of 1 Blood Reserve per physical injury).

#### 4. Sacred Geometry & Crucifixes (Sacred Repulsion Aura)
Faith-infused holy symbols (crucifixes, sacred seals, consecrated icons) project a barrier of spiritual repulsion against the unholy curse.
* **10-Foot Sacred Repulsion Aura:** A brandished holy symbol projects an invisible 10-foot repulsion field. A vampire attempting to enter this 10-foot radius or attack the bearer must pass a **Hard Self-Control check**.
* **Physical Touch:** Direct skin contact with a holy symbol inflicts immediate chemical searing burns and stuns the vampire for 1 combat round.

#### 5. Silver (Mythic Misconception)
Silver is a mythic misconception. While silver causes allergic silver-nitrate toxicity in lycanthropes (werewolves), silver stakes, blades, and bullets inflict standard physical damage on vampires without causing supernatural banes or suppressed regeneration.

### The Dying Echo
When a vampire meets their true death (whether by stake, sunlight, or other lethal means), their final emotional thought or dying word from their Pre-Change life erupts into a psychic shockwave. This "Dying Echo" is instantly felt by all vampires within a one-mile radius, regardless of bloodline or affiliation, serving as a grim, involuntary death knell.

* **Daytime Interruption:** If a vampire perishes during daylight hours, the psychic shockwave acts as a violent jolt. Sleeping vampires within the 1-mile radius must pass a **Self-Control** check; failure causes them to wake up in a panic during peak sunlight hours.
* **Feedback Suppression Rule (Preventing Cascade Loops):** A vampire awakened by a daylight Dying Echo who subsequently perishes during that daytime period does **NOT** trigger a secondary Daylight Interruption shockwave within the same 12-hour daytime window, preventing cascading city-wide death knell feedback loops.
* **Information Imparted:** The passive Dying Echo does *not* broadcast exact physical GPS coordinates. Instead, receiving vampires instinctively feel:
  1. An approximate **directional vector** (cardinal heading toward the death site).
  2. A **distance impression** (whether the death occurred in immediate proximity or near the 1-mile boundary).
  3. The victim's **final emotional state** (rage, terror, peaceful resignation) and their last spoken or thought word.
*(Note: Active telepathic invocations from a captive severed head override this passive limitation; see [Decapitation Telepathy Broadcast](#decapitation-head-severed)).*

### The Native Soil Dependency
A vampire is supernaturally tethered to the exact location of their creation. To maintain their immortality and strength, they must regularly rest in proximity to the soil of that land.

* **Volume Requirement & Slumber Contact:** A vampire requires no less than 3kg (roughly 2 liters) of their native soil. Portable Native Soil (3kg) only satisfies the supernatural tether while the vampire is in **stationary, undisturbed daytime slumber**. Carrying 3kg of soil in clothing, pouches, or footwear during active movement does NOT pause "[The Bleed](#the-home-sickness-regression-track-the-bleed)" timer; the soil must be laid beneath or around the resting body during daytime sleep.
* **Potency & Preservation:** Removed soil does not stay potent forever; it is a living tether that can "die."
* **Unpreserved Soil:** If kept in a dry box, bag, or otherwise neglected, the soil loses its potency after **30 days**. Once dead, the vampire must physically return to their creation site to replenish their 3kg supply.
* **Preserved Soil:** A vampire can preserve the soil indefinitely by maintaining it as a living micro-ecosystem. This requires regular watering and the introduction of earthworms and insects to keep the earth oxygenated and "alive."

#### Weaponizing & Sabotaging Native Soil
Because a vampire's life force is tethered to their 3kg of Native Soil, compromising this soil is a favored tactic of rival Covens and vampire hunters:
* **Holy Water Dousing:** Soaking a vampire's Native Soil in holy water corrupts the tether. Slumbering near holy-doused soil prevents rest, inflicts continuous holy burns while sleeping, and forces "[The Bleed](#the-home-sickness-regression-track-the-bleed)" progression to advance every 24 hours instead of every 3 days.
* **Chemical / Poison Contamination:** Salting or poisoning the soil destroys the living micro-ecosystem. Earthworms and insects die immediately, causing the soil to lose its potency in **6 days** instead of 30 days.
* **Parasitic / Diseased Infestation:** Introducing cursed or diseased parasites into the soil causes them to feed on the sleeping vampire's blood reserves during daytime slumber. The vampire wakes up at Stage 2 [Blood Starvation](#sustenance--blood-starvation-rules) with no stored blood reserves remaining.
* **Structural Containment Breach (Sci-Fi / Modern):** Native Soil preserved in high-tech containers (cryo-capsules, hydroponic terrariums) requires an intact structural seal. Shattering the glass casing, puncturing cryo-seal valves, or introducing toxic liquid chemicals breaks the 3kg soil threshold, causing the soil micro-ecosystem to die and initiating [The Bleed](#the-home-sickness-regression-track-the-bleed) after 48 hours.

#### The Home Sickness Regression Track (The Bleed)
A vampire can survive away from their preserved Native Soil for exactly 7 days. On the 8th consecutive day of absence, "Home Sickness" sets in, triggering a progressive mechanical and narrative decay known as **The Bleed**. Starting on Day 8, and every 3 days thereafter, the vampire suffers a permanent reduction in their capabilities across four distinct stages:

**Stage 1: Fading Vigor (Days 8 - 14)**
The supernatural tether stretches to its limit, causing immense metaphysical fatigue.
* **Narrative Effect:** The vampire sleeps longer and wakes up exhausted. Wounds close much slower, requiring twice the normal amount of blood to heal.
* **The Bleed (Days 8, 11, 14):** On each of these days, the vampire loses access to **1 [Supernatural Power](#supernatural-powers)**. If they run out of Supernatural Powers, the bleed targets [Behavioral Powers](#behavioral-powers) instead.

**Stage 2: The Mortal Coil (Days 15 - 21)**
The vampire's body begins to "forget" its immortality, reverting to their fragile Pre-Change state.
* **Narrative Effect:** Drinking blood no longer provides vitality; it merely prevents starvation. The mind clouds with creeping paranoia.
* **The Bleed (Days 15, 18, 21):** The vampire loses **1 Power** ([Supernatural](#supernatural-powers) or [Behavioral](#behavioral-powers)) on each of these days.

**Stage 3: Feral Desperation (Days 22 - 28)**
The "Hunger" panics, stripping away remaining humanity in a desperate bid to survive.
* **Narrative Effect:** Senses degrade or become agonizing. Light and sound become disorienting. All supernatural immunities fade—they can now catch human diseases and suffer mundane poisoning.
* **The Bleed (Days 22, 25, 28):** Once all Powers are drained, The Bleed targets base physical attributes. The vampire's core stats (Strength, Speed, Cognition) drop by one tier on each of these days.

**Stage 4: Terminal Withering (Day 29+)**
The vampire is completely untethered from the magic that sustains them.
* **Narrative Effect:** Total immune system collapse. The vampire lacks the physical strength to stand and becomes bedridden.
* **The Bleed (Day 29+):** The vampire suffers daily, unavoidable damage to their core health. A common cold or minor infection is now entirely lethal. Only being buried in their [Native Soil](#the-native-soil-dependency) can halt the decay.

##### Native Soil Recovery (Re-Rooting Track)
Once "The Bleed" has begun, the decay can only be reversed through complete earth immersion in Native Soil.

* **Immersion Requirement:** Portable resting amounts (3kg) are insufficient for recovery. To heal from The Bleed, the vampire must be **completely buried head-to-toe in pure, unadulterated Native Soil**.
* **Base Recovery Duration (10 Days Total):** Healing is a gradual process where deeper degradation takes significantly longer to mend. Reversing each stage requires consecutive days of continuous burial:
  * **Stage 4 -> Stage 3 (4 Days):** Halts terminal health decay. Reboots the immune system and stabilizes life functions.
  * **Stage 3 -> Stage 2 (3 Days):** Restores base physical attributes (Strength, Speed, Cognition) to standard tiers and normalizes sensory input.
  * **Stage 2 -> Stage 1 (2 Days):** Lifts creeping paranoia, restores blood vitality conversion, and re-awakens 50% of lost powers.
  * **Stage 1 -> Fully Healed (1 Day):** Re-awakens all remaining [Supernatural](#supernatural-powers) and [Behavioral](#behavioral-powers) powers, fully restoring the supernatural tether and resetting the 7-day safe timer.
* **Metabolic Stasis (Blood Starvation Suspension):** Complete head-to-toe burial in Native Soil places the vampire into a mystical metabolic stasis. This freezes the [Blood Starvation](#sustenance--blood-starvation-rules) clock entirely while underground, preventing nutritional decay during the 10-day recovery process.
* **Thrall Blood Sacrifice (Accelerated Recovery):** If multiple [Thralls](#social) drain their blood directly into the soil surrounding the buried vampire, the total burial time is **cut in half (5 days total)** (2 days for Stage 4, 1.5 days for Stage 3, 1 day for Stage 2, and 12 hours for Stage 1).
* **Interruption Penalty (Short, Moderate & Prolonged Tiers):** If a buried vampire is unburied or removed from their Native Soil during recovery:
  * **Brief Interruption ($\le$1 Hour):** Pauses Re-Rooting progress without penalty.
  * **Moderate Interruption (1 to 24 Hours):** Halts recovery at current progress and inflicts metaphysical shock, adding **1 additional day (24 hours)** of required burial time to the remaining recovery duration. This +24hr penalty is static and immune to Thrall acceleration.
  * **Prolonged Interruption (>24 Hours):** Resets current Re-Rooting progress for the active stage back to Day 0, and [The Bleed](#the-home-sickness-regression-track-the-bleed) resumes decaying downward.

### Dismemberment & Decapitation

#### Dismemberment (Severed Limbs)
* **Accelerated Re-attachment (Requires Accelerated Mend):** If a severed arm or leg is retrieved and pressed against the stump, a vampire possessing the [*Accelerated Mend*](#supernatural-powers) power can spend blood to supernaturally re-fuse bone, muscle, and nerve endings in **1 combat round**.
* **Surgical / Medical Sewing:** A severed limb can be manually stitched back onto the shoulder, arm, leg, or hip stump by surgical or medical means. Once bandaged and sewn in place, re-fusing the limb requires **12 hours of physical recovery** (without requiring full Native Soil burial).
* **Native Soil Re-attachment & Regrowth (Without Accelerated Mend or Surgery):** If a severed limb is completely destroyed (burned or dissolved) or left unstitched, regrowing a new limb requires **24 hours of undisturbed slumber in Native Soil**.
* **Autonomous Limb Action:** A severed limb remains supernaturally animated for up to 1 hour post-dismemberment. The vampire can telepathically command the severed limb to twitch, crawl, or grapple enemies.

#### Decapitation (Head Severed)
* **Life & Power Logic:** The heart is the ultimate source of a vampire's immortal existence (circulating vitae). Because the head is not the source of life, decapitation alone does **not** cause True Death; the vampire remains living indefinitely. However, the head (brain) is the controller of supernatural powers and blood flow. Severing the head breaks signal transmission to the heart, disabling [*Accelerated Mend*](#supernatural-powers) and all other active powers.
* **Blood Reserve Disconnect & Brain Torpor (24-Hour Cap):** A severed head is disconnected from the heart reservoir and holds **0 Blood Reserves**. Without blood flow or re-attachment, the severed head can only maintain sensory consciousness for a maximum of **24 hours**. On hour 24, the severed head lapses into **Brain Torpor** (eyes close, ears go deaf, telepathy shuts down) until re-attached to the torso.
* **Incapacitation:** While decapitated, the body is completely paralyzed and immobile. The severed head remains conscious (eyes can see, ears can hear, mouth can speak), but cannot activate any supernatural powers or move the body.
* **Re-attachment Methods & Durations:** To re-attach a severed head, the head must be placed back onto the neck stump using one of four specific methods:
  1. **Maker's Blood Bath (Fastest):** Placing the head on the stump while submerged in a tub of the Maker's blood re-fuses the neck in **1 combat round** (instantaneous).
  2. **Native Soil Burial:** Placing the head on the stump and burying the entire body in [Native Soil](#the-native-soil-dependency) takes **6 hours** (1 daytime slumber).
  3. **Surgical / Medical Sewing:** Stitching the head back onto the neck stump takes **12 hours** of physical recovery.
  4. **Manual Holding:** Holding the head tightly against the neck stump without moving takes **24 continuous hours** of manual pressure.
* **Heart Destruction & Active Telepathic Broadcast:** If the torso/heart of a decapitated vampire is destroyed while their severed head is held captive elsewhere, [The Dying Echo](#the-dying-echo) erupts from the torso's location. The severed head experiences the shockwave in real-time. If the vampire possesses mental or telepathic powers (*Mind Tear*, *Bloodline Memory*, or Sire tethers), the head can expend its final 6-second window to execute an **active, conscious telepathic broadcast**—transmitting a specific 3-word vocal message, captor identity, or exact landmark description to their Sire or Coven, overriding the passive Dying Echo limitation through active mental effort.

## Life

The life of a vampire is broken into 2 phases, [pre-change](#pre-change) and [post-change](#post-change).

### Pre-Change

Pre-Change represents life before being turned into a vampire—the reservoir where the human soul, moral convictions, and core identity reside.

* **Humanity Anchors (Selection & Categories):** Every vampire retains 1 to 3 "Anchors" from their Pre-Change life. During character generation, Anchors are selected from three distinct categories:
  * **Mortal Anchor:** A surviving human loved one, family member, spouse, or direct bloodline descendant.
  * **Sanctum Anchor:** A specific physical location, ancestral estate, or birthplace sacred to the vampire's mortal memories.
  * **Ideal / Relic Anchor:** A sacred personal oath, unshakeable moral code, or cherished physical heirloom carried from mortal life.
* **Anchor Mechanics (Restoring Sanity):** Visiting, protecting, or communing with a Pre-Change Anchor soothes the volatile Beast, **restoring 1 lost Self-Control point per scene**.
* **Anchor Destruction (Permanent Scarring & Replicas):** If an Anchor is destroyed, corrupted, or killed (such as failing an Anchor Break check), the vampire's soul suffers a severe tear, inflicting a **permanent -1 penalty to all future Self-Control checks**. Rebuilding a destroyed Sanctum estate or replacing a destroyed relic creates a physical replica, but does **NOT** restore the original emotional soul tether or remove the permanent -1 Self-Control penalty.

### Post-Change

Post-Change represents the ongoing struggle between lingering Pre-Change Humanity and the ravenous Post-Change Hunger.

* **The 5-Stage Humanity vs. Hunger Track:**
  * **Stage 5: Mortal Empathy:** The vampire maintains strong moral boundaries and emotional connection to mortals. No penalties near exposed blood.
  * **Stage 4: Detached Guardian:** The vampire feeds reluctantly, feeling minor irritation at mortal fragility and emotional drama.
  * **Stage 3: Predatory Pragmatism:** The vampire views mortals primarily as blood vessels and hunting livestock. Inflicts a **+1 difficulty penalty** on all empathy or social checks with mortals.
  * **Stage 2: Cold Monster:** Complete emotional numbness set in. The scent of exposed blood triggers an immediate **Self-Control frenzy check**.
  * **Stage 1: Feral Degradation:** The vampire exists on the razor's edge of permanent frenzy. Only active contact with a remaining Pre-Change Anchor prevents total, permanent loss of sanity.
* **The Feral State:** When blood-starved, severely wounded, or forced to commit horrific atrocities, the vampire must pass a **Humanity / Self-Control** test (see [Behavioral Powers](#behavioral-powers)). Failure plunges the vampire into a **Feral State**:
  * **Combat Instinct:** The vampire gains heightened physical ferocity (+1 melee damage bonus).
  * **Cognitive Loss:** The vampire loses the ability to use complex mental or emotional [Behavioral Powers](#behavioral-powers) (such as *Lethe’s Touch*, *Siren’s Cadence*, or *Mind Tear*).
  * **Predatory Fixation (Drinking vs. Draining):** The vampire MUST prioritize feeding upon the nearest blood source. Crucially, a blood-starved vampire in a Feral State instinctually **drinks** (restrained feeding to restore reserves to Stage 1), rather than aggressively draining to kill. However, if a Feral vampire consciously or frenziedly chooses to **drain** a victim while starving, their volatile hunger makes stopping at Stage 4 extremely difficult—requiring a **Hard Self-Control check** to avoid accidentally taking the final drop and triggering the True Death Cascade!
  * **The Anchor Break Check:** If a Feral vampire's nearest target or focal point is one of their own **Pre-Change Anchors** (a living loved one, a physical Sanctum/location, a cherished Relic, or a sacred Oath), the human soul violently resists the Beast. The vampire must immediately make a **Hard Self-Control check**:
    * *System-Agnostic "Hard" Check Definition:* A "Hard" difficulty check represents an extreme hurdle against a vampire's predatory instinct. In D20/attribute systems, apply a severe static penalty (-3 to -5 penalty to the roll or +3 to DC). In D10/D6 dice-pool systems, double the required success threshold (e.g., 4 successes instead of 2) or roll at Disadvantage / maximum difficulty tier.
    * *Success:* Sheer emotional horror snaps the vampire out of the Feral State immediately, halting the frenzy.
    * *Failure (Anchor Destruction):* The Beast overrides humanity, permanently destroying the Anchor:
      * **Mortal Anchors:** The frenzied Beast drains and slays the living loved one.
      * **Sanctum / Location Anchors:** In a bloodless frenzy, the Beast physically desecrates, burns, or demolishes the birthplace/estate.
      * **Relic / Heirloom Anchors:** The Beast violently smashes, shatters, or snaps the physical heirloom in half.
      * **Ideal / Oath Anchors:** The Beast forces the vampire to commit an unpardonable atrocity that directly and irrecoverably violates their sacred moral oath.

## Mechanics

### Draining

Draining is done to destroy the life of the victim, either to outright kill them or for [creation](#creation). Draining does not mean [drinking](#drinking--sustenance-rules) all of the victim's blood. Drinking the last drop must never be done. Consuming the final drop binds the vampire to the victim's death, triggering catastrophic consequences based on the victim's nature:
1. **Consuming the Final Drop of a Mortal:** Instantly severs the supernatural life tether, causing the vampire to perish immediately beside the mortal (**True Death**).
2. **Consuming the Final Drop of an Immortal / Vampire (Diablerie Attempt):** Triggers a violent metaphysical feedback shockwave. The drinker's body and internal organs instantly calcify into grey granite, plunging the vampire into an **Eternal Petrified Torpor (Eternal Slumber)**! (Note: Starving vampires in a Feral State who choose to drain must pass a **Hard Self-Control check** to avoid taking the final drop).

**The Brink of Death Progression**
To survive the creation process, the sire must pull away at the absolute brink of death. The victim's body goes through four distinct physiological stages of shutdown during a drain:

1. **Color Fade:** The victim's skin rapidly loses its flush as blood volume drops, turning pallid and ashen.
2. **Sunken Skin:** Extreme fluid depletion sets in. The loss of fundamental fluids causes the skin to visibly tighten and sink against the bone structure.
3. **Lack of Breath:** The lungs cease functioning. The victim's chest stops rising.
4. **Lack of Heartbeat:** Complete loss of blood pressure causes the heart to seize and stop. *The final drop is consumed mere milliseconds after this cue.*

**Knowing When to Stop**
Navigating these cues requires experience or raw willpower.
* **Unlearned Sires:** Vampires who have never successfully sired a fledgling act primarily on instinct. To stop after Stage 4 but before the final drop, they must rely on a **Sensory** [behavioral power](#behavioral-powers) or pass a **Self-Control** check. Failure means they take the last drop and die. Stopping prematurely results in a botched [mutation](#mutations).
  * **Crimson Scent Integration:** An Unlearned Sire who possesses the **Crimson Scent** [behavioral power](#behavioral-powers) gets an **automatic success** on this check. Because they can literally smell the micro-fluctuations in blood flow and hear/smell the victim's heartbeat halting in real-time, they instinctually know the exact millisecond to pull away.
* **Learned Sires:** Vampires who have successfully navigated creation before instinctively recognize the progression and no longer require a check to stop at the precise moment.

#### Drinking & Sustenance Rules

Drinking is done to sustain the life of the vampire. This is the sucking/drinking of blood from living victims (including animals). When a vampire drinks from a victim, they do so with restraint and in moderation to keep their meal alive. Drinking can be done from both willing and unwilling victims.

##### Blood Capacity, Growth Track & Passive Awakening Drain
All newly turned vampires begin with a baseline heart reservoir pool of **10 Blood Reserves** (each draft of ~250ml living mortal blood restores 1 Blood Reserve). Over centuries of unlife, as the vampire's undead heart calcifies and deepens its metaphysical blood reservoir, their maximum Blood Reserve capacity permanently expands.

* **Blood Reserves Aging Progression Track:**
  1. **Base Pool (Neonate / 0–249 Years):** 10 Blood Reserves.
  2. **Every 250 Years Post-Change:** The vampire gains **+1 Blood Reserve**.
  3. **Every 500 Years Post-Change:** The vampire gains an additional **+1 Blood Reserve** (+2 total at 500-year milestones).
  
  * **Age & Capacity Milestones (First 2,000 Years):**
    * **0 – 249 Years (Neonate):** 10 Blood Reserves
    * **250 Years:** 11 Blood Reserves (+1 from 250yr cycle)
    * **500 Years (Elder):** 13 Blood Reserves (+1 from 250yr cycle + 1 from 500yr milestone = 13 total)
    * **750 Years:** 14 Blood Reserves (+1 from 250yr cycle)
    * **1,000 Years:** 16 Blood Reserves (+1 from 250yr cycle + 1 from 500yr milestone = 16 total)
    * **1,250 Years (Ancient):** 17 Blood Reserves (+1 from 250yr cycle)
    * **1,500 Years:** 19 Blood Reserves (+1 from 250yr cycle + 1 from 500yr milestone = 19 total)
    * **1,750 Years:** 20 Blood Reserves (+1 from 250yr cycle)
    * **2,000 Years:** 22 Blood Reserves (+1 from 250yr cycle + 1 from 500yr milestone = 22 total)
  
  4. **Millennial Scaling (After 2,000 Years Post-Change):** Once a vampire survives past 2,000 years, the heart reservoir scales at a flat rate of **+2 Blood Reserves every 250 years**. 500-year milestone bonuses no longer apply after 2,000 years (e.g. 2,250 years = 24 Reserves; 2,500 years = 26 Reserves; 2,750 years = 28 Reserves; 3,000 years = 30 Reserves).

* **Physiological Rationale (Power, Siring & Thrall Dominance):** This mathematical expansion of blood reserves directly explains the staggering dominance of Elders and Ancients:
  * *Multi-Power Maintenance:* Holding 16 to 22+ reserves allows an Ancient to sustain multiple continuous powers (*Kinetic Barrier*, *Psychic Fortress*, *Pyre Aura*) simultaneously for an entire night without risking exhaustion.
  * *Siring Capacity:* Siring requires expending 5 Blood Reserves; a neonate with 10 reserves is drained to half capacity upon creating progeny, whereas an Ancient with 22 reserves barely notices the expenditure.
  * *Thrall Network Maintenance:* Maintaining extensive networks of mortal Thralls and feeding multiple fledglings becomes effortless as reserve capacity expands.

* **Passive Daytime Awakening Burn:** Every night at sunset, awakening from daytime slumber automatically consumes **1 Blood Reserve** to re-energize dead tissues and rouse consciousness.
##### Action Economy & Combat Turn Structure
In tactical combat, each vampire operates within a structured Action Economy on their turn:
1. **1 Main Action:** Execute a physical/weapon attack, cast an `Activated` power (*Hellfire Orb*, *Combust Vitae*, *Kinetic Blast*), or perform a complex skill task.
2. **1 Movement / Minor Action:** Move base distance, retrieve an item, or switch an `Innate Toggle` power.
3. **Continuous Upkeep (Start of Turn):** Expend required maintenance blood (1 Reserve per power) to sustain active `Sustained` powers (*Kinetic Barrier*, *Pyre Aura*, *Crimson Mist*).
4. **1 Off-Turn Reaction / Defense:** Execute a physical Dodge check or invoke a reactive defense (*Veil Flicker* teleport).

##### Categorized Per-Round Expenditure Caps (Age Tier Scaling)
To prevent physical vascular burnout while allowing ancient vampires to unleash their vast blood reservoirs, the total maximum blood reserve expenditure per combat round scales directly by **Age Tier**:
* **Neonate Tier (<500 Years):** Maximum **2 Blood Reserves / Combat Round** across all actions (e.g. 1 Surge + 1 Sustained Power, or 1 Sustained + 1 Healing).
* **Elder Tier (500–1,199 Years):** Maximum **3 Blood Reserves / Combat Round** across all actions (e.g. 1 Surge + 1 Sustained + 1 Healing, or 2 Sustained + 1 Surge).
* **Ancient Tier (1,200+ Years):** Maximum **4 Blood Reserves / Combat Round** across all actions (e.g. 2 Sustained + 1 Surge + 1 Healing, or 3 Sustained + 1 Activated Power).

* **Sub-Cap Allocations & Perks:**
  * **Blood Surge Cap (1 Reserve):** Grants a **+2 bonus** to Strength, Speed, or Initiative for 1 round **OR** grants **1 Extra Minor/Movement Action** on your turn. *Single-Stat Overwrite Cap:* Executing a new Blood Surge on a subsequent combat round immediately overwrites previous surge stat bonuses. Subject to the per-round expenditure cap, a vampire can only maintain a single +2 Blood Surge stat bonus (+2 Strength OR +2 Speed OR +2 Initiative) at any given moment.
  * **Active Power Maintenance Cost:** Ongoing `Sustained` powers consume **1 Blood Reserve per power per combat round** to sustain after activation.
  * **Sanguine Knit Healing Cap (1 Reserve):** Heals **1 physical wound** per round (max 1 wound/round, strictly affecting self).
  * **Master Power 0-Cost Advantage:** Because Master Powers possess a **0-Reserve initial activation cost**, invoking a Master Power does NOT count toward the per-round expenditure cap on the turn it is cast (blood is spent strictly for subsequent sustained upkeep).
* **Over-Push Strain (Exhaustion at 0 Reserves):** If a vampire holding **0 Blood Reserves** attempts to perform a Blood Surge, sustain an active power, or heal a physical wound, they suffer **Over-Push Strain**: taking **1 Direct Core Health Damage** (or triggering an immediate Self-Control check to enter the [Feral State](#post-change)).

##### Universal Age Tier Superiority Modifier System
Whenever two vampires engage in direct inter-vampire interaction (opposed mental battles, fear checks like *Visage of the Abyssal Nightmare* vs *Sovereign Temperament*, command checks like *Imperious Word*, telepathic probe defense, blood bond enforcement, or physical grapples/struggles), mechanical checks are modified by the relative age difference between the combatants:

* **Neonate Tier (<500 Years):** Baseline Modifier (**0**).
* **Elder Tier (500–1,199 Years):** **+1 Mechanical Bonus** against Neonates (or Neonates suffer a **-1 Penalty** when opposing Elders).
* **Ancient Tier (1,200+ Years):** **+2 Mechanical Bonus** against Neonates, and **+1 Mechanical Bonus** against Elders (or lower tiers suffer corresponding penalties when opposing Ancients).

*Application Note:* This modifier stacks with power bonuses (such as *Sovereign Temperament*'s +2 bonus on fear checks), reflecting how the overwhelming metaphysical pressure of ancient blood inherently dominates younger vampires.

##### Blood Quality Tiers
Not all blood provides equal nutritional and metaphysical value:

* **Tier 1: Animal Blood (Stale / Low Potency):** Draining animals (rats, dogs, cattle) staves off [Blood Starvation](#sustenance--blood-starvation-rules), but tastes like dry copper ash. Animal blood **cannot** be used to fuel [Supernatural Powers](#supernatural-powers) or Blood Surges.
* **Tier 2: Mundane Mortal Blood (Standard Potency):** Standard feeding source from living humans. 1 draft (~250ml) restores **1 Blood Reserve**, fully fueling basic powers, healing, and physical abilities.
* **Tier 3: High-Vibrancy / Hero Blood (Adrenaline & Magical Potency):** Blood drawn from passionate, adrenaline-filled, or magically infused mortals. 1 draft restores **2 Blood Reserves** and grants a **+1 bonus to physical actions** for 1 hour.
  * **Non-Stacking & Adrenaline Burnout:** Drinking multiple drafts of Hero Blood within the same hour resets the 1-hour duration, but does **NOT** stack the physical bonus (+1 physical action bonus maximum). Once the 1-hour bonus expires, the intense adrenaline and magical vibrancy wear off, inflicting a temporary **-1 penalty to physical actions for 1 hour** due to neural burnout.
* **Tier 4: Elder Vitae (Concentrated Ancient Power - 500 to 1,199 Years):** Blood drawn from Elder vampires (500–1,199 years). 1 draft restores **3 Blood Reserves** and grants a temporary 1-round free power invocation.
* **Tier 5: Ancient Vitae (Primordial Power - 1,200+ Years):** Blood drawn from Primordial Ancient vampires (1,200+ years). 1 draft restores **4 Blood Reserves**, grants all Tier 4 Elder benefits, and unlocks **Permanent Power Gain & Soul Strain Risk**.

##### The Effects of Drinking Elder Blood (500–1,199 Years)
Drinking the blood of an Elder (500–1,199 years) is an intoxicating, dangerous experience:
* **The High-Power Surge:** Ingesting Elder Vitae grants an immediate burst of ancient energy, allowing the drinker to invoke 1 free power without expending blood reserves.
* **Rival Lineage Static Bypass:** Temporarily neutralizes the -2 penalty on mental control powers against that Elder's rival bloodline for 24 hours.
* **Vitae Euphoria & Addiction Risk:** Elder blood is hyper-addictive. Upon drinking Elder Vitae, a neonate must pass an immediate **Self-Control check**. Failure inflicts *Vitae Euphoria*—the neonate becomes addicted to Elder blood, viewing mundane human blood as bland ash and suffering a -1 penalty to Self-Control checks when denied Elder Vitae.
* **Lingering Psychic Siphon:** The drinker absorbs residual psychic memories of the Elder. For 24 hours post-ingestion, the drinker experiences vivid first-person flashback flashes of the Elder's past centuries and personal rivalries.

##### The Effects of Drinking Ancient Blood (1,200+ Years)
Drinking the blood of a Primordial Ancient (1,200+ years) represents the ultimate threshold of vampiric alchemy, granting unprecedented rewards alongside catastrophic psychological risks:
* **All Tier 4 Elder Benefits Included:** Ingesting Ancient Vitae yields 4 Blood Reserves, High-Power Surge, Rival Lineage Static Bypass, and 24-hour Psychic Memory Siphon.
* **The Primordial Resonance (Unified Ancient Web):** All 1,200+ year Ancients are telepathically and metaphysically tethered across the globe via a collective ancestral web of bloodline magic known as *The Primordial Resonance*.
  * **Anti-Battery Farm Rule (Century Cap Across All Ancients):** Because all Ancients draw from this same unified web, a vampire can only acquire a permanent power slot from Ancient Vitae **ONCE PER CENTURY IN TOTAL across all Ancients** (not once per Ancient). Subsequent drafts from other Ancients within the same century yield 4 Blood Reserves and Elder benefits, but **no additional permanent power slot**.
  * **Primordial Telepathy:** Ancients can communicate telepathically across planetary distances via the Resonance.
  * **Ancient Death Shockwave:** When an Ancient perishes, a massive surge of energy ripples through the Resonance, temporarily empowering all neonates currently holding Ancient Vitae for 1 night (+1 to all power activation rolls).
* **Permanent Power Gain (Non-Lethal Ingestion):** Ingesting 1 full draft (~250ml) from a living Ancient **permanently grants 1 new Power Slot** (randomly selected from the Ancient's power sheet or bloodline latency). Subject to the *Primordial Resonance Century Cap* above.
* **Soul Strain Risk (Non-Lethal):** The drinker must pass an immediate **Hard Self-Control check** upon drinking; failure inflicts permanent mental derangement or leaves a persistent, echoing psychic voice of the Ancient in their head.
* **Full Diablerie of an Ancient (Consuming the Final Heart Drop):** Attempting to consume the absolute final drop of an Ancient's heart triggers an immediate, un-soakable blood feedback shockwave. The drinker's body and internal organs instantly calcify into grey granite, plunging the vampire into an **Eternal Petrified Torpor (Eternal Slumber)** beside the Ancient's desiccated remains!

##### Blood Surge (Physical Boost)
A vampire can actively force pressurized blood through their muscular system to perform a **Blood Surge**:
* **Mechanism:** The vampire expends **1 Blood Reserve** to gain a temporary **+2 bonus to Strength, Speed, or Initiative** for 1 combat round. (Subject to the **1 Blood Surge per round cap** defined under [Blood Capacity](#blood-capacity--passive-awakening-drain)).

##### Sustenance & Blood Starvation Rules
Unlike ["The Bleed"](#the-home-sickness-regression-track-the-bleed) (which is triggered by separation from Native Soil), **Blood Starvation** represents physical nutritional depletion. 
* **Interplay with Blood Reserves:** As long as a vampire holds **1 or more stored Blood Reserves**, consuming 1 reserve at sunset maintains **Stage 1 (Satiated)** status.
* **Starvation Initiation (0 Reserves):** The 3-day **Blood Starvation** progression initiates strictly when a vampire's stored Blood Reserves reach **0**:
  * **Stage 1: Satiated / Running on Fumes (Days 1–3 at 0 Reserves):** Vitality remains intact, but no blood reserves remain for active power expenditure or physical healing.
  * **Stage 2: Mild Starvation / The Edge (Days 4–7 at 0 Reserves):** The Hunger panics. The vampire suffers a **+1 difficulty penalty** on all Self-Control checks near exposed blood or wounded mortals.
  * **Stage 3: Severe Starvation / Feral Degradation (Days 8–14 at 0 Reserves):** Physical degradation sets in. Physical healing and supernatural blood expenditures are completely disabled. Cognitive actions suffer penalties, and any damage taken triggers an immediate frenzy check to enter the [Feral State](#post-change).
  * **Stage 4: Torpor / Desiccation (Days 15+ at 0 Reserves):** The vampire's body completely dries out and collapses into a mummified, paralyzed state of **Torpor**.
  * **Phase 1 Awakening (Single Drop - Sensory Consciousness):** Placing a single drop of living blood onto a Torpid vampire's lips immediately awakens sensory consciousness (eyes open, ears hear, mouth can speak weakly), but the physical body remains completely desiccated and paralyzed. If no further blood is supplied, the vampire remains paralyzed in conscious agony.
    * **Mental Torpor Drift (24-Hour Safety Valve):** If a vampire awakened to Phase 1 Sensory Consciousness receives no further blood within **24 hours**, their mind naturally drifts back into unconscious Torpor, ending the forced sensory state and preventing endless torture loops.
  * **Phase 2 Awakening (~250ml / 1 Draft - Physical Rousing):** Consuming a full draft (~250ml) of living blood restores motor function and rouses the body out of paralysis, restoring the vampire to **Stage 3 (Severe Starvation / Feral Degradation)**.
  * **Rousing Frenzy Check (Target Priority):** Because the vampire rouses at Stage 3 Starvation, the sudden surge of vitality triggers an immediate **Self-Control check**. Failure causes the ravenous vampire to instantly attack the nearest blood vessel—prioritizing living mortal blood first, followed by stored blood bags, and finally attempting to bite the rescuer's undead throat if no mortal blood is present!

### Feeding

Feeding is solely used for vampire creation. Once a victim has been [drained](#draining), they have to immediately be fed.

This is achieved by the vampire opening his/her wrist and letting their own blood flow into the mouth of the victim; or if technology allows, syringe injection into the heart of the victim.

## Powers

A vampire gains its powers during creation, from the [feeding](#feeding) process. A newly created vampire's power is dictated by the strength of their Maker and the latent traits hidden deep within their bloodline.

Vampires gain +1 additional power for each 150 years [post-change](#post-change). As an example, a vampire who is 1,200 years post-change could potentially have between 13-16 total powers (this includes [supernatural powers](#supernatural-powers) and [behavioral powers](#behavioral-powers)).

**Power Classification & Activation Cost Framework**
Every power within the [Behavioral Powers](#behavioral-powers) and [Supernatural Powers](#supernatural-powers) pools is mechanically categorized into one of three activation tiers:

1. **`Innate` (Passive / Toggleable / Composite - 0 Reserves):**
   * **Mechanism:** Woven into the vampire's physiology, bloodline, or presence. Requires zero blood reserves to maintain or invoke.
   * **Sub-Types:**
     * **`Innate Passive` `[0 Reserves]`:** Always active, permanent biological or supernatural traits (*Resonance Tasting*, *Crimson Scent*, *Sovereign Temperament*, *Unholy Primacy*, *Anointed Flesh*, *Alchemical Assimilation*, *Bane-Blindness*, *Earthbreaker*, *Spider's Grace*).
     * **`Innate Toggle` `[0 Reserves]`:** Always present, can be freely toggled on/off at will without blood cost (*Glamour of the Velvet Apex*, *Mask of Mortality*).
     * **`Innate Composite` `[Master Powers - 0 Reserves Activation]`:** Holding a Master Power slot passively grants all listed sub-powers. Sub-powers cost **0 Blood Reserves to activate** (free initial invocation), burning blood only when sustained. *Sub-Power Re-Roll Rule:* If a vampire acquires a Master Power (or possessed minor sub-powers before acquiring the Master Power), any pre-existing or duplicate minor sub-powers bestowed by that Master Power are automatically discarded and re-rolled for new distinct power slots.
2. **`Activated` (Instant / One-Time Invocation):**
   * **Mechanism:** A sharp expenditure of pressurized blood to invoke an immediate spell, attack, telepathic strike, or physical surge.
   * **Cost & Duration:** **1 Blood Reserve per invocation** (unless modified by Master Powers). Lasts for **Instantaneous (1 action/attack)** for combat strikes/teleports (*Veil Flicker*, *Hellfire Orb*, *Kinetic Blast*, *Sanguine Spike*), or **1 Scene** for mental/social/necromantic spells (*Siren's Cadence*, *Blood Harmonic*, *Mind Tear*, *Imperious Word*, *Lethe's Touch*, *Bloodline Memory*, *Rise of the Slumbering*, *Corpse Siphon*, *Soul Bind*).
3. **`Sustained` (Continuous / Active Upkeep):**
   * **Mechanism:** Ongoing, continuous physical transformations, dense shields, illusions, or mind-control tethers requiring active maintenance.
   * **Cost & Duration:** **1 Blood Reserve to activate + 1 Blood Reserve per upkeep cycle** (1 Reserve/Round in combat, 1 Reserve/Hour for Swarm Pocket-Realms, 1 Reserve/Day for Petrified Slumber).
   * *Per-Round Limit:* Subject to the **Total Per-Round Expenditure Cap** (max 2 reserves spent per round across all actions). If reserves reach 0, sustained powers immediately collapse.

### Combined Power Usage & Synergistic Scaling Matrix
When a vampire invokes two or more powers simultaneously (or multiple vampires pool their magic), their supernatural effects interweave:

1. **Per-Round Expenditure Cap Constraints:** Combining multiple active or sustained powers in combat MUST strictly respect the [Total Per-Round Expenditure Cap](#blood-capacity--passive-awakening-drain) for the vampire's age tier (Neonate = max 2 reserves/round; Elder = max 3 reserves/round; Ancient = max 4 reserves/round).
2. **Synergistic Pair Bonus (+1 Mechanical Enhancement):** Activating two complementary powers within the same scene or combat round unlocks a **+1 Synergy Bonus** to checks, range, or damage for both powers:
   * *Sensory Synergy (*Thermal Vitae Vision* + *Nyctophilous Apex Sight*):* Grants FLIR heat-mapping in pitch-black void with +1 perception tracking bonus.
   * *Psychic Dread Synergy (*Visage of the Abyssal Nightmare* + *Blood Harmonic*):* Injects terror directly into the victim's nervous system, imposing an additional **-1 penalty** on the target's fear resistance check.
   * *Elemental Force Synergy (*Pyre Aura* + *Umbral Blade*):* Ignites shadow whips in hellfire, adding **+1 fire damage** to shadow strike hits.
3. **Age Tier Synergy Scaling:**
   * **Neonates (<500 Years):** Standard +1 synergy bonus; standard power ranges.
   * **Elders (500–1,199 Years):** **+50% Range & Area Multiplier:** Synergy pairs invoked by Elders expand their effective range or blast radius by +50% (e.g. *Kinetic Blast* knockback expands to 30 feet).
   * **Ancients (1,200+ Years):** **Doubled Range & Area Multiplier (+100%):** Synergy pairs invoked by Ancients double their effective range or area radius, and grant a **+2 Synergy Bonus** instead of +1.
4. **Opposing Power Neutralization (Elemental Cancellation):** Invoking diametrically opposed supernatural elements simultaneously (*Grave Chill* ice wave vs *Pyre Aura* hellfire) causes thermal shock collapse, instantly **extinguishing and neutralizing both powers** with zero mechanical effect.
5. **Coven Power Ritual Nexus (Multi-Caster Stacking & Sequential Rotation):**
   When multiple vampires of the same Coven or bloodline simultaneously cast or sustain the exact same power on the same target, they form a **Coven Power Ritual Nexus**:
   * **Coven Stacking Math:** The Lead Caster establishes the baseline power check/DC. Each assisting caster adds a **+1 Coven Stacking Bonus** to the Lead Caster's check/DC (+1 per assisting member).
   * **Age Tier Caster Caps:** Neonate-led Coven = max **3 Casters** (Max +2 Bonus); Elder-led Coven = max **5 Casters** (Max +4 Bonus); Ancient-led Coven = max **7 Casters** (Max +6 Bonus).
   * **Sequential Rotation Upkeep (1 Reserve/Round Total):** The ritual nexus consumes **1 Blood Reserve per round in total** to maintain. Participating members take turns in sequential round-robin rotation (1 member pays 1 Reserve on their turn while the remaining members pay 0 Reserves that round). Because each member pays 1 Reserve once every $N$ rounds, all members remain under their per-round expenditure caps, retaining cap space for combat actions.
   * **Target Disruption Counterplay:** Disrupting an assisting member (damage, stun, knockback) removes their **+1 Coven Stacking Bonus** and skips them in the rotation sequence. If the current round's paying member is disrupted before paying their 1 Reserve, the next member in the rotation sequence must immediately pay 1 Reserve to prevent the ritual from collapsing.

**Power Fade & Inheritance**
Because all newly created vampires are born into the modern era, they generate their starting power slots using the [New World](#new-world) base. However, the creation process inherently causes a degradation of power from Maker to fledgling known as the "Power Fade." To determine a fledgling's starting powers, follow this process:

1. **Roll Base:** The fledgling rolls the New World base: 1 Supernatural power and 1d2+1 Behavioral powers.
2. **Ancestral Inheritance Scaling (Sire Potency Bonus):** The fledgling's starting pool scales with the age tier of their Maker:
   * **Sired by Neonate (<500 yrs):** Standard starting roll (1 Supernatural + 1d2+1 Behavioral).
   * **Sired by Elder (500–1,199 yrs):** Gains **+1 bonus starting Behavioral power slot**, reflecting elder bloodline potency.
   * **Sired by Ancient (1,200+ yrs):** Gains **+1 bonus starting Supernatural power slot AND +1 bonus starting Behavioral power slot**, reflecting primordial bloodline magic.
3. **The Power Fade (Cap):** A fledgling's total power count can never exceed their Maker's total minus one (Maker's Total - 1). If the fledgling's rolled slots exceed this limit, they must discard excess slots of their choice until they meet the limit.
4. **Mutation Risk & Siring Hubris:** If the Power Fade forces a fledgling's starting Supernatural or Behavioral slots down to 0, the creation botches, resulting in a [Power Fade Collapse Mutation](#mutations).
   * *Narrative Warning (The Hubris of Young Sires):* This mathematical bottleneck is an intentional physiological law designed to deter young, weak vampires from attempting to pass on the curse. A New World sire possessing only 2 or 3 total powers will mathematically force their fledgling down to 0 slots, virtually **guaranteeing a botched, mutated offspring**. To safely sire a healthy fledgling without mutation risk, a Maker should possess at least 4 or 5 total powers.
5. **Bloodline Latency (Manifestation):** A fledgling does not automatically inherit their exact Maker's powers. Instead, powers are drawn randomly from the broader power pools. This represents dormant ancestral traits awakening within the fledgling's newly turned blood.

#### Behavioral Powers

These powers project inward to control the vampire’s Beast or outward to manipulate the minds, memories, and emotions of mortals and weaker vampires.

**Charismatic**
* **Siren’s Cadence `[Activated - 1 Reserve | Duration: 1 Scene]`:** Your voice vibrates at a subconscious harmonic. Mortals hear your words like distant velvet music; their eyes grow heavy with agreeable compliance, instinctively rationalizing your suggestions as their own original thoughts while a faint scent of jasmine and ozone lingers in the air. *Live Vocal Presence Requirement:* Siren's Cadence relies on live supernatural vitae harmonics projected directly from the vampire's living vocal cords and aura. Digital or analog audio recordings stripped of the vampire's physical aura lose all supernatural compel properties, functioning as ordinary recorded speech.
* **Glamour of the Velvet Apex `[Innate Toggle - 0 Reserves | Duration: Continuous Toggle]`:** You project an irresistible, intoxicating aura of primordial beauty and absolute safety. Mortals in your presence feel a sudden rise in body temperature, hyper-fixating on your gaze while their heartbeats race with a mixture of romantic infatuation and subconscious surrender.

**Emotional**
* **The Cold Hush `[Activated - 1 Reserve | Duration: 1 Scene]`:** You reach outward with invisible cold tendrils to freeze a target's emotional core into silent marble. Panicked screaming crowds instantly fall into an unnatural, glassy-eyed hush; angry violent attackers drop their weapons as their rage vanishes into a hollow void of absolute indifference.
* **Blood Harmonic `[Activated - 1 Reserve | Duration: 1 Scene]`:** By locking eyes with a target, you inject a sudden surge of violent emotional frequency directly into their nervous system. You can force a calm mortal into a screaming frenzy or twist an enemy's hatred into weeping, subservient adoration within a single heartbeat. *Direct Visual Line-of-Sight Requirement:* Blood Harmonic requires direct, unmediated visual line-of-sight in physical space. Digital video screens, mirror reflections, and CCTV camera feeds filter out the vampire's physical gaze harmonic, rendering remote video casting impossible.
* **Visage of the Abyssal Nightmare `[Activated - 1 Reserve | Duration: 1 Scene (1-Round Fear Stun)]`:** You project pure, unadulterated dread. For a split second, your shadow stretches unnaturally and your iris turns into a pitch-black void. The target experiences a sudden drop in ambient room temperature and a roaring ringing in their ears, frozen in place by the absolute horror of staring directly into a primordial predator. *Fear Stun Immunity & Age Tier Superiority:* Resisting Visage is modified by [Universal Age Tier Superiority](#universal-age-tier-superiority-modifier-system) (+1 penalty against Elders, -2 against Ancients). A target successfully affected by Visage gains an immediate **1-Scene immunity window** against subsequent fear stuns from Visage, preventing infinite fear stun locking.
* **Resonance Tasting `[Innate Passive - 0 Reserves | Duration: Permanent]`:** You inhale deeply, "tasting" the emotional atmosphere of a room as distinct metallic flavors on your tongue. Fear tastes like bitter copper, lust like sweet honey, and isolation like dry ash, allowing you to instantly isolate vulnerable prey in a dense crowd.

**Thought**
* **The Collective Whisper `[Activated - 1 Reserve | Duration: 1 Scene]`:** You project a telepathic wave across a crowd that whispers simultaneously into dozens of mortal minds. The crowd reacts as a single organism—collectively dispersing, bursting into unexplained protest, or looking away from a bloody supernatural event as if nothing happened. *Supernatural Entity Exclusion:* The Collective Whisper targets unconditioned mortal minds. Any vampire or supernatural entity inside the crowd automatically senses the telepathic pulse, is immune to the crowd dispersion effect, and receives an instant alert to the invoking vampire's location.
* **Cognitive Distortion `[Activated - 1 Reserve | Duration: 1 Scene]`:** You flood a target's brain with disorienting psychic white noise. The victim experiences sudden severe vertigo, ringing ears, and blurred double vision, rendering sniper aim impossible and causing investigators to forget what they were searching for. *Disorientation Penalty Scope:* Cognitive Distortion imposes a **-2 penalty to all physical attack rolls** (melee and ranged) and forces area-of-effect attacks to scatter randomly in direction.
* **Mind Tear `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** You violently bore through a victim's mental barriers like a hot needle through silk. The target's eyes roll back as you pull surface thoughts, hidden passcodes, secret fears, or recent visual memories directly into your own consciousness, leaving the victim with a severe nosebleed. *Foundational Bloodline & Heritage Memory Wiping Prohibition:* Mind Tear and memory manipulation spells (*Lethe's Touch*) can probe or wipe mundane human memories, passcodes, combat trauma, or specific scene events. However, foundational metaphysical bloodline tethers—specifically the **Sire-Fledgling telepathic compass, Centenary Compulsion, Pre-Change Anchor identity, and bloodline heritage**—are etched into the vampire's undead vitae itself and **CANNOT** be erased, rewritten, or severed by mental probing or memory wiping under any circumstances.

**Self-Control**
* **Sovereign Temperament `[Innate Passive - 0 Reserves | Duration: Permanent]`:** You fortify your mind into an unbreachable fortress. The overwhelming scent of spilled blood becomes a faint whisper, your eyes retain their warm human flush, and even severe physical mutilation fails to ignite the feral Beast within you. *Shatter Bonus:* Grants a **+2 mechanical bonus** when attempting a [Shatter Attempt](#the-centenary-compulsion) to break a Sire's command, but does NOT grant automatic success or bypass the internal hemorrhaging trauma cost.
* **Imperious Word `[Activated - 1 Reserve | Duration: 1 Scene]`:** You utter a single, resonated, ancient word of power (e.g., *"Halt," "Kneel," "Sleep"*). The word echoes with supernatural weight, forcing a mortal or weaker vampire's vocal cords to lock and their knees to snap to the floor against their conscious will.

**Memory**
* **Lethe’s Touch `[Activated - 1 Reserve | Duration: Permanent Memory Edit]`:** Passing your fingers over a mortal's forehead leaves a faint, cooling mist. You erase the violent trauma of a feeding or an accidental slip of the shroud, replacing the terror with the pleasant, hazy memory of a heavy glass of wine or a fleeting dream.
* **Bloodline Memory `[Activated - 1 Reserve | Duration: 1 Scene]`:** You close your eyes and listen to the ancient pulse of your own blood, experiencing vivid, first-person memories of your Sire or Grand-Sire from centuries past. *Historical Scope Lock:* Bloodline Memory accesses **past historical memories only** (events experienced prior to the current scene or ancestral history). It CANNOT function as a real-time remote camera or live telepathic spy feed into a living Sire's present activities. *Scope & Limits:* Provides situational narrative context, language fluency, or ancient layout insights for 1 scene (or grants a +2 bonus to relevant lore/knowledge checks). It does **NOT** permanently grant combat skills, mechanical proficiencies, or new power slots.

**Sensory**
* **Crimson Scent `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Your olfactory sense expands into a multi-dimensional map. Every living mortal emits a unique crimson trail in the air—you can smell blood volume, heart rate, immune diseases, and track a bleeding target across miles of rain-soaked city streets. *Creation Benefit:* Grants Unlearned Sires an automatic success when navigating the [Brink of Death Progression](#draining) during Creation.
* **Thermal Vitae Vision `[Innate Toggle - 0 Reserves | Duration: Continuous Toggle]`:** Your retinas dilate into shimmering crimson optics, mapping heat signatures and internal blood circulation in thermal FLIR gradient hues. You see living targets through thick smoke, pitch-black darkness, thermal camouflage, and thin drywall or wooden doors. Living bodies glow in vivid reds/yellows (highlighting concealed handguns, body armor plates, or internal organ trauma), while undead vampires appear as cold blue/violet silhouettes.
* **Electromagnetic Shroud Gaze `[Innate Toggle - 0 Reserves | Duration: Continuous Toggle]`:** You shift your vision into the electromagnetic spectrum. Physical reality dims into shades of grey while electrical currents, camera lenses, radio waves, and security lasers glow in brilliant neon blue. Automatically highlights digital surveillance lenses, hidden wiretaps, infrared laser tripwires, and electronic security nodes, allowing you to trace wire runs through plaster walls and bypass security laser grids undetected. *Passive Optical Blindspot:* EM Shroud Gaze detects active electrical currents, RF signals, and metallic camera optics. Passive, unpowered glass fiber-optic light tubes or non-electronic periscopes emit zero electromagnetic radiation, remaining hidden from EM Shroud Gaze unless inspected via *Thermal Vitae Vision* or *Nyctophilous Apex Sight*.
* **Nyctophilous Apex Sight `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Your pupils absorb every stray photon in the atmosphere, granting crystal-clear, full-color vision in absolute pitch-black void environments without needing ambient light. Renders the vampire completely immune to darkness penalties, flashbang blinding flares, and optical disorientation spells.
* **Echolocation Pulse `[Activated - 1 Reserve | Duration: 1 Scene]`:** You emit high-frequency, sub-audible acoustic pulses from your throat—mimicking the ultrasonic bio-sonar of cave bats. The sound waves bounce off surrounding geometry, mapping a 3D acoustic blueprint of enclosed building layouts, hidden rooms, vault dimensions, and moving targets behind solid concrete walls up to **100 feet**. Completely bypasses visual illusions (*Phantasm*), smoke, and darkness, revealing invisible or cloaked enemies by their acoustic disruption. *Medium Requirement & Silence Suppression:* Requires a physical atmospheric medium (air, water, gas) to transmit sound waves; fails completely in hard vacuums or sound-dampened dead zones created by *The Cold Hush*. Entering or being engulfed by a silence dead zone immediately suppresses active acoustic sonar pings. However, terrain geometry scanned prior to suppression remains stored in the vampire's memory as a **faded, generalized mental layout map**, losing real-time tracking of moving targets or environmental alterations until atmospheric sound transmission is restored.
* **Sub-Auditory Tremor Echo `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Microscopic barbs in your inner ear and sole membranes feel sub-audible micro-vibrations echoing through floors, load-bearing beams, and stone foundations. You automatically sense the location, gait, and weight of any moving entity touching the floor or walls within **60 feet**—even through multiple floors or solid granite slabs—preventing stealth ambushes from behind walls, ceiling vents, or beneath floorboards. *Airborne & Levitating Blind Spot:* Sub-Auditory Tremor Echo detects physical kinetic micro-vibrations transmitted through solid surfaces only. Entities completely airborne or levitating (*Abyssal Levitation*, *Vesper Canopy*) do not touch solid surfaces and are **completely invisible** to Tremor Echo (requiring *Echolocation Pulse* or *Thermal Vitae Vision* to detect).
* **Cardiac Resonance `[Activated - 1 Reserve | Duration: 1 Scene]`:** Your hearing locks onto the rhythmic thumping of mortal hearts. You can isolate and listen to a single heartbeat across a crowded room, operating as a supernatural lie detector where any micro-spike in a target's heart rate or arrhythmia immediately alerts you to lies, panic, or deceit (+2 social interrogation bonus).
* **Omni-Sensory Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of nocturnal perception. You possess *Crimson Scent*, *Thermal Vitae Vision*, *Nyctophilous Apex Sight*, *Echolocation Pulse*, and *Sub-Auditory Tremor Echo*, granting complete multi-spectral mastery over sight, sound, vibration, flashbang immunity, and scent in a single Master power slot.

**Telekinesis & Psychokinesis**
* **Mind Grip `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** You project invisible, crushing hands of mental force. You can lift heavy objects, hurl combatants across the room, or suspend a target mid-air at a distance using pure will. *Mass & Weight Caps:* Mind Grip can lift, suspend, or hurl physical targets weighing up to **250kg (550lbs)** for Neonates, **500kg (1,100lbs)** for Elders, and **1,000kg (1 Ton)** for Ancients. Objects exceeding these mass caps cannot be lifted. *Off-Turn Reaction Interception & Supersonic Velocity Bounds:* Expending an off-turn reaction action allows a conscious vampire to invoke Mind Grip to catch or deflect thrown melee weapons, arrows, crossbow bolts, or subsonic pistol rounds mid-air. However, supersonic rifle and sniper rounds travel faster than neural visual processing; Mind Grip **cannot** catch supersonic gunfire off-turn. Deflecting high-velocity rifle fire requires pre-manifested *Kinetic Barrier* or physical cover.
* **Kinetic Barrier `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You project a dense telekinetic wall around yourself. Incoming bullets, arrows, shrapnel, and thrown weapons drop harmlessly to the floor as they impact your invisible shield. (Sustaining costs 1 Blood Reserve per combat round). *Evocation Deflection:* Kinetic Barrier completely deflects supernatural projectiles (*Sanguine Spikes*) and shadow whips (*Umbral Blades*) without collapsing, provided the defender maintains their 1 Blood Reserve per round upkeep.
* **Kinetic Crush `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** You focus intense telekinetic pressure onto a localized target. You can snap rifle barrels in half, crush heavy padlock mechanisms, or shatter a foe's arm bones from across the room. *Cybernetics & Powered Armor Servomotor Joint Lock Scope:* Targeting a target wearing powered armor, exoskeletons, or cybernetic limbs crushes external joint servomotors and hydraulics, **locking the mechanical joint in place** (disabling powered mobility bonuses and inflicting a -2 penalty to actions with that limb). Furthermore, because telekinetic force projects spatial pressure directly, Kinetic Crush passes through physical armor plates, inflicting standard crushing damage on internal biological bones unless protected by internal *Kinetic Barrier* shielding.
* **Telekinetic Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of psychokinesis. You possess *Mind Grip*, *Kinetic Barrier*, and *Kinetic Crush*, granting absolute mastery over telekinetic lifting, projectile defense, and force crushing in a single Master power slot.

**Advanced Mental & Illusion**
* **Phantasm `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You project vivid sensory illusions directly into a target's mind. You can make an ally appear as a monstrous threat, project false gunshots, or create an illusionary wall to hide your escape. *Mental Scope:* Because Phantasm projects directly into the target's brain rather than bending light in physical space, it affects all senses (visual, auditory, olfactory) of the targeted host mind. Automated non-sentient physical machines or optical security cameras are completely immune. *Non-Biological AI Immunity:* Phantasm operates exclusively upon organic neurological visual/auditory cortices. Non-biological automated AI turrets, combat drones, and security sensors possess zero organic brain tissue and are **completely immune** to Phantasm illusions (displaying true physical reality). *Cybernetic Optic Interaction:* If a target possesses cybernetic camera eyes or digital HUDs wired into their visual cortex, Phantasm affects the organic mind, but raw digital HUD overlays display un-distorted feeds. This visual clash inflicts a severe **-2 perceptual disorientation penalty** for 1 round as the host mind struggles to reconcile the mental illusion with the digital HUD.
* **Puppet Master `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You violently seize control of a target's motor nervous system like a marionette. The victim remains conscious but helpless as you force their body to pull a trigger, unlock a security vault, or drop their weapons. *Motor Nervous & Anatomical Scope:* Puppet Master operates strictly upon external skeletal push-pull and stabilizer muscles (forcing movement, weapon drops, pulling triggers). It cannot manipulate internal involuntary organs, diaphragmatic respiratory compression, or vocal cord air passage patterns. Consequently, Puppet Master **cannot force vocal compliance, speech, or password recitation** (forcing vocal speech requires *Imperious Word* or mental probe powers like *Mind Tear*). It does NOT grant access to internal brain thoughts, blood reserves, or supernatural power activations; the conscious victim may still attempt mental defenses (*Psychic Fortress*, *Mind Tear*) on their turn.
* **Psychic Fortress `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You build an impenetrable psychic barrier around your own mind. You are completely immune to mental probes (*Mind Tear*), emotional siphons, and memory wipes (*Lethe's Touch*) attempted by rival vampires. (Sustaining costs 1 Blood Reserve per combat round).

#### Supernatural Powers

These powers represent the physical, physics-defying magic of the vampiric curse. They dictate how a vampire moves, survives, and alters their physical form.

**Alteration (Forms & Shifting)**
* **Pocket-Realm Shift Mechanism:** Shifting into a Swarm Form (*Bat Primacy*, *Verminous Primacy*, *Arachnid Primacy*, *Crimson Mist*, *Primal Shift*) does NOT physically compress or dissolve the vampire's body. Instead, the vampire's true physical form and all carried inventory instantly teleport into a personal **Pocket-Realm dimension**—an isolated, safe-haven realm unique to that vampire. Simultaneously, a physical manifestation of the swarm appears in reality. The vampire gains full sensory consciousness and telepathic control over the swarm. Re-coalescing exits the Pocket-Realm back into reality at the swarm's location. If 100% of the swarm is destroyed, the vampire is forcibly ejected from the Pocket-Realm into reality at the swarm's last position in **Stage 4 Torpor** (Petrified Slumber; granite calcification). *Note:* Stage 4 Torpor is a petrified granite state; turning to ash represents absolute, unrecoverable True Death.
  * **Native Soil Torpor Stasis:** Vampires in ANY form of Torpor (Stage 3 Catatonic Torpor, Stage 4 Petrified Slumber, or Starvation Desiccation Torpor) enter a subterranean metabolic stasis that **SUSPENDS** [The Bleed](#the-home-sickness-regression-track-the-bleed) regression track until the vampire is roused or awakened.
  * **Solar Transference & Maintenance:** Sunlight shining upon the manifested swarm in reality transmits 100% of solar radiation/thermal burn through the dimensional tether into the body inside the Pocket-Realm. Sustaining a Pocket-Realm dimension consumes **1 Blood Reserve per hour**; if reserves drop to 0, the vampire is forcibly ejected into reality.
  * **Swarm Form Structural Clearance Specs:** Manifested swarms are physically constrained by structural opening clearances:
    * **Rat Swarms (*Trench Plague*, *Gnawing Scourge*):** Require a minimum opening diameter of **2 inches (5cm)** to squeeze through structural gaps or drain pipes.
    * **Bat Swarms (*Vesper Canopy*, *Blood-Siphon Gale*):** Require a minimum opening diameter of **3 inches (7.5cm)** to fly through window grates or ventilation ducts.
    * **Spider Swarms (*Weaver's Eclipse*, *Arachnid Tide*, *Silk & Shadow*):** Require a minimum micro-gap clearance of **0.25 inches (6mm)** to crawl beneath doors or keyholes.
    * **Crimson Mist (*Crimson Mist*):** Gaseous/vaporous state—passes through keyholes, micro-vents, and air filtration gaps down to **<0.1mm**.
* **Crimson Mist `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Your physical flesh instantly collapses inward into a dense, chilling, crimson-tinged fog. In this vaporous state, bullets pass through you harmlessly, and you can drift effortlessly through keyholes, air vents, or sewer grates.
* **Vesper Canopy `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Your body dissolves into a vortex of screeching, leathery-winged micro-bats. The swarm grants rapid aerial elevation over city walls, while high-frequency echolocation automatically maps hidden rooms and invisible targets in total darkness.
* **Blood-Siphon Gale `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** A ferocious storm of razor-clawed vampire bats erupts outward to engulf an enemy group. The swarm inflicts hundreds of tiny lacerations, siphoning micro-drafts of blood from living victims to nourish your stored blood reserves before re-coalescing.
* **Bat Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of nocturnal flight. You possess both *Vesper Canopy* (`Sustained`) and *Blood-Siphon Gale* (`Activated`), granting complete mastery over bat swarm flight, echolocation mapping, and aerial blood siphoning in a single Master power slot.
* **Trench Plague `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Your physical form disintegrates into a chittering tide of red-eyed sewer rats. The swarm flows effortlessly beneath floorboards, through sewage pipes, and under locked steel doors, bypassing security barriers completely undetected by mortal guards.
* **Gnawing Scourge `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** A ravenous horde of scavenger rats surges over an enemy or object. The swarm rapidly chews through Kevlar armor, leather, wooden doors, power lines, and security cables, destroying physical equipment while causing mass panic in crowds.
* **Verminous Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of subterranean infestation. You possess both *Trench Plague* (`Sustained`) and *Gnawing Scourge* (`Activated`), giving you complete control over rat swarm stealth infiltration, pipe navigation, and equipment sabotage in a single Master power slot.
* **Weaver’s Eclipse `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Your physical form dissolves into a silent, skittering carpet of thousands of black, venomous spiders. Moving in complete silence, the swarm can effortlessly scale sheer vertical walls, drop from ceilings, and weave razor-thin web traps across doorframes to entangle and paralyze enemies while in transit. *Web Trap Counterplay:* Cobwebs created by Weaver's Eclipse or *Silk & Shadow* paralyze enemies, requiring a **Hard Strength check** to break free. Fire (*Pyromancy*, *Pyre Aura*) or *Kinetic Blasts* destroy web traps instantly. *Swarm Mass Dispersal, Partial Destruction & Automatic Pocket-Realm Ejection Math:* The manifested swarm anchors its physical biomass through pocket-realm spatial projection. Individual lost or stepped-on spiders do not inflict damage. However, if concentrated area-of-effect attacks (flamethrowers, explosions, acid) destroy significant fractions of the swarm before re-forming, the vampire suffers **1 Wound per 25% of total swarm mass destroyed**. Crossing the **Total Dispersal Threshold ($\ge 75\%$ swarm destruction)** triggers an automatic pocket-realm spatial ejection: the remaining swarm mass collapses, forcibly ejecting the vampire out of swarm form into a mangled humanoid torso and collapsing them immediately into **Stage 3 Torpor**.
* **Arachnid Tide `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** Your body disintegrates into a rushing wave of shadow-spiders that cascades over terrain like dark liquid silk. The swarm inflicts micro-neurotoxic bites that numb a target's limbs, causing paralysis and disorientation before re-coalescing into human form behind them.
* **Silk & Shadow `[Activated - 1 Reserve | Duration: 1 Scene]`:** You split your mass into a skittering colony of albino and jet-black web-weavers. The spiders can coat an entire room in thick, sticky cobwebs within seconds, extinguishing light sources and obscuring vision while allowing you to sense vibrations anywhere in the webbed zone.
* **Arachnid Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of spider-swarm mastery. You possess *Weaver’s Eclipse*, *Arachnid Tide*, and *Silk & Shadow*. Whenever you shift into a spider swarm, you choose which specific manifestation or tactical effect to invoke—or combine their traits into a singular, terrifying arachnid storm.
* **Primal Shift `[Sustained - 1 Reserve Activation + 1 Reserve/Scene Upkeep | Duration: Continuous]`:** Your bones crack and reshape with terrifying speed, skin sprouting dark fur and teeth lengthening into ivory daggers as you shift into a giant shadow-wolf, mastiff, or massive cave bat—gaining apex predatory senses and blinding sprint speed. *Physical Tissue Solar Combustion:* Primal Shift is a direct physical flesh/bone transformation (not a Swarm Pocket-Realm). Sunlight shining upon a shifted wolf or bat form directly ignites the vampire's physical tissue per standard Solar Disintegration rules.
* **Petrified Slumber `[Sustained - 1 Reserve Activation + 1 Reserve/Day Upkeep | Duration: Minimum 30-Day Hibernation]`:** Your skin turns to cold, seamless grey granite. In this hardened petrified state, your body halts all physical decay and becomes immune to physical axes, explosives, and collapse, placing you in a deep defensive slumber at the cost of complete immobility.
  * **Minimum Hibernation Lock-in (30 Days Bare Minimum):** Once activated, the vampire cannot voluntarily wake up or toggle off the power for a **bare minimum lock-in period of 30 Days (1 Month)**. Vampires can select longer intended hibernation tiers upon entry: **30 Days** (Short Hibernation), **1 Year** (Extended Hibernation), or **100 Years** (Centenary Slumber).
  * **Early Awakening Rituals:** A petrified vampire cannot wake up on their own before their lock-in period expires. They can only be awakened early via external intervention:
    1. *External Blood Ingestion:* A Coven member or Thrall pours **3 drafts of fresh vampire blood** onto the statue's lips/mouth, awakening the vampire in 60 seconds.
    2. *Catastrophic Structural Shock:* If the stone body suffers heavy structural damage (>50 structural impact damage), the petrification fractures, forcibly ejecting the vampire awake in **Stage 3 Torpor**.
  * **Native Soil Maintenance & Earthbreaker:** Vampires possessing [*Earthbreaker*](#immunities--resistances) bypass Native Soil requirements completely while in stone. Vampires without *Earthbreaker* require Thralls or Coven members to maintain their 3kg Native Soil crypt during hibernation; if soil contact is destroyed while petrified, the vampire suffers [The Bleed](#the-home-sickness-regression-track-the-bleed) regression track upon awakening.
* **Chameleon Facade `[Activated - 1 Reserve | Duration: 1 Scene]`:** Underneath your skin, bone structure and cartilage audibly shift like wet clay. You can alter your facial structure, voice pitch, eye color, height, and fingerprints to perfectly impersonate another mortal or slide past security unnoticed for 1 scene. *Laboratory Bio-Limits & Thermal FLIR Masking Failure:* Chameleon Facade alters physical dermal contours, facial features, vocal pitch, and ridge fingerprints. However, non-physical deep biological markers (blood DNA sequencing, room-temperature non-circulating blood) still reveal vampiric biology under medical/laboratory equipment. Furthermore, Chameleon Facade does **NOT** generate internal body heat; under FLIR thermal imaging or heat-seeking sensors, the disguised vampire displays as a room-temperature cold blue silhouette, immediately failing thermal optic inspections unless external heating gear or heat-masking magic is used.

**Immunities & Resistances**
* **Daywalker's Grace `[Activated - 1 Reserve | Duration: Up to 3 Minutes Solar Shield]`:** Ancient protective sigils woven into your blood shield you from the holy fury of the sun. While mortals sizzle in seconds, your skin merely emits a faint vapor, allowing you to walk beneath unfiltered sunlight for up to **3 precious minutes (180 seconds)** per exposure to escape death (inflicting dermal steam burns and a persistent -2 action penalty while exposed).
  * **Concentrated Solar Beam Acceleration Multiplier (3x Drain):** Standard ambient natural sunlight drains the 180-second timer at normal 1:1 speed. However, focused high-intensity solar weaponry (magnifying solar lenses, parabolic heat-rays, orbital solar mirrors) overloads the blood sigils, consuming the timer at **3x speed** (10 seconds of concentrated beam exposure burns **30 seconds** of shield timer). Expiring the 180-second timer shatters protective sigils, advancing immediately into Round 2 Flesh Ignition!
  * **Required Recovery Window:** After direct solar exposure, the vampire MUST complete a **Recovery Window of 1 full night of undisturbed Native Soil slumber** (or 6 hours in total shadow) before *Daywalker's Grace* can be activated again. Re-exposure before completing the recovery window causes the power to fail, advancing immediately into Round 2 Flesh Ignition! *Strict Recovery Reset:* Any solar exposure before completing the 6-hour shadow / 1-night Native Soil recovery window immediately resets the recovery timer back to 0.
  * **Solar Swarm Transference Timer:** Sunlight shining upon a manifested swarm transfers 100% solar radiation into the Pocket-Realm body, **continuously consuming** the 3-minute Daywalker's Grace timer. Once the 3-minute timer expires, solar combustion erupts inside the Pocket-Realm, forcibly ejecting the vampire into Stage 4 Torpor.
* **Unholy Primacy `[Innate Passive - 0 Reserves | Duration: Permanent]`:** A rare and powerful trait inherited directly at Creation via bloodline latency. The pinnacle of bane immunity—your blood becomes dense and unyielding. You gain total, combined immunity to holy water, garlic, and crucifixes; holy water rolls off your skin like oil on glass, garlic smells like sweet perfume, and sacred symbols fail to repel or paralyze your march.
* **Anointed Flesh `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Your outer dermis develops a mystical resistance to consecrated liquids. Holy water no longer causes skin-melting burns or persistent *Scared Wound* debuffs upon contact.
* **Alchemical Assimilation `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Your internal physiology neutralizes divine and botanical toxins. Ingesting garlic or wolfsbane causes zero nausea, internal blistering, or organ failure.
* **Bane-Blindness `[Innate Passive - 0 Reserves | Duration: Permanent]`:** You are immune to the psychic repulsion of holy symbols. Crucifixes, consecrated ground, and holy chants fail to paralyze or repel your forward march.
* **Earthbreaker `[Innate Passive - 0 Reserves | Duration: Permanent]`:** A rare, god-tier anomaly that shatters the fundamental law of creation. Your soul severs its tether to your birthplace; you are permanently freed from the [Native Soil dependency](#the-native-soil-dependency), immune to "[The Bleed](#the-home-sickness-regression-track-the-bleed)", and no longer require 3kg of earth to survive.

**Travel**
* **Abyssal Levitation `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Gravity releases its hold upon you. With a silent rise of your coat, you hover effortlessly into the air, stepping across empty sky and soaring over skyscrapers as if walking down a marble staircase. *Kinetic Air Recoil & Stability:* Levitation suspends the vampire via supernatural force, maintaining air stability for standard melee strikes and light firearms. However, attempting physical grapples or firing heavy anti-materiel weapons while levitating suffers a **-1 Recoil Instability penalty** unless anchored to a solid surface or supported by *Mind Grip*. *Levitation Parameters:* Levitation movement speed equals normal base movement speed. Maximum altitude is capped at **1,000 feet above terrain**; ascending higher exposes the vampire to violent atmospheric turbulence and freezing altitude penalties.
* **Veil Flicker `[Activated - 1 Reserve | Duration: Instantaneous (30ft Teleport)]`:** You fold local space in a sharp crack of displaced air and a faint scent of burnt static, instantly vanishing from one spot to reappear 30 feet away behind your prey before their eyes can track your motion. *Visual Destination Scope & Spatial Bounce-Back:* Veil Flicker requires direct visual line-of-sight to the destination spot (or active acoustic/thermal mapping via *Echolocation Pulse* / *Thermal Vitae Vision*). Attempting a blind teleport into unmapped solid terrain causes spatial bounce-back, dropping the vampire at their starting location and inflicting **1 Direct Damage** from spatial displacement shock.
* **Umbral Crossing `[Activated - 1 Reserve | Duration: Instantaneous (Shadow Step)]`:** You step backward into a wall shadow and melt into black liquid silk, instantly emerging from a separate shadow across the room like a ghost stepping through a dark doorway.
* **Spider’s Grace `[Innate Passive - 0 Reserves | Duration: Permanent]`:** Microscopic barbs of vitae adhere your soles and fingertips to any surface. You can sprint vertically up glass skyscrapers, leap across 50-foot rooftops, or drop from a 10-story window landing silently on your feet without a scratch.

**Healing**
* **Sanguine Knit `[Activated - 1 Reserve | Duration: Instantaneous (1 Wound Mend)]`:** Burning stored blood reserves causes broken bones to snap back into place with wet clicks while deep lacerations knit together in seconds, sealing wounds mid-combat under a sheen of dark crimson mist (max 1 wound/round). *Strict Self-Only Scope:* Sanguine Knit affects **ONLY the invoking vampire**. A vampire cannot spend blood or use Sanguine Knit to mend another vampire, mortal, or thrall. *Control Signal Requirement:* Sanguine Knit is fueled by blood in the heart, but controlled strictly by brain signals from the head. Severing the neck breaks signal transmission; neither the detached head nor the headless torso can invoke Sanguine Knit to seal a severed neck stump while detached.
* **Mask of Mortality `[Innate Toggle - 0 Reserves | Duration: Continuous Toggle]`:** You suppress your supernatural regeneration, forcing injuries to bleed, scab, and bruise at a mundane human rate to fool medical examiners and maintain your cover in mortal society. *Forensic Detection:* While Mask of Mortality and Sovereign Temperament fool visual inspection and basic vital checks, deep medical blood tests (toxicology panels, DNA sequencing) reveal room-temperature non-circulating blood lacking oxygen, exposing vampiric anatomy to medical laboratory equipment.
* **Necrotic Vitae `[Activated - 1 Reserve | Duration: 1 Scene]`:** You coat your claws or weapons in corrupted, decaying vitae. Wounds inflicted by you turn black and gangrenous, refusing to close or heal for mortals. Rival vampires wounded by Necrotic Vitae suffer suppressed regeneration—they must burn **2 Blood Reserves per wound** (instead of 1) to mend Necrotic injuries via *Sanguine Knit*.
* **Grand Harmonization of Vitae (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The apex of biological control. You possess *Sanguine Knit*, *Mask of Mortality*, and *Necrotic Vitae*, manipulating your own lifeblood with absolute mastery. *Strict Self-Only Scope:* Grand Harmonization of Vitae operates exclusively upon the invoking vampire's own body; healing powers cannot be projected or cast upon allies under any circumstances. *Severed Limb Regrowth Duration & Concentration Math:* Re-attaching a retrieved severed limb held against the stump requires burning **1 Blood Reserve** to mend in 1 combat round. However, re-growing a completely destroyed or unretrievable major limb (arm, leg) from scratch requires expending **3 Blood Reserves total** over **3 consecutive combat rounds** (1 Reserve/round) while maintaining concentration. Taking damage during regrowth forces a **Hard Self-Control check**; failure interrupts the process, consuming the spent reserves without completing limb regrowth.

**Combat & Elemental Evocation**
* **Supernatural Fuel Source (Pyromancy Vacuum Immunity):** Blood Pyromancy (*Hellfire Orb*, *Combust Vitae*, *Pyre Aura*) consumes pressurized vampiric vitae as fuel rather than atmospheric oxygen. Hellfire Orbs and Pyre Auras burn continuously in zero-oxygen vacuums (orbital space stations, airlocks), underwater, and in toxic gas clouds without extinguishing!
* **Hellfire Orb `[Activated - 1 Reserve | Duration: Instantaneous (Area Detonation)]`:** You ignite a draft of your own blood, hurling a roaring sphere of unnatural black-and-crimson flame. Upon impact, the orb detonates in a fiery explosion, inflicting severe burning damage across an area and setting surrounding terrain ablaze.
* **Combust Vitae `[Activated - 1 Reserve | Duration: Instantaneous (Internal Combustion)]`:** You target an enemy who is currently bleeding or wounded, psychically igniting their exposed blood. The victim's own spilled blood violently bursts into internal flames, burning them from the inside out and causing panic.
  * **Age Tier Difference Scaling Math ($\Delta = \text{Attacker Tier} - \text{Target Tier}$):** Pyromantic blood combustion scales based on the [Age Tier Superiority](#mechanics) difference between the attacker and victim *(Age Tiers: Neonate = 0, Elder = +1, Ancient = +2)*:
    * **$\Delta = +2$ (Ancient vs. Neonate):** **Total Incineration:** Target's blood erupts into a localized inferno, dealing catastrophic fire damage and setting the target fully ablaze (inflicts instant **Round 2 Flesh Ignition**).
    * **$\Delta = +1$ (Ancient vs. Elder / Elder vs. Neonate):** **Severe Combustive Burst:** Ignites target's blood for heavy internal fire damage (+2 bonus damage) and forces an immediate panic/morale check.
    * **$\Delta = 0$ (Same Age Tier):** **Standard Internal Flame:** Deals standard internal fire damage (1 wound) and causes temporary combat disorientation.
    * **$\Delta = -1$ (Neonate vs. Elder / Elder vs. Ancient):** **Resisted Fizzle:** Target's dense blood resists ignition; inflicts minor superficial skin scorch (0 wounds), easily suppressed by the target.
    * **$\Delta = -2$ (Neonate vs. Ancient):** **Complete Immunity (Nothing Happens):** The Ancient's primordial blood completely smothers the weak pyromantic spark; the spell fails completely with **zero effect**.
* **Pyre Aura `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** Dark, supernatural hellfire erupts across your body and weapons. Your melee strikes ignite targets on contact, and any attacker foolish enough to strike you in close combat suffers immediate fire lashback. (Sustaining costs 1 Blood Reserve per combat round). *Pressurized Vitae Fuel & Extinguishing Exemption:* Pyre Aura consumes pressurized vampiric blood as fuel rather than atmospheric oxygen. Pyre Aura burns continuously underwater, in torrents of rain, in zero-oxygen vacuums, or under chemical fire suppression foam without extinguishing. It can only be extinguished by expiring the blood upkeep, entering an antimagic deadzone, or colliding with diametrically opposed ice magic (*Grave Chill*).
* **Pyromantic Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of blood pyromancy. You possess *Hellfire Orb*, *Combust Vitae*, and *Pyre Aura*, granting absolute mastery over infernal flame generation, blood combustion, and hellfire shields in a single Master power slot.
* **Sanguine Spike `[Activated - 1 Reserve | Duration: Instantaneous (1 Attack)]`:** You solidify a stream of pressurized vitae into razor-sharp, obsidian-hard blood javelins. You hurl these spikes with supernatural force, piercing heavy body armor and pinning targets to stone walls. *Environmental Density Solidification:* Sanguine Spikes are held together by supernatural pressure and blood density magic. They solidify instantly upon projection and do not dissolve in water, mud, or liquid atmospheres, maintaining standard armor-piercing damage underwater. *Armor Penetration:* Ignores mundane physical armor ratings (Kevlar, steel plate); targets may still attempt Dodge checks or project supernatural energy defenses (*Kinetic Barrier*). *Structural Hardness Math:* Applies strictly to personal body armor worn by combatants. Heavy structural barriers (armored vault doors, tank hulls, reinforced concrete) possess Structural Integrity Hit Points and are not instantly bypassed; Sanguine Spikes deal standard physical damage against the barrier's Structural HP pool.
* **Umbral Blade `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You extend your physical melee strikes with long, razor-thin whips of solid shadow. These dark blades bypass mundane physical shields and slice effortlessly through metal, armor, and bone. *Armor Penetration:* Ignores mundane physical armor ratings (Kevlar, steel plate); targets may still attempt Dodge checks or project supernatural energy defenses (*Kinetic Barrier*). *Structural Hardness Math:* Applies strictly to personal body armor worn by combatants. Heavy structural barriers (armored vault doors, tank hulls, reinforced concrete) possess Structural Integrity Hit Points and are not instantly bypassed; Umbral Blade strikes deal standard physical damage against the barrier's Structural HP pool.
* **Grave Chill `[Activated - 1 Reserve | Duration: 1 Scene]`:** You emit a flash-freeze wave of tomb cold. Ambient moisture turns to ice instantaneously, coating enemies in frost, slowing their movement to a crawl, and making their weapons brittle. *Kinetic Impact & Structural Fragility:* Grave Chill coats targets in structural frost; physical bludgeoning attacks or *Kinetic Blast* shockwaves against frozen targets deal **+1 bonus impact damage**, and parrying with frozen weapons carries a 1-in-6 chance of shattering mundane blades.
* **Kinetic Blast `[Activated - 1 Reserve | Duration: Instantaneous (20ft Knockback)]`:** You release a crushing wave of telekinetic force. The shockwave hurls enemy combatants backward up to **20 feet**, shattering bones, disarming foes, breaching reinforced wooden doors, and knocking targets prone. Targets hitting solid walls suffer minor impact damage; targets near ledges may make a physical Agility/Evasion check to catch a ledge.
* **Nerve Lightning `[Activated - 1 Reserve | Duration: Instantaneous (1 Action)]`:** You hijack the target's neural bio-electrical network, causing a sudden violent electrical short-circuit. The victim suffers blinding pain and muscular spasms, dropping held weapons and collapsing to their knees. *Bio-Neural Target Scope:* Nerve Lightning specifically targets biological neural nervous systems (living mortals, animals, vampires, Reapers). Purely mechanical, non-biological entities (drones, computer mainframes, security cameras) lack a biological neural network and are unaffected.

**Necromancy & Grave Arts**
* **Corpse Siphon `[Activated - 1 Reserve | Duration: 1 Scene (60s Memory Extraction)]`:** By placing your hand upon a corpse (or dead neural host) deceased within the last 24 hours, you commune with the cold residual echo of the soul/brain, viewing their final 60 seconds of memories or extracting 1 truthful answer to a spoken question. *Head-Touch Neural Requirement:* Corpse Siphon extracts residual neural memories from the brain cortex; the invoking vampire MUST make direct skin-to-skin contact with the **decapitated head itself** (touching a headless torso yields 0 memories). *Undead Head Interrogation Scope:* Corpse Siphon targets ONLY non-living, truly deceased mortal/host corpses. Invoking Corpse Siphon on a living or torpid decapitated vampire head fails automatically; probing an undead mind requires active mental powers (*Mind Tear*) and must overcome the target's mental defenses.
* **Rise of the Slumbering `[Activated - 1 Reserve | Duration: 1 Scene]`:** You inject a stream of black, necrotic vitae into a freshly deceased body. The corpse re-animates as a mindless, pain-immune minion under your direct command for 1 scene to fight, block doorways, or perform manual labor.
* **Aura of the Slumbering Legion `[Activated / Sustained - 1 Reserve Activation (1 Scene) | Upkeep: 1 Reserve/Round]`:** You pulse a shockwave of necrotic energy outward. This power re-animates up to **ROUND(VAMPIRE_AGE / 100)** dead human/mortal corpses within a **[10 + ROUND(VAMPIRE_AGE / 100)]** feet diameter sphere centered on yourself. The animated corpses rise as mindless, pain-immune minions under your direct command for **1 scene**. *Optional Sustained Maintenance:* If you burn **1 Blood Reserve per round** to sustain the aura, the re-animation field moves with you as an active aura sphere; any newly slain corpses entering or falling within the sphere during combat are automatically re-animated without spending additional activation blood! *Active Minion Cap & Trailing Minions:* A vampire can only maintain a maximum total of **ROUND(VAMPIRE_AGE / 100)** active re-animated corpses at any given time. Re-animated corpses that fall outside the trailing edge of a moving aura sphere remain active for the remainder of the 1-scene duration, provided total active minions do not exceed the active minion cap. Recasting the aura while at the cap replaces older minions; any excess animated corpses beyond the cap immediately collapse back into lifeless, inanimate remains. *Physical Excavation Constraints:* Re-animated corpses gain basic motor function but retain mortal physical Strength caps. Corpses submerged under loose dirt take 1 full combat round to claw out; corpses trapped beneath solid concrete slabs or reinforced coffin vaults cannot break free without external excavation support.
* **Grave Rot `[Sustained - 1 Reserve Activation + 1 Reserve/Round Upkeep | Duration: Continuous]`:** You emit a chilling aura of rapid decay. Organic flesh rots, iron/steel rusts, wood splinters, and synthetic armor degrades instantly within your immediate proximity. *Synthetic & Cybernetic Scope:* Grave Rot attacks physical structural integrity regardless of tech era, degrading mundane iron, steel, Kevlar, synthetic polymers, and cybernetic limb joints alike (-1 armor/structural penalty per round in the aura). Sacred relics, blood archives, and supernatural artifacts possess mystical resilience and are immune to passive Grave Rot decay.
* **Soul Bind `[Activated - 1 Reserve | Duration: Permanent Nocturnal Sentry]`:** You bind the restless spirit of a slain mortal to a physical object, grave marker, or terminal node, forcing the phantom to act as a permanent nocturnal sentry that alerts you to intruders. *Active Sentry Cap & Incorporeal Status:* A vampire can maintain a maximum total of **ROUND(VAMPIRE_AGE / 100)** active bound spirits (minimum 1). Bound spirits function purely as incorporeal nocturnal sentries (warning of intruders); they cannot inflict physical attack damage. *Ethereal Vitae Detection:* Bound spirits sense ethereal vitae signatures rather than light reflections; manifested swarms (even when tethered to Pocket-Realms) disturb local spiritual aura gradients, allowing bound sentries to alert their master to swarm intruders.
* **Necromantic Primacy (Master Power) `[Innate Composite - 0 Reserves Activation]`:** The pinnacle of death manipulation. You possess *Corpse Siphon*, *Rise of the Slumbering*, *Aura of the Slumbering Legion*, *Grave Rot*, and *Soul Bind*, granting absolute control over post-mortem interrogation, individual and mass corpse animation, decay, and spirit binding in a single Master power slot.

## Social
Vampire society is generally hidden but heavily structured to ensure survival and secrecy.

**Bloodline Dynamics & Telepathy**
* **The Psychic Network:** Vampires are capable of communicating telepathically with one another across short-to-medium distances. However, a profound mystical blind spot exists: **sires and their direct fledglings can never communicate telepathically with each other**, forcing them to rely on spoken words or intermediaries.
* **The Sire's Compass:** Sires possess an innate, permanent psychic sense of their fledglings' physical locations, acting as an internal compass pointing toward their progeny no matter the distance across the physical world. *Interdimensional Blind Spot:* If a fledgling shifts into a [Pocket-Realm dimension](#alteration-forms--shifting), the compass needle spins erratically in circles, losing tracking until the fledgling re-coalesces back into reality.
* **Blood Resonance & Synergies:** When vampires of the same bloodline come into close proximity, they instinctively taste and feel the resonance of their shared ancestry.
  * **Lineage Harmonization (Bonus):** Mental and emotional behavioral powers (such as *Siren’s Cadence*, *Imperious Word*, and *Mind Tear*, see [Behavioral Powers](#behavioral-powers)) are significantly more potent when targeting vampires of your own direct bloodline (sires, fledglings, or blood-siblings). The shared blood frequencies make their minds far easier to influence (+2 mechanical success bonus). *Modifier Stacking & Natural Critical Guarantee:* Lineage Harmonization (+2 bonus against direct bloodline) explicitly **STACKS** with [Universal Age Tier Superiority](#mechanics) modifiers (+1 or +2), reflecting how ancient sires possess near-absolute mental dominance over their direct progeny. However, in all mental/social resistance tests, the defending target always retains a minimum **Natural Critical Success Chance (1-in-20 / Natural 20 or Critical Pair)** to resist or break free against impossible odds, ensuring a defender can never be completely counted out regardless of numerical modifier gaps.
  * **Rival Lineage Static (Penalty):** Vampires from rival Old World lineages possess natural mystical static against one another. Attempting to use mind-control powers against a rival bloodline suffers a -2 penalty unless the attacker has previously ingested blood from that rival lineage.
* **The Centenary Compulsion:** For the first 100 years of their post-change existence, New World vampires suffer from an involuntary psychological and mystical imperative. They will unconsciously do almost anything to please, protect, or obey their sires, making independent rebellion nearly impossible during their first century. *Command Medium Scope:* The Centenary Compulsion forces obedience to a Sire's explicit intent regardless of medium (spoken voice in person, written letter/note, or third-party messenger), provided the fledgling recognizes the command as originating from their Sire. *Contradictory Command Supremacy:* If a Sire issues contradictory or opposing commands in rapid succession (e.g., *"Attack"* followed immediately by *"Halt"*), the fledgling does not enter a psychological paralysis loop; the Sire's **most recent explicit command** immediately supersedes and replaces all previous conflicting directives.
  * **Breaking the Compulsion (The Shatter Attempt):** A fledgling can attempt a Near-Impossible **Self-Control** check (greatly aided by the *Sovereign Temperament* power, see [Behavioral Powers](#behavioral-powers)) to break their sire's command for a single scene.
  * **Low-Reserve Shatter Degradation System (Trauma & Cost):** Defying the blood bond forces the fledgling's blood to boil backward against the ancestral tether. If attempted while Blood Reserves are at half capacity or less, the violent shockwave inflicts severe physiological and magical degradation based on stored reserves:
    * **High Reserves (>50% Capacity):** Burns **50% of remaining Blood Reserves** + physical agony and bleeding for 1 scene.
    * **Half Reserves ($\le$50% Capacity / $\le$5 Reserves):** Inflicts **1 Major Consequence** (Select 1: 1 Power Slot is locked & disabled for **30 days**, OR suffers a permanent **-1 penalty to Self-Control**).
    * **Critically Low ($\le$2 Reserves):** Inflicts **2 Severe Consequences** (1 Power Slot is locked & disabled for **1 full year** AND takes **2 Direct Core Health Damage**).
    * **Zero Reserves (0 Reserves):** Inflicts **ALL 3 Catastrophic Consequences** (**Permanently loses 1 Power Slot** [burned away by bloodline backlash], takes **3 Direct Core Health Damage**, AND forcibly plunges into **Stage 4 Torpor** immediately).
  * **Compulsion & Mutations:**
    * *Botched Drain Fledglings (Feral):* Lack the cognitive complexity to break or even comprehend the compulsion; they remain mindlessly obedient to their sire's immediate shouts or wander as feral beasts.
    * *Power-Fade Collapse Mutants:* Possess corrupted blood tethers. Attempting to enforce or break the compulsion triggers intense physical agony in BOTH mutant and sire. However, if a Power-Fade mutant successfully shatters the compulsion, the bond is permanently severed forever.

**Secrecy, Covens, and Thralls**
* **The Digital Shroud:** Beyond the traditional myth of casting no reflection in silver-backed mirrors, a vampire's presence causes severe digital distortion. High-resolution cameras, security feeds, and smartphones cannot capture a clear image of a vampire, rendering them as a pixelated blur or corrupted video static. *Sensor Scope & AI Turrets:* The Digital Shroud distorts optical image sensors and facial recognition cameras. However, non-optical physical sensors (infrared thermal sensors, acoustic motion detectors, pressure plates, laser tripwires) and automated AI turrets equipped with FLIR thermal vision still track the cold mass silhouette of a vampire unless the vampire actively invokes [*Crimson Mist*](#alteration-forms--shifting) or [*Veil Flicker*](#supernatural-powers).
* **Covens & Governance:** Sires hold absolute authority over their fledglings. Vampires rarely survive long alone, forming Covens for territorial control, collective defense, and bloodline preservation.
  * **Coven Roles & Hierarchy:**
    * **The Apex Elder / Sire:** The absolute ruler of the Coven, holding supreme authority over territory, bloodline decrees, and fledgling assignments.
    * **The Regent Enforcer:** Second-in-command handling martial defense, border patrols, and executing physical discipline upon rogue vampires.
    * **The Keeper of the Haven:** Responsible for securing haven perimeters, maintaining Native Soil crypts, and managing emergency escape vectors.
    * **The Arch-Chronicler / Blood Scribe:** Preserves the Coven's unwritten lineage histories, ancestral genealogies, and memory records.
    * **The Sanguine Steward:** Oversees mortal Thrall networks, medical blood bank infiltrations, and dietary supply chains.
    * **The Fledgling / Neonate:** Bound progeny undergoing their 100-year Centenary Compulsion, serving the Coven while learning the night.
  * **The Five Sacred Laws of the Coven:**
    1. **The Law of the Shroud / Veil:** Absolute enforcement of secrecy. Revealing the supernatural curse to mortal masses is high treason, punishable by immediate True Death.
    2. **The Law of Haven Sanctuary (Absolute Non-Violence):** All unsanctioned internal bloodletting, physical assault, or combat between vampires within haven grounds is strictly forbidden under penalty of forced Torpor or exile.
    3. **The Law of the Sanguine Tithe (Vault Contribution & Tithing Protocols):** Fledglings and lower members must yield a mandatory portion of their hunting yields to the Apex Elder's vault (**1 Blood Reserve per 5 reserves harvested** during hunts, or a minimum of 1 stored draft per week).
       * *Sealed Tithe Vessel Deposit (Universal Primary Method — All Eras):* Members harvest mortal blood during hunts outside haven grounds and store it in sealed tithe vessels matching setting technology (clay amphorae/flasks in Fantasy, glass carboys/phials in Gothic/Modern, vacuum bio-canisters in Sci-Fi). Deposits into the vault chamber require **0 bloodletting inside haven grounds**.
       * *In-Haven Voluntary Donation (Genre-Agnostic Closed-Conduit Protocol):* If a member donates directly from their own body inside haven grounds, open blood dripping is strictly forbidden under Law 2. Transfers must utilize setting-appropriate closed conduits (consecrated spigot/chalice altar in Fantasy, syringe conduit node in Modern, bio-extraction port in Sci-Fi) that seal the puncture upon removal.
       * *Tithe Default & Judicial Escalation:* If a member harvests 0 blood due to severe injury or stasis, a 1-week **Hardship Deferral** is granted automatically. If unpaid for 2 consecutive weeks, the matter escalates to [The Law of Sanguine Justice](#secrecy-covens-and-thralls).
       * *No Over-Tithe Credit Rule (Independent Settlement):* Each tithe period (weekly minimum or 1-per-5 harvested) is calculated and settled independently. Donating surplus blood vessels or reserves in excess of the mandatory obligation is received as voluntary tribute by the Apex Elder and absorbed permanently into the Coven Vaults — generating **zero forward credit** toward future weekly minimums or future harvest obligations.
    4. **The Law of the Tabula Rasa (Unwritten Memory):** It is strictly forbidden to write, draw, paint, photograph, or digitally record any image, name, physical description, or record of another vampire—or of oneself. All lineage history, names, and lore must be preserved purely through oral tradition or telepathic memory ([*Bloodline Memory*](#behavioral-powers)). Creating physical or digital records of a vampire is high treason, punished by immediate destruction of the records and severe physical discipline. *Discipline Tiers:* Tabula Rasa violations carry mandatory Coven penalties: Minor/Accidental (single photo/sketch) = **30-Day Power Lockout + 50% Blood Reserve Drain**; Major/Intentional (written journal or digital archive) = **Forced Stage 3 Torpor for 1 Year** + immediate destruction of all records.
       * **The Chronicler's Connection (Synchronized Network):** All Coven Arch-Chroniclers and Blood Scribes share a synchronized telepathic memory network. Wiping or altering the memory of a single Chronicler (e.g. via *Lethe's Touch*) is useless, as their memories are automatically backed up and mirrored across all other Coven Chroniclers worldwide.
       * **The Blood Archive Ritual (Action Economy, Overload & Archiver Immunity):** To maintain chronological physical backups without violating Tabula Rasa, Chroniclers conduct a periodic blood storage ritual: preserving micro-drafts of blood in small, sealed obsidian phials labeled chronologically (*Blood Archives*). Drinking a draft from a Blood Archive phial allows a vampire to "read" that era's recorded events in vivid, first-person sensory detail. Ingesting an Archive phial consumes **1 Action** (standard phial ingestion speed), but processing the abundant sensory data takes time—the psychic memories take effect on the **following round**. Non-vampires gain zero memories from drinking phials. For non-Archiver vampires, processing the intense influx of historical data is sensory-overwhelming: ingesting an Archive phial in mid-combat imposes a **-2 penalty to all actions/concentration for 1 combat round** while the brain digests the sensory overload. *Archiver Immunity:* Arch-Chroniclers and Blood Scribes (*Archivers*) possess conditioned psychic capacity to digest memory streams seamlessly; Archivers are completely **immune** to sensory flood and suffer **0 combat penalties** when ingesting Archive phials.
       * **Zero Nutritional Value & Crystallization:** Blood Archive phials are small historical records and **provide zero nutritional value (0 Blood Reserves)**; they cannot be consumed for sustenance or used to stave off starvation. As centuries pass, the blood inside the phial naturally crystallizes into red glass-like mineral. Crystallized blood retains 100% of its recorded psychic history indefinitely; dissolving or ingesting the red crystal allows a vampire to read that era's memories, but confers zero nutritional reserves or physical buffs.
       * **Mortal Ingestion Profile:** Only vampires can process psychic memories stored in Blood Archive phials. A mortal who drinks an Archive draft gains no memories; instead, they suffer severe vitae poisoning or become instantly enthralled as a [Thrall](#social).
       * **Lethe's Touch Archive Interaction:** Drinking a Blood Archive draft allows a vampire to experience recorded memories as a third-person observer, but does **NOT** remove or unlock a [*Lethe's Touch*](#behavioral-powers) memory block from their own personal brain.
    5. **The Law of Sanguine Justice (Judicial Authority & Penal Code):** The supreme legal framework governing all Coven trials, legal disputes, vault theft, tithe defaults, and treason.
       * *Judicial Exemption to Haven Sanctuary:* The Coven Tribunal (Apex Elder, Regent Enforcer, and Coven Council) holds the **exclusive lawful authority** to suspend [The Law of Haven Sanctuary](#secrecy-covens-and-thralls) for judicial enforcement inside haven grounds.
       * *Apex Vault High Theft Penalties:* Stealing stored blood reserves or relics from the Apex Elder's vault constitutes High Theft under Sanguine Justice, punished by an immediate **30-Day Power Lockout** AND **doubling the offender's tithe requirement for 1 full year**.
       * *Sanctioned Judicial Punishments:* Forced vein draining (extracting 2 reserves via judicial conduit for unpaid tithes or theft reparations), corporal branding, 30-Day Power Lockouts, forced Torpor, or True Death. Unsanctioned bloodletting by non-tribunal members remains a severe crime under Law 2.
  * **Territorial Conflict & Treaties:** Covens aggressively mark hunting boundaries. Invading a rival Coven's established hunting grounds without a formal Blood Treaty grants defending vampires a **+1 home-field ambush bonus** on their own turf.
* **Thralls & Vitae Addiction:** Mortals who are fed upon and given small drafts of vampire blood (vitae) become deeply bound to their vampire master.
  * **Capacity & Sire Bond Restriction:** A newly created New World vampire begins with **0 Thralls** and lacks the mystical capacity to bind mortals. Furthermore, a fledgling cannot possess a Thrall while bound in servitude to their sire (during the 100-year Centenary Compulsion).
  * **The 100-Year Capacity Milestone:** Thrall capacity is unlocked strictly at **100-year increments post-change** (Year 100+: 1 Thrall capacity; Year 200+: 2 Thralls capacity; Year 300+: 3 Thralls capacity).
  * **Early Shatter Attempt Clarification:** Executing a successful early Shatter Attempt severs psychological obedience to the Sire, but **does NOT grant early Thrall capacity slots**. The 100-year benchmark for unlocking the first Thrall slot is engraved in stone; an independent 20-year-old vampire who shattered their bond must still wait until their 100th year post-change to unlock their first Thrall slot. Thralls are never gained automatically; the vampire must actively perform the enthrallment process (feeding vitae over time) to fill an open capacity slot.
  * **Physical Benefits:** Thralls gain enhanced physical strength, rapid non-supernatural healing, immunity to mundane illnesses, and suspended aging while receiving regular doses of vitae.
  * **Feeding Cadence & Duration Cap:** A Thrall must consume at least 1 draft of their master's vitae every **14 days** to maintain the bond and physical enhancements. Consuming multiple drafts of vitae in a single sitting does **NOT** stack duration (capped at 14 days maximum).
  * **Dual-Master Conflict (Bloodline Duel):** If a rival vampire attempts to force-feed their vitae to an already bound Thrall, the Thrall becomes the physical vessel for a **Bloodline Duel** between the Original Master and the Intruder Vampire. The outcome is resolved using the [Universal Age Tier Superiority Modifier System](#age-tier-superiority-modifier-system) (Original Master Tier vs Intruder Tier):
    * *Original Master Wins (Higher/Equal Tier or Wins Test):* The intruder blood is violently purged from the Thrall's system. The Thrall remains loyal, but suffers physical nausea and vomiting for 1 scene.
    * *Intruder Wins (Higher Tier / Wins Test):* The Thrall's original master bond is shattered, and the Thrall suffers violent internal hemorrhaging bordering on death (takes **2 Direct Core Health Damage**, placing the Thrall on the Brink of Death).
  * **Withdrawal Penalties:** If denied vitae past 14 days, the Thrall loses all physical buffs within 48 hours and suffers excruciating withdrawal (fever, shivers, severe paranoia, suicidal depression, and intense craving for vitae). Long-term Thralls suffer a rapid aging catch-up over several months if permanently cut off.
  * **Vitae Sabotage & Desperation:** If a master is immobilized in Torpor or buried in Native Soil for Re-Rooting, Thralls approaching Day 14 without feeding face extreme panic. On Day 14, the Thrall must pass a **Self-Control / Willpower check**.
    * *Failure (Betrayal/Extraction):* Driven by survival instincts to stave off agonizing withdrawal, the Thrall attempts to harvest blood directly from their master.
    * *Accessible Master:* If the master is accessible (e.g. Torpid in a coffin), the Thrall bleeds their master's heart/wrist for 1 draft—stealing 1 blood reserve from a Torpid master or interrupting a Re-Rooting recovery with a **+1 day penalty**.
    * *Inaccessible Master (Buried Soil Extraction):* If the master is buried deep underground, the desperate Thrall frantically digs up and ingests the blood-infused Native Soil surrounding the vampire. Consuming the earth staves off the Thrall's withdrawal, but **corrupts the Native Soil micro-ecosystem** and halts the master's Re-Rooting recovery track entirely.
    * *Multiplicative Soil Decay (Multiple Thralls):* Multiple Thralls digging up the same Native Soil grave site stack their destruction: the first Thrall reduces soil life from 30 days to **6 days**, and each subsequent Thrall digging on Day 14 reduces remaining soil life by **50%** (6 days $\rightarrow$ 3 days $\rightarrow$ 1.5 days $\rightarrow$ Total Soil Ruin).
  * **Master True Death Sanguine Withdrawal vs Full Diablerie Bond Inheritance & Overage Strain:** Upon a master's True Death (sunlight incineration, decapitation), the blood bond shatters instantly; living Thralls lose physical buffs within 48 hours and enter acute [Sanguine Withdrawal](#withdrawal-penalties). However, if a rival vampire commits [Full Diablerie](#diablerie-the-ultimate-taboo) upon the master, the Diablerist absorbs the master's soul resonance, **automatically inheriting the blood bond** over the victim's living Thralls.
    * **Thrall Cap Overage Drawback (Psychic & Vitae Upkeep Drain):** Any inherited Thralls exceeding the Diablerist's age-tier Thrall capacity create **Thrall Cap Overage Strain**. Each overage Thrall imposes a **-1 penalty to daily Blood Reserve regeneration** and a **-1 penalty to Self-Control checks** due to the psychic clutter of managing multiple conflicting blood bond frequencies simultaneously.
    * **Coven Law on Overage Release (Sanctioned Termination vs Council Dispensation):** Coven Law strictly forbids abandoning overage Thralls into mortal society due to secrecy breach risks. To resolve Overage Strain, the master must return to or below capacity via **Sanctioned Termination** (execution conducted off Coven sanctum grounds) or by obtaining a formal **Sanctioned Release Dispensation** from the Coven Council (permitting controlled euthanasia or deep memory erasure via *Lethe's Touch*). Abandoning an overage Thrall inside Coven territory without Council authorization is a punishable Coven offense.

## Types

There are 3 types of vampires; [Old World](#old-world), [New World](#new-world), and various [mutations](#mutations).

### Mutations

Mutations represent tragic catastrophes during creation, resulting in a fractured, corrupted transformation. Mutations are mechanically triggered by one of three specific failures, producing distinct mutant strains:

#### 1. The Feral Husk (Trigger: Botched Drain / Premature Pull-Away)
Created when an Unlearned Sire fails their **Self-Control** check during [Creation](#creation) and pulls away from the victim before Stage 4 of the [Brink of Death progression](#draining). The victim's brain suffers partial necrosis before Sire blood enters, producing a zombie-like predatory husk.
* **Sensory Profile:** Gaunt, sunken yellow eyes, grey translucent skin tightly stretched over bone, elongated jagged nails, and a perpetually open mouth dripping black bile. Incapable of speech, complex thought, or emotional connection.
* **Behavioral Traits:** Locked in a **permanent [Feral State](#post-change)**. Cannot be reasoned with, commanded via *Imperious Word*, or pacified by Pre-Change Anchors.
* **Combat Adjustments:**
  * **+2 Melee Damage:** Savage claws deal heightened physical damage.
  * **-2 Defense / Cognition:** Lacks tactical awareness, charging blindly into melee.
  * **Pain Immunity:** Immune to pain penalties, fear checks, and psychological stun.

#### 2. The Hollow Abomination (Trigger: Power Fade Collapse)
Created when a young Sire's power count is so low (2–3 total powers) that the [Power Fade](#power-fade--inheritance) math forces the fledgling's starting power slots to 0. The ancient vampiric bloodline collapses into an unstable, hollow shell.
* **Sensory Profile:** Translucent, paper-thin white skin revealing pulsing black veins underneath; irregular obsidian bone ridges erupting from the spine and jaw. The Abomination emits a constant low-frequency hum of distorted blood static.
* **Behavioral Traits:** Suffers constant, excruciating physical agony as their corrupted blood tethers attempt to draw non-existent magic. Highly volatile and prone to sudden explosive violence.
* **Combat Adjustments:**
  * **0 Starting Power Slots:** Possesses no standard [Supernatural](#supernatural-powers) or [Behavioral](#behavioral-powers) powers.
  * **Sanguine Shockwave:** Can expend 1 blood reserve to emit a violent, 15-foot telekinetic explosion of dark blood, knocking back all surrounding enemies up to **20 feet**, knocking them prone, and dealing area damage. *Haven Sanctuary Law Notice:* Sanguine Shockwave hits ALL targets (allies and enemies) within 15 feet. Invoking Sanguine Shockwave inside Haven grounds that hits or bleeds a fellow Coven member strictly violates the [Law of Haven Sanctuary](#secrecy-covens-and-thralls).
  * **Solar Vulnerability:** Takes **double damage** from sunlight (advancing to Round 3 Ash Collapse in 9 seconds instead of 18 seconds).

#### 3. The Spliced Reaper (Trigger: Artificial / Cyber-Gene Tampering)
Created when advanced technology or gene-splicing experiments tamper with vampiric DNA, forcing synthetic viral strains or cybernetic filters into the bloodline.
* **Sensory Profile:** Terrifying apex predator featuring a triple-hinged jaw that unhinges wide, a 6-foot prehensile barbed tongue, jet-black eyes with no iris, and bioluminescent crimson veins.
* **Behavioral Traits:** Driven by hyper-engineered predatory aggression. Reapers do not respect Coven laws or Sire authority, hunting both mortals and standard vampires indiscriminately.
* **Combat Adjustments:**
  * **+1 Initiative Bonus:** Hyper-engineered reflex response.
  * **Prehensile Tongue Grapple (15-Foot Range):** Can extend their barbed tongue up to 15 feet to snag, drag, and reel enemies into melee range. *Opposed Grapple Math:* Executing a tongue grapple requires an opposed Strength vs Strength/Agility check against the target. Targets exceeding 250kg (550lbs) cannot be dragged, and instead pull the Spliced Reaper toward the heavy target.
  * **Reaper Contagion & Contact Check:** Bypasses traditional draining/feeding rituals entirely. A bite, claw laceration, or barbed tongue grapple from a Spliced Reaper injects a synthetic viral mutagen. Any target hit must immediately pass a **Hard Constitution / Self-Control check** to fight off the contagion:
    * *Mortal Failure (Epidemic Transformation):* The synthetic virus mutates living human tissue within 60 seconds, transforming the mortal into either a **Secondary Spliced Reaper (50% chance)** or a **Secondary Feral Husk (50% chance)**.
    * *Thrall Response:* Thralls are living humans infused with a master's vampiric vitae. A Thrall receives a **+2 bonus to their Resistance check** (granted by their master's vitae). However, because human blood remains susceptible to viral taint, a Thrall who fails the check **succumbs to the contagion**, transforming into a Secondary Reaper/Husk.
    * *Vampire Failure:* True vampires are immune to full mutation but suffer severe internal tissue decay, taking **1 Direct Core Health Damage** and suffering a **-1 penalty to physical actions** for 1 scene.
  * **Exemption & Epidemic Mechanism (No Sire Tether / 0 Creation Cost):** Reapers created via viral contagion share **NO Sire-Fledgling bond, soul tether, or Centenary Compulsion** to their creator. Furthermore, viral creation consumes **0 Blood Reserves** and completely bypasses the 30-day siring cooldown and progeny capacity caps, allowing a single Reaper to trigger catastrophic, exponential epidemic outbreaks across dense cities within hours.
  * **Synthetic DNA Cellular Breakdown (Secondary Lifespans):** The original **Primary Spliced Reaper (Patient Zero)** possesses a laboratory-stabilized bloodline and does **NOT** suffer cellular breakdown. However, Secondary Reapers and Husks spawned via field contagion lack a true heart reservoir tether, causing their synthetic DNA to suffer catastrophic cellular breakdown:
    * **Secondary Feral Husks:** Possess a strict lifespan of **24 Hours** before their internal organs liquify into toxic black sludge.
    * **Secondary Spliced Reapers:** Possess a strict lifespan of **7 Days (1 Week)** of active hunting before synthetic genetic decay dissolves their body into grey ash and sludge (unless sustained by continuous drafts of fresh living blood).

#### Neonates (New World: < 500 Years)

Neonates (New World vampires) have existed for less than 500 years [post-change](#post-change). They make up for their relative lack of ancient powers with intense reactions, raw emotion, volatile adaptability, and deep familiarity with mortal society.

* **Starting Character Generation:** A newly generated Neonate begins with a starting pool of **1 [supernatural power](#supernatural-powers)** and **1d2+1 [behavioral powers](#behavioral-powers)**.
* **Natural Power Progression:** A Neonate naturally gains **+1 additional power slot for every 150 years** lived post-change (e.g., at Year 150, Year 300, Year 450).
* **Blood Potency:** Produces **Tier 2 Standard Vitae** (1 Blood Reserve per draft).
* **Species Perks:** Receives **+1 Initiative bonus** and **1.5x base movement speed**.
* **Societal Role:** Neonates act as front-line emissaries, hunters, and technological operators. Because they remember mortal life in recent decades, they view mortals as former peers—making them adept at blending into modern cities, operating technology, and managing Thrall networks.
* **Milestone Rite (Year 100 - The Freedom Rite):** Reaching the 100-year mark is celebrated as the neonate's first major milestone. The [Centenary Compulsion](#social) naturally breaks, freeing the neonate from involuntary sire servitude and unlocking their **1st Thrall capacity slot**.

#### Elders (Old World: 500 to 1,199 Years)

Elders (Old World vampires) are ancient lords who have survived between **500 and 1,199 years post-change**. They are formidable, cold, and deeply detached from mortal humanity, viewing living humans as livestock and neonates as temporary pawns.

* **Starting NPC / Elder Generation:** The starting pool of **1d3+2 [supernatural powers](#supernatural-powers)** and **1d2+1 [behavioral powers](#behavioral-powers)** is **exclusively used when creating a brand-new Elder character** who enters the game already at 500+ years of age.
* **Natural Transition at Year 500 (The Ascension):** When a neonate naturally reaches their 500th anniversary post-change, they undergo **The Ascension**, officially achieving **Elder Status**:
  1. **Species Perk Upgrade:** Their blood crystallizes. They immediately unlock all Elder physical enhancements (+2 Initiative bonus, 2x base movement speed, doubled jump distance, 1 free Round 1 positioning action, and an extra bonus action during surprise rounds).
  2. **Continued Power Growth:** Total power slot count continues scaling naturally (+1 power per 150 years lived).
* **Blood Potency:** Produces **Tier 4 Elder Vitae** (3 Blood Reserves per draft, High-Power Surge, Vitae Euphoria addiction risk, 24-hr memory siphon, bypasses rival lineage static).
* **Governance & Feudal Ideology:** Elders govern Covens with feudal discipline, preserving traditional haven sanctuary laws and territorial boundaries.

#### Ancients (Primordial Old World: 1,200+ Years)

Ancients (Primordial Old World vampires) are legendary figures who have survived for **1,200+ years post-change**. Their very presence distorts ambient reality, and their blood carries god-tier metaphysical weight.

* **Starting NPC / Ancient Generation:** The starting pool of **2d3+3 [supernatural powers](#supernatural-powers)** and **2d2+2 [behavioral powers](#behavioral-powers)** is **exclusively used when generating a Primordial Ancient NPC**.
* **Natural Transition at Year 1,200 (The Primordial Rite):** When an Elder survives to their 1,200th anniversary post-change, they achieve **Ancient Status**:
  1. **Primordial Species Perk Upgrade:** Their physical form becomes near-godlike (+3 Initiative bonus, 3x base movement speed, doubled jump distance, 2 free Round 1 positioning actions, and complete immunity to non-magical physical weapon damage).
  2. **Continued Power Growth:** Total power slot count continues scaling naturally (+1 power per 150 years lived).
* **Blood Potency:** Produces **Tier 5 Ancient Vitae** (4 Blood Reserves per draft, all Tier 4 Elder benefits, plus **Permanent Power Gain & Soul Strain Risk**).
* **Mythic Status:** Ancients rarely walk the public night, dwelling in deep haven vaults or orbital sanctuaries. They are revered as living gods by their bloodline descendants.
