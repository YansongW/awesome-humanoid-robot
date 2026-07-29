# Stage 0 Foundation Building: Getting Your Ticket to Humanoid Robotics

## Positioning of This Stage

The goal of Stage 0 is not to "learn all the basics" – that's a bottomless pit where countless people get stuck. The goal is to obtain four tickets:

1.  **Mathematics**: Be familiar with matrices, probability, dynamics equations, and QP when you see them in control papers;
2.  **Programming and Toolchain**: Be able to work with Python/C++/git/ROS 2, and understand what 3D printing is about;
3.  **Circuit Concepts**: Know where electricity comes from and how signals travel, so you don't burn boards when you later work with real hardware;
4.  **Simulation**: Read a URDF file and make a bipedal model stand up in MuJoCo.

-   **Time Budget**: 6–10 weeks part-time (8–10 hours per week), 3–4 weeks full-time.
-   **Budget**: Approximately ¥0 – all software in this stage is open-source; optional 3D printing prototyping costs should be confirmed directly with suppliers.
-   **Core Discipline**: Each topic provides a criterion for "how much is enough to learn." **Stop once you meet the criteria, and do not go back to grind problems.** Real gaps will be exposed in later stages; come back to fill them with specific problems then – it's ten times more efficient.

## Step 1: The Math Quartet

Don't learn it the way a math major would (definition-theorem-proof). Learn it as a "control engineer's minimum ammunition dump." The criteria for all four subjects are **demonstrable**, not "I feel like I understand."

### 1.1 Linear Algebra

【What to do】Vector and matrix operations, eigenvalues/eigenvectors, rotation matrices and homogeneous transformations, least squares and pseudoinverse. Hands-on practice: Write a 4×4 homogeneous transformation in NumPy to transform foot coordinates from the ankle joint frame to the torso frame; then write the forward kinematics of a two-link planar arm.

【Why】Linear algebra is the language of all spatial relationships in humanoid robotics: forward kinematics is a product of homogeneous transformations, the Jacobian maps joint velocities to end-effector velocities, and every QP in whole-body control is a matrix operation. Card: [Linear Algebra](/entry/ent_foundation_linear_algebra/) (the branch of mathematics studying vector spaces, linear transformations, matrices, and linear systems of equations). The kinematic derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) are all built on this.

【How to approach based on your background】CS background: You already know the computation. Focus on **geometric intuition** – a rotation matrix isn't nine numbers; it's the three axes of a coordinate system. Physics/Math background: Do the exercises above directly as your validation. Zero background: Start with 3Blue1Brown's "Essence of Linear Algebra" to build intuition, then start calculating.

**How much is enough** (stop when all three are met): ① Can manually derive a 2D rotation matrix and explain the geometric meaning of each column; ② The forward kinematics code for a two-link planar arm runs and its output matches manual calculation; ③ When you see the pseudoinverse J⁺, you know it solves a least-squares problem.

### 1.2 Probability Theory

【What to do】Random variables, expectation and covariance, Gaussian distribution, Bayes' theorem, conditioning and marginalization. Hands-on practice: Simulate "joint encoder readings" with Gaussian noise using NumPy, plot a histogram, calculate mean/variance; then manually solve a "sensor alarm → true fault probability" problem using Bayes' theorem.

【Why】Real sensors always have noise. State estimation (the Kalman filter family) is essentially recursive Bayesian inference. Imitation learning and VLA models used later also output probability distributions of actions, not deterministic values. Card: [Probability Theory](/entry/ent_foundation_probability_theory/) – the foundation of all probabilistic models in robotics and machine learning.

【How to approach based on your background】AI background: Self-check with the criteria; you'll likely pass directly. Hardware background: This is often your weakest subject among the four, and it directly determines whether you can understand state estimation later – it's worth investing half your math budget here. Zero background: Study this after linear algebra.

**How much is enough**: ① Explain in one sentence what the diagonal and off-diagonal elements of a covariance matrix represent; ② Can manually solve a Bayes' theorem problem with correct numerical results; ③ Don't panic when you see the five Kalman filter equations – you don't need to derive them, but you should be able to state the role of each equation (predict, gain, update).

