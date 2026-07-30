---
$id: ent_paper_xiloyannis_soft_robotic_suits_state_of_th_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Soft robotic suits: State of the art, core technologies and open challenges'
  zh: 软体机器人服：现状、核心技术与开放挑战
  ko: '소프트 로봇 슈트: 최신 기술, 핵심 기술 및 열린 과제'
summary:
  en: A 2021 arXiv survey that defines soft robotic suits, proposes a taxonomy, and reviews actuation, physical human-robot
    interfaces, intention-detection strategies, and biomechanical effects on human movement.
  zh: 这是一篇2021年arXiv上的综述论文，由研究团队撰写，系统定义了软体机器人服并提出了分类法。核心贡献在于全面回顾了驱动方式、人机物理接口和意图检测策略，并评估了其对人体运动的生物力学影响。
  ko: 2021년 arXiv에 발표된 종합 논문으로, 소프트 로봇 슈트를 정의하고 분류 체계를 제안하며 구동 방식, 물리적 인간-로봇 인터페이스, 의도 검출 전략 및 인간 움직임에 대한 생체역학적 영향을 검토한다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- soft_robotic_suit
- wearable_robot
- exosuit
- actuation
- human_robot_interface
- intention_detection
- assistive_robotics
- human_augmentation
- textile_based_assistance
- metabolic_cost
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.10588v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Soft robotic suits: State of the art, core technologies and open challenges'
  url: https://arxiv.org/abs/2105.10588
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该综述指出，可穿戴机器人正从早期科幻中的刚性机器向轻量、类衣的软体服装转型。论文首先给出了软体机器人服的定义，并建立了分类体系以归类现有系统。随后，它批判性地审视了当前最先进软体机器人服的驱动模式、物理人机接口和意图检测方法，分析了不同方案的优劣。最后，论文讨论了该技术在增强人体功能和辅助运动障碍方面的生物力学效应，并指出了未来需要进一步发展的关键领域。

## 核心内容
### 定义与分类
- 软体机器人服被定义为一种由柔性材料构成、可穿戴于人体外部的机器人系统，旨在提供运动辅助或增强。
- 论文提出的分类法基于三个维度：**驱动类型**（如气动、线缆驱动、电活性聚合物）、**结构设计**（如外骨骼式、织物式、混合式）和**功能目标**（如助力、康复、增强）。

### 核心技术综述
- **驱动方式**：气动人工肌肉（PAM）提供高功率密度但需外部气源；线缆驱动（如Bowden cable）轻便但效率受摩擦影响；电活性聚合物（如介电弹性体）响应快但驱动力小。每种方式在力输出、响应速度和系统复杂度上各有权衡。
- **物理人机接口**：软体接口通过柔性织物或弹性带贴合身体，减少压力点，但需解决滑移和力传递效率问题。论文指出，接口设计需平衡舒适性与机械耦合强度。
- **意图检测策略**：主要方法包括肌电图（EMG）、惯性测量单元（IMU）和力传感器。EMG能预测运动意图但受噪声干扰；IMU适合姿态估计但延迟较高；力传感器直接测量交互力但需校准。混合传感策略（如EMG+IMU）在准确性和鲁棒性上表现更优。

### 生物力学影响与挑战
- **运动辅助**：软体机器人服在步态辅助中可降低代谢消耗（如减少10-20%的行走能耗），但效果受个体差异和任务类型影响。在增强方面，如负重行走时，可提升关节力矩输出。
- **运动障碍支持**：对中风或脊髓损伤患者，软体服能改善步态对称性和关节活动范围，但长期效果和适应性仍需验证。
- **开放挑战**：包括驱动系统的能源自主性（如电池续航与重量矛盾）、意图检测的实时性与鲁棒性、以及软体材料在长期使用中的耐久性。此外，个性化适配和用户接受度也是关键瓶颈。

## Overview
Wearable robots are undergoing a disruptive transition, from the rigid machines that populated the science-fiction world in the early eighties to lightweight robotic apparel, hardly distinguishable from our daily clothes. In less than a decade of development, soft robotic suits have achieved important results in human motor assistance and augmentation. In this paper, we start by giving a definition of soft robotic suits and proposing a taxonomy to classify existing systems. We then critically review the modes of actuation, the physical human-robot interface and the intention-detection strategies of state of the art soft robotic suits, highlighting the advantages and limitations of different approaches. Finally, we discuss the impact of this new technology on human movements, for both augmenting human function and supporting motor impairments, and identify areas that are in need of further development.

## 개요
웨어러블 로봇은 1980년대 초반 공상과학 세계를 가득 채웠던 딱딱한 기계에서 일상복과 구별하기 어려운 경량 로봇 의류로의 혁신적인 전환을 겪고 있습니다. 10년도 채 되지 않은 개발 기간 동안 소프트 로봇 슈트는 인간의 운동 보조 및 증강 분야에서 중요한 성과를 거두었습니다. 본 논문에서는 먼저 소프트 로봇 슈트의 정의를 내리고 기존 시스템을 분류하기 위한 분류 체계를 제안합니다. 그런 다음 최신 소프트 로봇 슈트의 구동 방식, 물리적 인간-로봇 인터페이스 및 의도 감지 전략을 비판적으로 검토하며, 다양한 접근 방식의 장점과 한계를 강조합니다. 마지막으로, 인간 기능 증강과 운동 장애 지원 모두에서 이 새로운 기술이 인간의 움직임에 미치는 영향을 논의하고, 추가 개발이 필요한 영역을 식별합니다.

## 핵심 내용
웨어러블 로봇은 1980년대 초반 공상과학 세계를 가득 채웠던 딱딱한 기계에서 일상복과 구별하기 어려운 경량 로봇 의류로의 혁신적인 전환을 겪고 있습니다. 10년도 채 되지 않은 개발 기간 동안 소프트 로봇 슈트는 인간의 운동 보조 및 증강 분야에서 중요한 성과를 거두었습니다. 본 논문에서는 먼저 소프트 로봇 슈트의 정의를 내리고 기존 시스템을 분류하기 위한 분류 체계를 제안합니다. 그런 다음 최신 소프트 로봇 슈트의 구동 방식, 물리적 인간-로봇 인터페이스 및 의도 감지 전략을 비판적으로 검토하며, 다양한 접근 방식의 장점과 한계를 강조합니다. 마지막으로, 인간 기능 증강과 운동 장애 지원 모두에서 이 새로운 기술이 인간의 움직임에 미치는 영향을 논의하고, 추가 개발이 필요한 영역을 식별합니다.

## 参考
- http://arxiv.org/abs/2105.10588v2
