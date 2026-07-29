# M17 · Teleoperation and Data Collection: How Imitation Learning Data is Gathered

**Global Position**: After the arm (M15) and perception stack (M16) are ready, before imitation learning training (M18). Input is a safely movable robot + a calibrated perception stack, output is **≥50 quality-checked episode datasets**—the M18 training script can use them directly without rework.

**Prerequisites**: M16 acceptance passed (perception output stable, time synchronization verified); robot can be safely powered on and moved, emergency stop circuit available (see [Stage 3 Overview](../stage-3-humanoid.md) Step 15).

Theoretical background: [Chapter 17: Teleoperation and Human-Robot Collaboration](/wiki/chapters/chapter-17/) covers teleoperation system design, [Chapter 21: Data Infrastructure](/wiki/chapters/chapter-21/) covers data pipelines, [Appendix B: Key Dataset List](/wiki/appendices/appendix-b/) lists comparable public datasets.

## Step 1: Teleoperation Scheme Selection

[What to do] Compare four options, choose one based on budget and task:

| Scheme | Cost Level | Data Quality | Suitable For |
|---|---|---|---|
| Leader-follower master-slave arm ([ALOHA](/entry/ent_technology_aloha_teleoperation_system_2023/) approach) | ~$20k for full set (card-level) | High: isomorphic mapping, joint-level correspondence | Dual-arm fine manipulation |
| VR controller/headset | Consumer VR device price | Medium: end-effector pose + posture retargeting | Mobile humanoid, whole-body teleoperation |
| Exoskeleton | Confirm with supplier | High but cumbersome to wear | Research teams |
| Keyboard/joystick | Nearly zero | Low: slow, coarse actions | Fallback for pipeline validation |

Two important variants:

- **Collect without full robot**: [UMI gripper interface](/entry/ent_technology_umi_gripper_interface_2024/)—handheld gripper + wrist camera, human holds gripper to demonstrate and collect training data (card-level).
- **Practical division for mobile humanoid**: lower body joystick fixed-point + upper body master-slave, drawing on [Mobile ALOHA](/entry/ent_technology_mobile_aloha_2024/) whole-body teleoperation approach (Stage 3 level)—don't expect to walk via teleoperation while performing fine grasping.

Anchor points: [ToddlerBot](/entry/ent_robot_system_toddlerbot/) uses isomorphic teaching arm (handle with embedded FSR force-sensitive resistor) + handheld joystick buttons, version 2.0 adds Meta Quest 2 VR teleoperation; Berkeley Humanoid Lite uses SteamVR base stations + controller teleoperation for dual-arm tasks like Rubik's cube, writing, block stacking (see [ToddlerBot paper](https://arxiv.org/html/2502.00893v2) and [Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)).

[Why] Teleoperation serves three purposes: verify hardware reachability, collect imitation learning data, establish task baseline (Stage 3). VR approach has two hard constraints: **latency** (end-to-end latency reaching hundreds of milliseconds noticeably degrades operator feel, engineering experience, measure on your system) and **motion sickness**—first test latency with small-scale data, then schedule long collection sessions.

[How to analyze your situation] Very tight budget: start with UMI, align format, reuse with real robot later; have bipedal humanoid: upper body master-slave + lower body joystick fixed-point; just want to validate pipeline: use joystick as fallback to run through "record → replay → train" loop, then upgrade equipment.

## Step 2: Collection Pipeline Setup

[What to do] Freeze "what to record, how to record, where to store" into specifications:

1. **Recorded fields** (consistent with Stage 3 Step 9): multi-view images (head + dual wrist), joint states (position/velocity), actions (target joint positions after master-slave mapping), language instructions, timestamps.
2. **Unified frame rate**: all streams uniformly sampled at **10–30 Hz** (engineering recommendation, finalize based on storage and compute), align using M16 time synchronization infrastructure.
3. **Storage format**: start with [ROS 2](/entry/ent_software_ros_2_middleware_2024/) bag; to interface with open-source training ecosystem, use [LeRobot](/entry/ent_software_lerobot_2024/) or RLDS style—[Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) uses unified RLDS format to aggregate millions of demonstration frames across embodiments, serving as standard VLA pre-training corpus (card-level).
4. **Directory and naming**: `task_name/date/operator/episode_number`, metadata (calibration version, instruction text, success label) saved with the package.

[Why] Format determines reusability: missing a field (e.g., no language instruction) means re-collecting the entire batch for instruction-conditioned policy training. Naming convention makes "which data was collected with which calibration version" traceable—expired calibration batches must be filterable as a whole.

[How to analyze your situation] Single machine, single task: bag + one parsing script is enough; planning multiple tasks/robots: directly align with LeRobot/OXE format, don't invent a private format from the start.

## Step 3: Task and Scene Design

[What to do]

1. **Start with one task**: first task fixed as "grab cup and place in box", run through full pipeline before expanding categories.
2. **Scene randomization checklist**: object position/orientation (uniformly distributed within workspace), lighting (brightness/direction variation), background (change tablecloth/clutter), distractors (gradually add irrelevant objects). Roll dice before each recording to determine randomization level.
3. **Instruction templating**: template like "put {object} into {container}", freeze vocabulary, instruction strings stored in episodes are always generated from templates.
4. **Define success criteria upfront**: e.g., "gripper closes, object hovers for 3 seconds without falling, finally lands in container"—label each episode as success/failure on the spot.

[Why] The policy learns the data distribution: if you only collect "cup in the center", it will only grasp in the center. The randomization checklist defines the policy's generalization boundary and must be written into the collection plan, not based on daily mood. Vague success criteria cause label noise—during M18 training, this manifests as "some demonstrations can be learned, others cannot".

