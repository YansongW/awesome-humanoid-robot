---
$id: ent_paper_learning_all_terrain_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  zh: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  ko: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
summary:
  en: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
  zh: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
  ko: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_all_terrain_locomotio
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.06790v2.
sources:
- id: src_001
  type: paper
  title: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  url: https://arxiv.org/abs/2606.06790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc

## 核心内容
This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc

## 参考
- http://arxiv.org/abs/2606.06790v2

## Overview
This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc

## Content
This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc

## 개요
본 논문은 요(yaw) 및 롤(roll) 구동을 결합하여 바퀴 재구성, 조향 및 능동적 하중 재분배를 가능하게 하는 2자유도 능동 짐벌 서스펜션(Active Gimbal Suspension)을 장착한 4륜 행성 탐사 로버 개념인 ERNEST를 제시합니다. 단일 신경망 제어기는 험난한 지형에서 목표 경로를 추종하도록 훈련되어, 이 구동식 서스펜션 시스템의 자율적 장애물 극복 능력을 완전히 활용합니다. 강화 학습 프레임워크는 고충실도 DARTS 시뮬레이션 엔진을 사용하여 개발되었으며, 이 엔진은 강체 접촉 역학과 Bekker-Wong 지반 역학을 결합하여 느슨한 토양 조건에 적응된 주행 전략의 출현을 가능하게 합니다. 이질적인 지형에서 단일 통합 제어기를 얻기 위해, 정책 통합 전략은 지형 특화 에이전트의 경험을 하나의 신경망으로 병합하여 명시적인 지형 분류 및 제어기 전환의 필요성을 제거합니다. 결과 제어기는 희소 스테레오 기반 지형 고도, 섀시 자세, 관절 상태 및 힘-토크 측정을 포함한 고유 감각 및 외부 감각 피드백의 조합으로 작동합니다. 물리적 로버로의 제로샷 전환은 도메인 무작위화, 센서 노이즈 주입 및 모델-실제 시스템 식별을 통해 달성됩니다. 실험 결과는 암석 지대, Bickler 트랩(범프 장애물), 바퀴 높이 단차, 모래 물결 및 모래 경사면의 자율적 주행을 입증합니다. 20° 모래 경사면에서 학습된 제어기는 추가 구동에도 불구하고 건조 모래에서 운송 비용을 37% 절감하며, 수동 서스펜션이 완전히 움직이지 못하는 습윤 모래에서 우수한 성능을 달성합니다. 본 논문의 동반 비디오는 https://youtu.be/d684P5a3xMc 에서 확인할 수 있습니다.

## 핵심 내용
본 논문은 요(yaw) 및 롤(roll) 구동을 결합하여 바퀴 재구성, 조향 및 능동적 하중 재분배를 가능하게 하는 2자유도 능동 짐벌 서스펜션(Active Gimbal Suspension)을 장착한 4륜 행성 탐사 로버 개념인 ERNEST를 제시합니다. 단일 신경망 제어기는 험난한 지형에서 목표 경로를 추종하도록 훈련되어, 이 구동식 서스펜션 시스템의 자율적 장애물 극복 능력을 완전히 활용합니다. 강화 학습 프레임워크는 고충실도 DARTS 시뮬레이션 엔진을 사용하여 개발되었으며, 이 엔진은 강체 접촉 역학과 Bekker-Wong 지반 역학을 결합하여 느슨한 토양 조건에 적응된 주행 전략의 출현을 가능하게 합니다. 이질적인 지형에서 단일 통합 제어기를 얻기 위해, 정책 통합 전략은 지형 특화 에이전트의 경험을 하나의 신경망으로 병합하여 명시적인 지형 분류 및 제어기 전환의 필요성을 제거합니다. 결과 제어기는 희소 스테레오 기반 지형 고도, 섀시 자세, 관절 상태 및 힘-토크 측정을 포함한 고유 감각 및 외부 감각 피드백의 조합으로 작동합니다. 물리적 로버로의 제로샷 전환은 도메인 무작위화, 센서 노이즈 주입 및 모델-실제 시스템 식별을 통해 달성됩니다. 실험 결과는 암석 지대, Bickler 트랩(범프 장애물), 바퀴 높이 단차, 모래 물결 및 모래 경사면의 자율적 주행을 입증합니다. 20° 모래 경사면에서 학습된 제어기는 추가 구동에도 불구하고 건조 모래에서 운송 비용을 37% 절감하며, 수동 서스펜션이 완전히 움직이지 못하는 습윤 모래에서 우수한 성능을 달성합니다. 본 논문의 동반 비디오는 https://youtu.be/d684P5a3xMc 에서 확인할 수 있습니다.
