---
$id: ent_paper_end_to_end_humanoid_robot_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
  zh: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
  ko: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
summary:
  en: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
  zh: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
  ko: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- end_to_end_humanoid_robot_safe
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07611v1.
sources:
- id: src_001
  type: paper
  title: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy (arXiv)
  url: https://arxiv.org/abs/2508.07611
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## 核心内容
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## 参考
- http://arxiv.org/abs/2508.07611v1

