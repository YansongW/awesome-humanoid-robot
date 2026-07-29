# Stage 0 Foundation Building: Getting Your Ticket to Humanoid Robotics

## Stage Positioning

The goal of Stage 0 is not to "learn all the basics" – that's a bottomless pit where countless people get stuck. The goal is to obtain four tickets:

1. **Mathematics**: Be familiar with matrices, probability, dynamics equations, and QP when you see them in control papers;
2. **Programming and Toolchain**: Be able to work with Python/C++/git/ROS 2, and understand what 3D printing is about;
3. **Circuit Concepts**: Know where electricity comes from and how signals travel, so you don't burn boards when you later work with real hardware;
4. **Simulation**: Read a URDF file and make a biped model stand up in MuJoCo.

- **Time Budget**: 6–10 weeks part-time (8–10 hours per week), 3–4 weeks full-time.
- **Budget**: Approximately ¥0 – all software in this stage is open source; optional 3D printing prototyping costs should be confirmed with your supplier.
- **Core Discipline**: Each topic provides a criterion for "how much is enough to learn." **Stop once you meet the criteria, and don't go back to do more exercises.** Real gaps will be exposed in later stages, and you can come back to fill them with specific problems – ten times more efficient.

## Step 1: The Four Pillars of Mathematics

Don't learn them like a math major (definition-theorem-proof). Learn them as a "control engineer's minimum ammunition depot." The criteria for all four are **demonstrable**, not "I feel I understand."

### 1.1 Linear Algebra

**[What to do]** Vector and matrix operations, eigenvalues/eigenvectors, rotation matrices and homogeneous transformations, least squares and pseudoinverse. Hands-on exercise: Write a 4×4 homogeneous transformation in NumPy to transform foot coordinates from the ankle joint frame to the torso frame; then write the forward kinematics of a two-link planar arm.

**[Why]** Linear algebra is the language of all spatial relationships in humanoid robotics: forward kinematics is a product of homogeneous transformations, the Jacobian maps joint velocities to end-effector velocities, and every QP in whole-body control is a matrix operation. Card: [Linear Algebra](/entry/ent_foundation_linear_algebra/) (the branch of mathematics studying vector spaces, linear transformations, matrices, and linear systems of equations). The kinematics derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) are all built on this.

**[How to approach based on your background]** CS background: You already know the computation, focus on **geometric intuition** – a rotation matrix is not nine numbers, it's three axes of a coordinate system; Physics/Math background: Do the exercises above directly as a verification; Zero background: Start with 3Blue1Brown's "Essence of Linear Algebra" to build intuition, then do the calculations.

**How much is enough** (stop when all three are met): ① Can manually derive a 2D rotation matrix and explain the geometric meaning of each column; ② The forward kinematics code for a two-link planar arm runs and matches manual calculations; ③ Seeing the pseudoinverse J⁺, you know it solves a least-squares problem.

### 1.2 Probability Theory

**[What to do]** Random variables, expectation and covariance, Gaussian distribution, Bayes' theorem, conditioning and marginalization. Hands-on exercise: Simulate "joint encoder readings" with Gaussian noise using NumPy, plot a histogram, calculate mean/variance; then manually solve a "sensor alarm → true fault probability" problem using Bayes' theorem.

**[Why]** Real sensors always have noise; state estimation (the Kalman filter family) is essentially recursive Bayesian inference; imitation learning and VLA models used later also output probability distributions of actions, not deterministic values. Card: [Probability Theory](/entry/ent_foundation_probability_theory/) – the foundation of all probabilistic models in robotics and machine learning.

**[How to approach based on your background]** AI background: Self-check with the criteria, you'll likely pass directly; Hardware background: This is often your weakest of the four, and it directly determines whether you can understand state estimation later – worth investing half your math budget here; Zero background: Learn this after linear algebra.

**How much is enough**: ① Explain in one sentence what the diagonal and off-diagonal elements of a covariance matrix represent; ② Can manually solve a Bayes' theorem problem with correct numerical results; ③ Seeing the five equations of a Kalman filter doesn't panic – you don't need to derive them, but you should be able to state the role of each equation (prediction, gain, update).

