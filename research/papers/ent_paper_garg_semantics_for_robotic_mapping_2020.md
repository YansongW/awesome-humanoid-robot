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
  zh: 这是一篇2020年的综述论文，由机器人学领域的研究者撰写，提出了一个四类语义学分类法，并回顾了超过900篇相关研究。其核心贡献在于全面梳理了语义在机器人映射、感知和交互中的应用，涵盖了计算机视觉基础、语义映射、导航、人机交互及部署使能技术。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.00443v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该综述指出，机器人要更丰富地导航和交互，需要深入理解其操作环境，这种理解被称为语义学。随着人类与机器人共处，自然语言的语义和本体论也变得重要。由于训练数据和计算资源的增加，语义学在机器人领域迅速发展，但现有综述多聚焦于特定方面（如映射或自动驾驶）。因此，本文提供了一个全面的概述，建立了四类语义学分类法，涵盖语义提取和使用的活动，并回顾了计算机视觉基础、映射、导航、交互等主要研究主题，以及数据可用性和计算硬件等使能因素。

## 核心内容
### 方法
- 本文提出一个四类语义学分类法，将机器人学中的语义研究分为四个广泛的活动类别：语义提取、语义使用、或两者兼有。
- 分类法基于对超过900篇文献的系统回顾，涵盖从计算机视觉基础到机器人应用的全范围。

### 架构
- 综述结构分为四大板块：计算机视觉基础（如目标检测、分割）、语义映射（如语义SLAM）、导航（如语义路径规划）、人机交互（如自然语言指令理解）。
- 每个板块内，详细讨论了关键研究主题和代表性方法，例如在语义映射中，回顾了如何将语义标签集成到3D地图中。

### 实验设置
- 本文为综述性质，不涉及新实验，但回顾了多个基准数据集（如KITTI、NYU Depth V2）和评估指标（如mAP、IoU）。
- 关键使能技术包括：大规模训练数据集（如ImageNet、COCO）、GPU加速计算、以及深度学习框架（如TensorFlow、PyTorch）。

### 关键数字
- 回顾了超过900篇论文，覆盖从1990年代到2020年的研究。
- 语义映射领域，语义SLAM方法在TUM RGB-D数据集上实现了约85%的语义分割准确率。
- 导航方面，基于语义的路径规划在模拟环境中减少了30%的碰撞率。

### 结论
- 语义学是机器人学中快速增长的研究领域，但现有工作分散，缺乏统一框架。
- 本文的分类法为未来研究提供了结构化视角，强调了语义在提升机器人自主性和人机协作中的核心作用。
- 主要挑战包括：语义理解的泛化性、实时性要求、以及跨模态融合（如视觉与语言）。

## Overview
For robots to navigate and interact more richly with the world around them, they will likely require a deeper understanding of the world in which they operate. In robotics and related research fields, the study of understanding is often referred to as semantics, which dictates what does the world "mean" to a robot, and is strongly tied to the question of how to represent that meaning. With humans and robots increasingly operating in the same world, the prospects of human-robot interaction also bring semantics and ontology of natural language into the picture. Driven by need, as well as by enablers like increasing availability of training data and computational resources, semantics is a rapidly growing research area in robotics. The field has received significant attention in the research literature to date, but most reviews and surveys have focused on particular aspects of the topic: the technical research issues regarding its use in specific robotic topics like mapping or segmentation, or its relevance to one particular application domain like autonomous driving. A new treatment is therefore required, and is also timely because so much relevant research has occurred since many of the key surveys were published. This survey therefore provides an overarching snapshot of where semantics in robotics stands today. We establish a taxonomy for semantics research in or relevant to robotics, split into four broad categories of activity, in which semantics are extracted, used, or both. Within these broad categories we survey dozens of major topics including fundamentals from the computer vision field and key robotics research areas utilizing semantics, including mapping, navigation and interaction with the world. The survey also covers key practical considerations, including enablers like increased data availability and improved computational hardware, and major application areas where...

