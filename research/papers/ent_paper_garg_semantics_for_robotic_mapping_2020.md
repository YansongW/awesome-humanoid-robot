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
  zh: For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding
    of the world in which they operate. In robotics and related research fields, the study of understanding is often referred
    to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to
    represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot
    interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enab
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

## Overview
For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding of the world in which they operate. In robotics and related research fields, the study of understanding is often referred to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enablers like increasing availability of training data and computational resources, semantics is a rapidly growing research area in robotics. The field has received significant attention in the research literature to date, but most reviews and surveys have focused on particular aspects of the topic: the technical research issues regarding its use in specific robotic topics like mapping or segmentation, or its relevance to one particular application domain like autonomous driving. A new treatment is therefore required, and is also timely because so much relevant research has occurred since many of the key surveys were published. This survey therefore provides an overarching snapshot of where semantics in robotics stands today. We establish a taxonomy for semantics research in or relevant to robotics, split into four broad categories of activity, in which semantics are extracted, used, or both. Within these broad categories we survey dozens of major topics including fundamentals from the computer vision field and key robotics research areas utilizing semantics, including mapping, navigation and interaction with the world. The survey also covers key practical considerations, including enablers like increased data availability and improved computational hardware, and major application areas where...

## Content
For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding of the world in which they operate. In robotics and related research fields, the study of understanding is often referred to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enablers like increasing availability of training data and computational resources, semantics is a rapidly growing research area in robotics. The field has received significant attention in the research literature to date, but most reviews and surveys have focused on particular aspects of the topic: the technical research issues regarding its use in specific robotic topics like mapping or segmentation, or its relevance to one particular application domain like autonomous driving. A new treatment is therefore required, and is also timely because so much relevant research has occurred since many of the key surveys were published. This survey therefore provides an overarching snapshot of where semantics in robotics stands today. We establish a taxonomy for semantics research in or relevant to robotics, split into four broad categories of activity, in which semantics are extracted, used, or both. Within these broad categories we survey dozens of major topics including fundamentals from the computer vision field and key robotics research areas utilizing semantics, including mapping, navigation and interaction with the world. The survey also covers key practical considerations, including enablers like increased data availability and improved computational hardware, and major application areas where...

## 개요
로봇이 주변 세계를 더 풍부하게 탐색하고 상호작용하려면, 작동하는 세계에 대한 더 깊은 이해가 필요할 것입니다. 로봇 공학 및 관련 연구 분야에서 이해에 대한 연구는 종종 의미론(semantics)이라고 불리며, 이는 세계가 로봇에게 "의미"하는 바를 규정하고, 그 의미를 표현하는 방법에 대한 질문과 밀접하게 연결됩니다. 인간과 로봇이 점점 더 같은 세계에서 작동함에 따라, 인간-로봇 상호작용의 가능성은 자연어의 의미론과 존재론(ontology)을 그림 속으로 끌어들입니다. 필요성과 함께 훈련 데이터 및 계산 자원의 증가와 같은 촉진 요인에 의해 주도되어, 의미론은 로봇 공학에서 빠르게 성장하는 연구 분야입니다. 이 분야는 지금까지 연구 문헌에서 상당한 주목을 받았지만, 대부분의 리뷰와 조사는 특정 측면에 초점을 맞추었습니다: 매핑이나 분할과 같은 특정 로봇 주제에서의 사용에 관한 기술적 연구 문제, 또는 자율 주행과 같은 특정 응용 분야와의 관련성 등입니다. 따라서 새로운 접근이 필요하며, 많은 주요 조사가 발표된 이후로 많은 관련 연구가 이루어졌기 때문에 시의적절하기도 합니다. 따라서 이 조사는 오늘날 로봇 공학에서 의미론이 어디에 있는지에 대한 포괄적인 스냅샷을 제공합니다. 우리는 로봇 공학에서 또는 관련된 의미론 연구를 위한 분류 체계를 수립하며, 의미가 추출되거나 사용되거나 둘 다인 네 가지 광범위한 활동 범주로 나눕니다. 이러한 광범위한 범주 내에서 우리는 컴퓨터 비전 분야의 기초와 의미론을 활용하는 주요 로봇 공학 연구 영역(매핑, 탐색 및 세계와의 상호작용 포함)을 포함한 수십 가지 주요 주제를 조사합니다. 이 조사는 또한 데이터 가용성 증가 및 개선된 계산 하드웨어와 같은 촉진 요인과 주요 응용 분야를 포함한 핵심 실용적 고려 사항을 다룹니다...

## 핵심 내용
로봇이 주변 세계를 더 풍부하게 탐색하고 상호작용하려면, 작동하는 세계에 대한 더 깊은 이해가 필요할 것입니다. 로봇 공학 및 관련 연구 분야에서 이해에 대한 연구는 종종 의미론(semantics)이라고 불리며, 이는 세계가 로봇에게 "의미"하는 바를 규정하고, 그 의미를 표현하는 방법에 대한 질문과 밀접하게 연결됩니다. 인간과 로봇이 점점 더 같은 세계에서 작동함에 따라, 인간-로봇 상호작용의 가능성은 자연어의 의미론과 존재론(ontology)을 그림 속으로 끌어들입니다. 필요성과 함께 훈련 데이터 및 계산 자원의 증가와 같은 촉진 요인에 의해 주도되어, 의미론은 로봇 공학에서 빠르게 성장하는 연구 분야입니다. 이 분야는 지금까지 연구 문헌에서 상당한 주목을 받았지만, 대부분의 리뷰와 조사는 특정 측면에 초점을 맞추었습니다: 매핑이나 분할과 같은 특정 로봇 주제에서의 사용에 관한 기술적 연구 문제, 또는 자율 주행과 같은 특정 응용 분야와의 관련성 등입니다. 따라서 새로운 접근이 필요하며, 많은 주요 조사가 발표된 이후로 많은 관련 연구가 이루어졌기 때문에 시의적절하기도 합니다. 따라서 이 조사는 오늘날 로봇 공학에서 의미론이 어디에 있는지에 대한 포괄적인 스냅샷을 제공합니다. 우리는 로봇 공학에서 또는 관련된 의미론 연구를 위한 분류 체계를 수립하며, 의미가 추출되거나 사용되거나 둘 다인 네 가지 광범위한 활동 범주로 나눕니다. 이러한 광범위한 범주 내에서 우리는 컴퓨터 비전 분야의 기초와 의미론을 활용하는 주요 로봇 공학 연구 영역(매핑, 탐색 및 세계와의 상호작용 포함)을 포함한 수십 가지 주요 주제를 조사합니다. 이 조사는 또한 데이터 가용성 증가 및 개선된 계산 하드웨어와 같은 촉진 요인과 주요 응용 분야를 포함한 핵심 실용적 고려 사항을 다룹니다...
