---
$id: ent_paper_pro_crisp_compliant_ros2_controlle_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation
  zh: CRISP
  ko: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation
summary:
  en: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (CRISP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Technical University of Munich (TUM), TUM School
    of Computation, Information and Technology.
  zh: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (CRISP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Technical University of Munich (TUM), TUM School
    of Computation, Information and Technology.
  ko: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (CRISP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Technical University of Munich (TUM), TUM School
    of Computation, Information and Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- crisp
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06819v2.
sources:
- id: src_001
  type: paper
  title: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (arXiv)
  url: https://arxiv.org/abs/2509.06819
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CRISP source
  url: https://doi.org/10.48550/arXiv.2509.06819
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level targets commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

## 核心内容
Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level targets commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

## 参考
- http://arxiv.org/abs/2509.06819v2

