---
$id: ent_paper_booster_gym_an_end_to_end_rl_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
  zh: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
  ko: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
summary:
  en: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion is a 2025 work on locomotion for humanoid robots.'
  ko: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- booster_gym
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15132v1.
sources:
- id: src_001
  type: paper
  title: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion (arXiv)'
  url: https://arxiv.org/abs/2506.15132
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advancements in reinforcement learning (RL) have led to significant progress in humanoid robot locomotion, simplifying the design and training of motion policies in simulation. However, the numerous implementation details make transferring these policies to real-world robots a challenging task. To address this, we have developed a comprehensive code framework that covers the entire process from training to deployment, incorporating common RL training methods, domain randomization, reward function design, and solutions for handling parallel structures. This library is made available as a community resource, with detailed descriptions of its design and experimental results. We validate the framework on the Booster T1 robot, demonstrating that the trained policies seamlessly transfer to the physical platform, enabling capabilities such as omnidirectional walking, disturbance resistance, and terrain adaptability. We hope this work provides a convenient tool for the robotics community, accelerating the development of humanoid robots. The code can be found in https://github.com/BoosterRobotics/booster_gym.

## 核心内容
Recent advancements in reinforcement learning (RL) have led to significant progress in humanoid robot locomotion, simplifying the design and training of motion policies in simulation. However, the numerous implementation details make transferring these policies to real-world robots a challenging task. To address this, we have developed a comprehensive code framework that covers the entire process from training to deployment, incorporating common RL training methods, domain randomization, reward function design, and solutions for handling parallel structures. This library is made available as a community resource, with detailed descriptions of its design and experimental results. We validate the framework on the Booster T1 robot, demonstrating that the trained policies seamlessly transfer to the physical platform, enabling capabilities such as omnidirectional walking, disturbance resistance, and terrain adaptability. We hope this work provides a convenient tool for the robotics community, accelerating the development of humanoid robots. The code can be found in https://github.com/BoosterRobotics/booster_gym.

## 参考
- http://arxiv.org/abs/2506.15132v1

