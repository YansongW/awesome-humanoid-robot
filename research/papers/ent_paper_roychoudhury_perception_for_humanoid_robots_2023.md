---
$id: ent_paper_roychoudhury_perception_for_humanoid_robots_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perception for Humanoid Robots
  zh: 人形机器人感知
  ko: 휴머노이드 로봇의 인지
summary:
  en: A 2023 survey by Roychoudhury, Khorshidi, Agrawal, and Bennewitz reviews perception modalities and algorithmic approaches
    for humanoid robots, covering internal state estimation, external environment understanding, and human-robot interaction
    through proprioceptive, visual, auditory, and tactile sensing.
  zh: Roychoudhury、Khorshidi、Agrawal 和 Bennewitz 于 2023 年发表的综述，系统梳理了人形机器人的感知模态与算法方法，涵盖本体感觉、视觉、听觉和触觉传感，核心贡献在于将感知应用划分为内部状态估计、外部环境理解与人机交互三大领域，并总结了多传感器融合与机器学习的最新趋势。
  ko: Roychoudhury, Khorshidi, Agrawal, Bennewitz가 2023년에 발표한 설문조사로, 본체감각, 시각, 청각 및 촉각 센싱을 활용한 내부 상태 추정, 외부 환경 이해, 인간-로봇 상호작용을
    포함하는 휴머노이드 로봇의 인지 모달리티와 알고리즘 접근법을 검토한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- perception
- humanoid_perception
- state_estimation
- sensor_fusion
- multi_sensor_fusion
- dynamic_slam
- human_robot_interaction
- tactile_sensing
- proprioceptive_sensing
- machine_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.15616v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Perception for Humanoid Robots
  url: https://arxiv.org/abs/2309.15616
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---
## 概述
该综述聚焦人形机器人感知技术，旨在提升机器人与人及环境交互的安全性、效率与体验。研究探讨了视觉、听觉和触觉等多种感知模态，并分析了内部状态估计、外部环境理解与人机交互三个关键应用方向。内部状态估计主要依赖贝叶斯滤波和最大后验优化方法；外部环境理解则强调多传感器融合与机器学习，以应对动态环境变化；人机交互方法突出了上下文信息表示与记忆对理解人类意图的重要性。

## 核心内容
### 综述目的
人形机器人感知是实现与人类及环境无缝交互的基础，直接影响安全性、效率与用户体验。本研究系统调查了人形机器人采用的多种感知模态（视觉、听觉、触觉）及算法，重点分析感知内部状态、环境、物体与人类活动的最新方法。

### 近期发现
- **内部状态估计**：广泛使用贝叶斯滤波方法及基于最大后验（maximum a-posteriori）公式的优化技术，依赖本体感觉（proprioceptive sensing）实现。
- **外部环境理解**：为应对动态、不可预测的环境变化，新研究聚焦多传感器融合与机器学习，取代了传统手工规则系统，强调鲁棒性与适应性。
- **人机交互**：方法确立了上下文信息表示与记忆在理解人类意图中的重要性。

### 总结
本综述总结了人形机器人感知领域的最新进展与趋势，识别出三大应用领域：内部状态估计、外部环境估计与人机交互。文章分别讨论了各领域中不同传感器模态的应用，并评述了近期重要工作。

## Overview
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities.   Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions.   Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## Overview
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities. Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions. Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## Content
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities. Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions. Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## 개요
검토 목적: 휴머노이드 로봇 분야에서 인식은 로봇이 인간 및 주변 환경과 원활하게 상호작용할 수 있도록 하는 근본적인 역할을 하며, 이는 안전성, 효율성 및 사용자 경험 향상으로 이어집니다. 본 과학적 연구는 휴머노이드 로봇에 사용되는 다양한 인식 양식과 기술(시각, 청각, 촉각 감지 포함)을 조사하며, 내부 상태, 환경, 사물 및 인간 활동을 인식하고 이해하기 위한 최신 최첨단 접근법을 탐구합니다. 최근 발견: 내부 상태 추정은 고유 감각(proprioceptive sensing)을 활용하여 베이지안 필터링 방법과 최대 사후 확률(maximum a-posteriori) 공식에 기반한 최적화 기법을 광범위하게 사용합니다. 외부 환경 이해 영역에서는 동적이고 예측 불가능한 환경 변화에 대한 견고성과 적응성을 강조하며, 본 연구에서 논의된 새로운 연구 흐름은 수작업으로 제작된 규칙 기반 시스템과 달리 다중 센서 융합 및 머신 러닝에 크게 초점을 맞추고 있습니다. 인간-로봇 상호작용 방법은 인간의 의도를 이해하기 위한 맥락 정보 표현과 기억의 중요성을 확립했습니다. 요약: 본 리뷰는 휴머노이드 로봇 인식 분야의 최근 발전과 동향을 요약합니다. 내부 상태 추정, 외부 환경 추정, 인간-로봇 상호작용이라는 세 가지 주요 응용 영역이 식별되었습니다. 각 영역에서 다양한 센서 양식의 응용이 고려되었으며, 최근의 중요한 연구들이 논의됩니다.

## 핵심 내용
검토 목적: 휴머노이드 로봇 분야에서 인식은 로봇이 인간 및 주변 환경과 원활하게 상호작용할 수 있도록 하는 근본적인 역할을 하며, 이는 안전성, 효율성 및 사용자 경험 향상으로 이어집니다. 본 과학적 연구는 휴머노이드 로봇에 사용되는 다양한 인식 양식과 기술(시각, 청각, 촉각 감지 포함)을 조사하며, 내부 상태, 환경, 사물 및 인간 활동을 인식하고 이해하기 위한 최신 최첨단 접근법을 탐구합니다. 최근 발견: 내부 상태 추정은 고유 감각(proprioceptive sensing)을 활용하여 베이지안 필터링 방법과 최대 사후 확률(maximum a-posteriori) 공식에 기반한 최적화 기법을 광범위하게 사용합니다. 외부 환경 이해 영역에서는 동적이고 예측 불가능한 환경 변화에 대한 견고성과 적응성을 강조하며, 본 연구에서 논의된 새로운 연구 흐름은 수작업으로 제작된 규칙 기반 시스템과 달리 다중 센서 융합 및 머신 러닝에 크게 초점을 맞추고 있습니다. 인간-로봇 상호작용 방법은 인간의 의도를 이해하기 위한 맥락 정보 표현과 기억의 중요성을 확립했습니다. 요약: 본 리뷰는 휴머노이드 로봇 인식 분야의 최근 발전과 동향을 요약합니다. 내부 상태 추정, 외부 환경 추정, 인간-로봇 상호작용이라는 세 가지 주요 응용 영역이 식별되었습니다. 각 영역에서 다양한 센서 양식의 응용이 고려되었으며, 최근의 중요한 연구들이 논의됩니다.

## 参考
- http://arxiv.org/abs/2309.15616v1
