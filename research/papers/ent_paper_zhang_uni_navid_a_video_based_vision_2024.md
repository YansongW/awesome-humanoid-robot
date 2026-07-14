---
$id: ent_paper_zhang_uni_navid_a_video_based_vision_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
  zh: Uni-NaVid
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
summary:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
  zh: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
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
- uni_navid
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.06224v2.
sources:
- id: src_001
  type: paper
  title: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (arXiv)'
  url: https://arxiv.org/abs/2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Uni-NaVid source
  url: https://doi.org/10.48550/arXiv.2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 核心内容
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 参考
- http://arxiv.org/abs/2412.06224v2

