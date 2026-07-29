# M09 · Complete Machine Assembly, Wiring Harness and Power Supply: From a Box of Parts to a Machine That Can Stand

**Global Position**: After procurement and arrival in [M08](m08-platform-selection.md), this is Step 3 (Mechanical Assembly) and Step 6 (First Power-On) of the [Stage 2 Overview](../stage-2-biped.md) replication process. The input is a box of parts and tools; the output is a **mechanically complete machine + a power supply and wiring harness system that passes the smoke test**. Downstream [M10 · URDF Modeling and Export](m10-urdf-modeling.md) will use the weighing and measurement data from this task—if the structure is not well-defined, the model will be inaccurate, so modeling is scheduled after this task.

**Prerequisites**: M08 acceptance passed (all parts arrived, tools in place, lithium battery storage compliant); experience with Stage 1 (M05/M07) assembly and bench testing; have read the safety red lines (emergency stop, gantry, lithium battery) in the [Stage 2 Overview](../stage-2-biped.md).

Theoretical background: [Chapter 11 Assembly, Integration and Testing](/wiki/chapters/chapter-11/), [Chapter 6 Computation, Power and Thermal Management](/wiki/chapters/chapter-06/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/). Platform facts are cited from [public research archives](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/).

## Step 1: Modular Assembly—Single Leg → Single Arm → Torso → Final Assembly

【What to Do】Strictly follow the sequence "Single Leg → Single Arm → Torso → Final Assembly". **After completing each module, do three things before moving to the next step**:

1.  Manual Crank Test: Without power, manually rotate each joint through its full range of motion to feel smoothness and backlash.
2.  Interference Check: Move joints to their limit positions to confirm that structural parts and wiring harnesses do not scrape against each other.
3.  Weighing Record: Place the module on a scale and record the number in a table—the inertial parameters for M10 and the simulation in Stage 2 Step 5 rely entirely on this data.

Fastener Specification: Follow the official manual torque values (if not specified, use engineering recommended values for the thread size, which must be verified independently). Apply thread locker to threads in vibration zones. Do not force printed part pre-drilled holes all the way down. Replicate the platform according to official materials: ToddlerBot has an assembly manual + assembly video + printed jigs; the paper verifies that someone with no hardware experience can independently complete the full machine assembly in 3 days (toddlerbot.md); Berkeley requires building 22 actuators first—fully assemble one 6512, pass the no-load test, then batch produce the remaining 21. CAN bus soldering is also completed in this step (berkeley-humanoid-lite.md).

【Why】If rework is needed after final assembly, the disassembly cost is several times that of the module level. The feel of the manual crank is the cheapest quality inspection—if assembly is too tight or misaligned, your hand will know before the current sensor. Verifying a single unit before batch production is the only way to compress a "systematic error × 22" into "error × 1".

【How to Analyze Your Situation】Servo bus platform (ToddlerBot): Assembly mainly involves screwing and plugging wires; focus on checking servo ID programming and horn zero position. Self-developed actuator platform (Berkeley): Run a single actuator through a no-load test before discussing final assembly; do not power on all 22 at once.

## Step 2: Complete Machine Wiring Harness Planning—Two Diagrams First

【What to Do】Draw two diagrams before touching the soldering iron:

1.  **Power Tree**: Battery → Fuse → Emergency Stop → Power Distribution Board → Each Driver/Main Controller, annotating voltage and expected current for each segment (see background in the [Power Distribution System](/entry/ent_component_power_distribution_system_2024/) card).
2.  **Signal Tree**: Main Controller → Communication Bus Segments → Each Actuator/Sensor. Reference specifications: Berkeley uses one CAN 2.0 bus per limb (1 Mbps, actuators and IMU communicate at 250 Hz, berkeley-humanoid-lite.md); ToddlerBot uses a 5V TTL serial bus (2 Mbps, full state feedback for 30 motors at 50 Hz, toddlerbot.md). See the [CAN Bus](/entry/ent_technology_can_bus_2024/) card for bus topology and termination.

Four Construction Steps: **Measure wire length → Cut → Crimp → Label** (label both ends, and write the label number into the signal tree diagram). Specification: Route power and signal wires in separate bundles; leave torsion allowance at joints (wire should not be taut during full joint movement); use pluggable connectors between modules so that replacing a component does not require disassembling the whole machine; provide strain relief at the root of each wire bundle—secure with cable ties to structural parts so that force is not borne by solder joints or terminals.

