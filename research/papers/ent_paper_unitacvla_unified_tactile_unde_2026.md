---
$id: ent_paper_unitacvla_unified_tactile_unde_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  zh: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  ko: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
summary:
  en: "arXiv:2606.31723v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models have achieved strong performance\
    \ in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation,\
    \ recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact\
    \ information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model\
    \ tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for\
    \ contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and\
    \ prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future\
    \ contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming\
    \ a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller\
    \ that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections.\
    \ Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly,\
    \ under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy,\
    \ and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction."
  zh: "arXiv:2606.31723v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models have achieved strong performance\
    \ in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation,\
    \ recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact\
    \ information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model\
    \ tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for\
    \ contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and\
    \ prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future\
    \ contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming\
    \ a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller\
    \ that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections.\
    \ Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly,\
    \ under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy,\
    \ and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction."
  ko: "arXiv:2606.31723v1 Announce Type: new \nAbstract: Vision-language-action (VLA) models have achieved strong performance\
    \ in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation,\
    \ recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact\
    \ information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model\
    \ tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for\
    \ contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and\
    \ prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future\
    \ contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming\
    \ a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller\
    \ that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections.\
    \ Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly,\
    \ under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy,\
    \ and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- unitacvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31723v1.
sources:
- id: src_001
  type: paper
  title: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  url: https://arxiv.org/abs/2606.31723
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction.

## 核心内容
Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction.

## 参考
- http://arxiv.org/abs/2606.31723v1

