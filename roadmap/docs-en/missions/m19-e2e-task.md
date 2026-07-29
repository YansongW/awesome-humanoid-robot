# M19 · End-to-End Task Integration: Hear the Command, Walk Over, Pick It Up

**Global Position**: After both M14 Walking Deployment and M18 Grasping Strategy have passed. The input consists of subsystems that have individually passed unit tests (command, navigation, detection, grasping, placement). The output is an end-to-end system (Stage 3 overall acceptance criterion) where the "command → navigation → grasping" full chain succeeds ≥7 times out of 10 consecutive trials, with each trial ≤2 minutes. M20 will add reliability and safety shells to this system.

**Prerequisites**: [M18 · Imitation Learning Training and Deployment](m18-imitation-learning.md) meets the standard (fixed-protocol grasping success rate ≥70%, clipping and degradation are effective); [M14 · Sim-to-Real Deployment](m14-sim-to-real.md) meets the standard (stable walking on flat ground + communication watchdog graded activation); M16 localization stack is available (SLAM mapping and online localization); [ROS 2](/entry/ent_software_ros_2_middleware_2024/) node topology and interfaces are frozen.

Theoretical Background: The end-to-end task chain is the final assembly of perception, planning, learning strategies, and middleware. A systematic discussion can be found in [Chapter 24: End-to-End Software Stack](/wiki/chapters/chapter-24/) and [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/); the command layer and VLA are covered in [Chapter 19: VLA](/wiki/chapters/chapter-19/), and the manipulation segment is covered in [Chapter 16: Manipulation and Grasping](/wiki/chapters/chapter-16/).

## Step 1: Task Decomposition and State Machine—Test Segments Individually First, Then the Full Chain

[What to Do] Freeze the task into a five-segment pipeline. For each segment, clearly define the four elements: **Input / Output / Timeout / Failure Exit**:

| Segment | Input | Output | Timeout (Engineering Suggested Value) | Failure Exit |
|---|---|---|---|---|
| 1 Command Parsing | Text/Voice | Target Object + Target Location | 5 s | Ask back/Report error, wait for resend |
| 2 Navigation to Table | Target Standing Point | Arrival (Dual Threshold Criterion) | 60 s | Replan ≤2 times → Stand still in place and report error |
| 3 Detection and Localization | RGB-D Frame | Object 6D Pose | 10 s | Redetect ≤2 times → Return to Segment 2 for a small step reposition |
| 4 Grasping | Object Pose | Gripper Closed + Confirmation Signal | 30 s | Retract wrist and reset → Return to Segment 3 |
| 5 Placement Confirmation | Target Placement Point | Placement + Verification | 30 s | Placement fails → Keep holding and report error |

Implement using a state machine or behavior tree (see [Chapter 24](/wiki/chapters/chapter-24/) for selection and software stack organization). Each segment should first pass individual tests in simulation or static scenes before being integrated into the full chain.

[Why] The end-to-end task is a cross-validation of all subsystems. Segmented observability is necessary to locate the failing segment (original text from Stage 3 overview). Without an explicit state machine, a "monolithic script" makes it impossible to identify which segment failed; timeouts and failure exits are prerequisites for the system to "report errors safely" rather than "run amok"—Step 5's failure injection test specifically examines this.

[How to Analyze Your Situation] Walking is not yet stable enough: According to the pragmatic advice from Stage 3, first run the Segment 3–5 closed loop with a "fixed stance + tabletop grasping" approach, and unlock Segment 2 last. Don't pursue a perfect framework for the state machine implementation: a Python state machine script with logging is better than a heavy behavior tree that never runs.

## Step 2: Command Layer—Start with Fixed Phrases, VLA Only for Scheduling

[What to Do] Three levels from simple to complex, choose based on acceptance requirements:

1. **Fixed Phrase Text** (Starting point, default for acceptance): Input "go to the table and grab the cup" in the terminal, template parsing yields "target object=cup, target location=table standing point A";
2. **ASR Voice** (Optional enhancement): Voice-to-text followed by the same template parsing; ask back if recognition confidence is low;
3. **VLA Scheduling** (Advanced): Introduce [OpenVLA](/entry/ent_method_openvla/), [π0](/entry/ent_method_pi0/), or [GR00T N1](/entry/ent_method_gr00t_n1/) for open-vocabulary command parsing and skill scheduling—but **the underlying grasping is still executed by the M18 strategy** (Stage 3 pragmatic route: VLA is responsible for "understanding", the dedicated strategy is responsible for "grasping").

[Why] Under personal data and computational constraints, the real-robot success rate and latency of VLA directly outputting full-body actions cannot yet support the acceptance protocol; after decoupling "understanding the command" from "successful grasping", the two segments can iterate and be accepted independently. Positioning of the three cards: OpenVLA is trained on open-source data from [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/), π0 is a versatile strategy pre-trained across multiple embodiments, and GR00T N1 is NVIDIA's general-purpose foundation model for humanoids (see each card and [Chapter 19](/wiki/chapters/chapter-19/) for details).

