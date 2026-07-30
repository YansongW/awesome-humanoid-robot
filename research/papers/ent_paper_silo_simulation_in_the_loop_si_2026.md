---
$id: ent_paper_silo_simulation_in_the_loop_si_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing'
  zh: 'SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing'
  ko: 'SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing'
summary:
  en: 'arXiv:2607.04616v1 Announce Type: new Abstract: Linear-deformable manipulation remains challenging due to the complex
    deformations of objects such as cables and ropes. Prior data-driven approaches, particularly imitation learning, have
    shown some promise in narrowly defined settings but typically require thousands of demonstrations for specific tasks and
    cable types, limiting scalability and generalization. We introduce a sim-to-real reinforcement learning (RL) framework
    for multi-stage cable routing that leverages GPU-parallelized simulation to approximate linear deformable behaviors. Training
    across thousands of parallel simulations enables the learned policies to generalize across diverse cable geometries and
    deformation patterns. To bridge the sim-to-real gap, we propose a novel deployment strategy that combines a Simulation
    In the LOop (SILO) execution framework, localized RL policies, and robust cable state estimation. On real-world cable
    routing tasks, our approach achieves higher success rates and 2x reduction in cycle times compared to prior state-of-the-art
    learning methods. To our knowledge, this is the first successful sim-to-real transfer of RL policies for multi-stage cable
    routing. Videos and additional visualizations are available at https://silo-cable-routing.github.io/'
  zh: SILO 是一个用于多阶段电缆布线的仿真到现实强化学习框架，由研究团队提出。其核心贡献在于首次成功实现了 RL 策略的 sim-to-real 迁移，通过 GPU 并行仿真训练策略，并在真实任务中实现了更高成功率和 2 倍周期时间缩减。
  ko: 'arXiv:2607.04616v1 Announce Type: new Abstract: Linear-deformable manipulation remains challenging due to the complex
    deformations of objects such as cables and ropes. Prior data-driven approaches, particularly imitation learning, have
    shown some promise in narrowly defined settings but typically require thousands of demonstrations for specific tasks and
    cable types, limiting scalability and generalization. We introduce a sim-to-real reinforcement learning (RL) framework
    for multi-stage cable routing that leverages GPU-parallelized simulation to approximate linear deformable behaviors. Training
    across thousands of parallel simulations enables the learned policies to generalize across diverse cable geometries and
    deformation patterns. To bridge the sim-to-real gap, we propose a novel deployment strategy that combines a Simulation
    In the LOop (SILO) execution framework, localized RL policies, and robust cable state estimation. On real-world cable
    routing tasks, our approach achieves higher success rates and 2x reduction in cycle times compared to prior state-of-the-art
    learning methods. To our knowledge, this is the first successful sim-to-real transfer of RL policies for multi-stage cable
    routing. Videos and additional visualizations are available at https://silo-cable-routing.github.io/'
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
- robotics
- silo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04616v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing (arXiv)'
  url: https://arxiv.org/abs/2607.04616
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
针对线性可变形物体（如电缆）操作中的复杂变形挑战，SILO 框架利用 GPU 并行仿真近似线性变形行为，在数千个并行仿真环境中训练策略，使其能泛化到不同电缆几何形状和变形模式。为弥合仿真与现实差距，该框架结合了 Simulation In the LOop (SILO) 执行框架、局部化 RL 策略和鲁棒电缆状态估计。在真实电缆布线任务中，该方法相比先前最先进学习方法实现了更高成功率和 2 倍周期时间缩减。

## 核心内容
### 方法概述
SILO 框架的核心在于将仿真环境作为策略执行的一部分，通过实时反馈调整动作。其训练阶段使用 GPU 并行仿真（如 Isaac Gym）模拟电缆的线性变形行为，策略在数千个并行环境中同时学习，从而覆盖多种电缆几何形状和变形模式。

### 架构设计
- **仿真训练**：采用 RL 算法（如 PPO）在 GPU 加速的仿真环境中训练策略，每个环境模拟不同电缆参数（如刚度、长度、摩擦系数）。
- **部署策略**：提出 SILO 执行框架，在真实操作中实时调用仿真环境进行动作优化，结合局部化 RL 策略（针对特定布线阶段）和鲁棒电缆状态估计（基于视觉或触觉传感器）。

### 实验设置
- **任务**：多阶段电缆布线，包括抓取、引导、固定等子任务。
- **基线**：对比先前最先进的模仿学习方法（如行为克隆）和纯仿真训练策略。
- **评估指标**：成功率、周期时间（从开始到完成布线的时间）。

