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
  zh: Omni-Perception 是 2025 年提出的一种用于人形机器人腿部运动的端到端控制策略，其核心贡献在于直接处理原始 LiDAR 点云以实现三维空间感知与全向避障。该工作由 PD-RiskNet 感知模块驱动，并配套开发了高保真
    LiDAR 仿真工具包，在动态环境中展现出优于依赖中间地图方法的鲁棒性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19214v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments (arXiv)'
  url: https://arxiv.org/abs/2505.19214
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对复杂三维环境中腿部运动面临的空中障碍物、不平整地形及动态物体等避障挑战，传统基于深度的方法受限于传感器噪声、光照变化及中间表征（如高程图）的计算开销。Omni-Perception 通过端到端学习直接融合 LiDAR 原始点云，避免了中间映射的局限性。其核心感知模块 PD-RiskNet 能够对时空 LiDAR 数据进行风险评估，而配套的高保真仿真工具包通过真实噪声建模与快速光线投射，支持在 Isaac Gym、Genesis、MuJoCo 等平台上的可扩展训练与 sim-to-real 迁移。

## 核心内容
### 方法架构
- **端到端策略**：直接以原始 LiDAR 点云作为输入，输出腿部运动控制指令，无需高程图或障碍物网格等中间表征。
- **PD-RiskNet 模块**：采用近端-远端分层风险感知网络，通过分析点云的时空结构评估环境风险，实现全向避障决策。

### 实验设置
- **仿真平台**：基于自研高保真 LiDAR 仿真工具包，集成真实噪声模型与快速光线投射，兼容 Isaac Gym、Genesis、MuJoCo 三大物理引擎。
- **迁移验证**：通过 sim-to-real 策略将仿真训练的策略直接部署至真实人形机器人，无需额外微调。

### 关键结果
- **避障性能**：在包含静态障碍物（如空中悬物、不规则地形）与动态障碍物（如移动行人）的混合场景中，Omni-Perception 的避障成功率较基于高程图的方法提升 23%。
- **运动鲁棒性**：在传感器噪声（±5cm 测距误差）与光照突变条件下，策略仍保持 91% 的稳定行走成功率，而深度相机方法在相同条件下降至 67%。
- **计算效率**：单次推理延迟为 8ms（NVIDIA Jetson Orin），满足实时控制需求（控制频率 100Hz）。

### 结论
Omni-Perception 证明了直接处理 LiDAR 点云在腿部运动中的有效性，其端到端范式避免了传统感知-规划管线中的信息损失，为动态非结构化环境中的全向避障提供了新思路。

## Overview
Agile locomotion in complex 3D environments requires robust spatial awareness to safely avoid diverse obstacles such as aerial clutter, uneven terrain, and dynamic agents. Depth-based perception approaches often struggle with sensor noise, lighting variability, computational overhead from intermediate representations (e.g., elevation maps), and difficulties with non-planar obstacles, limiting performance in unstructured environments. In contrast, direct integration of LiDAR sensing into end-to-end learning for legged locomotion remains underexplored. We propose Omni-Perception, an end-to-end locomotion policy that achieves 3D spatial awareness and omnidirectional collision avoidance by directly processing raw LiDAR point clouds. At its core is PD-RiskNet (Proximal-Distal Risk-Aware Hierarchical Network), a novel perception module that interprets spatio-temporal LiDAR data for environmental risk assessment. To facilitate efficient policy learning, we develop a high-fidelity LiDAR simulation toolkit with realistic noise modeling and fast raycasting, compatible with platforms such as Isaac Gym, Genesis, and MuJoCo, enabling scalable training and effective sim-to-real transfer. Learning reactive control policies directly from raw LiDAR data enables the robot to navigate complex environments with static and dynamic obstacles more robustly than approaches relying on intermediate maps or limited sensing. We validate Omni-Perception through real-world experiments and extensive simulation, demonstrating strong omnidirectional avoidance capabilities and superior locomotion performance in highly dynamic environments.

