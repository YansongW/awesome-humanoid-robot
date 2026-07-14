---
$id: ent_paper_yan_when_alignment_fails_multimoda_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
  zh: VLA-Fool
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
summary:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
  zh: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
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
- vla_fool
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16203v3.
sources:
- id: src_001
  type: paper
  title: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Fool source
  url: https://doi.org/10.48550/arXiv.2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 核心内容
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 参考
- http://arxiv.org/abs/2511.16203v3