### 1.3 Classical Mechanics

【What to do】Newton-Euler equations, Lagrangian method, kinetic/potential energy, inertia tensor, angular momentum. Hands-on practice: Derive the dynamics equations for a simple pendulum and a double pendulum using the Lagrangian method, numerically integrate for 5 seconds, and plot the angle curves.

【Why】A humanoid robot is a floating-base multi-rigid-body system. The equation M(q)q̈ + C(q,q̇) + g(q) = τ will run through every control paper you read later. Bipedal balance (ZMP, capture point) is a direct consequence of classical mechanics. Card: [Classical Mechanics](/entry/ent_foundation_classical_mechanics/) (including Newton's laws, conservation principles, and rigid body dynamics). The derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) and [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) start from here.

【How to approach based on your background】Mechanical/Vehicle background: You likely have this covered. Do the double pendulum exercise for validation and move on. Pure software background: This is your **most important** catch-up in this stage – without mechanical intuition, when a robot falls in simulation, you won't know if it's the controller's fault or the model's fault.

**How much is enough**: ① Can derive the double pendulum equations (it's okay to follow a book, but you should be able to explain what each step does with the book closed); ② Can qualitatively explain "why a humanoid robot with a larger torso inertia is actually easier to stabilize"; ③ Understand the meaning of each field in the `<inertial>` tag of a URDF – this directly paves the way for Step 4.

### 1.4 Convex Optimization

【What to do】Identifying convex sets/functions, standard QP (Quadratic Programming) form, geometric meaning of equality/inequality constraints, calling an existing solver to solve a QP. Hands-on practice: Solve min ‖x‖² s.t. Ax=b, x≥0 in Python (solver options include OSQP, quadprog, etc.; choose based on your environment).

【Why】The real-time layer of humanoid control almost always solves a QP: Whole-Body Control (WBC) formulates "task tracking + contact force constraints + torque limits" as an inverse dynamics QP, solved every millisecond; MPC solves a QP in a receding horizon manner. Convexity guarantees that any local optimum is global – this is the fundamental reason engineers trust QP in kHz-level control loops. Card: [Convex Optimization](/entry/ent_foundation_convex_optimization/). For deeper dives, see Wiki [Chapter 14](/wiki/chapters/chapter-14/).

【How to approach based on your background】This is the subject in the quartet with the **fastest diminishing marginal returns**: if you aren't writing controllers yourself, "can identify convexity + can tune a solver + can read a QP formulation" is enough. Leave KKT derivations for later, to be learned on demand. Operations research background: self-check and pass.

**How much is enough**: ① Given a problem, can determine if it's convex (quadratic positive definite objective + linear constraints → yes); ② The solution to the practice problem satisfies all constraints upon verification; ③ Can explain to someone else "why WBC dares to use QP in a real-time loop."

## Step 2: Programming and Toolchain

【What to do】① Python proficiency: NumPy vectorization, matplotlib plotting, writing classes; ② C++ to "read and modify" level: pointers/references, header files, compilation/linking; ③ Daily git operations: clone, branch, commit, push, submit PR; ④ Install ROS 2 LTS, run the talker/listener example, and write your own pair of publisher/subscriber nodes; ⑤ Understand the basic FDM 3D printing workflow (modeling → slicing → printing) and strength fundamentals.

【Why】The de facto standard for the humanoid software stack is [ROS 2 middleware](/entry/ent_software_ros_2_middleware_2024/) – a DDS-based publish/subscribe mechanism with real-time support (source: ros.org, see card). In later stages, your simulation, drivers, and state estimation will be organized around nodes/topics. The industry standard division of labor is C++ for the low-level real-time loop and Python for algorithm prototyping. 3D printing is the primary manufacturing method for the full-robot stage: the structural parts and cycloidal reducers of the open-source humanoid Berkeley Humanoid Lite are printed parts, with a total BOM cost of approximately $4,312 in the US and $3,236 in China (source: [EECS-2025-207 Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)). The slicing and tolerance knowledge you learn now will directly translate into money and time savings. For a full picture of the software ecosystem, see Wiki [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

【How to approach based on your background】Pure software background: Self-check on Python/git and skip if passed. Invest time in C++ memory and real-time concepts, and the ROS 2 node/topic/service triad. Hardware background: Learning Python starting from NumPy is most efficient, as it's closest to MATLAB thinking. Zero background: Learn Python first, then git. Defer C++ until you need it – if you learn it without using it, you'll forget it.

**How much is enough**: ① ROS 2: Can independently write two nodes (one publisher, one subscriber) and verify data flow using `ros2 topic echo`; ② git: Independently complete the full fork → branch → commit → PR workflow once (practice on your own exercise repository); ③ 3D printing: Can explain how FDM layer orientation affects part strength, and why clearance is necessary for mating holes (the specific tolerance magnitude for a given machine should be confirmed directly with the supplier).

## Step 3: Circuits and Embedded Basics

**[What to Do]** In this phase, you won't build any boards, only establish three sets of concepts: **Power Supply** (voltage rails, current budget, wire gauge and voltage drop, fuses and switches), **Ground** (common ground, ground loops), and **Signals** (digital levels, differential transmission, anti-interference). Then focus on understanding the role of the [CAN Bus](/entry/ent_technology_can_bus_2024/): it is the fieldbus connecting the joint motor drivers of a humanoid robot to the central controller (Source: Card, Wikipedia CAN bus 2024). Optional hands-on: Buy an entry-level CAN adapter (price to be confirmed with the supplier), use can-utils to capture a segment of real bus data and observe the frame structure.

**[Why]** At the full-robot stage, you will face a dozen to over twenty joint drivers hanging on the bus: the Berkeley Humanoid Lite uses CAN to connect all actuators, with the main controller being an Intel N95 mini PC (approx. $129, placed in the torso, running both low-level control and RL policies; Source: [EECS-2025-207 Technical Report BOM](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)). During full-robot debugging, more than half of the "mysterious issues" originate from the electrical layer: voltage drop, common ground, termination resistors, and wiring harnesses. Establish these concepts now to avoid burning boards later. Details on power system engineering can be found in Wiki [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/).

**[How to Analyze Your Background]** EE/Automation background: Spend 30 minutes reviewing the concepts; Software or no background: You are not required to design circuits, but you must be "brave enough to measure, and know how to measure" – use a multimeter to measure voltage and continuity, and understand what a short circuit on a 24 V bus means. Safety tip: Lithium batteries and bus capacitors are not toys. Verify safety specifications yourself before any live operation. If unsure, have someone with hardware experience present.

**What Counts as Sufficient Learning:** ① Can sketch a power supply topology diagram by hand: "Battery → Fuse/E-Stop → Bus → Each Driver"; ② Can explain why 120 Ω termination resistors are needed at both ends of a CAN bus; ③ Can explain why differential signals are more immune to interference than single-ended signals.

## Step 4: First Simulation Experience – Read URDF, Make a Biped Stand Up

**[What to Do]** ① Install the [MuJoCo Physics Engine](/entry/ent_software_mujoco_physics_engine_2022/); ② Find an open-source humanoid/biped [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) file and read through it – URDF is an XML format describing robot links, joints, inertia, and geometry (Source: wiki.ros.org/urdf, see card); ③ Load the model into MuJoCo (or use the project's built-in MJCF); ④ Write a simple position PD controller: given target joint angles for a standing posture, make the biped model stand still in place for 10 seconds.

**[Why]** MuJoCo is a high-fidelity physics engine with rich contact dynamics, widely used in humanoid control research (Source: mujoco.org, see card) – the core difficulty of bipedal standing is precisely foot contact and balance, which plays to its strengths. Reading URDF is the first key to unlocking any open-source humanoid repository: real open-source projects maintain three description formats (URDF/MJCF/USD) simultaneously (Berkeley Humanoid Lite, Source: [Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)). Understanding this format means you can read the "skeleton blueprint" of someone else's robot. A systematic discussion of the simulation technology stack is in Wiki [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**[How to Analyze Your Background]** No GPU is fine – rigid body simulation for standing is sufficient on CPU. Prioritize open-source bipeds that are "small size, well-documented" ([Public Survey Archive](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/) lists candidates like Berkeley Humanoid Lite, ToddlerBot, with cost and difficulty analysis). Don't tackle full-size models right away. **If you can only complete one thing in this phase, make it this one** – it simultaneously validates mechanics, programming, and toolchain.

**What Counts as Sufficient Learning:** This corresponds to acceptance criteria items 1 and 2 below – this step is the capstone project for Stage 0.

## Acceptance Criteria

Self-check each item. Only proceed to Stage 1 if all are passed:

1.  **URDF Reading Comprehension**: Given an unfamiliar biped URDF, can verbally answer without documentation – how many controllable joints, what is the root link, what are the `origin`/`axis` of the ankle joint, the meaning of `ixx/iyy/izz` in `<inertial>`; and use `check_urdf` or equivalent tool to confirm no parsing errors.
2.  **MuJoCo Standing**: Load a biped model, use your own position PD control to achieve standing without external force for ≥ 10 seconds without falling; after applying a small impulse to the torso, the model can recover standing – or you can correctly explain why it cannot recover (gain, contact, or model issue). This tests mechanical intuition, not tuning luck.
3.  **Math Spot Check**: Randomly select one item from each of the four "sufficiency criteria" and demonstrate it on the spot (hand calculation or code execution).
4.  **Toolchain**: ROS 2 talker/listener has been successfully run (terminal screenshot or screen recording); all practice code for this phase is in your git repository with clear, readable commit history.
5.  **Circuit Concepts**: Can explain to a peer (or to the air) the three topics: power supply topology, CAN termination resistor, and differential signal; failure to explain clearly is considered not meeting the standard.

Two warning signals for "not sufficient": Unable to write a PD controller without following a tutorial (Step 4 is done by following along); Changing the `origin` in URDF and not understanding why the model floats (1.1 Geometric intuition not established). If either occurs, go back to the corresponding section and re-verify.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
| :--- | :--- | :--- |
| Model falls apart/flies around upon loading in MuJoCo | Initial pose interpenetration (joints embedded in each other); A link missing `<inertial>` causing zero mass/inertia | First check simulator compilation warnings; Give the model a reasonable initial keyframe; Check inertial parameters link by link |
| Joint high-frequency oscillation during PD standing | Gain too high, integration step too large, numerical stiffness | First halve P gain then slowly increase; Reduce simulation timestep to reproduce and compare; Check if desired damping was written as spring stiffness |
| Feet slip like on ice | Contact friction parameters use default values, lower than real sole-ground combination | Check friction parameters for geom/contact pairs; Look up friction coefficient magnitude based on sole material (rubber/printed PLA) and adjust, specific values need to be confirmed based on material |
| Joint motion direction reversed after URDF to MJCF conversion | URDF `axis` definition inconsistent with target simulator convention; Mixed angle units (degrees vs radians) | Drive each joint individually in the viewer to check direction; Full-text search for angle fields to confirm units |
| Two ROS 2 nodes cannot receive messages from each other | `ROS_DOMAIN_ID` mismatch; Firewall blocking DDS traffic; Topic name/QoS mismatch | First test on the same machine before cross-machine; `ros2 topic list` to confirm both see the same topic; Check environment variables (refer to official documentation for your distribution) |
| Reluctant to enter Stage 1, repeatedly re-learning math | Perfectionism trap: using "building foundation" as an excuse to procrastinate | Check off each acceptance criterion one by one. Once met, move on. Let Stage 1 expose the real gaps. |

Stage 0 is now complete. Next stop: [Stage 1: Build a Joint (Actuator)](stage-1-actuator.md): Apply the circuit concepts from Step 3 and PD control to real hardware for the first time; the foundation in URDF and MuJoCo will be realized in the simulated walking of [Stage 2: Biped Platform](stage-2-biped.md).

## Companion Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) – The first simulation experience in Stage 0 will use the engine installation and model preparation from this guide.
- [Roadmap Overview](index.md)
