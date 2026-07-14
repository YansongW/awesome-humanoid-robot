---
$id: ent_paper_lyu_reinforcement_fine_tuning_of_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
  zh: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
  ko: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
summary:
  en: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
  zh: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
  ko: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
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
- reinforcement_fine_tuning_of_f
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09976v2.
sources:
- id: src_001
  type: paper
  title: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.09976
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2510.09976
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 核心内容
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 参考
- http://arxiv.org/abs/2510.09976v2

