---
$id: ent_paper_dexcap_scalable_and_portable_m_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
  zh: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
  ko: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
summary:
  en: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  zh: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  ko: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexcap
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.07788v2.
sources:
- id: src_001
  type: paper
  title: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation (arXiv)'
  url: https://arxiv.org/abs/2403.07788
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation project page'
  url: https://dex-cap.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## 核心内容
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## 参考
- http://arxiv.org/abs/2403.07788v2