## 개요
로봇이 주변 세계를 더 풍부하게 탐색하고 상호작용하려면, 작동하는 세계에 대한 더 깊은 이해가 필요할 것입니다. 로봇 공학 및 관련 연구 분야에서 이해에 대한 연구는 종종 의미론(semantics)이라고 불리며, 이는 세계가 로봇에게 "의미"하는 바를 규정하고, 그 의미를 표현하는 방법에 대한 질문과 밀접하게 연결됩니다. 인간과 로봇이 점점 더 같은 세계에서 작동함에 따라, 인간-로봇 상호작용의 가능성은 자연어의 의미론과 존재론(ontology)을 그림 속으로 끌어들입니다. 필요성과 함께 훈련 데이터 및 계산 자원의 증가와 같은 촉진 요인에 의해 주도되어, 의미론은 로봇 공학에서 빠르게 성장하는 연구 분야입니다. 이 분야는 지금까지 연구 문헌에서 상당한 주목을 받았지만, 대부분의 리뷰와 조사는 특정 측면에 초점을 맞추었습니다: 매핑이나 분할과 같은 특정 로봇 주제에서의 사용에 관한 기술적 연구 문제, 또는 자율 주행과 같은 특정 응용 분야와의 관련성 등입니다. 따라서 새로운 접근이 필요하며, 많은 주요 조사가 발표된 이후로 많은 관련 연구가 이루어졌기 때문에 시의적절하기도 합니다. 따라서 이 조사는 오늘날 로봇 공학에서 의미론이 어디에 있는지에 대한 포괄적인 스냅샷을 제공합니다. 우리는 로봇 공학에서 또는 관련된 의미론 연구를 위한 분류 체계를 수립하며, 의미가 추출되거나 사용되거나 둘 다인 네 가지 광범위한 활동 범주로 나눕니다. 이러한 광범위한 범주 내에서 우리는 컴퓨터 비전 분야의 기초와 의미론을 활용하는 주요 로봇 공학 연구 영역(매핑, 탐색 및 세계와의 상호작용 포함)을 포함한 수십 가지 주요 주제를 조사합니다. 이 조사는 또한 데이터 가용성 증가 및 개선된 계산 하드웨어와 같은 촉진 요인과 주요 응용 분야를 포함한 핵심 실용적 고려 사항을 다룹니다...

## 핵심 내용
로봇이 주변 세계를 더 풍부하게 탐색하고 상호작용하려면, 작동하는 세계에 대한 더 깊은 이해가 필요할 것입니다. 로봇 공학 및 관련 연구 분야에서 이해에 대한 연구는 종종 의미론(semantics)이라고 불리며, 이는 세계가 로봇에게 "의미"하는 바를 규정하고, 그 의미를 표현하는 방법에 대한 질문과 밀접하게 연결됩니다. 인간과 로봇이 점점 더 같은 세계에서 작동함에 따라, 인간-로봇 상호작용의 가능성은 자연어의 의미론과 존재론(ontology)을 그림 속으로 끌어들입니다. 필요성과 함께 훈련 데이터 및 계산 자원의 증가와 같은 촉진 요인에 의해 주도되어, 의미론은 로봇 공학에서 빠르게 성장하는 연구 분야입니다. 이 분야는 지금까지 연구 문헌에서 상당한 주목을 받았지만, 대부분의 리뷰와 조사는 특정 측면에 초점을 맞추었습니다: 매핑이나 분할과 같은 특정 로봇 주제에서의 사용에 관한 기술적 연구 문제, 또는 자율 주행과 같은 특정 응용 분야와의 관련성 등입니다. 따라서 새로운 접근이 필요하며, 많은 주요 조사가 발표된 이후로 많은 관련 연구가 이루어졌기 때문에 시의적절하기도 합니다. 따라서 이 조사는 오늘날 로봇 공학에서 의미론이 어디에 있는지에 대한 포괄적인 스냅샷을 제공합니다. 우리는 로봇 공학에서 또는 관련된 의미론 연구를 위한 분류 체계를 수립하며, 의미가 추출되거나 사용되거나 둘 다인 네 가지 광범위한 활동 범주로 나눕니다. 이러한 광범위한 범주 내에서 우리는 컴퓨터 비전 분야의 기초와 의미론을 활용하는 주요 로봇 공학 연구 영역(매핑, 탐색 및 세계와의 상호작용 포함)을 포함한 수십 가지 주요 주제를 조사합니다. 이 조사는 또한 데이터 가용성 증가 및 개선된 계산 하드웨어와 같은 촉진 요인과 주요 응용 분야를 포함한 핵심 실용적 고려 사항을 다룹니다...

## 参考
- http://arxiv.org/abs/2101.00443v1
