# Appendix G Glossary

> This appendix is automatically generated from the knowledge graph data by `scripts/build_appendices.py` and is updated as the KG evolves.

One-sentence definitions of formal entities such as concepts, principles, operators, and algorithms in the knowledge graph, grouped by category.

## G.1 Concepts (17)

| Term | Definition |
|---|---|
| [World Model](/entry/ent_concept_world_model/) | A learned or handcrafted internal model that predicts the future state of the environment, supporting planning and reasoning in robotics and AI. |
| [Product Liability](/entry/ent_concept_product_liability/) | The legal responsibility of manufacturers and sellers for personal injury or property damage caused by defective or unsafe products, directly applicable to humanoid robots. |
| [Production Ramp-Up](/entry/ent_paper_production_ramp_2024/) | The current humanoid robot actuator supply chain is characterized by a high concentration of high-end reducers and high-end encoders: global leaders in harmonic reducers, Harmonic Drive, and RV reducers, Nabtesco, hold significant market shares; high-end magnetic/optical encoders are also primarily supplied by Japanese and European companies. |
| [Human-Robot Collaboration Safety](/entry/ent_concept_human_robot_collaboration_safety/) | A collection of standards, sensors, control laws, and workspace environment designs ensuring safe coexistence and collaboration between humans and robots, encompassing core standards such as ISO 13482, ISO/TS 15066, IEC 61508, ISO 13849, IEC 62368, and regional market certifications like CE, UL, FCC, CR, CCC… |
| [Seven Transitions from 0 to 1](/entry/ent_concept_seven_transitions/) | A framework of seven key transitions—technology, system, supply chain, manufacturing, cost, validation, and market—required to advance a humanoid robot from prototype to product. |
| [Embodied General Intelligence](/entry/ent_concept_embodied_general_intelligence/) | $$ \dot{x}(t) = f\big(x(t), u(t)\big), \quad y(t) = h\big(x(t), u(t)\big) $$ |
| [Decision Stack](/entry/ent_concept_decision_stack/) | The software subsystem that transforms perception results and task objectives into planning, strategies, and behavioral decisions. |
| [Perception Stack](/entry/ent_concept_perception_stack/) | The software subsystem that processes sensor data to estimate state, detect objects, and build environmental representations, providing input for decision-making. |
| [Actuation Stack](/entry/ent_concept_actuation_stack/) | The hardware and software subsystem that executes low-level motor commands, safety limits, and fault responses based on decision outputs. |
| [Digital Twin](/entry/ent_concept_digital_twin/) | A digital twin is a real-time mapping of a physical entity in digital space, usable for design validation, virtual commissioning, health monitoring, and predictive maintenance. |
| [Data Flywheel](/entry/ent_concept_data_flywheel/) | A self-reinforcing cycle where deployed robots generate data, data improves AI models, models enhance robot performance, and better performance generates more data. |
| [Robot as a Service (RaaS)](/entry/ent_concept_robot_as_a_service/) | A business model where robots are provided via leasing or subscription rather than outright purchase, bundled with maintenance, software updates, and fleet management. |
| [Demo-to-Product Gap](/entry/ent_concept_demo_to_product_gap/) | Unlike ASIMO and early Atlas, the new wave of 2025–2026 emphasizes long-term deployment in real-world scenarios and mass production feasibility: |
| [Bill of Materials](/entry/ent_paper_bill_of_materials_2024/) | A structured list of all parts, sub-assemblies, and raw materials required to build a humanoid robot. |
| [Constraint Qualification](/entry/ent_constraint_qualification/) | A regularity condition for optimization problem constraints that guarantees the validity of the Karush-Kuhn-Tucker necessary optimality conditions at a local optimum. |
| [Torque Density](/entry/ent_metric_torque_density/) | 1. |
| [Privacy and Biometrics](/entry/ent_concept_privacy_biometrics/) | Governance of personal information and biometric data (e.g., face, voiceprint, gait) collected by robots. |

## G.2 Principles (10)

