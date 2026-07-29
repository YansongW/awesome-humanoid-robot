# M17 · Teleoperation and Data Collection: How Imitation Learning Data is Gathered

**Global Position**: After the arm (M15) and perception stack (M16) are ready, before imitation learning training (M18). Input is a safely movable robot + a calibrated perception stack, output is **≥50 quality-checked episode datasets**—the M18 training script can use them directly without rework.

**Prerequisites**: M16 acceptance passed (perception output stable, time synchronization verified); robot can be safely powered on and moved, emergency stop circuit available (see [Stage 3 Overview](../stage-3-humanoid.md) Step 15).

Theoretical background: [Chapter 17: Teleoperation and Human-Robot Collaboration](/wiki/chapters/chapter-17/) covers teleoperation system design, [Chapter 21: Data Infrastructure](/wiki/chapters/chapter-21/) covers data pipelines, [Appendix B: Key Dataset List](/wiki/appendices/appendix-b/) lists comparable public datasets.

## Step 1: Teleoperation Scheme Selection

[What to do] Compare four options, choose one based on budget and task:

| Scheme | Cost Magnitude | Data Quality | Suitable For |
|---|---|---|---|
| Leader-follower master-slave arm ([ALOHA](/entry/ent_technology_aloha_teleoperation_system_2023/) approach) | ~$20k for full set (card-level) | High: isomorphic mapping, joint-level correspondence | Dual-arm fine manipulation |
| VR controller/headset | Consumer VR device price | Medium: end-effector pose + posture retargeting | Mobile humanoid, whole-body teleoperation |
| Exoskeleton | Confirm with supplier | High but cumbersome to wear | Research teams |
| Keyboard/joystick | Nearly zero | Low: slow, coarse actions | Fallback pipeline validation |

Two important variants:

- **Data collection without a full robot**: [UMI gripper interface](/entry/ent_technology_umi_gripper_interface_2024/)—handheld gripper + wrist camera, human holds the gripper to demonstrate and collect training data (card-level).
- **Practical division for mobile humanoids**: Lower body joystick for fixed-point control + upper body master-slave, drawing on [Mobile ALOHA](/entry/ent_technology_mobile_aloha_2024/)'s whole-body teleoperation approach (Stage 3 level)—don't expect to walk via teleoperation while performing fine grasping.

Anchor: [ToddlerBot](/entry/ent_robot_system_toddlerbot/) uses an isomorphic teaching arm (handle embedded with FSR force-sensitive resistor) + handheld joystick buttons; version 2.0 adds Meta Quest 2 VR teleoperation; Berkeley Humanoid Lite uses SteamVR base stations + controller teleoperation for dual-arm tasks like Rubik's cube, writing, and block stacking (all per `data/roadmap/research/` survey archives).

[Why] Teleoperation serves three purposes: verify hardware reachability, collect imitation learning data, and establish task baselines (Stage 3). The VR route has two hard constraints: **latency** (end-to-end latency reaching hundreds of milliseconds significantly degrades operator feel, engineering experience, measure with your system) and **motion sickness**—first test latency with small-scale trials, then schedule long-duration collection.

[How to analyze your situation] Very tight budget: Start with UMI collection, align format, reuse later with real robot; have a bipedal humanoid: Upper body master-slave + lower body joystick fixed-point; just want to validate pipeline: Use joystick as fallback to run through the "record → playback → train" loop, then upgrade equipment.

## Step 2: Collection Pipeline Setup

[What to do] Freeze "what to record, how to record, where to store" into specifications:

1. **Recorded fields** (consistent with Stage 3 Step 9): Multi-view images (head + dual wrists), joint states (position/velocity), actions (target joint positions after master-slave mapping), language instructions, timestamps.
2. **Unified frame rate**: All streams uniformly sampled at **10–30 Hz** (engineering recommendation, finalize based on storage and compute), align using M16's time synchronization facility.
3. **Storage format**: Start with [ROS 2](/entry/ent_software_ros_2_middleware_2024/) bag; to interface with open-source training ecosystems, use [LeRobot](/entry/ent_software_lerobot_2024/) or RLDS style—[Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) aggregates millions of demonstration frames across embodiments using the unified RLDS format, serving as standard VLA pre-training corpus (card-level).
4. **Directory and naming**: `task_name/date/operator/episode_number`, metadata (calibration version, instruction text, success label) saved with the package.

[Why] Format determines reusability: Missing a field (e.g., no language instruction) means you must re-collect the entire batch to train instruction-conditioned policies later. Naming conventions make it traceable "which data was collected with which calibration version"—batches with expired calibrations must be filterable as a whole.

[How to analyze your situation] Single robot, single task: bag + one parsing script is sufficient; planning multi-task/multi-robot: Align directly with LeRobot/OXE format from the start, don't invent a private format.

## Step 3: Task and Scene Design

[What to do]

1. **Start with a single task**: First task fixed as "grasp cup and place in box", run through the full pipeline before expanding categories.
2. **Scene randomization checklist**: Object position/orientation (uniformly distributed within workspace), lighting (brightness/direction variation), background (change tablecloth/clutter), distractors (gradually add irrelevant objects). Randomize the randomization level for each episode before recording.
3. **Instruction templating**: Template like "put {object} into {container}", freeze vocabulary, instruction strings stored in episodes are always generated from templates.
4. **Define success criteria upfront**: e.g., "object hovers for 3 seconds without falling after gripper closes, and finally lands in the container"—label each episode as success/failure on the spot.

[Why] The policy learns the data distribution: If you only collect "cup in the center", it will only grasp in the center. The randomization checklist defines the policy's generalization boundary and should be written into the collection plan, not based on daily mood. Vague success criteria cause label noise—during M18 training, this manifests as "some demonstrations are learnable, others are not".

