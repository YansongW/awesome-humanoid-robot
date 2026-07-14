---
$id: ent_paper_mao_beyond_success_refining_elegan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention'
  zh: Beyond Success
  ko: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention'
summary:
  en: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention (Beyond Success),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Jilin University, Microsoft Research
    Asia.'
  zh: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention (Beyond Success),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Jilin University, Microsoft Research
    Asia.'
  ko: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention (Beyond Success),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Jilin University, Microsoft Research
    Asia.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- beyond_success
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22555v1.
sources:
- id: src_001
  type: paper
  title: 'Beyond Success: Refining Elegant Robot Manipulation from Mixed-Quality Data via Just-in-Time Intervention (arXiv)'
  url: https://arxiv.org/abs/2511.22555
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Beyond Success source
  url: https://doi.org/10.48550/arXiv.2511.22555
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have enabled notable progress in general-purpose robotic manipulation, yet their learned policies often exhibit variable execution quality. We attribute this variability to the mixed-quality nature of human demonstrations, where the implicit principles that govern how actions should be carried out are only partially satisfied. To address this challenge, we introduce the LIBERO-Elegant benchmark with explicit criteria for evaluating execution quality. Using these criteria, we develop a decoupled refinement framework that improves execution quality without modifying or retraining the base VLA policy. We formalize Elegant Execution as the satisfaction of Implicit Task Constraints (ITCs) and train an Elegance Critic via offline Calibrated Q-Learning to estimate the expected quality of candidate actions. At inference time, a Just-in-Time Intervention (JITI) mechanism monitors critic confidence and intervenes only at decision-critical moments, providing selective, on-demand refinement. Experiments on LIBERO-Elegant and real-world manipulation tasks show that the learned Elegance Critic substantially improves execution quality, even on unseen tasks. The proposed model enables robotic control that values not only whether tasks succeed, but also how they are performed.

## 核心内容
Vision-Language-Action (VLA) models have enabled notable progress in general-purpose robotic manipulation, yet their learned policies often exhibit variable execution quality. We attribute this variability to the mixed-quality nature of human demonstrations, where the implicit principles that govern how actions should be carried out are only partially satisfied. To address this challenge, we introduce the LIBERO-Elegant benchmark with explicit criteria for evaluating execution quality. Using these criteria, we develop a decoupled refinement framework that improves execution quality without modifying or retraining the base VLA policy. We formalize Elegant Execution as the satisfaction of Implicit Task Constraints (ITCs) and train an Elegance Critic via offline Calibrated Q-Learning to estimate the expected quality of candidate actions. At inference time, a Just-in-Time Intervention (JITI) mechanism monitors critic confidence and intervenes only at decision-critical moments, providing selective, on-demand refinement. Experiments on LIBERO-Elegant and real-world manipulation tasks show that the learned Elegance Critic substantially improves execution quality, even on unseen tasks. The proposed model enables robotic control that values not only whether tasks succeed, but also how they are performed.

## 参考
- http://arxiv.org/abs/2511.22555v1