【Why】The wiring harness is the subsystem with the highest failure rate in homemade robots, and its failure mode is the worst (intermittent, hard to reproduce). The two diagrams are your only map when troubleshooting three months later—the wire not on the diagram is the one you will miss during your investigation.

【How to Analyze Your Situation】Select wire gauge by looking up the current of each branch in a table, leaving a 50% current-carrying margin (engineering recommended value, must be verified against wire specifications). Prioritize connectors with anti-reverse keying features—plugging in a connector backwards and burning a board is the most expensive lesson in homemade robotics. The diagrams do not need to be pretty; hand-drawn and photo-archived is acceptable, but they must be consistent with the actual wiring.

## Step 3: Power System—Battery, BMS, Fuse and Emergency Stop

【What to Do】

1.  **Battery Capacity → Runtime Estimation**:

```
Battery Energy (Wh) = Nominal Voltage (V) × Capacity (Ah)
Runtime (h) ≈ Battery Energy (Wh) ÷ Average Machine Power (W)
```

Example calculation (back-calculated from archive data): Berkeley's 6S 4000 mAh LiPo ≈ 22.2 V × 4.0 Ah ≈ 88.8 Wh, measured runtime ≈ 30 min (berkeley-humanoid-lite.md), implying average machine power ≈ 88.8 Wh ÷ 0.5 h ≈ 178 W. Forward calculation: target runtime 45 min, estimated average machine power 150 W → need ≥ 150 × 0.75 ≈ 112.5 Wh → under 6S (22.2 V) capacity ≥ 5.1 Ah, choose a 6S 5200 mAh class. Note that runtime is also constrained by thermal limits: ToddlerBot RL walking measured only 19 minutes before thermal throttling (toddlerbot.md)—power remains, but the machine can no longer move.

2.  **BMS and Monitoring**: The battery pack must have a protection board/management system (see [Battery Management System](/entry/ent_component_battery_management_system/) card). Implement on-board voltage monitoring and set a low-voltage protection threshold.
3.  **Fuse**: Rated value ≥ the maximum operating current of that branch, and < the current-carrying limit of the wire; 1.25–1.5× the operating current is an engineering recommended starting point, must be verified against wire gauge and component specifications.
4.  **Emergency Stop (E-Stop)**: Hardwired physical disconnection of motor power, **independent of the software chain** (see [Emergency Stop System](/entry/ent_component_emergency_stop_system_2024/) card). Reference: BRUCE is equipped with an independent wireless emergency stop (bruce-westwood.md); THORMANG3 comes standard with a wireless emergency stop and lifting sling (thormang3.md).
5.  **Anti-Spark and Power-On Sequence**: Use an anti-spark connector or pre-charge circuit for the first connection of a large-capacity battery. See the [Lithium Battery Technology Card](/entry/ent_tech_li_battery_humanoid/) for the full lifecycle specification of lithium batteries.

【Why】Most catastrophic failure chains in bipedal robots start from the power supply: short circuit causing fire, loss of control causing leg flailing, over-discharge causing battery destruction. Relying on software for the emergency stop is like entrusting your life to the scheduling luck of the operating system. A fuse is a "sacrifice fifty cents to save five hundred dollars" component.

【How to Analyze Your Situation】First, purchase the official battery specification for your platform as-is (the platform has been verified). If you want to switch to a larger capacity, go back to the formula above to calculate Wh and discharge rate. Test the emergency stop circuit on a bare board for ten on-off cycles before installing it in the machine.

## Step 4: Main Controller and Network Installation

【What to Do】

1.  **Mounting and Vibration Damping**: Rigidly mount the main controller in the torso, adding vibration damping pads—structural vibration will directly couple into the IMU readings (see [Inertial Measurement Unit](/entry/ent_component_imu_2024/) card). Reference: Berkeley places an approximately $129 Intel N95 mini PC in the torso, running both low-level control and RL policies (berkeley-humanoid-lite.md); ToddlerBot uses a Jetson Orin NX 16GB for on-board inference (toddlerbot.md).
2.  **Cooling Airflow Path**: Ensure the air intake/exhaust vents are not blocked by structural parts. First, run a no-load burn-in test and measure the temperature curve. The measured 19-minute thermal throttling of ToddlerBot shows that cooling in a small chassis is a real constraint.
3.  **Communication Adapter**: Secure the USB-CAN adapter and USB cable with clips to prevent loosening during motion.
4.  **Software Configuration**: Set up auto-start on boot + SSH remote login (BRUCE is controlled via SSH over Wi-Fi/Bluetooth, bruce-westwood.md). Implement the real-time solution according to Step 3 of the [Compute Platform Selection Playbook](../playbooks/compute-selection.md); the logic of compute tiering is not repeated in this task.

