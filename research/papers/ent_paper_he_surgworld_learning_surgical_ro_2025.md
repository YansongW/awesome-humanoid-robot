---
$id: ent_paper_he_surgworld_learning_surgical_ro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling'
  zh: SurgWorld
  ko: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling'
summary:
  en: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (SurgWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, The Chinese University of Hong Kong, Sung Kyun Kwan University,
    Wenzhou Medical University, National University of Singapore, Ruijin Hospital.'
  zh: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (SurgWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, The Chinese University of Hong Kong, Sung Kyun Kwan University,
    Wenzhou Medical University, National University of Singapore, Ruijin Hospital.'
  ko: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (SurgWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, The Chinese University of Hong Kong, Sung Kyun Kwan University,
    Wenzhou Medical University, National University of Singapore, Ruijin Hospital.'
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
- surgworld
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23162v4.
sources:
- id: src_001
  type: paper
  title: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.23162
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SurgWorld source
  url: https://doi.org/10.48550/arXiv.2512.23162
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Data scarcity remains a fundamental barrier to achieving fully autonomous surgical robots. While large scale vision language action (VLA) models have shown impressive generalization in household and industrial manipulation by leveraging paired video action data from diverse domains, surgical robotics suffers from the paucity of datasets that include both visual observations and accurate robot kinematics. In contrast, vast corpora of surgical videos exist, but they lack corresponding action labels, preventing direct application of imitation learning or VLA training. In this work, we aim to alleviate this problem by learning policy models from Cosmos-H-Surgical, a world model designed for surgical physical AI. We curated the Surgical Action Text Alignment (SATA) dataset with detailed action description specifically for surgical robots. Then we built Cosmos-H-Surgical based on the most advanced physical AI world model and SATA. It's able to generate diverse, generalizable and realistic surgery videos. We are also the first to use an inverse dynamics model to infer pseudokinematics from synthetic surgical videos, producing synthetic paired video action data. We demonstrate that a surgical VLA policy trained with these augmented data significantly outperforms models trained only on real demonstrations on a real surgical robot platform. Our approach offers a scalable path toward autonomous surgical skill acquisition by leveraging the abundance of unlabeled surgical video and generative world modeling, thus opening the door to generalizable and data efficient surgical robot policies.

## 核心内容
Data scarcity remains a fundamental barrier to achieving fully autonomous surgical robots. While large scale vision language action (VLA) models have shown impressive generalization in household and industrial manipulation by leveraging paired video action data from diverse domains, surgical robotics suffers from the paucity of datasets that include both visual observations and accurate robot kinematics. In contrast, vast corpora of surgical videos exist, but they lack corresponding action labels, preventing direct application of imitation learning or VLA training. In this work, we aim to alleviate this problem by learning policy models from Cosmos-H-Surgical, a world model designed for surgical physical AI. We curated the Surgical Action Text Alignment (SATA) dataset with detailed action description specifically for surgical robots. Then we built Cosmos-H-Surgical based on the most advanced physical AI world model and SATA. It's able to generate diverse, generalizable and realistic surgery videos. We are also the first to use an inverse dynamics model to infer pseudokinematics from synthetic surgical videos, producing synthetic paired video action data. We demonstrate that a surgical VLA policy trained with these augmented data significantly outperforms models trained only on real demonstrations on a real surgical robot platform. Our approach offers a scalable path toward autonomous surgical skill acquisition by leveraging the abundance of unlabeled surgical video and generative world modeling, thus opening the door to generalizable and data efficient surgical robot policies.

## 参考
- http://arxiv.org/abs/2512.23162v4