[How to Analyze Your Situation] No GPU cluster: OpenVLA public weights + LoRA fine-tuning on self-collected data is the lowest-barrier entry point (Stage 3 Step 11 suggestion). Just want to pass acceptance: Level 1 is sufficient; focus your energy on the success rates of Segments 2–4. For the edge-side latency budget of VLA inference, see [M18](m18-imitation-learning.md) Step 5 and the [Computing Platform Selection Guide](../playbooks/compute-selection.md).

## Step 3: Navigation Segment—Reuse M16 Localization Stack, Interface with M14 Walking

[What to Do]

1. **Mapping and Localization**: Use M16's SLAM stack for offline mapping and online localization (sensor configuration see Stage 3 Perception Stack section; background on localization sensors see [Chapter 5: Sensing](/wiki/chapters/chapter-05/));
2. **Standing Point Calibration**: Table-side operation standing points are **calibrated offline manually** and written into the map (standing points facing the table, with the end-effector reachable to the cup); do not calculate online in real-time;
3. **Walking Interface**: Path planning outputs velocity/target commands to the M14 walking strategy; the walking segment is only responsible for "arriving at the point", fine alignment is left to Segment 3's vision;
4. **Arrival Criterion**: **Dual thresholds** for position error and orientation error (e.g., ≤10 cm and ≤10°, engineering suggested values, to be verified against your operation precision); both must be met for Segment 2 to be considered complete.

[Why] Offline calibration of standing points is the cheapest way to keep "insufficient navigation accuracy" out of the door: the arrival accuracy required for operation (centimeter-level) is often higher than what SLAM localization can stably achieve. Both thresholds are indispensable: if the position is reached but the orientation is off by 20°, the end-effector workspace may not even cover the cup.

[How to Analyze Your Situation] Fixed room, short route: RGB-D odometry is sufficient (Stage 3 Step 5 scope); use LiDAR for cross-room scenarios. How to determine the arrival threshold: measure the robot's limit position where it can "just barely grab the cup"—if set too large, Segment 4 takes the blame; if set too small, Segment 2 never converges.

## Step 4: Manipulation Segment—Detection, Grasping, Confirmation, Stand Still Before Acting

[What to Do] Details of the Segment 3–5 closed loop:

1. **Detection and Localization**: [RGB-D Camera](/entry/ent_component_rgbd_camera/) detects the cup and outputs a 6D pose (Stage 3 criterion: 3D localization error ≤1 cm);
2. **Grasping Execution**: The pose is passed to the M18 strategy (learning-based route) or IK + planning primitives (traditional route, [Inverse Kinematics](/entry/ent_method_inverse_kinematics/)), executing approach—close—lift;
3. **Grasping Confirmation**: Two out of three signals—gripper current (load detected), equivalent weight (current/force estimation after lifting), camera visual verification;
4. **Mutual Exclusion Rule**: Walking and manipulation are strictly mutually exclusive—only after arriving and stopping stably (velocity zero + posture stable for 1 s, engineering suggested value) is the manipulation segment allowed to start; the chassis command is locked during manipulation;
5. **Failure Retry**: Occasional detection failures allow in-place retries ≤2 times; if still failing, follow the state machine failure exit.

[Why] The confirmation signal is the referee for "whether the grasp was successful": without it, the system would treat an "empty grasp" as a success and continue, inflating the full-chain success rate. The walking-manipulation mutual exclusion comes from physics: a humanoid has no fixed base, and the reaction torque from reaching can disturb balance (Stage 3 common pitfall: "whole-body shaking and falling during reaching"); standing still before operation is a standard trade-off for the first robot. Retries ≤2 times are a statistical trade-off: one retry for occasional failures can recover most cases, while retrying structural failures is useless.

[How to Analyze Your Situation] When M18 strategy and IK primitives coexist, run 20 trials each and compare success rates; use the one with the higher rate—learning strategies are more robust for in-distribution scenarios, while IK primitives are more honest for out-of-distribution positions. If one confirmation signal is missing (e.g., no wrist camera): current + weight dual criteria are sufficient, but mark the confirmation confidence in the log.

## Step 5: Full Chain Integration and Failure Injection – Time to Find Bottlenecks, Inject Faults to Verify Degradation

【What to Do】