【Why】Loose main controller and overheating are the most common causes of "mysterious reboots". The ability to log in remotely enables the gantry debugging workflow—you do not need to be right next to the suspended robot to operate it.

【How to Analyze Your Situation】Before installing the mini PC/development board, confirm the orientation of its cooling vents. If the airflow path is blocked by the structure, change the mounting orientation. If fan noise is an issue, reserve structural margin for modifying the airflow path. If on-board compute selection has not been done yet, go back to the playbook to catch up before installation.

## Step 5: First Power-On Smoke Test – Two-Person, Under Gantry, Channel-by-Channel Enable

【What to Do】Pre-power-on checklist (sign off item by item):

1. Polarity verification: Use a multimeter to confirm positive and negative on each channel; connect the battery interface last.
2. Insulation test: No short circuit between power rails and chassis.
3. Emergency stop link no-load verification: Without motors connected, press the emergency stop to confirm power is indeed disconnected; time from press to power-off < 1 s.
4. Single-channel sequential enable: Enable only one branch at a time; proceed to the next only after current is normal.

First power-on is performed **under gantry suspension** (feet off the ground), with two people: one monitors the interface readings, the other keeps a hand on the emergency stop. Monitor three items: current per branch, motor/drive temperature, and bus communication (packet loss rate). Perform small-amplitude sinusoidal swings on all joints to verify direction and response. Any abnormality: power off immediately, record the phenomenon, then troubleshoot.

【Why】Electrical errors are concentrated during the first power-on. Under suspension, any loss of control will not cause the robot to crash – this is the safety red line for Stage 2 and the full-robot version of the M07 bench procedure.

【Your Situation Analysis】No gantry: Use a gantry frame + top strap for simple protection (full-size models like THORMANG3 come with lifting straps from the factory, thormang3.md; desktop machines have even less excuse to go unprotected). Save the smoke test record; you will refer back to it during M14 sim-to-real troubleshooting.

## Acceptance Criteria

- [ ] Records for joint turning, interference checking, and weighing are complete; full-robot weighing is done and compared with BOM estimates.
- [ ] Power tree and signal tree diagrams are documented; cable labeling matches the diagrams; no tension stress throughout the full range of motion (including joint limits).
- [ ] Emergency stop hardwiring is independent of software; measured time from press to power-off < 1 s is recorded and archived.
- [ ] Fuse specifications have written selection rationale; voltage monitoring and low-voltage protection thresholds are set.
- [ ] All joints enable without abnormal current or noise; communication has no abnormal packet loss; smoke test checklist is signed and archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Motor remains powered after emergency stop | Emergency stop uses software/relay control path | Return to Step 3: Emergency stop must physically cut power, independent of the software chain |
| CAN communication chaos, high packet loss | Ground loop/poor common grounding, missing termination resistors | Check common ground at each node and 120 Ω termination resistors at both bus ends; use a dedicated USB adapter port |
| Repeated bending and breakage of joint cables | Insufficient twist margin, no strain relief at the root | Reroute cables: verify no tension during full joint range of motion; secure cable ties at the root to the structure |
| Battery shifts or makes noise during operation | Battery not securely fastened | Add straps/foam to the battery compartment; perform tilt and shake tests |
| Board damage due to incorrect power-on sequence | Signal connected before power; surge enters via signal lines | Define a fixed power-on sequence: stabilize power first, then connect signal/main controller; write it into the checklist |
| Mysterious main controller reset | Loose mounting or thermal throttling | Check mounting and airflow; monitor temperature curve (refer to ToddlerBot 19-minute throttling threshold) |

## Related Reading

- Previous task: [M08 · Platform Selection and Procurement](m08-platform-selection.md)
- Next task: [M10 · URDF Modeling and Export](m10-urdf-modeling.md)
- [Stage 2 Overview](../stage-2-biped.md) · [Compute Platform Selection Guide](../playbooks/compute-selection.md)
- Theoretical background: [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), [Chapter 6 Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/)
