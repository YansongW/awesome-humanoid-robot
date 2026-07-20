# Stage 0 Foundation Building: Getting Your Ticket to Humanoid Robotics

> ⚠️ The content of this roadmap is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when dealing with electrical or mechanical operations.

## Positioning of This Stage

The goal of Stage 0 is not to "learn all the basics" – that's a bottomless pit where countless people get stuck. The goal is to obtain four tickets:

1.  **Mathematics**: Be familiar with matrices, probability, dynamics equations, and QP when you see them in control papers;
2.  **Programming & Toolchain**: Be able to work with Python/C++/git/ROS 2, and know what 3D printing is about;
3.  **Circuit Concepts**: Know where electricity comes from and how signals travel, so you don't burn boards when you later work with real hardware;
4.  **Simulation**: Read a URDF file and make a bipedal model stand up in MuJoCo.

- **Time Budget**: 6–10 weeks part-time (8–10 hours/week), 3–4 weeks full-time.
- **Budget**: Approximately ¥0 – all software in this stage is open source; costs for optional 3D printing prototyping experience need to be confirmed with the supplier.
- **Core Discipline**: Each topic provides a criterion for "how much is enough to learn". **Meet the criterion and move on; do not go back for more practice**. Real gaps will be exposed in later stages, and you can return to fill them with specific problems, which is ten times more efficient.

## Step 1: The Four Pillars of Mathematics

Don't learn them the way math majors do (definition-theorem-proof). Learn them as a "control engineer's minimum ammunition depot". The criterion for all four is **demonstrable**, not "I feel I understand".

### 1.1 Linear Algebra

【What to do】Vector and matrix operations, eigenvalues/eigenvectors, rotation matrices and homogeneous transformations, least squares and pseudo-inverse. Hands-on practice: Use NumPy to write a 4×4 homogeneous transformation to transform foot coordinates from the ankle frame to the torso frame; then write the forward kinematics of a two-link planar arm.

【Why】Linear algebra is the language of all spatial relationships in humanoid robots: forward kinematics is the multiplication of homogeneous transformations, the Jacobian matrix maps joint velocities to end-effector velocities, and every QP in whole-body control is a matrix operation. Card: [Linear Algebra](/entry/ent_foundation_linear_algebra/) (the branch of mathematics studying vector spaces, linear transformations, matrices, and systems of linear equations). The kinematic derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) are all built on this.

【How to approach based on your background】CS background: You already know the calculations; focus on **geometric intuition** – a rotation matrix is not nine numbers, it's the three axes of a coordinate system. Physics/Math background: Go straight to the exercises above as a test. Zero background: First watch 3Blue1Brown's "Essence of Linear Algebra" to build intuition, then start calculating.

**How much is enough** (stop when all three criteria are met): ① Can manually derive a 2D rotation matrix and explain the geometric meaning of each column; ② The forward kinematics code for a two-link planar arm runs and its output matches manual calculation; ③ When you see the pseudo-inverse J⁺ of the Jacobian, you know it's solving a least-squares problem.

### 1.2 Probability Theory

【What to do】Random variables, expectation and covariance, Gaussian distribution, Bayes' theorem, conditioning and marginalization. Hands-on practice: Use NumPy to simulate "joint encoder readings" with Gaussian noise, plot a histogram, and calculate the mean/variance; then manually solve a "sensor alarm → true fault probability" problem using Bayes' theorem.

【Why】Real sensors always have noise. State estimation (the Kalman filter family) is essentially recursive Bayesian inference. Imitation learning and VLA models used later also output probability distributions of actions, not deterministic values. Card: [Probability Theory](/entry/ent_foundation_probability_theory/) – the foundation of all probabilistic models in robotics and machine learning.

【How to approach based on your background】AI background: Self-check with the criteria; you'll likely pass directly. Hardware background: This is often your weakest of the four, and it directly determines whether you can understand state estimation later – it's worth investing half your math budget here. Zero background: Study this after linear algebra.

**How much is enough**: ① Can explain in one sentence what the diagonal and off-diagonal elements of a covariance matrix represent; ② Can manually solve a Bayes' theorem problem with correct numerical results; ③ When you see the five equations of the Kalman filter, you don't panic – you don't need to derive them, but you can state the role of each equation (predict, gain, update).

