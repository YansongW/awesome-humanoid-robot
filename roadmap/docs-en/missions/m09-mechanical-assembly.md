# M09 · Complete Machine Assembly, Wiring Harness and Power Supply: From a Box of Parts to a Machine That Can Stand

**Global Position**: After the procurement and arrival of [M08](m08-platform-selection.md), Step 3 (Mechanical Assembly) and Step 6 (First Power-On) of the [Stage 2 Overview](../stage-2-biped.md) replication process. Input is a box of parts and tools; output is a **mechanically complete machine + a power supply and wiring harness system that has passed the smoke test**. Downstream [M10 · URDF Modeling and Export](m10-urdf-modeling.md) will use the weighing and measurement data from this task—if the structure is not well-defined, the model will be inaccurate, so modeling is scheduled after this task.

**Prerequisites**: M08 acceptance passed (all parts arrived, tools in place, lithium battery storage compliant); experience with Stage 1 (M05/M07) assembly and bench testing; have read the safety red lines (emergency stop, gantry, lithium battery) in the [Stage 2 Overview](../stage-2-biped.md).

Theoretical background: [Chapter 11 Assembly, Integration and Testing](/wiki/chapters/chapter-11/), [Chapter 6 Computation, Power and Thermal Management](/wiki/chapters/chapter-06/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/). Platform facts are cited from the `data/roadmap/research/` research files.

## Step 1: Modular Assembly—Single Leg → Single Arm → Torso → Final Assembly

【What to Do】Strictly follow the sequence "Single Leg → Single Arm → Torso → Final Assembly". **After completing each module, do three things before proceeding to the next**:

1. Manual Cranking: Without power, manually move each joint through its full range of motion to feel for smoothness and backlash;
2. Interference Check: Move the joint to its limit positions to confirm that structural parts and wiring harnesses do not scrape against each other;
3. Weighing and Recording: Place the module on a scale and write the number into a table—the inertial parameters for M10 and the simulation for Stage 2 Step 5 rely entirely on this set of data.

Fastener Specifications: Follow the official manual for torque (if not specified, use engineering recommended values based on thread specifications, which need to be verified independently); apply thread locker to threads in vibration zones; do not force printed part pre-drilled holes to the bottom. Replicate the platform according to official materials: ToddlerBot has an assembly manual + assembly video + printed jigs; the paper verifies that someone with no hardware experience can independently complete the full machine assembly in 3 days (toddlerbot.md); Berkeley requires first building 22 actuators yourself—first fully assemble one 6512 and pass a no-load test, then batch replicate the remaining 21; CAN bus soldering is also completed in this step (berkeley-humanoid-lite.md).

【Why】The cost of rework after final assembly is several times that of the module level; the feel of manual cranking is the cheapest quality inspection—if the assembly is too tight or misaligned, your hand will know before the current sensor does. Verifying a single unit before batch replication is the only way to compress a "systematic error × 22" into an "error × 1".

【How to Analyze Your Situation】Servo bus platform (ToddlerBot): Assembly mainly involves screwing and plugging wires; focus on checking servo ID programming and horn zero position. Self-developed actuator platform (Berkeley): Get a single actuator running with a no-load test before talking about final assembly; don't power on all 22 at once.

## Step 2: Complete Machine Wiring Harness Planning—Two Diagrams First

【What to Do】Before touching the soldering iron, draw two diagrams:

1. **Power Tree**: Battery → Fuse → Emergency Stop → Power Distribution Board → Each Driver/Main Controller, annotate the voltage and expected current for each segment (background in the [Power Distribution System](/entry/ent_component_power_distribution_system_2024/) card);
2. **Signal Tree**: Main Controller → Communication Bus Segments → Each Actuator/Sensor. Reference specifications: Berkeley has one CAN 2.0 bus per limb (1 Mbps, actuators and IMU communicate at 250 Hz, berkeley-humanoid-lite.md); ToddlerBot uses a 5V TTL serial bus (2 Mbps, 30 motors full state feedback at 50 Hz, toddlerbot.md). Bus topology and termination matching are in the [CAN Bus](/entry/ent_technology_can_bus_2024/) card.