### 1.3 Classical Mechanics

**[What to do]** Newton-Euler equations, Lagrangian method, kinetic/potential energy, inertia tensor, angular momentum. Hands-on exercise: Derive the dynamics equations for a simple pendulum and a double pendulum using the Lagrangian method, numerically integrate for 5 seconds, and plot the angle curves.

**[Why]** A humanoid robot is a floating-base multi-rigid-body system. The equation M(q)q̈ + C(q,q̇) + g(q) = τ will run through every control paper you read later; bipedal balance (ZMP, capture point) are direct consequences of classical mechanics. Card: [Classical Mechanics](/entry/ent_foundation_classical_mechanics/) (including Newton's laws, conservation principles, and rigid body dynamics). The derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) and [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) start from here.

**[How to approach based on your background]** Mechanical/Vehicle background: You likely have this covered; do the double pendulum exercise to verify and move on; Pure software background: This is your **most important** catch-up in this stage – without mechanical intuition, when a robot falls in simulation, you won't know if it's the controller's fault or the model's fault.

**How much is enough**: ① Can derive the double pendulum equations (allowed to follow a book, but should be able to explain each step without the book); ② Can qualitatively explain "why a humanoid with a larger torso inertia is actually easier to stabilize"; ③ Understand the meaning of each field in the `<inertial>` tag of a URDF – this directly paves the way for Step 4.

### 1.4 Convex Optimization

**[What to do]** Identifying convex sets/functions, standard QP (Quadratic Programming) form, geometric meaning of equality/inequality constraints, solving a QP using an existing solver. Hands-on exercise: Solve min ‖x‖² s.t. Ax=b, x≥0 in Python (choose a solver like OSQP, quadprog, etc., based on your environment).

**[Why]** The real-time layer of humanoid control almost always solves a QP: Whole-Body Control (WBC) formulates "task tracking + contact force constraints + torque limits" as an inverse dynamics QP, solved every millisecond; MPC solves a QP in a receding horizon manner. Convexity guarantees that any local optimum is global – this is the fundamental reason engineers can put QP into kHz-level control loops. Card: [Convex Optimization](/entry/ent_foundation_convex_optimization/). For deeper dives, see Wiki [Chapter 14](/wiki/chapters/chapter-14/).

**[How to approach based on your background]** This is the one of the four with the **fastest diminishing marginal returns**: if you're not writing your own controller, "can identify convexity + can call a solver + can read a QP formulation" is enough. Leave KKT derivations for later, as needed. Operations research background: self-check and pass.

**How much is enough**: ① Given a problem, can determine if it's convex (quadratic positive definite objective + linear constraints → yes); ② The solution to the exercise satisfies all constraints upon verification; ③ Can explain to someone else "why WBC dares to use QP in a real-time loop."

## Step 2: Programming and Toolchain

**[What to do]** ① Python proficiency: NumPy vectorization, matplotlib plotting, writing classes; ② C++ to "read and modify" level: pointers/references, header files, compilation/linking; ③ Daily git operations: clone, branch, commit, push, create PR; ④ Install ROS 2 LTS, run the talker/listener example, and write your own pair of publisher/subscriber nodes; ⑤ Understand the basic FDM 3D printing workflow (modeling → slicing → printing) and strength basics.

**[Why]** The de facto standard for the humanoid software stack is [ROS 2 middleware](/entry/ent_software_ros_2_middleware_2024/) – a DDS-based publish/subscribe mechanism with real-time support (source: ros.org, see card). In later stages, your simulation, drivers, and state estimation will all be organized as nodes/topics. The low-level real-time loop uses C++, algorithm prototypes use Python – this is the industry standard division of labor. 3D printing is the primary manufacturing method for the full robot stage: the structural parts and cycloidal reducers of the open-source humanoid Berkeley Humanoid Lite are printed parts, with a total BOM cost of approximately $4,312 in the US and $3,236 in China (source: `data/roadmap/research/berkeley-humanoid-lite.md`) – the slicing and tolerance knowledge you learn now will directly translate into money and time savings. For the software ecosystem overview, see Wiki [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

**[How to approach based on your background]** Pure software background: Self-check and skip Python/git if proficient; invest time in C++ memory and real-time concepts, and the ROS 2 node/topic/service trio; Hardware background: Starting Python with NumPy is the most efficient path, closest to MATLAB thinking; Zero background: Learn Python first, then git; postpone C++ until needed, as you'll forget it if you don't use it.

**How much is enough**: ① ROS 2: Can independently write two nodes that publish and subscribe, and verify data flow with `ros2 topic echo`; ② git: Independently complete the full fork→branch→commit→PR workflow once (use your own practice repository); ③ 3D printing: Can explain how FDM layer orientation affects part strength, and why clearance is needed for mating holes (the specific tolerance magnitude for your machine should be confirmed with your supplier).

## Step 3: Circuits and Embedded Basics

**[What to Do]** In this phase, you will not build any boards, only establish three sets of concepts: **Power Supply** (voltage rails, current budget, wire gauge and voltage drop, fuses and switches), **Ground** (common ground, ground loops), and **Signals** (digital levels, differential transmission, anti-interference). Then, focus on understanding the role of the [CAN Bus](/entry/ent_technology_can_bus_2024/): it is the fieldbus connecting the joint motor drivers of a humanoid robot to the central controller (Source: Card, Wikipedia CAN bus 2024). Optional hands-on: Buy an entry-level CAN adapter (price needs to be confirmed with the supplier), and use can-utils to capture a segment of real bus data to observe the frame structure.

**[Why]** At the full robot stage, you will face a dozen to over twenty joint drivers hanging on the bus: The Berkeley Humanoid Lite uses CAN to connect all actuators, with the main controller being an Intel N95 mini PC (approx. $129, placed in the torso, running both low-level control and RL policies; Source: `data/roadmap/research/berkeley-humanoid-lite.md`). During full robot debugging, more than half of the "mysterious problems" originate from the electrical layer: voltage drop, common ground, termination resistors, and wiring harnesses. Building these concepts now will save you from burning boards later. For details on power system engineering, see Wiki [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/).

**[How to Analyze Your Situation]** EE/Automation background: Spend 30 minutes reviewing the concepts; Software or zero background: You are not required to design circuits, but you must be "brave enough to measure, and know how to measure" – use a multimeter to measure voltage and continuity, and understand what a short circuit on a 24V bus means. Safety Tip: Lithium batteries and bus capacitors are not toys. Verify safety protocols yourself before any live operation. If unsure, have someone with hardware experience present.

**What is Sufficient to Learn**: ① Be able to sketch a power supply topology diagram of "Battery → Fuse/E-Stop → Bus → Each Driver" by hand; ② Be able to explain why 120 Ω termination resistors are needed at both ends of a CAN bus; ③ Be able to explain why differential signals are more resistant to interference than single-ended signals.

## Step 4: First Simulation Experience – Read URDF, Make a Biped Stand Up

**[What to Do]** ① Install the [MuJoCo Physics Engine](/entry/ent_software_mujoco_physics_engine_2022/); ② Find an open-source humanoid/biped [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) file and read through it – URDF is a format using XML to describe robot links, joints, inertia, and geometry (Source: wiki.ros.org/urdf, see card); ③ Load the model into MuJoCo (or use the project's built-in MJCF); ④ Write a simple position PD controller: given target joint angles for a standing posture, make the biped model stand still in place for 10 seconds.

**[Why]** MuJoCo is a high-fidelity physics engine with rich contact dynamics, widely used in humanoid control research (Source: mujoco.org, see card) – the core difficulty of bipedal standing is precisely foot contact and balance, which plays to its strengths. Reading URDF is the first key to unlocking any open-source humanoid repository: real open-source projects maintain three description formats (URDF/MJCF/USD) simultaneously (Berkeley Humanoid Lite, Source: `data/roadmap/research/berkeley-humanoid-lite.md`). Understanding this format means you can read the "skeleton blueprint" of other people's robots. For a systematic discussion of simulation technology stacks, see Wiki [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**[How to Analyze Your Situation]** No GPU is fine – CPU is sufficient for standing-level rigid body simulation. When choosing a model, prioritize "small size, good documentation" open-source bipeds (the research archive `data/roadmap/research/` contains candidates like Berkeley Humanoid Lite, ToddlerBot, along with cost and complexity analysis). Don't jump straight into a full-size model. **If you can only complete one thing in this phase, make it this one** – it simultaneously validates mechanics, programming, and toolchain skills.

**What is Sufficient to Learn**: i.e., verification criteria items 1 and 2 below – this step is the capstone project for Stage 0.

## Verification Criteria

Check each item yourself. Only proceed to Stage 1 if all are passed:

1.  **URDF Reading Comprehension**: Given an unfamiliar biped URDF, be able to answer verbally without documentation – how many controllable joints, where is the root link, what are the `origin`/`axis` of the ankle joint, the meaning of `ixx/iyy/izz` in `<inertial>`; and use `check_urdf` or equivalent tool to confirm no parsing errors.
2.  **MuJoCo Standing**: Load the biped model, use your own position PD controller to achieve standing without external force for ≥ 10 seconds without falling; after applying a small impulse to the torso, the model can recover standing – or you can correctly explain why it cannot recover (gain, contact, or model issue). This tests mechanical intuition, not parameter tuning luck.
3.  **Math Spot Check**: Randomly pick one item from the "sufficiency criteria" of the four core subjects and demonstrate it on the spot (by hand calculation or running code).
4.  **Toolchain**: Have a record of successfully running ROS 2 talker/listener (terminal screenshot or screen recording); all practice code from this phase is in your git repository with clear, readable commit history.
5.  **Circuit Concepts**: Be able to explain the three topics – power supply topology, CAN termination resistor, and differential signals – to a peer (or to the air); failure to explain clearly means not meeting the standard.

Two warning signals for "not sufficient": Unable to write a PD controller without following a tutorial (Step 4 is done by following along); Not understanding why the model floats after changing the `origin` in URDF (geometric intuition from 1.1 not established). If either occurs, go back to the corresponding section and re-verify.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---------|---------------|------------------------|
| Model falls apart or flies around upon loading in MuJoCo | Initial pose has interpenetration (joints embedded in each other); a link lacks `<inertial>` causing zero mass/inertia | First check simulator compilation warnings; give the model a reasonable initial keyframe; check inertia parameters for each link |
| Joint high-frequency oscillation during PD standing | Gain too high, integration step too large, numerical stiffness | First halve P gain then slowly increase; reduce simulation timestep for comparison; check if desired damping was written as spring stiffness |
| Foot slipping like on ice | Contact friction parameters use defaults, lower than real sole-ground combination | Check `friction` parameters for geom/contact pairs; adjust based on material (rubber/PLA print) friction coefficient magnitude; specific values need to be confirmed based on material |
| Joint movement direction reversed after URDF to MJCF conversion | URDF `axis` definition inconsistent with target simulator convention; angle unit mix-up (degrees vs radians) | Drive each joint individually in the viewer to check direction; full-text search angle fields to confirm units |
| Two ROS 2 nodes cannot receive messages from each other | `ROS_DOMAIN_ID` mismatch; firewall blocking DDS traffic; topic name/QoS mismatch | First get it working on the same machine before cross-machine; use `ros2 topic list` to confirm both see the same topic; check environment variables (refer to official documentation for your distribution) |
| Reluctant to enter Stage 1, repeatedly re-studying math | Perfectionism trap: using "building a foundation" as an excuse to procrastinate | Check off items against the verification criteria one by one, move on when met; let Stage 1 expose the real gaps |

Stage 0 is now complete. Next stop: [Stage 1: Build an Actuator](stage-1-actuator.md): Apply the circuit concepts from Step 3 and PD control to real hardware for the first time; the URDF and MuJoCo foundation will be realized in the simulated walking of [Stage 2: Biped Platform](stage-2-biped.md).

## Companion Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) – The first simulation experience in Stage 0 will use the engine installation and model preparation from this guide.
- [Roadmap Overview](index.md)
