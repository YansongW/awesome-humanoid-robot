---
$id: ent_paper_zhang_safevla_towards_safety_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
  zh: SafeVLA
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
summary:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
  zh: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- safevla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03480v4.
sources:
- id: src_001
  type: paper
  title: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (arXiv)'
  url: https://arxiv.org/abs/2503.03480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 核心内容
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 参考
- http://arxiv.org/abs/2503.03480v4

