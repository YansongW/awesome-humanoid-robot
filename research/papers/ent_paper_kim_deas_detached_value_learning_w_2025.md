---
$id: ent_paper_kim_deas_detached_value_learning_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL'
  zh: DEAS
  ko: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL'
summary:
  en: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (DEAS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, University of Texas at Austin, NVIDIA.'
  zh: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (DEAS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, University of Texas at Austin, NVIDIA.'
  ko: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (DEAS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, University of Texas at Austin, NVIDIA.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deas
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07730v1.
sources:
- id: src_001
  type: paper
  title: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (arXiv)'
  url: https://arxiv.org/abs/2510.07730
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DEAS source
  url: https://doi.org/10.48550/arXiv.2510.07730
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Offline reinforcement learning (RL) presents an attractive paradigm for training intelligent agents without expensive online interactions. However, current approaches still struggle with complex, long-horizon sequential decision making. In this work, we introduce DEtached value learning with Action Sequence (DEAS), a simple yet effective offline RL framework that leverages action sequences for value learning. These temporally extended actions provide richer information than single-step actions and can be interpreted through the options framework via semi-Markov decision process Q-learning, enabling reduction of the effective planning horizon by considering longer sequences at once. However, directly adopting such sequences in actor-critic algorithms introduces excessive value overestimation, which we address through detached value learning that steers value estimates toward in-distribution actions that achieve high return in the offline dataset. We demonstrate that DEAS consistently outperforms baselines on complex, long-horizon tasks from OGBench and can be applied to enhance the performance of large-scale Vision-Language-Action models that predict action sequences, significantly boosting performance in both RoboCasa Kitchen simulation tasks and real-world manipulation tasks.

## 核心内容
Offline reinforcement learning (RL) presents an attractive paradigm for training intelligent agents without expensive online interactions. However, current approaches still struggle with complex, long-horizon sequential decision making. In this work, we introduce DEtached value learning with Action Sequence (DEAS), a simple yet effective offline RL framework that leverages action sequences for value learning. These temporally extended actions provide richer information than single-step actions and can be interpreted through the options framework via semi-Markov decision process Q-learning, enabling reduction of the effective planning horizon by considering longer sequences at once. However, directly adopting such sequences in actor-critic algorithms introduces excessive value overestimation, which we address through detached value learning that steers value estimates toward in-distribution actions that achieve high return in the offline dataset. We demonstrate that DEAS consistently outperforms baselines on complex, long-horizon tasks from OGBench and can be applied to enhance the performance of large-scale Vision-Language-Action models that predict action sequences, significantly boosting performance in both RoboCasa Kitchen simulation tasks and real-world manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.07730v1

