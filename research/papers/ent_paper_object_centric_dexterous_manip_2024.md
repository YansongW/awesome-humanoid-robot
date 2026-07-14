---
$id: ent_paper_object_centric_dexterous_manip_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Object-Centric Dexterous Manipulation from Human Motion Data
  zh: Object-Centric Dexterous Manipulation from Human Motion Data
  ko: Object-Centric Dexterous Manipulation from Human Motion Data
summary:
  en: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
  zh: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
  ko: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
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
- manipulation
- object_centric_dexterous_manip
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.04005v1.
sources:
- id: src_001
  type: paper
  title: Object-Centric Dexterous Manipulation from Human Motion Data (arXiv)
  url: https://arxiv.org/abs/2411.04005
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Object-Centric Dexterous Manipulation from Human Motion Data project page
  url: https://cypypccpy.github.io/obj-dex.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 核心内容
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 参考
- http://arxiv.org/abs/2411.04005v1