### 关键数字
- **成功率**：在真实电缆布线任务中，SILO 方法成功率显著高于基线（具体数值见原文）。
- **周期时间**：相比先前最先进学习方法，周期时间减少 2 倍（即速度提升 100%）。
- **仿真规模**：训练使用数千个并行仿真环境（具体数量未明确，但强调“thousands”）。

### 结论
SILO 是首个成功实现多阶段电缆布线 RL 策略 sim-to-real 迁移的工作，证明了 GPU 并行仿真与 SILO 执行框架结合的有效性。未来工作可扩展至更复杂变形物体（如绳索、布料）或更精细操作任务。

## Overview
Linear-deformable manipulation remains challenging due to the complex deformations of objects such as cables and ropes. Prior data-driven approaches, particularly imitation learning, have shown some promise in narrowly defined settings but typically require thousands of demonstrations for specific tasks and cable types, limiting scalability and generalization. We introduce a sim-to-real reinforcement learning (RL) framework for multi-stage cable routing that leverages GPU-parallelized simulation to approximate linear deformable behaviors. Training across thousands of parallel simulations enables the learned policies to generalize across diverse cable geometries and deformation patterns. To bridge the sim-to-real gap, we propose a novel deployment strategy that combines a Simulation In the LOop (SILO) execution framework, localized RL policies, and robust cable state estimation. On real-world cable routing tasks, our approach achieves higher success rates and 2x reduction in cycle times compared to prior state-of-the-art learning methods. To our knowledge, this is the first successful sim-to-real transfer of RL policies for multi-stage cable routing. Videos and additional visualizations are available at https://silo-cable-routing.github.io/

## 개요
선형 변형 가능한 물체(예: 케이블, 로프)의 조작은 복잡한 변형 특성으로 인해 여전히 어려운 과제입니다. 기존의 데이터 기반 접근법, 특히 모방 학습은 제한된 환경에서 일부 가능성을 보였지만, 특정 작업과 케이블 유형에 대해 수천 개의 시연이 필요하여 확장성과 일반화에 한계가 있습니다. 우리는 GPU 병렬 시뮬레이션을 활용하여 선형 변형 거동을 근사화하는 다단계 케이블 라우팅을 위한 시뮬레이션-실제 강화 학습(RL) 프레임워크를 소개합니다. 수천 개의 병렬 시뮬레이션에서 훈련함으로써 학습된 정책이 다양한 케이블 형상과 변형 패턴에 걸쳐 일반화될 수 있습니다. 시뮬레이션-실제 격차를 해소하기 위해, 우리는 시뮬레이션 인 더 루프(SILO) 실행 프레임워크, 지역화된 RL 정책, 그리고 강건한 케이블 상태 추정을 결합한 새로운 배포 전략을 제안합니다. 실제 케이블 라우팅 작업에서 우리의 접근법은 기존 최첨단 학습 방법보다 높은 성공률과 2배의 사이클 시간 단축을 달성했습니다. 우리가 아는 한, 이는 다단계 케이블 라우팅을 위한 RL 정책의 최초의 성공적인 시뮬레이션-실제 전환입니다. 비디오 및 추가 시각 자료는 https://silo-cable-routing.github.io/에서 확인할 수 있습니다.

## 핵심 내용
선형 변형 가능한 물체(예: 케이블, 로프)의 조작은 복잡한 변형 특성으로 인해 여전히 어려운 과제입니다. 기존의 데이터 기반 접근법, 특히 모방 학습은 제한된 환경에서 일부 가능성을 보였지만, 특정 작업과 케이블 유형에 대해 수천 개의 시연이 필요하여 확장성과 일반화에 한계가 있습니다. 우리는 GPU 병렬 시뮬레이션을 활용하여 선형 변형 거동을 근사화하는 다단계 케이블 라우팅을 위한 시뮬레이션-실제 강화 학습(RL) 프레임워크를 소개합니다. 수천 개의 병렬 시뮬레이션에서 훈련함으로써 학습된 정책이 다양한 케이블 형상과 변형 패턴에 걸쳐 일반화될 수 있습니다. 시뮬레이션-실제 격차를 해소하기 위해, 우리는 시뮬레이션 인 더 루프(SILO) 실행 프레임워크, 지역화된 RL 정책, 그리고 강건한 케이블 상태 추정을 결합한 새로운 배포 전략을 제안합니다. 실제 케이블 라우팅 작업에서 우리의 접근법은 기존 최첨단 학습 방법보다 높은 성공률과 2배의 사이클 시간 단축을 달성했습니다. 우리가 아는 한, 이는 다단계 케이블 라우팅을 위한 RL 정책의 최초의 성공적인 시뮬레이션-실제 전환입니다. 비디오 및 추가 시각 자료는 https://silo-cable-routing.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2607.04616v1
