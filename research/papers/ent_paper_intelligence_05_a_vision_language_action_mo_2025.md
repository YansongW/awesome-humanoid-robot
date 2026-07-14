---
$id: ent_paper_intelligence_05_a_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0.5: a Vision-Language-Action Model with Open-World Generalization'
  zh: π0.5
  ko: 'π0.5: a Vision-Language-Action Model with Open-World Generalization'
summary:
  en: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
  zh: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
  ko: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- '05'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.16054v1.
sources:
- id: src_001
  type: paper
  title: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (arXiv)'
  url: https://arxiv.org/abs/2504.16054
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π0.5 source
  url: https://doi.org/10.48550/arXiv.2504.16054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 核心内容
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 参考
- http://arxiv.org/abs/2504.16054v1

