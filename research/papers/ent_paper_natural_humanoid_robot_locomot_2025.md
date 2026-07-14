---
$id: ent_paper_natural_humanoid_robot_locomot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Natural Humanoid Robot Locomotion with Generative Motion Prior
  zh: Natural Humanoid Robot Locomotion with Generative Motion Prior
  ko: Natural Humanoid Robot Locomotion with Generative Motion Prior
summary:
  en: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
  zh: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
  ko: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
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
- natural_humanoid_robot_locomot
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09015v1.
sources:
- id: src_001
  type: paper
  title: Natural Humanoid Robot Locomotion with Generative Motion Prior (arXiv)
  url: https://arxiv.org/abs/2503.09015
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## 核心内容
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## 参考
- http://arxiv.org/abs/2503.09015v1