1. **Segmented Timing**: Record the time consumption of each segment during each trial to identify bottlenecks (navigation is usually the time-consuming part); target total single trial duration ≤2 min (Stage 3 criterion);
2. **Failure Injection Testing**: Artificially create anomalies – occlude the camera, move the cup midway, send illegal commands, place obstacles on the navigation path – and observe whether the system **safely reports errors and stops in a defined state**, rather than running wild, waiting indefinitely, or silently continuing;
3. **Log Aggregation**: Store the input summary, output, time consumption, and failure reason for each segment in a database ([ROS 2](/entry/ent_software_ros_2_middleware_2024/) bag or structured logs), and generate a one-click report after 10 trials (segment success rate × full chain success rate matrix).

【Why】When each segment works correctly but the full chain fails, it is a classic death scenario for integration tasks, with the cause almost always being interface assumptions (coordinate systems, units, timestamp bases, frame rates); segmented timing and logs make interface issues visible. Failure injection is an introductory action in safety engineering: the system's default behavior for "unseen anomalies" must be a safe state – this is a rehearsal for the M20 FMEA.

【How to Analyze Your Situation】When the full chain does not meet the standard, do not rush to modify any segment: first look at the report matrix – if failures are concentrated in one segment, fix that segment; if failures are scattered across segments, prioritize fixing segments with unclean failure exits (if the system cannot even "fail gracefully", discussing success rates is meaningless). For the coordinate system, always use the TF tree; only pass "poses in the map frame" between segment interfaces, not local coordinates.

## Step 6: Acceptance Rehearsal – Follow the Formal Process According to Stage 3 Criteria

【What to Do】Conduct a complete acceptance test according to the formal protocol and archive the results: 10 consecutive trials (objects and positions arranged according to a fixed checklist, commands using fixed sentence patterns), record the success/failure, total duration, failed segment, and failure reason for each trial; record the entire process on video (head camera view + third-person view). The criterion is the Stage 3 overall acceptance: **success ≥7 times, single trial ≤2 minutes**. For each failure, write a root cause analysis (which segment, what type of failure, what to change next), and archive it together with the video as a report.

【Why】The value of the acceptance rehearsal is not in "passing", but in leaving a reproducible baseline: after M20, every change (model swap, firmware update, structural part change) must be re-run using the same protocol so that numbers can be compared horizontally. The video is the only evidence that can be "reviewed after the fact" – if the root cause analysis says "segment 3 detection failed", the video allows you to verify this judgment three months later.

【How to Analyze Your Situation】Barely passing (7/10): Perform one round of root cause analysis for the 3 failures before declaring completion – a system that barely passes cannot withstand the regression of changes in M20. If the results of two acceptance tests differ by >2 trials: check environmental variables (lighting, battery level, floor), and also write the acceptance conditions into the protocol to fix them.

## Acceptance Criteria

- [ ] Five-segment state machine documented: each segment has complete input/output/timeout/failure exit elements, and segment-level single test records are archived.
- [ ] Command layer runs through according to the selected gear (fixed sentence pattern as the default gear), with safe exits for illegal commands.
- [ ] Arrival criterion dual-threshold calibrated through actual testing; navigation segment time consumption and success rate included in the report.
- [ ] Grasp confirmation signal ≥2 channels; walk-manipulation mutual exclusion rule verified on the actual robot.
- [ ] Failure injection test passed: system reports errors safely under occlusion/moving objects/illegal commands, with no running wild or deadlock.
- [ ] Formal acceptance: 10 consecutive trials with success ≥7, single trial ≤2 min, video and root cause analysis report documented.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Each segment correct, full chain fails | Inconsistent interface assumptions (coordinate system/units/timestamps) | Only pass map-frame poses between segments; print the units and coordinate system of each segment's input/output |
| System runs wild after a segment fails | That segment has no failure exit or the exit is not implemented | Go back to Step 1 state machine table and check segment by segment; reproduce with failure injection |
| Navigation time exceeds budget | Conservative path planning / walking speed not released / re-planning infinite loop | Locate with segmented timing; release speed and retest; cap the number of re-plannings |
| Intermittent detection failures drag down success rate | Lighting sensitivity / view blind spots / calibration drift | Fix acceptance lighting; add visual verification retry; recalibrate extrinsic parameters |
| State machine deadlock (two segments waiting for each other) | State transition condition written as a circular wait | Add timeouts to all waits; draw a state transition diagram to check for loops |
| Unintended operation during walking causes shaking | Mutual exclusion rule not effective | Check the mutual exclusion flag; add a "stationary for 1 s" condition to the arrival criterion |

## Companion Reading

- Previous task: [M18 · Imitation Learning Training and Deployment](m18-imitation-learning.md)
- Next task: [M20 · Reliability, Maintenance, and Safety Engineering](m20-reliability-safety.md)
- Theoretical background: [Chapter 19 VLA](/wiki/chapters/chapter-19/), [Chapter 24 End-to-End Software Stack](/wiki/chapters/chapter-24/), [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/)
- [Stage 3 Overview](../stage-3-humanoid.md) · [Roadmap Overview](../index.md)
