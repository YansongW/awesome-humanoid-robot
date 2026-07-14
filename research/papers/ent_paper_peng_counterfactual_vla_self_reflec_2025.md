---
$id: ent_paper_peng_counterfactual_vla_self_reflec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning'
  zh: Counterfactual VLA
  ko: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning'
summary:
  en: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
  zh: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
  ko: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- counterfactual_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24426v1.
sources:
- id: src_001
  type: paper
  title: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (arXiv)'
  url: https://arxiv.org/abs/2512.24426
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Counterfactual VLA source
  url: https://doi.org/10.48550/arXiv.2512.24426
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## 核心内容
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## 参考
- http://arxiv.org/abs/2512.24426v1

