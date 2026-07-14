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

