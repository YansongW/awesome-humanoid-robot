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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.15616v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (616 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2309.15616v1

## 개요
본综述는 인간형 로봇의 인식 기술에 초점을 맞추며, 로봇과 인간 및 환경 간의 상호작용 안전성, 효율성, 사용자 경험을 향상시키는 것을 목표로 한다. 연구는 시각, 청각, 촉각 등 다양한 인식 양식을 탐구하고, 내부 상태 추정, 외부 환경 이해, 인간-로봇 상호작용이라는 세 가지 핵심 응용 방향을 분석한다. 내부 상태 추정은 주로 베이즈 필터링과 최대 사후(maximum a-posteriori) 최적화 방법에 의존한다. 외부 환경 이해는 동적 환경 변화에 대응하기 위해 다중 센서 융합과 머신러닝을 강조한다. 인간-로봇 상호작용 방법은 인간 의도 이해에 있어 맥락 정보 표현과 기억의 중요성을 부각한다.

## 핵심 내용
### 综述 목적
인간형 로봇 인식은 인간 및 환경과의 원활한 상호작용을 위한 기반으로, 안전성, 효율성, 사용자 경험에 직접적인 영향을 미친다. 본 연구는 인간형 로봇이 채택한 다양한 인식 양식(시각, 청각, 촉각)과 알고리즘을 체계적으로 조사하며, 내부 상태, 환경, 객체, 인간 활동을 인식하는 최신 방법을 중점적으로 분석한다.

### 최근 발견
- **내부 상태 추정**: 베이즈 필터링 방법과 최대 사후(maximum a-posteriori) 공식 기반 최적화 기술이 널리 사용되며, 고유 감각(proprioceptive sensing)에 의존한다.
- **외부 환경 이해**: 동적이고 예측 불가능한 환경 변화에 대응하기 위해, 새로운 연구는 전통적인 수동 규칙 시스템을 대체하는 다중 센서 융합과 머신러닝에 초점을 맞추며, 견고성과 적응성을 강조한다.
- **인간-로봇 상호작용**: 방법은 인간 의도 이해에 있어 맥락 정보 표현과 기억의 중요성을 확립한다.

### 요약
본 综述는 인간형 로봇 인식 분야의 최신 발전과 추세를 요약하며, 내부 상태 추정, 외부 환경 추정, 인간-로봇 상호작용이라는 세 가지 응용 영역을 식별한다. 논문은 각 영역에서 다양한 센서 양식의 적용을 개별적으로 논의하고, 최근 주요 작업을 검토한다.