Four construction steps: **Measure actual wire length → Cut → Crimp → Label** (label both ends, write the label number into the signal tree diagram). Specifications: Route power and signal wires in separate bundles; leave torsion allowance at joints (the wire should not be taut during the joint's full range of motion); use pluggable connectors between modules so that replacing a part does not require disassembling the whole machine; provide strain relief at the root of each wire bundle—secure with cable ties to structural parts so that force is not borne by solder joints or terminals.

【Why】The wiring harness is the subsystem with the highest failure rate in homemade robots, and the failure modes are the worst (intermittent, hard to reproduce); the two diagrams are your only map when troubleshooting three months later—the wire not on the diagram is the one you will miss during your inspection.

【How to Analyze Your Situation】Select wire gauge by looking up the current of each branch in a table, leaving a 50% current-carrying margin (engineering recommended value, needs to be verified according to wire specifications); prioritize connectors with anti-reverse keying features—plugging in a connector backwards and burning a board is the most expensive lesson in homemade robotics. The diagrams don't need to be beautiful; hand-drawn and photographed for archiving is fine, but they must be consistent with the actual wiring.

## Step 3: Power System—Battery, BMS, Fuse and Emergency Stop

【What to Do】

1. **Battery Capacity → Runtime Estimation**:

```
Battery Energy (Wh) = Nominal Voltage (V) × Capacity (Ah)
Runtime (h) ≈ Battery Energy (Wh) ÷ Average Machine Power (W)
```

Calculation example (back-calculated from file data): Berkeley's 6S 4000 mAh LiPo ≈ 22.2 V × 4.0 Ah ≈ 88.8 Wh, measured runtime about 30 min (berkeley-humanoid-lite.md), back-calculated average machine power ≈ 88.8 Wh ÷ 0.5 h ≈ 178 W. Forward calculation: target runtime 45 min, estimated average machine power 150 W → need ≥ 150 × 0.75 ≈ 112.5 Wh → under 6S (22.2 V) capacity ≥ 5.1 Ah, choose a 6S 5200 mAh class. Note that runtime is also constrained by thermal limits: ToddlerBot RL walking test showed thermal throttling after 19 minutes (toddlerbot.md)—power remains, but the machine can no longer run.

2. **BMS and Monitoring**: The battery pack must have a protection board/management system ([Battery Management System](/entry/ent_component_battery_management_system/) card); implement voltage monitoring on the machine and set a low battery protection threshold.
3. **Fuse**: Rated value ≥ the maximum operating current of that branch, and < the current-carrying limit of the wire; 1.25–1.5× the operating current is an engineering recommended starting point, which needs to be verified against wire gauge and component specifications.
4. **Emergency Stop (E-Stop)**: Hardwired physical disconnection of motor power, **independent of the software chain** ([Emergency Stop System](/entry/ent_component_emergency_stop_system_2024/) card). Reference: BRUCE is equipped with an independent wireless emergency stop (bruce-westwood.md); THORMANG3 comes standard with a wireless emergency stop and lifting straps (thormang3.md).
5. **Anti-Spark and Power-On Sequence**: Use anti-spark connectors or a pre-charge circuit for the first connection of a large-capacity battery; the full lifecycle specifications for lithium batteries are in the [Lithium Battery Technology Card](/entry/ent_tech_li_battery_humanoid/).

【Why】Most catastrophic accident chains for bipeds start from the power supply: short circuit causing fire, runaway leg swinging, over-discharge ruining the battery. Relying on software for the emergency stop is like entrusting your life to the scheduling luck of the operating system; a fuse is a component that "sacrifices fifty cents to save five hundred dollars".

【How to Analyze Your Situation】First, purchase the official battery specification for the platform as-is (the platform has been verified); if you want to switch to a larger capacity, go back to the formula above to verify the Wh and discharge rate. Test the emergency stop circuit on a bare board for continuity ten times before installing it in the machine.

## Step 4: Main Controller and Network Installation

【What to Do】

1. **Mounting and Vibration Damping**: Rigidly mount the main controller in the torso, add vibration damping pads—structural vibration will directly couple into the IMU readings ([Inertial Measurement Unit](/entry/ent_component_imu_2024/) card). Reference: Berkeley places an approximately $129 Intel N95 mini PC in the torso, running both low-level control and the RL policy (berkeley-humanoid-lite.md); ToddlerBot uses a Jetson Orin NX 16GB for on-board inference (toddlerbot.md).
2. **Cooling Airflow Path**: Ensure the air intake/exhaust vents are not blocked by structural parts; first run a no-load burn-in test to measure the temperature curve; ToddlerBot's 19-minute thermal throttling measurement shows that heat dissipation in a small chassis is a real constraint.
3. **Communication Adapter**: Secure the USB-CAN adapter and USB cable with clips to prevent loosening during movement.
4. **Software Configuration**: Enable auto-start on boot + SSH remote login (BRUCE is controlled via SSH over Wi-Fi/Bluetooth, bruce-westwood.md); execute the real-time solution according to Step 3 of the [Computing Platform Selection Playbook](../playbooks/compute-selection.md); the logic of computational hierarchy is not repeated in this task.

【Why】A loose or overheating main controller is the most common source of "mysterious reboots"; with remote login, the gantry debugging workflow becomes possible—you don't have to work right next to the suspended robot.

【How to Analyze Your Situation】Before installation, confirm the orientation of the cooling vents on the mini PC/development board; if the airflow path is blocked by structural parts, change the mounting orientation. If fan noise is an issue, reserve structural margin for modifying the airflow path. If the on-board computing selection has not been made yet, go back to the playbook to study before installing.

## Step 5: First Power-On Smoke Test—Two-Person, Under Gantry, Channel-by-Channel Enable

【What to Do】Pre-power-on checklist (sign off item by item):

1. Polarity verification: Use a multimeter to confirm positive and negative on each channel; connect the battery interface last.
2. Insulation test: No short circuit between power rails and chassis.
3. Emergency stop link no-load verification: Without motors connected, press the emergency stop to confirm power is indeed disconnected; time from press to power-off < 1 s.
4. Single-channel sequential enable: Enable only one branch at a time; proceed to the next only after current is normal.

First power-on is performed **under gantry suspension** (feet off the ground), with two people: one monitors the interface readings, the other keeps a hand on the emergency stop. Monitor three items: current on each branch, motor/drive temperature, and bus communication (packet loss rate). Perform small-amplitude sinusoidal swings on all joints to verify direction and response. Any abnormality: immediately cut power, record the phenomenon, then troubleshoot.

【Why】Electrical errors are concentrated during the first power-on. Under suspension, any loss of control will not cause the robot to fall—this is the safety red line for Stage 2 and the full-robot version of the M07 bench process.

【How to Analyze Your Situation】No gantry: Use a gantry frame + top strap for simple protection (full-size models like THORMANG3 come with lifting straps from the factory, thormang3.md; desktop machines have even less excuse to go unprotected); archive the smoke test record sheet; you will refer back to it during M14 sim-to-real troubleshooting.

## Acceptance Criteria

- [ ] Records for joint turning, interference checks, and weighing are complete; full-robot weighing is done and compared with BOM estimates.
- [ ] Power tree and signal tree diagrams are documented; cable labeling matches the diagrams; no tension stress throughout the full range of motion (including joint limits).
- [ ] Emergency stop hardwiring is independent of software; measured time from press to power-off < 1 s is recorded and archived.
- [ ] Fuse specifications have written selection rationale; voltage monitoring and low-voltage protection thresholds are set.
- [ ] All joints enable without abnormal current or noise; no abnormal communication packet loss; smoke test checklist is signed and archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Motor remains powered after pressing emergency stop | Emergency stop uses software/relay control path | Return to Step 3: Emergency stop must physically cut power, independent of the software chain |
| CAN communication chaos, high packet loss | Ground loop/poor common grounding, missing termination resistors | Check common ground at each node and 120 Ω termination resistors at both bus ends; use a separate USB adapter port |
| Repeated bending and breakage of cables at joints | Insufficient twist margin, no strain relief at the root | Reroute cables: verify no tension during full joint range of motion; secure cable ties at the root to the structure |
| Battery shifting or abnormal noise during operation | Battery not securely fastened | Add straps/foam to the battery compartment; perform tilt and shake tests |
| Board damage due to incorrect power-on sequence | Signal connected before power; surge enters via signal lines | Define a fixed power-on sequence: stabilize power first, then connect signal/main controller; write it into the checklist |
| Mysterious main controller reboot | Loose mounting or thermal throttling due to overheating | Check mounting and airflow; monitor temperature curve (refer to ToddlerBot 19-minute throttling benchmark) |

## Companion Reading

- Previous task: [M08 · Platform Selection and Procurement](m08-platform-selection.md)
- Next task: [M10 · URDF Modeling and Export](m10-urdf-modeling.md)
- [Stage 2 Overview](../stage-2-biped.md) · [Compute Platform Selection Guide](../playbooks/compute-selection.md)
- Theoretical background: [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), [Chapter 6 Compute, Power, and Thermal Management](/wiki/chapters/chapter-06/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/)
