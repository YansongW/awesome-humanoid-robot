# M15 · Upper Limbs and End Effectors: Giving Hands to a Walking Robot

**Global Position**: After the six-checkpoint acceptance of Stage 2's walking platform (M14), this is the first task of Stage 3. The input is a walking biped + the actuator selection method from Stage 1, and the output is an upper body with **both arms + end effectors assembled and tuned, with IK solvable**. Downstream M16's perception stack will mount cameras on the head/wrist, and M17's teleoperation will drive the arms and end effectors—this task is their common carrier.

**Prerequisites**: [M14 · sim-to-real deployment and walking acceptance](m14-sim-to-real.md) passed; familiarity with M01's joint index algorithm; familiarity with M10's URDF workflow (arms must be integrated into the full robot model); the four questions for actuator selection are in the [Actuator Selection Handbook](../playbooks/actuator-selection.md).

**Theoretical Background**: Cards for [7-DOF Robotic Arm](/entry/ent_component_7dof_arm_2024/), [Forward Kinematics](/entry/ent_method_forward_kinematics/), [Inverse Kinematics](/entry/ent_method_inverse_kinematics/), [Dexterous Hand](/entry/ent_component_dexterous_hand_2024/); [Chapter 16: Manipulation and Grasping](/wiki/chapters/chapter-16/), [Chapter 8: Humanoid Robot Design Principles](/wiki/chapters/chapter-08/), [Chapter 9: Key Subsystem Design](/wiki/chapters/chapter-09/), and [Chapter 4: Actuators](/wiki/chapters/chapter-04/).

## Step 1: Arm Configuration and DOF Allocation

【What to Do】First determine the DOF per arm, then calculate joint indices. Three tiers for selection:

| Configuration | Capability | Cost | Precedent |
|---|---|---|---|
| 7 DOF (Shoulder 3, Elbow 1, Wrist 3) | Redundant DOF: elbow can still rotate when end-effector is stationary, obstacle avoidance, singularity avoidance | Highest cost, wiring, and control complexity | ToddlerBot uses 7 DOF per arm with Dynamixel bus servos (toddlerbot.md) |
| 6 DOF | Can reach any pose, no redundancy | One less axis, singularity avoidance relies on path planning | Standard industrial arm configuration |
| 5 DOF | Sacrifices one wrist orientation axis | Most economical, sufficient for desktop fixed-point grasping | Berkeley Humanoid Lite uses 5 DOF per arm (berkeley-humanoid-lite.md) |

It is recommended to start with a lightweight 5–6 DOF for the first robot. Reuse the M01 lever algorithm for joint indices. Example calculation (shoulder flexion/extension joint): arm + hand total 1.2 kg, end-effector grasps 0.5 kg, center of mass equivalent arm length 0.25 m, dynamic safety factor 2:

```
τ ≥ (1.2 + 0.5) × 9.81 × 0.25 × 2 ≈ 8.3 N·m
```

Two routes for actuators: reuse Stage 1's self-developed modules, or use servo buses (especially suitable for low-torque joints like the wrist, e.g., the [Dynamixel XM430](/entry/ent_component_dynamixel_xm430_w210_t/) series; torque/price confirmed with supplier per model).

【Why】DOF is a three-way trade-off between "capability, cost, and complexity": each additional joint adds one more BOM item, one more wire, and one more failure point. The KPI for the first robot is "end-to-end grasping of a cup," not replicating a human arm's anatomy—two benchmark robots completed manipulation demonstrations with 5–7 DOF; choose the configuration based on the task, not on preconceptions. The value of redundancy is detailed in the [7-DOF Robotic Arm](/entry/ent_component_7dof_arm_2024/) card.

【How to Analyze Your Situation】Only doing desktop fixed-point grasping: start with 5–6 DOF; clearly requiring two-hand coordination and obstacle avoidance manipulation: use 7 DOF. For joints with peak torque < 4 N·m, use servos for simplicity; if force control/backdrivability is needed (for future compliant manipulation), use QDD, accepting the cost and tuning effort (comparison in [Actuator Selection Handbook](../playbooks/actuator-selection.md)).

## Step 2: Structural Integration and Whole-Robot Balance

【What to Do】

1.  **Inertia Backfill**: The arm's mass/center of mass/inertia must be included in the URDF (return to M10 workflow). After merging the full robot model, recalculate the total center of mass—if the arm is not modeled, the walking strategy will see incorrect dynamics.
2.  **Shoulder Mount Stiffness and Cable Routing**: The shoulder root is the cantilever pivot for the entire arm; bracket deformation directly consumes end-effector precision. Reserve slack for cables as joints rotate (twist loops or slip rings), especially for multi-turn wrist rotations.
3.  **Walking Arm Posture**: During walking, fold both arms (elbows flexed, arms close to the body) to reduce inertia. Write this folded posture into the default joint angles of the walking strategy.
4.  **Center of Mass Compensation Concept**: Before manipulation, ask "Is the projection of the whole-robot center of mass still within the support polygon after reaching out?" If not, adjust the stance or reach out in stages.