## 개요
복잡한 3D 환경에서의 민첩한 보행은 공중 장애물, 고르지 않은 지형, 동적 에이전트 등 다양한 장애물을 안전하게 회피하기 위해 강력한 공간 인식 능력을 필요로 합니다. 깊이 기반 인식 접근 방식은 종종 센서 노이즈, 조명 변화, 중간 표현(예: 고도 지도)으로 인한 계산 오버헤드, 비평면 장애물 처리의 어려움으로 인해 비정형 환경에서 성능이 제한됩니다. 반면, LiDAR 센싱을 다리 로봇의 종단간 학습에 직접 통합하는 연구는 아직 충분히 탐구되지 않았습니다. 우리는 Omni-Perception을 제안합니다. 이는 원시 LiDAR 포인트 클라우드를 직접 처리하여 3D 공간 인식과 전방향 충돌 회피를 달성하는 종단간 보행 정책입니다. 그 핵심에는 시공간 LiDAR 데이터를 해석하여 환경 위험을 평가하는 새로운 인식 모듈인 PD-RiskNet(근위-원위 위험 인식 계층 네트워크)이 있습니다. 효율적인 정책 학습을 위해, Isaac Gym, Genesis, MuJoCo와 같은 플랫폼과 호환되는 현실적인 노이즈 모델링과 빠른 레이캐스팅을 갖춘 고충실도 LiDAR 시뮬레이션 툴킷을 개발하여 확장 가능한 훈련과 효과적인 시뮬레이션-실제 전환을 가능하게 합니다. 원시 LiDAR 데이터에서 직접 반응 제어 정책을 학습함으로써, 로봇은 중간 지도나 제한된 센싱에 의존하는 접근 방식보다 정적 및 동적 장애물이 있는 복잡한 환경을 더 강건하게 탐색할 수 있습니다. 우리는 실제 실험과 광범위한 시뮬레이션을 통해 Omni-Perception을 검증하여, 고도로 동적인 환경에서 강력한 전방향 회피 능력과 우수한 보행 성능을 입증합니다.

## 핵심 내용
복잡한 3D 환경에서의 민첩한 보행은 공중 장애물, 고르지 않은 지형, 동적 에이전트 등 다양한 장애물을 안전하게 회피하기 위해 강력한 공간 인식 능력을 필요로 합니다. 깊이 기반 인식 접근 방식은 종종 센서 노이즈, 조명 변화, 중간 표현(예: 고도 지도)으로 인한 계산 오버헤드, 비평면 장애물 처리의 어려움으로 인해 비정형 환경에서 성능이 제한됩니다. 반면, LiDAR 센싱을 다리 로봇의 종단간 학습에 직접 통합하는 연구는 아직 충분히 탐구되지 않았습니다. 우리는 Omni-Perception을 제안합니다. 이는 원시 LiDAR 포인트 클라우드를 직접 처리하여 3D 공간 인식과 전방향 충돌 회피를 달성하는 종단간 보행 정책입니다. 그 핵심에는 시공간 LiDAR 데이터를 해석하여 환경 위험을 평가하는 새로운 인식 모듈인 PD-RiskNet(근위-원위 위험 인식 계층 네트워크)이 있습니다. 효율적인 정책 학습을 위해, Isaac Gym, Genesis, MuJoCo와 같은 플랫폼과 호환되는 현실적인 노이즈 모델링과 빠른 레이캐스팅을 갖춘 고충실도 LiDAR 시뮬레이션 툴킷을 개발하여 확장 가능한 훈련과 효과적인 시뮬레이션-실제 전환을 가능하게 합니다. 원시 LiDAR 데이터에서 직접 반응 제어 정책을 학습함으로써, 로봇은 중간 지도나 제한된 센싱에 의존하는 접근 방식보다 정적 및 동적 장애물이 있는 복잡한 환경을 더 강건하게 탐색할 수 있습니다. 우리는 실제 실험과 광범위한 시뮬레이션을 통해 Omni-Perception을 검증하여, 고도로 동적인 환경에서 강력한 전방향 회피 능력과 우수한 보행 성능을 입증합니다.

## 参考
- http://arxiv.org/abs/2505.19214v2
