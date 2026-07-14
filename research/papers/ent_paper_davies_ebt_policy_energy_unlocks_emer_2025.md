---
$id: ent_paper_davies_ebt_policy_energy_unlocks_emer_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
  zh: EBT-Policy
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
summary:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
  zh: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ebt_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27545v1.
sources:
- id: src_001
  type: paper
  title: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (arXiv)'
  url: https://arxiv.org/abs/2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EBT-Policy source
  url: https://doi.org/10.48550/arXiv.2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 核心内容
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 参考
- http://arxiv.org/abs/2510.27545v1