【Why】The robot with arms installed is no longer the one accepted in M14: the center of mass has shifted upward, inertia has increased, and the dynamic margin for walking has decreased. Modeling first allows the problem of "can't walk after adding arms" to be exposed in the simulation phase, rather than by crashing the physical robot. Systematic discussion is in [Chapter 9: Key Subsystem Design](/wiki/chapters/chapter-09/) and [Chapter 8: Humanoid Robot Design Principles](/wiki/chapters/chapter-08/).

【How to Analyze Your Situation】For replicated platforms (ToddlerBot/Berkeley), the official model already includes the arms; this step only requires physical weighing for verification. For self-developed platforms, follow M10's three-step inertia process (CAD reading / geometric approximation via weighing / pendulum method). After adding arms, first re-run standing and walking in simulation, fine-tune the strategy via M13's process if necessary, then verify on a gantry—the order cannot be reversed.

## Step 3: End Effectors—Start with Gripper, Reserve Interface, Then Upgrade

【What to Do】

1.  **First Version: Electric Parallel Gripper** (servo/motor direct drive). For tasks like grasping a cup, the success rate of a gripper is far higher than a poorly tuned dexterous hand (experience from [Stage 3 Overview](../stage-3-humanoid.md) Section 3.2).
2.  **Quick-Change Interface**: Make the wrist a mechanical locating flange + unified power/communication connector, allowing end-effector changes without modifying the arm—ToddlerBot's parallel gripper and compliant palm can be swapped in 2 minutes (toddlerbot.md).
3.  **Upgrade Path** (choose based on task, background in [Dexterous Hand](/entry/ent_component_dexterous_hand_2024/) card):

| Solution | DOF/Drive | Features | Suitable For |
|---|---|---|---|
| Parallel Gripper | 1 DOF | Cheap and reliable, limited grasp types | First version end-to-end validation |
| [LEAP Dexterous Hand](/entry/ent_component_leap_hand/) | 16 DOF, Dynamixel direct drive + 3D printing | Open-source low-cost anthropomorphic hand, BOM needs confirmation with project | Starting manipulation learning research |
| [Allegro Dexterous Hand](/entry/ent_component_allegro_hand/) | 16 DOF four-finger, torque-controlled joints, ROS compatible | Commercially reliable, price needs confirmation with supplier | Scenarios requiring reliability |

4.  **Grasp Taxonomy**: First distinguish whether the task requires a power grasp (squeezing, relying on contact area) or a precision pinch (picking up, relying on fingertip opposition)—cups/tools are power grasps, coins/thin objects are precision pinches. The type determines the end-effector morphology and DOF requirements.

【Why】The 16 DOF of a dexterous hand simultaneously represent 16 times the control and data requirements. Using it in the first version is like fighting two battles at once. The value of a quick-change interface only becomes apparent in the second version—reserving it is the cheapest foresight in the first version.

【How to Analyze Your Situation】First robot: gripper + quick-change flange, no hesitation. For imitation learning research: start with LEAP (open-source, modifiable); if budget is sufficient and stability is required: use Allegro. Tendon-driven vs. linkage: tendon-driven fingers have low inertia but are high maintenance; linkages have high stiffness and are easy to model. For the first hand, direct drive or linkage is recommended.

## Step 4: Kinematics Solution—FK Build Chain, IK Solve, Verify Success Rate

【What to Do】

1.  **FK**: Build the homogeneous transformation chain from base to end-effector according to the URDF ([Forward Kinematics](/entry/ent_method_forward_kinematics/)). Compare joint by joint with the physical robot—manually set angles, compare FK output end-effector pose with calipers/calibration plate measurements.
2.  **IK**: Start with a numerical method, Jacobian pseudoinverse iterative solution; switch to Damped Least Squares (DLS) near singularities. For arms with simple geometry, an analytical solution can be derived ([Inverse Kinematics](/entry/ent_method_inverse_kinematics/)).
3.  **7 DOF Redundancy Utilization**: Add secondary objectives in the null space (elbow lift for obstacle avoidance, staying away from joint limits):

```
q̇ = J⁺·ẋ + (I − J⁺J)·∇H(q)        # H: potential function for elbow lift/limit avoidance
```

4.  **Tools**: Prioritize mature IK solvers in the ROS ecosystem; for teaching purposes, a Jacobian can be handwritten in Python + numpy.
5.  **Verification**: Randomly sample 100 target poses within the workspace and calculate the solution success rate—Stage 3 acceptance line is ≥95% ([Stage 3 Overview](../stage-3-humanoid.md)).

【Why】The essence of manipulation is coordinate transformation and inversion: after vision (M16) provides the cup's position, IK translates it into 5–7 joint angles. Singular configurations are the Achilles' heel of numerical methods—when the arm is fully extended, the Jacobian is rank-deficient, the pseudoinverse outputs exploding joint velocities, and DLS trades a bit of accuracy for numerical stability. The null space is the "free lunch" of 7 DOF: the end-effector is stationary, but the arm's posture can still be optimized.