[How to analyze your situation] Fixed desktop robot: start randomization with object position/orientation (highest cost-effectiveness); add lighting and background after single-task success rate stabilizes. For each added randomization level, double the episode budget accordingly.

## Step 4: Collection Execution Standards

[What to do]

1. **Quality > quantity**: smooth motion, moderate speed (the pace the operator feels is "a bit slow" is just right), no occlusion; always keep both end-effector and target object visible in the frame.
2. **Failed episode handling**: **keep and label as failed** entire episodes that fail mid-demonstration, but M18 training defaults to using only successful set; operator-initiated "recovery from failure" segments (e.g., drop and re-grasp) are separately marked—recovery data teaches policy error correction, high value, but keep proportion within 20–30% (engineering recommendation) to avoid the policy learning "intentional failure".
3. **Production expectation**: skilled operator produces 10–20 episodes per hour (engineering recommendation, including scene reset and spot checks); plan 3–5 working hours for 50 high-quality data points.
4. **Immediate replay spot check**: replay 1 out of every 5–10 collected episodes, check visuals, time alignment, labels; record operator ID for each episode during multi-person collection—style differences are part of the data distribution.

[Why] Imitation learning is extremely sensitive to demonstration quality: shaky and fast demonstrations produce shaky and fast policies. Immediate spot check compresses incidents like "collected all day only to find timestamps drifted" to within 10 episodes.

[How to analyze your situation] Solo project: set your own pace, prefer 20 high-quality episodes per day; multi-person shifts: watch 3 "standard demonstrations" together before starting to calibrate feel, cross-check 2 of each other's episodes at end of shift.

## Step 5: Data Quality Check and Split

[What to do]

1. **Automated quality check script**, each episode passes three checks:
   - Time alignment: image and action timestamp offset < 1 frame (engineering recommendation);
   - Frame drop detection: actual vs target frame rate for each stream, flag if drop rate exceeds threshold;
   - Image quality: blur (Laplacian variance), overexposure/underexposure (histogram) filtered by threshold.
2. **Training/validation 9:1 split**: randomly split by episode, once validation set is defined, freeze it—M18 uses the same set for every experiment.
3. **Dataset card**: robot model/sensor configuration/calibration version/collection date/task definition/instruction template/number of episodes and statistics, all in one page. [DROID](/entry/ent_dataset_droid/) is a reference for distributed multi-lab collection (card-level, limitation: only covers fixed arms); [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) is a format reference for cross-embodiment aggregation.

[Why] "Whether data is usable" relies on scripts, not memory: after archiving the quality report (alignment error, frame drop rate, blur ratio), when M18 training has issues, data can be ruled out first. The dataset card is your only source of truth one month later, or when someone else takes over.

[How to analyze your situation] Even 50 episodes go through the full process: write the script once, zero cost to reuse at 500 episodes; even 5 validation episodes must be kept—without a frozen validation set, every "improvement" in M18 cannot be attributed.

## Acceptance Criteria

- [ ] ≥50 quality-checked episodes (Stage 3 criterion), with complete success/failure labels.
- [ ] Recording fields and frame rate specifications documented, and verified to be directly readable by the M18 training script.
- [ ] Scene randomization checklist and instruction templates frozen, with episodes covering all randomization levels.
- [ ] Quality inspection report archived: includes numerical statistics on time alignment error, frame drop rate, and image quality.
- [ ] Training/validation 9:1 split completed, with the validation set frozen.
- [ ] Dataset card documented: includes robot/sensor/calibration version/date/task definition/statistics and operator information.
- [ ] Data backed up: one copy each of raw bag files and parsed format, stored on different disks or in different locations.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Policy actions always lag behind the image | Undetected drift in image-action timestamps | Check alignment error with quality inspection script; return to M16 to check dual-machine time synchronization |
| Image stuttering during playback of a certain segment | Frame drops during collection (USB bandwidth/disk write bottleneck) | Check frame drop report; reduce resolution or switch to SSD; return to M16 to check USB topology |
| Policy learns jittery actions | Demonstration itself is fast and jittery | Spot-check playback of demonstration video; reduce operation speed and re-collect |
| Cannot grasp object when moved to a different position | Only collected center area/single pose | Compare with randomization checklist and supplement collection of edge cases and diverse poses |
| Success rate statistics fluctuate erratically | Inconsistent execution of success criteria | Write success criteria as a step-by-step checklist and check off each item when labeling |
| Disk full or data loss | No backup, only one copy of bag files | Double backup on the day of collection; include storage margin in pre-operation checks |
| Fragmented data style from multiple operators | Operator handling differences not recorded | Record operator ID in dataset card; conduct unified demonstration and calibration before starting |

## Supporting Reading

- Previous task: [M16 · Perception Stack Setup](m16-perception-stack.md)
- Next task: [M18 · Imitation Learning Training](m18-imitation-learning.md) ([Behavior Cloning](/entry/ent_method_behavior_cloning/) → [ACT](/entry/ent_method_action_chunking_transformer/) in practice)
- Theoretical background: [Chapter 17 Teleoperation and Human-Robot Collaboration](/wiki/chapters/chapter-17/), [Chapter 21 Data Infrastructure](/wiki/chapters/chapter-21/), [Chapter 16 Manipulation and Grasping](/wiki/chapters/chapter-16/)
- Dataset references: [Appendix B Key Dataset List](/wiki/appendices/appendix-b/), [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/), [DROID](/entry/ent_dataset_droid/)
- [Stage 3 Overview](../stage-3-humanoid.md) · [Sensor Selection Guide](../playbooks/sensor-selection.md)
