---
$id: ent_paper_li_vla_models_are_more_generaliza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
  zh: FTM, FLA
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
summary:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
  zh: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ftm_fla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02902v2.
sources:
- id: src_001
  type: paper
  title: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FTM, FLA source
  url: https://doi.org/10.48550/arXiv.2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 核心内容
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 参考
- http://arxiv.org/abs/2512.02902v2

