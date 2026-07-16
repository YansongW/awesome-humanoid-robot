---
$id: ent_paper_vision_in_action_learning_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  zh: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations'
summary:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
  zh: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
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
- manipulation
- vision_in_action
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15666v1.
sources:
- id: src_001
  type: paper
  title: 'Vision in Action: Learning Active Perception from Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2506.15666
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 核心内容
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 参考
- http://arxiv.org/abs/2506.15666v1

## Overview
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## Content
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 개요
우리는 양팔 로봇 조작을 위한 능동 지각 시스템인 Vision in Action (ViA)을 제시합니다. ViA는 인간 시연으로부터 작업 관련 능동 지각 전략(예: 탐색, 추적, 집중)을 직접 학습합니다. 하드웨어 측면에서 ViA는 간단하면서도 효과적인 6자유도 로봇 목을 사용하여 유연하고 인간과 유사한 머리 움직임을 가능하게 합니다. 인간의 능동 지각 전략을 포착하기 위해, 우리는 로봇과 인간 조작자 간의 공유 관찰 공간을 생성하는 VR 기반 원격 조작 인터페이스를 설계했습니다. 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 완화하기 위해, 인터페이스는 중간 3D 장면 표현을 사용하여 조작자 측에서 실시간 뷰 렌더링을 가능하게 하면서 비동기적으로 로봇의 최신 관찰로 장면을 업데이트합니다. 이러한 설계 요소들은 함께 시각적 폐색을 포함하는 세 가지 복잡한 다단계 양팔 조작 작업에 대해 강력한 시각-운동 정책 학습을 가능하게 하며, 기준 시스템을 크게 능가합니다.

## 핵심 내용
우리는 양팔 로봇 조작을 위한 능동 지각 시스템인 Vision in Action (ViA)을 제시합니다. ViA는 인간 시연으로부터 작업 관련 능동 지각 전략(예: 탐색, 추적, 집중)을 직접 학습합니다. 하드웨어 측면에서 ViA는 간단하면서도 효과적인 6자유도 로봇 목을 사용하여 유연하고 인간과 유사한 머리 움직임을 가능하게 합니다. 인간의 능동 지각 전략을 포착하기 위해, 우리는 로봇과 인간 조작자 간의 공유 관찰 공간을 생성하는 VR 기반 원격 조작 인터페이스를 설계했습니다. 로봇의 물리적 움직임 지연으로 인한 VR 멀미를 완화하기 위해, 인터페이스는 중간 3D 장면 표현을 사용하여 조작자 측에서 실시간 뷰 렌더링을 가능하게 하면서 비동기적으로 로봇의 최신 관찰로 장면을 업데이트합니다. 이러한 설계 요소들은 함께 시각적 폐색을 포함하는 세 가지 복잡한 다단계 양팔 조작 작업에 대해 강력한 시각-운동 정책 학습을 가능하게 하며, 기준 시스템을 크게 능가합니다.
