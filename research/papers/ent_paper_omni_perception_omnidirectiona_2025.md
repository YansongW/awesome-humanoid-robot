---
$id: ent_paper_omni_perception_omnidirectiona_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
  zh: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
  ko: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments'
summary:
  en: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
  zh: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
  ko: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments is a 2025 work on
    locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- omni_perception
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19214v2.
sources:
- id: src_001
  type: paper
  title: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments (arXiv)'
  url: https://arxiv.org/abs/2505.19214
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 核心内容
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 参考
- http://arxiv.org/abs/2505.19214v2

## Overview
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## Content
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 개요
복잡한 3D 환경에서의 민첩한 보행은 공중 장애물, 고르지 않은 지형, 동적 에이전트 등 다양한 장애물을 안전하게 회피하기 위해 강력한 공간 인식 능력을 필요로 합니다. 깊이 기반 인식 접근 방식은 종종 센서 노이즈, 조명 변화, 중간 표현(예: 고도 지도)으로 인한 계산 오버헤드, 비평면 장애물 처리의 어려움으로 인해 비정형 환경에서 성능이 제한됩니다. 반면, LiDAR 센싱을 다리 로봇의 종단간 학습에 직접 통합하는 연구는 아직 충분히 탐구되지 않았습니다. 우리는 Omni-Perception을 제안합니다. 이는 원시 LiDAR 포인트 클라우드를 직접 처리하여 3D 공간 인식과 전방향 충돌 회피를 달성하는 종단간 보행 정책입니다. 그 핵심에는 시공간 LiDAR 데이터를 해석하여 환경 위험을 평가하는 새로운 인식 모듈인 PD-RiskNet(근위-원위 위험 인식 계층 네트워크)이 있습니다. 효율적인 정책 학습을 위해, Isaac Gym, Genesis, MuJoCo와 같은 플랫폼과 호환되는 현실적인 노이즈 모델링과 빠른 레이캐스팅을 갖춘 고충실도 LiDAR 시뮬레이션 툴킷을 개발하여 확장 가능한 훈련과 효과적인 시뮬레이션-실제 전환을 가능하게 합니다. 원시 LiDAR 데이터에서 직접 반응 제어 정책을 학습함으로써, 로봇은 중간 지도나 제한된 센싱에 의존하는 접근 방식보다 정적 및 동적 장애물이 있는 복잡한 환경을 더 강건하게 탐색할 수 있습니다. 우리는 실제 실험과 광범위한 시뮬레이션을 통해 Omni-Perception을 검증하여, 고도로 동적인 환경에서 강력한 전방향 회피 능력과 우수한 보행 성능을 입증합니다.

## 핵심 내용
복잡한 3D 환경에서의 민첩한 보행은 공중 장애물, 고르지 않은 지형, 동적 에이전트 등 다양한 장애물을 안전하게 회피하기 위해 강력한 공간 인식 능력을 필요로 합니다. 깊이 기반 인식 접근 방식은 종종 센서 노이즈, 조명 변화, 중간 표현(예: 고도 지도)으로 인한 계산 오버헤드, 비평면 장애물 처리의 어려움으로 인해 비정형 환경에서 성능이 제한됩니다. 반면, LiDAR 센싱을 다리 로봇의 종단간 학습에 직접 통합하는 연구는 아직 충분히 탐구되지 않았습니다. 우리는 Omni-Perception을 제안합니다. 이는 원시 LiDAR 포인트 클라우드를 직접 처리하여 3D 공간 인식과 전방향 충돌 회피를 달성하는 종단간 보행 정책입니다. 그 핵심에는 시공간 LiDAR 데이터를 해석하여 환경 위험을 평가하는 새로운 인식 모듈인 PD-RiskNet(근위-원위 위험 인식 계층 네트워크)이 있습니다. 효율적인 정책 학습을 위해, Isaac Gym, Genesis, MuJoCo와 같은 플랫폼과 호환되는 현실적인 노이즈 모델링과 빠른 레이캐스팅을 갖춘 고충실도 LiDAR 시뮬레이션 툴킷을 개발하여 확장 가능한 훈련과 효과적인 시뮬레이션-실제 전환을 가능하게 합니다. 원시 LiDAR 데이터에서 직접 반응 제어 정책을 학습함으로써, 로봇은 중간 지도나 제한된 센싱에 의존하는 접근 방식보다 정적 및 동적 장애물이 있는 복잡한 환경을 더 강건하게 탐색할 수 있습니다. 우리는 실제 실험과 광범위한 시뮬레이션을 통해 Omni-Perception을 검증하여, 고도로 동적인 환경에서 강력한 전방향 회피 능력과 우수한 보행 성능을 입증합니다.