### 1.3 Classical Mechanics

【What to do】Newton-Euler equations, Lagrangian method, kinetic/potential energy, inertia tensor, angular momentum. Hands-on practice: Use the Lagrangian method to derive the dynamics equations for a simple pendulum and a double pendulum, perform numerical integration for a 5-second simulation, and plot the angle curves.

【Why】A humanoid robot is a floating-base multi-rigid-body system. The equation M(q)q̈ + C(q,q̇) + g(q) = τ will run through every control paper you read later. Bipedal balance (ZMP, capture point) is a direct consequence of classical mechanics. Card: [Classical Mechanics](/entry/ent_foundation_classical_mechanics/) (including Newton's laws, conservation principles, and rigid body dynamics). The derivations in Wiki [Chapter 8](/wiki/chapters/chapter-08/) and [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/) all start from here.

【How to approach based on your background】Mechanical/Automotive background: You're likely good enough; just do the double pendulum exercise to verify and move on. Pure software background: This is your **most important** catch-up in this stage – without mechanical intuition, when a robot falls in simulation, you won't know if it's the controller's fault or the model's fault.

**How much is enough**: ① Can derive the double pendulum equations (allowed to follow a book, but can explain each step without it); ② Can qualitatively explain "why a humanoid robot with a larger torso inertia is actually easier to stabilize"; ③ Understand the meaning of each field in the `<inertial>` tag of a URDF – this directly paves the way for Step 4.

### 1.4 Convex Optimization

【What to do】Identifying convex sets/functions, standard QP (Quadratic Programming) form, geometric meaning of equality/inequality constraints, solving a QP using an existing solver. Hands-on practice: Use Python to solve min ‖x‖² s.t. Ax=b, x≥0 (choose a solver like OSQP, quadprog, etc., based on your environment).

【Why】The real-time layer of humanoid control almost always solves a QP: Whole-Body Control (WBC) formulates "task tracking + contact force constraints + torque limits" as an inverse dynamics QP, solved every millisecond; MPC solves QPs in a receding horizon. Convexity guarantees that any local optimum is also global – this is the fundamental reason engineers can put QP into kHz-level control loops. Card: [Convex Optimization](/entry/ent_foundation_convex_optimization/). For deeper study, see Wiki [Chapter 14](/wiki/chapters/chapter-14/).

【How to approach based on your background】This is the subject with the **fastest diminishing marginal returns** among the four: if you're not writing your own controller, "can identify convexity + can use a solver + can understand QP structure" is enough; leave KKT derivation for later when needed. Operations research background: self-check and pass.

**How much is enough**: ① Given a problem, can determine if it's convex (quadratic positive definite objective + linear constraints → yes); ② The solution to the practice problem satisfies all constraints upon verification; ③ Can explain to someone else "why WBC dares to use QP in a real-time loop".

## Step 2: Programming & Toolchain

【What to do】① Python proficiency: NumPy vectorization, matplotlib plotting, writing classes; ② C++ to the level of "can read and modify": pointers/references, header files, compilation/linking; ③ Daily git operations: clone, branch, commit, push, submit a PR; ④ Install ROS 2 LTS, run the talker/listener example, and write your own pair of publisher/subscriber nodes; ⑤ Understand the basic FDM 3D printing workflow (modeling → slicing → printing) and strength fundamentals.

【Why】The de facto standard for the humanoid software stack is [ROS 2 middleware](/entry/ent_software_ros_2_middleware_2024/) – a DDS-based publish/subscribe mechanism with real-time support (source: ros.org, see card). Your simulation, drivers, and state estimation in later stages will all be organized as nodes/topics. The industry standard division of labor is C++ for the low-level real-time loop and Python for algorithm prototyping. 3D printing is the primary manufacturing method for the later full-robot stage: the structural parts and cycloidal reducers of the open-source humanoid Berkeley Humanoid Lite are printed parts, with a total BOM cost of approximately $4,312 in the US and $3,236 in China (source: `data/roadmap/research/berkeley-humanoid-lite.md`). The slicing and tolerance knowledge you learn now will directly translate into money and time savings. For a full picture of the software ecosystem, see Wiki [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/).

【How to approach based on your background】Pure software background: Skip Python/git if you pass the self-check; invest time in C++ memory/real-time concepts and the ROS 2 node/topic/service trio. Hardware background: Starting Python with NumPy is the most efficient path, as it's closest to MATLAB thinking. Zero background: Learn Python first, then git; postpone C++ until needed, as you'll forget it if you don't use it.

**How much is enough**: ① ROS 2: Can independently write two nodes (one publisher, one subscriber) and verify data flow using `ros2 topic echo`; ② git: Complete the full fork→branch→commit→PR workflow once (practice on your own exercise repository); ③ 3D printing: Can explain the effect of FDM layer orientation on part strength, and why clearance is needed for mating holes (the specific tolerance magnitude for a given machine needs to be confirmed with the supplier).

## Step 3: Circuits and Embedded Basics

**[What to Do]** In this phase, you will not build any boards, only establish three sets of concepts: **Power Supply** (voltage rails, current budget, wire gauge and voltage drop, fuses and switches), **Ground** (common ground, ground loops), and **Signals** (digital levels, differential transmission, anti-interference). Then focus on understanding the role of the [CAN Bus](/entry/ent_technology_can_bus_2024/): it is the fieldbus connecting the joint motor drivers of a humanoid robot with the central controller (Source: Card, Wikipedia CAN bus 2024). Optional hands-on: Buy an entry-level CAN adapter (price to be confirmed with the supplier), use can-utils to capture a segment of real bus data and observe the frame structure.

**[Why]** At the full robot stage, you will face a dozen to over twenty joint drivers hanging on the bus: Berkeley Humanoid Lite uses CAN to connect all actuators, with the main controller being an Intel N95 mini PC (approx. $129, placed in the torso, running both low-level control and RL policies; Source: `data/roadmap/research/berkeley-humanoid-lite.md`). During full robot debugging, more than half of the "mysterious problems" originate from the electrical layer: voltage drop, common ground, termination resistors, and wiring harnesses. Establishing these concepts now will save you from burning boards later. For details on power system engineering, see Wiki [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/).

**[How to Analyze Your Situation]** EE/Automation background: Spend 30 minutes reviewing the concepts; Software or zero background: You are not required to design circuits, but you must be "brave enough to measure, and know how to measure" — use a multimeter to measure voltage and continuity, and understand what a short circuit on a 24 V bus means. Safety tip: Lithium batteries and bus capacitors are not toys. Verify safety regulations yourself before any live operation. If unsure, have someone with hardware experience present.

**What is Sufficient to Learn**: ① Be able to sketch a power supply topology diagram by hand: "Battery → Fuse/Emergency Stop → Bus → Each Driver"; ② Be able to explain why 120 Ω termination resistors are needed at both ends of a CAN bus; ③ Be able to explain why differential signals are more immune to interference than single-ended signals.

## Step 4: First Simulation Experience — Understand URDF, Make a Biped Stand Up

**[What to Do]** ① Install the [MuJoCo Physics Engine](/entry/ent_software_mujoco_physics_engine_2022/); ② Find an open-source humanoid/biped [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) file and read through it — URDF is an XML format describing robot links, joints, inertia, and geometry (Source: wiki.ros.org/urdf, see card); ③ Load the model into MuJoCo (or use the project's built-in MJCF); ④ Write a simple position PD controller: given target joint angles for a standing posture, make the biped model stand still for 10 seconds.

**[Why]** MuJoCo is a high-fidelity physics engine with rich contact dynamics, widely used in humanoid control research (Source: mujoco.org, see card) — the core difficulty of bipedal standing is precisely foot contact and balance, which plays to its strengths. Understanding URDF is the first key to unlocking any open-source humanoid repository: real open-source projects maintain three description formats (URDF/MJCF/USD) simultaneously (Berkeley Humanoid Lite, Source: `data/roadmap/research/berkeley-humanoid-lite.md`). Understanding this format allows you to read the "skeleton blueprint" of other robots. For a systematic discussion of the simulation technology stack, see Wiki [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**[How to Analyze Your Situation]** No GPU is fine — CPU is sufficient for standing-level rigid body simulation. Prioritize "small size, good documentation" open-source bipeds (the research archive `data/roadmap/research/` contains candidates like Berkeley Humanoid Lite, ToddlerBot, along with cost and complexity analysis). Don't jump into full-size models. **If you can only complete one thing in this phase, make it this one** — it simultaneously validates mechanics, programming, and toolchain skills.

**What is Sufficient to Learn**: i.e., verification criteria items 1 and 2 below — this step is the graduation project for Stage 0.

## Verification Criteria

Self-check each item. Only proceed to Stage 1 if all are passed:

1.  **URDF Reading Comprehension**: Given an unfamiliar biped URDF, be able to answer verbally without documentation — how many controllable joints, where is the root link, what are the `origin`/`axis` of the ankle joint, the meaning of `ixx/iyy/izz` in `<inertial>`; and use `check_urdf` or an equivalent tool to confirm no parsing errors.
2.  **MuJoCo Standing**: Load the biped model, use your own position PD controller to achieve standing without external force for ≥ 10 seconds without falling; after applying a small impulse to the torso, the model can recover standing — or you can correctly explain why it cannot recover (gain, contact, or model issue). This tests mechanical intuition, not parameter tuning luck.
3.  **Math Spot Check**: Randomly pick one item from each of the "sufficiency criteria" of the four core subjects, and be able to demonstrate it on the spot (hand calculation or running code).
4.  **Toolchain**: Have a record of successfully running ROS 2 talker/listener (terminal screenshot or screen recording); all practice code from this phase is in your git repository with clear commit history.
5.  **Circuit Concepts**: Be able to explain to a peer (or to the air) the three topics: power supply topology, CAN termination resistors, and differential signals; if you cannot explain clearly, it is considered not up to standard.

Two "not sufficient" warning signals: Unable to write a PD controller without following a tutorial (Step 4 is done by following along); Changing the `origin` in URDF and not understanding why the model floats (geometric intuition from 1.1 not established). If either occurs, go back to the corresponding section for re-verification.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---------|---------------|------------------------|
| Model falls apart or flies around upon loading in MuJoCo | Initial pose has interpenetration (joints embedded in each other); a link lacks `<inertial>` causing zero mass/inertia | First check simulator compilation warnings; give the model a reasonable initial keyframe; check inertia parameters for each link |
| Joints oscillate at high frequency during PD standing | Gain too high, integration step too large, numerical stiffness | First halve P gain then slowly increase; reduce simulation timestep to reproduce and compare; check if desired damping was written as spring stiffness |
| Feet slip like on ice | Contact friction parameters use defaults, lower than real sole-ground combination | Check friction parameters for geom/contact pairs; adjust based on friction coefficient magnitude for sole material (rubber/PLA print), specific values need to be confirmed based on material |
| Joint motion direction reversed after URDF to MJCF conversion | URDF `axis` definition inconsistent with target simulator convention; angle unit mix-up (degrees vs radians) | Drive each joint individually in the viewer to check direction; full-text search angle fields to confirm units |
| Two ROS 2 nodes cannot receive messages from each other | `ROS_DOMAIN_ID` inconsistent; firewall blocking DDS traffic; topic name/QoS mismatch | First get it working on the same machine, then across machines; `ros2 topic list` to confirm both see the same topic; check environment variables (refer to the official documentation of your distribution) |
| Reluctant to enter Stage 1, repeatedly re-learning math | Perfectionism trap: using "building a foundation" as an excuse to procrastinate | Check off items against the verification criteria one by one; move on when criteria are met; let Stage 1 expose the real gaps |

Stage 0 is now complete. Next stop: [Stage 1: Build an Actuator (Joint)](stage-1-actuator.md): Apply the circuit concepts from Step 3 and PD control to real hardware for the first time; the foundation in URDF and MuJoCo will pay off in [Stage 2: Biped Platform](stage-2-biped.md) for simulated walking.

## Companion Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) — The first simulation experience in Stage 0 will use the engine installation and model preparation from this guide.
- [Roadmap Overview](index.md)