【How to Analyze Your Situation】Verification order: simulation spot-check → unloaded trajectory → loaded trajectory, do not reverse. If the success rate is < 95%, first check if the target points are outside the workspace; the target end-effector positioning error on the physical robot should be ≤ 2 cm (Stage 3 criterion, recommended threshold). If exceeded, first check shoulder mount stiffness and zero-point calibration, then suspect the algorithm.

## Step 5: Whole-Body TF and Manipulation Primitives—Integrating the Arm into the Robot's Coordinate World

【What to Do】

1. **Integrate the arm into the full-robot URDF/TF tree**: Use base_link as the unified root node, with a clear transform chain covering legs, torso, arm, end-effector, and camera (the M16 camera extrinsic parameters are also attached to this tree).
2. **Camera layout selection**: Eye-to-hand (head/chest camera, wide field of view but more occlusion and longer calibration chain) vs. eye-in-hand (wrist camera, precise close-range but narrow field of view)—a head camera is sufficient for the first version; reserve mounting positions and cable routing at the wrist.
3. **Grasp primitive state machine**: Pre-grasp pose → Approach (slow linear motion) → Close → Load confirmation (current/position feedback) → Retract, each stage with timeout and failure rollback.
4. **Walking-manipulation mutual exclusion**: Stand still before manipulation (experience from [Stage 3 Overview](../stage-3-humanoid.md))—lock the lower body in standing control when reaching out; retract the arm before walking; implement mutual exclusion in software interlocking.

【Why】Humanoids lack a fixed base; end-effector accuracy = arm accuracy + torso posture error + foot slip accumulation (Section 3.1 of [Stage 3 Overview](../stage-3-humanoid.md))—walking while grasping is a research topic, but standing still to grasp is engineering wisdom. The state machine breaks "grasping" into observable, revertible segments, allowing failure localization to a specific segment rather than facing a "can't grasp" black box.

【How to Analyze Your Situation】First draw the TF tree on paper: clearly note each frame's parent node and transform source (URDF static / calibration extrinsic). Write the primitive state machine manually using a Python state loop—no need for a behavior tree framework. Enforce walking-manipulation mutual exclusion via software, not operator discipline.

## Acceptance Criteria

- [ ] Arm configuration and DOF allocation documented; peak torque for each joint includes formula, numerical value, and safety factor (≥2) with justification.
- [ ] Arm mass/center of mass/inertia backfilled into URDF; full-robot model center of mass recalculated and verified; simulation standing/walking retested for stability.
- [ ] End-effector quick-change interface (mechanical alignment + electrical connector) assembled and tuned; gripper opening/closing controlled.
- [ ] FK verified joint-by-joint against the physical robot; IK success rate ≥95% for 100 random targets.
- [ ] Physical robot end-effector positioning error ≤2 cm (no load, recommended threshold); trajectory replay recorded for both no-load and loaded conditions.
- [ ] Full process of standing and reaching for manipulation does not cause the robot to tip over (or center-of-mass compensation is implemented and validated).
- [ ] Grasp primitive state machine includes all five stages (with timeout and failure rollback); successful physical robot grasp demonstration.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Joint jumps/velocity explosion near singularities | Target near singular configuration, pseudo-inverse divergence | Switch to damped least squares; filter target points for reachability; use null-space for singularity avoidance with 7 DoF |
| Walking performance degrades after adding arm | Arm inertia not included in the model | Return to Step 2 to backfill URDF; re-simulate and fine-tune walking strategy |
| Repeated wrist cable breakage | Insufficient torsion margin, fatigue fracture | Add torsion loops in cable routing; evaluate slip rings for multi-turn rotation scenarios |
| Gripper collides with wrist when closing | End-effector and wrist joint collision geometry not modeled | Return to URDF to add collision geometry; add self-collision check in IK |
| IK reports solution failure | Target outside workspace | Visualize target point; perform workspace analysis before assigning targets |
| Robot shakes or tips over when reaching out | No center-of-mass compensation / excessive speed | Reduce speed and retest; operate while standing; check center-of-mass projection before reaching |

## Companion Reading

- Previous task: [M14 · Sim-to-Real Deployment and Walking Acceptance](m14-sim-to-real.md)
- Next task: [M16 · Perception Stack Setup](m16-perception-stack.md)
- Theoretical background: [Chapter 16: Manipulation and Grasping](/wiki/chapters/chapter-16/), [Chapter 4: Actuators](/wiki/chapters/chapter-04/), [Chapter 8: Humanoid Robot Design Principles](/wiki/chapters/chapter-08/), [Chapter 9: Key Subsystem Design](/wiki/chapters/chapter-09/)
- [Actuator Selection Handbook](../playbooks/actuator-selection.md) · [Stage 3 Overview](../stage-3-humanoid.md)
