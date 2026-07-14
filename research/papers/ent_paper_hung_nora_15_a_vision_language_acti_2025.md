---
$id: ent_paper_hung_nora_15_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards'
  zh: NORA-1.5
  ko: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards'
summary:
  en: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
  zh: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
  ko: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
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
- nora_15
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14659v1.
sources:
- id: src_001
  type: paper
  title: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (arXiv)'
  url: https://arxiv.org/abs/2511.14659
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NORA-1.5 source
  url: https://doi.org/10.48550/arXiv.2511.14659
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## 核心内容
Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## 参考
- http://arxiv.org/abs/2511.14659v1

