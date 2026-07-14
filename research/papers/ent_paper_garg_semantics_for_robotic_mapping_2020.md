---
$id: ent_paper_garg_semantics_for_robotic_mapping_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Semantics for Robotic Mapping, Perception and Interaction: A Survey'
  zh: 机器人建图、感知与交互中的语义研究综述
  ko: '로봇 매핑, 인식 및 상호작용을 위한 의미론: 서베이'
summary:
  en: A 2020 survey that proposes a four-category taxonomy for semantics research in robotics and reviews more than 900 works
    spanning computer-vision fundamentals, semantic mapping, navigation, human-robot interaction, and deployment enablers.
  zh: 2020年发表的一篇综述，提出了机器人语义研究的四类别分类法，并调研了900多篇相关文献，涵盖计算机视觉基础、语义建图、导航、人机交互以及实际部署使能技术。
  ko: 2020년에 발표된 서베이로, 로봇 공학에서 의미론 연구를 위한 네 가지 범주 분류법을 제안하고 컴퓨터 비전 기초, 의미론적 매핑, 내비게이션, 인간-로봇 상호작용, 실제 배포 가능성 기술을 포함하여 900개
    이상의 관련 연구를 조사한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- semantic_mapping
- perception
- human_robot_interaction
- scene_understanding
- semantic_slam
- object_detection
- affordance
- survey
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.00443v1.
sources:
- id: src_001
  type: paper
  title: 'Semantics for Robotic Mapping, Perception and Interaction: A Survey'
  url: https://arxiv.org/abs/2101.00443
  date: '2020'
  accessed_at: '2026-06-27'
  doi: 10.1561/2300000059
theoretical_depth:
- method
---
## 概述
For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding of the world in which they operate. In robotics and related research fields, the study of understanding is often referred to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enablers like increasing availability of training data and computational resources, semantics is a rapidly growing research area in robotics. The field has received significant attention in the research literature to date, but most reviews and surveys have focused on particular aspects of the topic: the technical research issues regarding its use in specific robotic topics like mapping or segmentation, or its relevance to one particular application domain like autonomous driving. A new treatment is therefore required, and is also timely because so much relevant research has occurred since many of the key surveys were published. This survey therefore provides an overarching snapshot of where semantics in robotics stands today. We establish a taxonomy for semantics research in or relevant to robotics, split into four broad categories of activity, in which semantics are extracted, used, or both. Within these broad categories we survey dozens of major topics including fundamentals from the computer vision field and key robotics research areas utilizing semantics, including mapping, navigation and interaction with the world. The survey also covers key practical considerations, including enablers like increased data availability and improved computational hardware, and major application areas where...

## 核心内容
For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding of the world in which they operate. In robotics and related research fields, the study of understanding is often referred to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enablers like increasing availability of training data and computational resources, semantics is a rapidly growing research area in robotics. The field has received significant attention in the research literature to date, but most reviews and surveys have focused on particular aspects of the topic: the technical research issues regarding its use in specific robotic topics like mapping or segmentation, or its relevance to one particular application domain like autonomous driving. A new treatment is therefore required, and is also timely because so much relevant research has occurred since many of the key surveys were published. This survey therefore provides an overarching snapshot of where semantics in robotics stands today. We establish a taxonomy for semantics research in or relevant to robotics, split into four broad categories of activity, in which semantics are extracted, used, or both. Within these broad categories we survey dozens of major topics including fundamentals from the computer vision field and key robotics research areas utilizing semantics, including mapping, navigation and interaction with the world. The survey also covers key practical considerations, including enablers like increased data availability and improved computational hardware, and major application areas where...

## 参考
- http://arxiv.org/abs/2101.00443v1

