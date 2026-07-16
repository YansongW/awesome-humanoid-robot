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
  zh: Roychoudhury、Khorshidi、Agrawal和Bennewitz于2023年发表的一篇综述，回顾了人形机器人的感知模态与算法方法，涵盖利用本体感觉、视觉、听觉和触觉传感进行的内部状态估计、外部环境理解和人机交互。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.15616v1.
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
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities.   Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions.   Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## 核心内容
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities.   Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions.   Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## 参考
- http://arxiv.org/abs/2309.15616v1

## Overview
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities. Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions. Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## Content
Purpose of Review: The field of humanoid robotics, perception plays a fundamental role in enabling robots to interact seamlessly with humans and their surroundings, leading to improved safety, efficiency, and user experience. This scientific study investigates various perception modalities and techniques employed in humanoid robots, including visual, auditory, and tactile sensing by exploring recent state-of-the-art approaches for perceiving and understanding the internal state, the environment, objects, and human activities. Recent Findings: Internal state estimation makes extensive use of Bayesian filtering methods and optimization techniques based on maximum a-posteriori formulation by utilizing proprioceptive sensing. In the area of external environment understanding, with an emphasis on robustness and adaptability to dynamic, unforeseen environmental changes, the new slew of research discussed in this study have focused largely on multi-sensor fusion and machine learning in contrast to the use of hand-crafted, rule-based systems. Human robot interaction methods have established the importance of contextual information representation and memory for understanding human intentions. Summary: This review summarizes the recent developments and trends in the field of perception in humanoid robots. Three main areas of application are identified, namely, internal state estimation, external environment estimation, and human robot interaction. The applications of diverse sensor modalities in each of these areas are considered and recent significant works are discussed.

## 개요
검토 목적: 휴머노이드 로봇 분야에서 인식은 로봇이 인간 및 주변 환경과 원활하게 상호작용할 수 있도록 하는 근본적인 역할을 하며, 이는 안전성, 효율성 및 사용자 경험 향상으로 이어집니다. 본 과학적 연구는 휴머노이드 로봇에 사용되는 다양한 인식 양식과 기술(시각, 청각, 촉각 감지 포함)을 조사하며, 내부 상태, 환경, 사물 및 인간 활동을 인식하고 이해하기 위한 최신 최첨단 접근법을 탐구합니다. 최근 발견: 내부 상태 추정은 고유 감각(proprioceptive sensing)을 활용하여 베이지안 필터링 방법과 최대 사후 확률(maximum a-posteriori) 공식에 기반한 최적화 기법을 광범위하게 사용합니다. 외부 환경 이해 영역에서는 동적이고 예측 불가능한 환경 변화에 대한 견고성과 적응성을 강조하며, 본 연구에서 논의된 새로운 연구 흐름은 수작업으로 제작된 규칙 기반 시스템과 달리 다중 센서 융합 및 머신 러닝에 크게 초점을 맞추고 있습니다. 인간-로봇 상호작용 방법은 인간의 의도를 이해하기 위한 맥락 정보 표현과 기억의 중요성을 확립했습니다. 요약: 본 리뷰는 휴머노이드 로봇 인식 분야의 최근 발전과 동향을 요약합니다. 내부 상태 추정, 외부 환경 추정, 인간-로봇 상호작용이라는 세 가지 주요 응용 영역이 식별되었습니다. 각 영역에서 다양한 센서 양식의 응용이 고려되었으며, 최근의 중요한 연구들이 논의됩니다.

## 핵심 내용
검토 목적: 휴머노이드 로봇 분야에서 인식은 로봇이 인간 및 주변 환경과 원활하게 상호작용할 수 있도록 하는 근본적인 역할을 하며, 이는 안전성, 효율성 및 사용자 경험 향상으로 이어집니다. 본 과학적 연구는 휴머노이드 로봇에 사용되는 다양한 인식 양식과 기술(시각, 청각, 촉각 감지 포함)을 조사하며, 내부 상태, 환경, 사물 및 인간 활동을 인식하고 이해하기 위한 최신 최첨단 접근법을 탐구합니다. 최근 발견: 내부 상태 추정은 고유 감각(proprioceptive sensing)을 활용하여 베이지안 필터링 방법과 최대 사후 확률(maximum a-posteriori) 공식에 기반한 최적화 기법을 광범위하게 사용합니다. 외부 환경 이해 영역에서는 동적이고 예측 불가능한 환경 변화에 대한 견고성과 적응성을 강조하며, 본 연구에서 논의된 새로운 연구 흐름은 수작업으로 제작된 규칙 기반 시스템과 달리 다중 센서 융합 및 머신 러닝에 크게 초점을 맞추고 있습니다. 인간-로봇 상호작용 방법은 인간의 의도를 이해하기 위한 맥락 정보 표현과 기억의 중요성을 확립했습니다. 요약: 본 리뷰는 휴머노이드 로봇 인식 분야의 최근 발전과 동향을 요약합니다. 내부 상태 추정, 외부 환경 추정, 인간-로봇 상호작용이라는 세 가지 주요 응용 영역이 식별되었습니다. 각 영역에서 다양한 센서 양식의 응용이 고려되었으며, 최근의 중요한 연구들이 논의됩니다.
