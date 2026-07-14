---
$id: ent_paper_lu_when_robots_obey_the_patch_uni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
  zh: UPA-RFAS
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
summary:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
  zh: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
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
- upa_rfas
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21192v3.
sources:
- id: src_001
  type: paper
  title: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UPA-RFAS source
  url: https://doi.org/10.48550/arXiv.2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 核心内容
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 参考
- http://arxiv.org/abs/2511.21192v3

