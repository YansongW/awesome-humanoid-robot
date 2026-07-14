---
$id: ent_paper_chen_training_strategies_for_effici_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Training Strategies for Efficient Embodied Reasoning
  zh: ECoT-Lite
  ko: Training Strategies for Efficient Embodied Reasoning
summary:
  en: Training Strategies for Efficient Embodied Reasoning (ECoT-Lite), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Stanford, and published at CoRL25.
  zh: Training Strategies for Efficient Embodied Reasoning (ECoT-Lite), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Stanford, and published at CoRL25.
  ko: Training Strategies for Efficient Embodied Reasoning (ECoT-Lite), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Stanford, and published at CoRL25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ecot_lite
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.08243v2.
sources:
- id: src_001
  type: paper
  title: Training Strategies for Efficient Embodied Reasoning (arXiv)
  url: https://arxiv.org/abs/2505.08243
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ECoT-Lite source
  url: https://doi.org/10.48550/arXiv.2505.08243
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot chain-of-thought reasoning (CoT) -- wherein a model predicts helpful intermediate representations before choosing actions -- provides an effective method for improving the generalization and performance of robot policies, especially vision-language-action models (VLAs). While such approaches have been shown to improve performance and generalization, they suffer from core limitations, like needing specialized robot reasoning data and slow inference speeds. To design new robot reasoning approaches that address these issues, a more complete characterization of why reasoning helps policy performance is critical. We hypothesize several mechanisms by which robot reasoning improves policies -- (1) better representation learning, (2) improved learning curricularization, and (3) increased expressivity -- then devise simple variants of robot CoT reasoning to isolate and test each one. We find that learning to generate reasonings does lead to better VLA representations, while attending to the reasonings aids in actually leveraging these features for improved action prediction. Our results provide us with a better understanding of why CoT reasoning helps VLAs, which we use to introduce two simple and lightweight alternative recipes for robot reasoning. Our proposed approaches achieve significant performance gains over non-reasoning policies, state-of-the-art results on the LIBERO-90 benchmark, and a 3x inference speedup compared to standard robot reasoning.

## 核心内容
Robot chain-of-thought reasoning (CoT) -- wherein a model predicts helpful intermediate representations before choosing actions -- provides an effective method for improving the generalization and performance of robot policies, especially vision-language-action models (VLAs). While such approaches have been shown to improve performance and generalization, they suffer from core limitations, like needing specialized robot reasoning data and slow inference speeds. To design new robot reasoning approaches that address these issues, a more complete characterization of why reasoning helps policy performance is critical. We hypothesize several mechanisms by which robot reasoning improves policies -- (1) better representation learning, (2) improved learning curricularization, and (3) increased expressivity -- then devise simple variants of robot CoT reasoning to isolate and test each one. We find that learning to generate reasonings does lead to better VLA representations, while attending to the reasonings aids in actually leveraging these features for improved action prediction. Our results provide us with a better understanding of why CoT reasoning helps VLAs, which we use to introduce two simple and lightweight alternative recipes for robot reasoning. Our proposed approaches achieve significant performance gains over non-reasoning policies, state-of-the-art results on the LIBERO-90 benchmark, and a 3x inference speedup compared to standard robot reasoning.

## 参考
- http://arxiv.org/abs/2505.08243v2

