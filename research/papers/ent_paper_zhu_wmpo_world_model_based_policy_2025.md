---
$id: ent_paper_zhu_wmpo_world_model_based_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
  zh: WMPO
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
summary:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
  zh: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
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
- wmpo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09515v1.
sources:
- id: src_001
  type: paper
  title: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WMPO source
  url: https://doi.org/10.48550/arXiv.2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 核心内容
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 参考
- http://arxiv.org/abs/2511.09515v1

