---
$id: ent_paper_humanoid_robot_acrobatics_util_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
summary:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- humanoid_robot_acrobatics_util
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.08258v1.
sources:
- id: src_001
  type: paper
  title: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics (arXiv)
  url: https://arxiv.org/abs/2508.08258
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 核心内容
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 参考
- http://arxiv.org/abs/2508.08258v1

## Overview
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## Content
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 개요
휴머노이드 로봇이 인간 수준의 곡예와 같은 고도로 역동적인 동작을 수행할 수 있는 능력을 부여하는 것은 오랜 도전 과제였습니다. 이러한 동작을 성공적으로 수행하려면 계획을 위한 궤적 최적화와 실행 중 제어 모두에서 기본 물리 법칙을 면밀히 고려해야 합니다. 이는 휴머노이드의 높은 자유도와 그에 따른 기하급수적으로 증가하는 복잡성으로 인해 특히 어려우며, 명시적 운동 방정식에 대한 계획을 다루기 어렵게 만듭니다. 일반적인 해결 방법으로는 선형화 방법과 모델 근사가 있습니다. 그러나 둘 다 실제 로봇 시스템에서 성능 저하를 초래하기 때문에 충분하지 않습니다. 본 논문은 궤적 최적화와 전신 제어로 구성된 제어 아키텍처를 제시하며, 이는 일치하는 모델 추상화에 의해 중재되어 관절 강체 모델의 축약되지 않은 운동 방정식에 기반한 제약 및 자세 동작을 포함한 곡예 동작의 실행을 가능하게 합니다. 기본 모델링 및 제어 방법에 대한 검토가 제공되며, 모델 추상화, 궤적 최적화 및 전신 제어기를 포함한 구현 세부 사항이 이어집니다. 시스템의 효과는 시뮬레이션에서 분석됩니다.

## 핵심 내용
휴머노이드 로봇이 인간 수준의 곡예와 같은 고도로 역동적인 동작을 수행할 수 있는 능력을 부여하는 것은 오랜 도전 과제였습니다. 이러한 동작을 성공적으로 수행하려면 계획을 위한 궤적 최적화와 실행 중 제어 모두에서 기본 물리 법칙을 면밀히 고려해야 합니다. 이는 휴머노이드의 높은 자유도와 그에 따른 기하급수적으로 증가하는 복잡성으로 인해 특히 어려우며, 명시적 운동 방정식에 대한 계획을 다루기 어렵게 만듭니다. 일반적인 해결 방법으로는 선형화 방법과 모델 근사가 있습니다. 그러나 둘 다 실제 로봇 시스템에서 성능 저하를 초래하기 때문에 충분하지 않습니다. 본 논문은 궤적 최적화와 전신 제어로 구성된 제어 아키텍처를 제시하며, 이는 일치하는 모델 추상화에 의해 중재되어 관절 강체 모델의 축약되지 않은 운동 방정식에 기반한 제약 및 자세 동작을 포함한 곡예 동작의 실행을 가능하게 합니다. 기본 모델링 및 제어 방법에 대한 검토가 제공되며, 모델 추상화, 궤적 최적화 및 전신 제어기를 포함한 구현 세부 사항이 이어집니다. 시스템의 효과는 시뮬레이션에서 분석됩니다.
