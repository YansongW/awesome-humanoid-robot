---
$id: ent_paper_yang_discover_learn_and_reinforce_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories'
  zh: DLR
  ko: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories'
summary:
  en: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
  zh: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
  ko: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dlr
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19528v1.
sources:
- id: src_001
  type: paper
  title: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories
    (arXiv)'
  url: https://arxiv.org/abs/2511.19528
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DLR source
  url: https://doi.org/10.48550/arXiv.2511.19528
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Lea rn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## 核心内容
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Lea rn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## 参考
- http://arxiv.org/abs/2511.19528v1

