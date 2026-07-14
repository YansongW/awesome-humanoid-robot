---
$id: ent_paper_omni_perception_omnidirectiona_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
  zh: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
  ko: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
summary:
  en: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
  zh: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
  ko: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- omni_perception
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19214v2.
sources:
- id: src_001
  type: paper
  title: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments (arXiv)'
  url: https://arxiv.org/abs/2505.19214
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 核心内容
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 参考
- http://arxiv.org/abs/2505.19214v2

