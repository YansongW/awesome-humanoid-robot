---
$id: ent_paper_zhao_learning_fine_grained_bimanual_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
  zh: ACT
  ko: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
summary:
  en: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
  zh: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
  ko: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- act
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.13705v1.
sources:
- id: src_001
  type: website
  title: ACT source
  url: https://doi.org/10.15607/RSS.2023.XIX.016
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## 核心内容
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## 参考
- http://arxiv.org/abs/2304.13705v1

