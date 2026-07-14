---
$id: ent_paper_ye_vla_r1_enhancing_reasoning_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models'
  zh: VLA-R1
  ko: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models'
summary:
  en: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
  zh: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
  ko: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
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
- vla_r1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01623v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.01623
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-R1 source
  url: https://doi.org/10.48550/arXiv.2510.01623
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## 核心内容
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## 参考
- http://arxiv.org/abs/2510.01623v1

