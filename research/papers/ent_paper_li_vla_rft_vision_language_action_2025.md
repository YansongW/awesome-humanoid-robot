---
$id: ent_paper_li_vla_rft_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators'
  zh: VLA-RFT
  ko: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators'
summary:
  en: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (VLA-RFT), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    OpenHelix Team, Fudan University, Zhengzhou University, BUPT, Hebei University of Technology.'
  zh: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (VLA-RFT), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    OpenHelix Team, Fudan University, Zhengzhou University, BUPT, Hebei University of Technology.'
  ko: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (VLA-RFT), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    OpenHelix Team, Fudan University, Zhengzhou University, BUPT, Hebei University of Technology.'
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
- vision_language_action
- vla
- vla_rft
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.00406v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (arXiv)'
  url: https://arxiv.org/abs/2510.00406
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-RFT source
  url: https://doi.org/10.48550/arXiv.2510.00406
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models enable embodied decision-making but rely heavily on imitation learning, leading to compounding errors and poor robustness under distribution shift. Reinforcement learning (RL) can mitigate these issues yet typically demands costly real-world interactions or suffers from sim-to-real gaps. We introduce VLA-RFT, a reinforcement fine-tuning framework that leverages a data-driven world model as a controllable simulator. Trained from real interaction data, the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references. This design delivers an efficient and action-aligned learning signal, drastically lowering sample requirements. With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL. Moreover, it exhibits strong robustness under perturbed conditions, sustaining stable task execution. Our results establish world-model-based RFT as a practical post-training paradigm to enhance the generalization and robustness of VLA models. For more details, please refer to https://vla-rft.github.io/.

## 核心内容
Vision-Language-Action (VLA) models enable embodied decision-making but rely heavily on imitation learning, leading to compounding errors and poor robustness under distribution shift. Reinforcement learning (RL) can mitigate these issues yet typically demands costly real-world interactions or suffers from sim-to-real gaps. We introduce VLA-RFT, a reinforcement fine-tuning framework that leverages a data-driven world model as a controllable simulator. Trained from real interaction data, the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references. This design delivers an efficient and action-aligned learning signal, drastically lowering sample requirements. With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL. Moreover, it exhibits strong robustness under perturbed conditions, sustaining stable task execution. Our results establish world-model-based RFT as a practical post-training paradigm to enhance the generalization and robustness of VLA models. For more details, please refer to https://vla-rft.github.io/.

## 参考
- http://arxiv.org/abs/2510.00406v1