| Term | Definition |
|---|---|
| [Force Closure](/entry/ent_principle_force_closure/) | A grasping condition where contact forces can balance any external wrench on the object without changing the contact configuration. |
| [Form Closure](/entry/ent_principle_form_closure/) | A grasping condition where the geometry and arrangement of frictionless contacts alone completely constrain the object's motion. |
| [Capture Point](/entry/ent_principle_capture_point/) | The Capture Point (CP) is a core concept in humanoid robot push recovery and gait planning: it is a point on the ground such that if the robot immediately steps onto it and places its center of mass directly above the support foot, it can stop without taking another step [44][45]. |
| [Maximum Likelihood Estimation](/entry/ent_principle_maximum_likelihood_estimation/) | A statistical principle that selects model parameters maximizing the probability of observing the training data, forming the basis for cross-entropy and next-token prediction loss. |
| [Newton-Euler Equations of Motion](/entry/ent_principle_newton_euler_equations/) | Coupled translational and rotational equations describing how forces and torques produce linear and angular accelerations of a rigid body. |
| [Current Loop / Velocity Loop / Position Loop](/entry/ent_principle_current_velocity_position_loops/) | 4. |
| [Conservation of Charge](/entry/ent_principle_conservation_of_charge/) | The fundamental principle that electric charge can neither be created nor destroyed, only redistributed; it underlies Kirchhoff's current law and charge balance equations in electrochemical systems. |
| [Fick's Law](/entry/ent_ficks_law/) | A constitutive principle stating that the diffusion flux of a substance is proportional to the negative of its concentration gradient. |
| [Center of Mass (COM)](/entry/ent_principle_center_of_mass/) | A humanoid robot is a multi-link system; its overall motion state is not only determined by the velocities of individual links but can also be uniformly described by the centroidal momentum. |
| [Zero Moment Point (ZMP)](/entry/ent_principle_zero_moment_point/) | 8. |

## G.3 Operators (3)

| Term | Definition |
|---|---|
| [Softmax Function](/entry/ent_operator_softmax_function/) | A differentiable operator that transforms a vector of real-valued scores into a probability distribution, highlighting the maximum while keeping all probabilities positive and summing to 1. |
| [Task Jacobian](/entry/ent_operator_task_jacobian/) | A matrix mapping joint-space velocities and accelerations to task-space coordinate velocities/accelerations in operational space. |
| [Voltage Divider](/entry/ent_operator_voltage_divider/) | A linear circuit operator that distributes the total voltage across series resistors in proportion to their resistance values. |

## G.4 Algorithms (9)

| Term | Definition |
|---|---|
| [DDPM Reverse Process](/entry/ent_ddpm_reverse_process/) | The learned reverse Markov chain in Denoising Diffusion Probabilistic Models (DDPM) that gradually transforms Gaussian noise into data-like samples. |
| [Active Set Method for Quadratic Programming](/entry/ent_algorithm_active_set_method/) | An iterative algorithm for solving quadratic programming problems that maintains a working set of active constraints and solves equality-constrained subproblems until optimality conditions are met. |
| [Interior Point Method](/entry/ent_interior_point_method/) | A class of optimization algorithms that solve constrained optimization problems by following a smooth central path within the feasible region using barrier or penalty functions. |
| [Score Matching](/entry/ent_score_matching/) | A parameter estimation technique that learns the gradient of an unknown log probability density (called the score) without requiring a normalized probability density. |
| [Backpropagation](/entry/ent_backpropagation/) | An efficient algorithm that computes the gradient of the loss function with respect to all parameters of a feedforward neural network by applying the chain rule layer by layer in reverse order. |
| [Gradient Descent](/entry/ent_gradient_descent/) | > Life example: Imagine you are blindfolded on a mountain trying to find the lowest point. |
| [Active Set Method](/entry/ent_active_set_method/) | > Life example: Imagine assembling a puzzle by first guessing which pieces touch the border (active constraints), assembling only those border pieces, and then checking if any internal pieces protrude. |
| [Soft Actor-Critic (SAC)](/entry/ent_algorithm_sac/) | An off-policy actor-critic reinforcement learning algorithm that maximizes expected return while also maximizing policy entropy to promote exploration. |
| [Proximal Policy Optimization (PPO)](/entry/ent_algorithm_ppo/) | A policy gradient reinforcement learning algorithm that improves sample efficiency by limiting the policy update step size to avoid destructive changes. |

## G.5 Formal Methods (8)

| Term | Definition |
|---|---|
| [Thevenin Equivalent Circuit](/entry/ent_formalism_thevenin_equivalent_circuit/) | A formal method that replaces any linear electrical network, as seen from two terminals, with an equivalent ideal voltage source in series with an equivalent resistance. |
| [Transformer Action Decoder Formalism](/entry/ent_formalism_transformer_action_decoder/) | A formal generative framework that uses a Transformer architecture and a learned vocabulary of action tokens to decode robot actions from visual-linguistic context. |
| [Lagrangian](/entry/ent_lagrangian/) | A scalar function that characterizes system dynamics through the difference between kinetic and potential energy (or a more general combination), from which equations of motion are derived via the variational principle. |
| [Standard Quadratic Programming (QP)](/entry/ent_qp_standard_form/) | The mainstream implementation of modern WBC is whole-body QP control. |
| [Euler-Lagrange Equations](/entry/ent_formalism_euler_lagrange_equations/) | A set of second-order differential equations derived from the stationary condition of the action variation, giving the equations of motion for mechanical systems in generalized coordinates. |
| [Floating Base Dynamics](/entry/ent_formalism_floating_base_dynamics/) | Unlike fixed-base industrial robotic arms, the base (torso) of a humanoid robot can move freely in space. |
| [Bayesian Filtering](/entry/ent_bayesian_filtering/) | A probabilistic framework that recursively maintains and updates the belief distribution of a hidden state using a dynamics model and noisy observations. |
| [Inverse Dynamics Quadratic Programming Formalism](/entry/ent_formalism_inverse_dynamics_qp/) | A quadratic programming formalism that computes generalized accelerations, contact forces, and joint torques by minimizing task tracking errors subject to floating base dynamics and physical constraints. |

## G.6 Theorems (2)

| Term | Definition |
|---|---|
| [Karush-Kuhn-Tucker (KKT) Conditions](/entry/ent_kkt_conditions/) | > Life example: Imagine you are in a mall trying to find the location closest to the exit, but you are told "you cannot enter any store" (inequality constraints) and "you must stand on the centerline of the aisle" (equality constraints). |
| [Chain Rule](/entry/ent_chain_rule/) | A fundamental calculus rule stating that the derivative of a composite function equals the product of the derivatives of its constituent functions. |

## G.7 Equations (7)

| Term | Definition |
|---|---|
| [Butler-Volmer Equation](/entry/ent_butler_volmer_equation/) | > Life example: Charging a battery is like many people squeezing through a revolving door at the same time. |
| [Thevenin Terminal Voltage Equation](/entry/ent_equation_thevenin_terminal_voltage/) | An equation stating that the terminal voltage of a Thevenin equivalent circuit equals the open-circuit voltage minus the voltage drop across the equivalent resistance. |
| [Weighted Task Error Objective Function](/entry/ent_equation_weighted_task_error_objective/) | A QP objective that penalizes the weighted squared difference between desired task accelerations and predicted task accelerations, with a regularization term added for generalized accelerations. |
| [Newton-Euler Equations](/entry/ent_newton_euler_equations/) | A set of coupled force balance and torque balance equations describing the motion of a rigid body or articulated multibody system. |
| [Scaled Dot-Product Self-Attention](/entry/ent_self_attention_equation/) | > Life example: When reading a sentence, each word "looks back" at the entire sentence and decides which words to focus on based on relevance. |
| [Nernst-Planck Equation](/entry/ent_nernst_planck_equation/) | A transport equation describing the flux of charged particles under the combined action of a concentration gradient and an electric field, integrating diffusion and electromigration. |
| [Continuity Equation](/entry/ent_continuity_equation/) | A partial differential equation that expresses local conservation by equating the rate of change of a physical quantity to the negative divergence of its flux. |

## G.8 Foundational Disciplines (5)

| Term | Definition |
|---|---|
| [Convex Optimization](/entry/ent_foundation_convex_optimization/) | The mathematical discipline of minimizing a convex function over a convex set, guaranteeing that any local optimum is also a global optimum. |
| [Probability Theory](/entry/ent_foundation_probability_theory/) | The mathematical foundation of uncertainty, random variables, distributions, and expectations, forming the basis of all probabilistic models in robotics and machine learning. |
| [Electrochemistry](/entry/ent_foundation_electrochemistry/) | The energy storage in lithium-ion batteries is essentially the reversible intercalation/deintercalation reaction of lithium in the crystal lattices of the positive and negative electrode active materials. |
| [Linear Algebra](/entry/ent_foundation_linear_algebra/) | The branch of mathematics studying vector spaces, linear transformations, matrices, and systems of linear equations. |
| [Classical Mechanics](/entry/ent_foundation_classical_mechanics/) | The branch of physics describing the motion of macroscopic objects under the action of forces, including Newton's laws, conservation principles, and rigid body dynamics. |
