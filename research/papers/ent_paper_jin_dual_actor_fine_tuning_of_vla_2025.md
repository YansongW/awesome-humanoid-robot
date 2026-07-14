---
$id: ent_paper_jin_dual_actor_fine_tuning_of_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
  zh: Dual-Actor Fine-Tuning of VLA Models
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
summary:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
  zh: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_actor_fine_tuning_of_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13774v1.
sources:
- id: src_001
  type: paper
  title: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (arXiv)'
  url: https://arxiv.org/abs/2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Actor Fine-Tuning of VLA Models source
  url: https://doi.org/10.48550/arXiv.2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 核心内容
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 参考
- http://arxiv.org/abs/2509.13774v1

