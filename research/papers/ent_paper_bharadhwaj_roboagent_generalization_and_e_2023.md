---
$id: ent_paper_bharadhwaj_roboagent_generalization_and_e_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking'
  zh: MT-ACT
  ko: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking'
summary:
  en: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
  zh: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
  ko: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- mt_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.01918v1.
sources:
- id: src_001
  type: website
  title: MT-ACT source
  url: https://doi.org/10.1109/ICRA57147.2024.10611293
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## 核心内容
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## 参考
- http://arxiv.org/abs/2309.01918v1