[How to analyze your situation] Desktop fixed robot: Start randomization with object position/orientation (best cost-benefit); add lighting and background after single-task success rate stabilizes. For each added randomization level, double the episode budget accordingly.

## Step 4: Collection Execution Specifications

[What to do]

1. **Quality > Quantity**: Smooth movements, moderate speed (operator feels "a bit slow" is just right), no occlusion; always see both the end-effector and target object in the frame.
2. **Handling failed episodes**: **Keep** episodes that fail mid-demonstration and **label them as failures**, but M18 training defaults to using only successful sets; operator-initiated "recovery from error" segments (e.g., dropped and re-grasped) are marked separately—recovery data teaches the policy error correction, high value, but keep proportion within 20–30% (engineering recommendation) to avoid the policy learning to "intentionally fail".
3. **Productivity expectation**: Skilled operator: ~10–20 episodes per hour (engineering recommendation, including scene reset and spot checks); plan 3–5 working hours for 50 high-quality episodes.
4. **Immediate playback spot check**: Play back 1 episode every 5–10 collected, check visuals, time alignment, labels; record operator ID for multi-person collection—style differences are part of the data distribution.

[Why] Imitation learning is extremely sensitive to demonstration quality: Shaky and fast demonstrations produce shaky and fast policies. Immediate spot checks compress incidents like "collected for a whole day only to find timestamps drifted" to within 10 episodes.

[How to analyze your situation] Solo project: Set your own pace, prefer 20 high-quality episodes per day; multi-person shifts: Watch 3 "standard demonstrations" together before starting to calibrate feel, check 2 of each other's episodes at the end of the shift.

## Step 5: Data Quality Check and Split

[What to do]

1. **Automated quality check script**, each episode passes three checks:
   - Time alignment: Image and action timestamp offset < 1 frame magnitude (engineering recommendation);
   - Frame drop detection: Actual frame rate vs target frame rate for each stream, flag if drop rate exceeds threshold;
   - Image quality: Blur (Laplacian variance), overexposure/underexposure (histogram) filtered by threshold.
2. **Training/validation 9:1 split**: Randomly split by episode, once the validation set is defined, freeze it; M18 uses the same set for every experiment.
3. **Dataset card**: Robot model/sensor configuration/calibration version/collection date/task definition/instruction template/episode count and statistics, all in one page. [DROID](/entry/ent_dataset_droid/) is a reference for distributed multi-lab collection (card-level, limitation: only covers fixed arms); [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) is a format reference for cross-embodiment aggregation.

[Why] "Whether data is usable" relies on scripts, not memory: After archiving the quality report (alignment error, frame drop rate, blur ratio), when M18 training has issues, you can first rule out data problems. The dataset card is your only source of truth a month later, or when someone else takes over.

[How to analyze your situation] Even 50 episodes require the full process: Write the script once, reuse at zero cost for 500 episodes; even 5 validation episodes must be kept—without a frozen validation set, every "improvement" in M18 cannot be attributed.

## Acceptance Criteria

- [ ] ≥50 quality-checked episodes (Stage 3 criterion), with complete success/failure labels.
- [ ] Recording fields and frame rate specifications documented, and verifiably readable directly by the M18 training script.
- [ ] Scene randomization list and instruction templates frozen, with episodes covering each randomization level.
- [ ] Quality inspection report archived: includes numerical statistics on time alignment error, frame drop rate, and image quality.
- [ ] Training/validation 9:1 split completed, with the validation set frozen.
- [ ] Dataset card documented: includes robot/sensor/calibration version/date/task definition/statistics and operator information.
- [ ] Data backed up: one copy each of the raw bag and parsed format, stored on different disks or in different locations.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Policy actions always lag behind the image | Undetected drift in image-action timestamps | Use quality inspection script to check alignment error; go back to M16 to check dual-machine time synchronization |
| Image freezes during playback at a certain segment | Frame drops during collection (USB bandwidth/disk write bottleneck) | Check frame drop report; reduce resolution or switch to SSD; go back to M16 to check USB topology |
| Policy learns jittery actions | Demonstration itself is fast and shaky | Spot-check playback of demonstration video; reduce operation speed and re-collect |
| Object cannot be grasped after changing position | Only collected from the center area/single pose | Refer to randomization list to supplement collection of edge cases and diverse poses |
| Success rate statistics fluctuate significantly | Inconsistent execution of success criteria | Write success criteria as a step-by-step checklist, and check off each item when labeling |
| Disk full or data loss | No backup, only one copy of the bag | Double backup on the collection day; include storage margin in pre-operation checks |
| Stylistic divergence in multi-operator data | Operator handling differences not recorded | Record operator ID in the dataset card; conduct unified demonstration and calibration before starting work |

## Supporting Reading

- Previous task: [M16 · Perception Stack Setup](m16-perception-stack.md)
- Next task: [M18 · Imitation Learning Training](m18-imitation-learning.md) ([Behavior Cloning](/entry/ent_method_behavior_cloning/) → [ACT](/entry/ent_method_action_chunking_transformer/) in practice)
- Theoretical background: [Chapter 17 Teleoperation and Human-Robot Collaboration](/wiki/chapters/chapter-17/), [Chapter 21 Data Infrastructure](/wiki/chapters/chapter-21/), [Chapter 16 Manipulation and Grasping](/wiki/chapters/chapter-16/)
- Dataset references: [Appendix B Key Dataset List](/wiki/appendices/appendix-b/), [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/), [DROID](/entry/ent_dataset_droid/)
- [Stage 3 Overview](../stage-3-humanoid.md) · [Sensor Selection Guide](../playbooks/sensor-selection.md)
