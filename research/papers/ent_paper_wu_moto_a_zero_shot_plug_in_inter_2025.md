---
$id: ent_paper_wu_moto_a_zero_shot_plug_in_inter_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
  zh: MoTo
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
summary:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
  zh: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- moto
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01658v1.
sources:
- id: src_001
  type: paper
  title: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoTo source
  url: https://doi.org/10.48550/arXiv.2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 核心内容
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 参考
- http://arxiv.org/abs/2509.01658v1

## Overview
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## Content
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 개요
모바일 조작은 로봇 공학의 핵심 과제로, 로봇이 다양한 작업과 역동적인 일상 환경에서 인간을 도울 수 있게 합니다. 기존의 모바일 조작 접근 방식은 대규모 훈련 데이터 부족으로 인해 다양한 작업과 환경에 일반화하는 데 어려움을 겪는 경우가 많습니다. 그러나 최근 조작 기반 모델의 발전은 고정 베이스 조작 작업의 광범위한 범위에서 인상적인 일반화 능력을 보여주지만, 여전히 고정된 환경으로 제한됩니다. 따라서 우리는 MoTo라는 플러그인 모듈을 설계하여, 기성 조작 기반 모델과 결합하여 모바일 조작 능력을 부여할 수 있도록 했습니다. 구체적으로, 일반화된 모바일 조작을 위해 로봇 도킹 지점을 생성하는 상호작용 인식 내비게이션 정책을 제안합니다. 제로샷 능력을 구현하기 위해, 다중 뷰 일관성을 갖춘 비전-언어 모델(VLM)을 통해 대상 객체와 로봇 팔의 지시를 따르는 상호작용 키포인트 프레임워크를 제안하며, 여기에 고정 베이스 조작 기반 모델을 적용할 수 있습니다. 또한, 모바일 베이스와 로봇 팔을 위한 모션 계획 목표를 제안하여, 두 키포인트 간의 거리를 최소화하고 궤적의 물리적 실현 가능성을 유지합니다. 이렇게 MoTo는 로봇이 고정 베이스 조작이 성공적으로 수행될 수 있는 도킹 지점으로 이동하도록 안내하며, VLM 생성과 궤적 최적화를 활용하여 모바일 조작 전문가 데이터 없이 제로샷 방식으로 모바일 조작을 달성합니다. OVMM 및 실제 환경에서의 광범위한 실험 결과는 MoTo가 추가 훈련 데이터 없이 최신 모바일 조작 방법보다 각각 2.68% 및 16.67% 더 높은 성공률을 달성함을 보여줍니다.

## 핵심 내용
모바일 조작은 로봇 공학의 핵심 과제로, 로봇이 다양한 작업과 역동적인 일상 환경에서 인간을 도울 수 있게 합니다. 기존의 모바일 조작 접근 방식은 대규모 훈련 데이터 부족으로 인해 다양한 작업과 환경에 일반화하는 데 어려움을 겪는 경우가 많습니다. 그러나 최근 조작 기반 모델의 발전은 고정 베이스 조작 작업의 광범위한 범위에서 인상적인 일반화 능력을 보여주지만, 여전히 고정된 환경으로 제한됩니다. 따라서 우리는 MoTo라는 플러그인 모듈을 설계하여, 기성 조작 기반 모델과 결합하여 모바일 조작 능력을 부여할 수 있도록 했습니다. 구체적으로, 일반화된 모바일 조작을 위해 로봇 도킹 지점을 생성하는 상호작용 인식 내비게이션 정책을 제안합니다. 제로샷 능력을 구현하기 위해, 다중 뷰 일관성을 갖춘 비전-언어 모델(VLM)을 통해 대상 객체와 로봇 팔의 지시를 따르는 상호작용 키포인트 프레임워크를 제안하며, 여기에 고정 베이스 조작 기반 모델을 적용할 수 있습니다. 또한, 모바일 베이스와 로봇 팔을 위한 모션 계획 목표를 제안하여, 두 키포인트 간의 거리를 최소화하고 궤적의 물리적 실현 가능성을 유지합니다. 이렇게 MoTo는 로봇이 고정 베이스 조작이 성공적으로 수행될 수 있는 도킹 지점으로 이동하도록 안내하며, VLM 생성과 궤적 최적화를 활용하여 모바일 조작 전문가 데이터 없이 제로샷 방식으로 모바일 조작을 달성합니다. OVMM 및 실제 환경에서의 광범위한 실험 결과는 MoTo가 추가 훈련 데이터 없이 최신 모바일 조작 방법보다 각각 2.68% 및 16.67% 더 높은 성공률을 달성함을 보여줍니다.
