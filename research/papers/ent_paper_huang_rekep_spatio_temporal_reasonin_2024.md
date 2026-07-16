---
$id: ent_paper_huang_rekep_spatio_temporal_reasonin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
  zh: ReKep
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
summary:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
  zh: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- rekep
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.01652v2.
sources:
- id: src_001
  type: paper
  title: ReKep source
  url: https://proceedings.mlr.press/v270/huang25g.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 核心内容
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 参考
- http://arxiv.org/abs/2409.01652v2

## Overview
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## Content
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 개요
로봇 조작 작업을 로봇과 환경을 연결하는 제약 조건으로 표현하는 것은 원하는 로봇 동작을 인코딩하는 유망한 방법입니다. 그러나 이러한 제약 조건을 1) 다양한 작업에 적용 가능하고, 2) 수동 레이블링이 필요 없으며, 3) 기성 솔버를 통해 실시간으로 로봇 동작을 생성할 수 있도록 최적화 가능하게 공식화하는 방법은 여전히 명확하지 않습니다. 본 연구에서는 로봇 조작에서 제약 조건을 위한 시각 기반 표현인 관계형 키포인트 제약 조건(ReKep)을 소개합니다. 구체적으로, ReKep은 환경 내 3D 키포인트 집합을 수치적 비용으로 매핑하는 Python 함수로 표현됩니다. 조작 작업을 일련의 관계형 키포인트 제약 조건으로 표현함으로써, 계층적 최적화 절차를 사용하여 SE(3)에서의 엔드 이펙터 자세 시퀀스로 표현되는 로봇 동작을 실시간 주파수의 인식-행동 루프로 해결할 수 있음을 보여줍니다. 또한, 각각의 새로운 작업에 대해 ReKep을 수동으로 지정해야 하는 필요성을 피하기 위해, 대규모 비전 모델과 비전-언어 모델을 활용하여 자유 형식의 언어 명령과 RGB-D 관측으로부터 ReKep을 생성하는 자동화된 절차를 고안했습니다. 우리는 작업별 데이터나 환경 모델 없이도 다단계, 실제 환경, 양팔, 반응형 동작을 특징으로 하는 다양한 조작 작업을 수행할 수 있는 바퀴 달린 단일 팔 플랫폼과 고정형 이중 팔 플랫폼에서의 시스템 구현을 제시합니다. 웹사이트: https://rekep-robot.github.io/.

## 핵심 내용
로봇 조작 작업을 로봇과 환경을 연결하는 제약 조건으로 표현하는 것은 원하는 로봇 동작을 인코딩하는 유망한 방법입니다. 그러나 이러한 제약 조건을 1) 다양한 작업에 적용 가능하고, 2) 수동 레이블링이 필요 없으며, 3) 기성 솔버를 통해 실시간으로 로봇 동작을 생성할 수 있도록 최적화 가능하게 공식화하는 방법은 여전히 명확하지 않습니다. 본 연구에서는 로봇 조작에서 제약 조건을 위한 시각 기반 표현인 관계형 키포인트 제약 조건(ReKep)을 소개합니다. 구체적으로, ReKep은 환경 내 3D 키포인트 집합을 수치적 비용으로 매핑하는 Python 함수로 표현됩니다. 조작 작업을 일련의 관계형 키포인트 제약 조건으로 표현함으로써, 계층적 최적화 절차를 사용하여 SE(3)에서의 엔드 이펙터 자세 시퀀스로 표현되는 로봇 동작을 실시간 주파수의 인식-행동 루프로 해결할 수 있음을 보여줍니다. 또한, 각각의 새로운 작업에 대해 ReKep을 수동으로 지정해야 하는 필요성을 피하기 위해, 대규모 비전 모델과 비전-언어 모델을 활용하여 자유 형식의 언어 명령과 RGB-D 관측으로부터 ReKep을 생성하는 자동화된 절차를 고안했습니다. 우리는 작업별 데이터나 환경 모델 없이도 다단계, 실제 환경, 양팔, 반응형 동작을 특징으로 하는 다양한 조작 작업을 수행할 수 있는 바퀴 달린 단일 팔 플랫폼과 고정형 이중 팔 플랫폼에서의 시스템 구현을 제시합니다. 웹사이트: https://rekep-robot.github.io/.
