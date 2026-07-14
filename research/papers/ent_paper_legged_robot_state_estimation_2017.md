---
$id: ent_paper_legged_robot_state_estimation_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
  zh: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
  ko: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
summary:
  en: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
  zh: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
  ko: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- legged_robot_state_estimation
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1712.05873v2.
sources:
- id: src_001
  type: paper
  title: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors (arXiv)
  url: https://arxiv.org/abs/1712.05873
  date: '2017'
  accessed_at: '2026-07-01'
---
## 概述
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## 核心内容
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## 参考
- http://arxiv.org/abs/1712.05873v2

