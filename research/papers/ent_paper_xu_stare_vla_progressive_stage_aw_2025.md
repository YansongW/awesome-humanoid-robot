---
$id: ent_paper_xu_stare_vla_progressive_stage_aw_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
  zh: STARE-VLA
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
summary:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
  zh: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
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
- stare_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05107v2.
sources:
- id: src_001
  type: paper
  title: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: STARE-VLA source
  url: https://doi.org/10.48550/arXiv.2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 核心内容
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 参考
- http://arxiv.org/abs/2512.05107v2

