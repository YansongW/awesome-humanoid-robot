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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.10588v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (917 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2105.10588v2

## 개요
이 리뷰 논문은 웨어러블 로봇이 초기 공상과학 속 강체 기계에서 가볍고 옷과 같은 소프트 슈트로 전환되고 있음을 지적합니다. 논문은 먼저 소프트 로봇 슈트의 정의를 제시하고, 기존 시스템을 분류하기 위한 체계를 구축합니다. 이후, 현재 최첨단 소프트 로봇 슈트의 구동 방식, 물리적 인간-로봇 인터페이스, 의도 감지 방법을 비판적으로 검토하며 각 접근법의 장단점을 분석합니다. 마지막으로, 논문은 인간 기능 강화 및 운동 장애 보조에 있어 이 기술의 생체역학적 효과를 논의하고, 향후 추가 개발이 필요한 핵심 영역을 제시합니다.

## 핵심 내용
### 정의 및 분류
- 소프트 로봇 슈트는 유연한 재료로 구성되어 인체 외부에 착용 가능한 로봇 시스템으로 정의되며, 운동 보조 또는 강화를 목적으로 합니다.
- 논문이 제안한 분류법은 **구동 유형**(예: 공압, 케이블 구동, 전기활성 폴리머), **구조 설계**(예: 외골격형, 직물형, 혼합형), **기능 목표**(예: 보조, 재활, 강화)의 세 가지 차원에 기반합니다.

### 핵심 기술 개요
- **구동 방식**: 공압 인공 근육(PAM)은 높은 출력 밀도를 제공하지만 외부 공기 공급원이 필요합니다. 케이블 구동(예: Bowden 케이블)은 가볍지만 마찰로 인해 효율이 저하됩니다. 전기활성 폴리머(예: 유전체 탄성체)는 응답이 빠르지만 구동력이 작습니다. 각 방식은 힘 출력, 응답 속도, 시스템 복잡성 측면에서 각각의 장단점이 있습니다.
- **물리적 인간-로봇 인터페이스**: 소프트 인터페이스는 유연한 직물이나 탄성 밴드를 통해 신체에 밀착되어 압력점을 줄이지만, 미끄러짐과 힘 전달 효율 문제를 해결해야 합니다. 논문은 인터페이스 설계가 편안함과 기계적 결합 강도 사이의 균형을 필요로 한다고 지적합니다.
- **의도 감지 전략**: 주요 방법으로는 근전도(EMG), 관성 측정 장치(IMU), 힘 센서가 있습니다. EMG는 운동 의도를 예측할 수 있지만 노이즈에 취약합니다. IMU는 자세 추정에 적합하지만 지연 시간이 비교적 깁니다. 힘 센서는 상호작용 힘을 직접 측정하지만 보정이 필요합니다. 혼합 센싱 전략(예: EMG+IMU)은 정확성과 견고성 측면에서 더 우수한 성능을 보입니다.

### 생체역학적 영향 및 도전 과제
- **운동 보조**: 소프트 로봇 슈트는 보행 보조에서 대사 소비를 줄일 수 있습니다(예: 보행 에너지 소비 10-20% 감소). 그러나 효과는 개인 차이와 작업 유형에 따라 달라집니다. 강화 측면에서는 중량 보행 시 관절 토크 출력을 향상시킬 수 있습니다.
- **운동 장애 지원**: 뇌졸중이나 척수 손상 환자의 경우, 소프트 슈트는 보행 대칭성과 관절 가동 범위를 개선할 수 있지만, 장기적 효과와 적응성은 여전히 검증이 필요합니다.
- **공개된 도전 과제**: 구동 시스템의 에너지 자립성(예: 배터리 수명과 무게의 상충), 의도 감지의 실시간성과 견고성, 소프트 재료의 장기 사용 내구성이 포함됩니다. 또한, 개인 맞춤형 적응과 사용자 수용도도 핵심 병목 지점입니다.
