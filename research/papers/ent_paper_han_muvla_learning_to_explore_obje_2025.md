---
$id: ent_paper_han_muvla_learning_to_explore_obje_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MUVLA: Learning to Explore Object Navigation via Map Understanding'
  zh: MUVLA
  ko: 'MUVLA: Learning to Explore Object Navigation via Map Understanding'
summary:
  en: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
  zh: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
  ko: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
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
- muvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25966v1.
sources:
- id: src_001
  type: paper
  title: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (arXiv)'
  url: https://arxiv.org/abs/2509.25966
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MUVLA source
  url: https://doi.org/10.48550/arXiv.2509.25966
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## 核心内容
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## 参考
- http://arxiv.org/abs/2509.25966v1

