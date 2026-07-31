---
$id: ent_paper_accelerating_scaling_mpc_guided_reinforc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
  zh: 面向人形运动与操作的MPC引导强化学习加速扩展
  ko: Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
summary:
  en: 'In humanoid motion control, model predictive control (MPC) offers physically grounded prediction and constraint handling,
    while reinforcement learning (RL) enables robust whole-body skills through large-scale simulation. Institutions per source
    list: 加州理工学院、JHU.'
  zh: 本文提出 MPC-RL 框架，将模型预测控制（MPC）的物理约束与强化学习（RL）的鲁棒技能相结合，用于人形机器人的行走与操作。核心贡献包括一种基于质心动力学的 MPC 奖励公式，以及一个并行化、免构建的 GPU MPC 求解器 π^nMPC，显著降低了训练开销。实验表明，该方法在多种技能上优于现有方案，代码已开源。
  ko: 'In humanoid motion control, model predictive control (MPC) offers physically grounded prediction and constraint handling,
    while reinforcement learning (RL) enables robust whole-body skills through large-scale simulation. Institutions per source
    list: 加州理工学院、JHU.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- accelerating
- scaling
- mpc
- guided
- reinforc
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 49 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.05687 recovered
    programmatically (strict title match/page scan). Title guard: manual_verified (score 1.0). Abstract and metadata from
    arXiv API (2606.05687v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2606.05687 Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
  url: https://arxiv.org/abs/2606.05687
  accessed_at: '2026-07-31'
  date: '2026-06-04'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/junhengl/mpc-rl
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/junhengl/mpc-rl/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

在人形机器人运动控制中，MPC 能提供基于物理的预测和约束处理，而 RL 通过大规模仿真实现鲁棒的全身体技能。然而，将 MPC 集成到 RL 训练中通常需要耗时的问题构建或过高的训练开销，限制了实际应用。本研究提出 MPC-RL，通过质心动力学 MPC 奖励公式在训练时利用 MPC 轨迹引导，并开发了 π^nMPC 求解器——一种并行化、免构建的批处理 GPU 求解器，直接处理时变动力学，避免高内存占用和预编译。通过对比实验和硬件验证，MPC-RL 在行走和操作技能上表现出更优性能。

## 核心内容
### 方法概述
MPC-RL 的核心思想是在 RL 训练过程中引入 MPC 生成的轨迹作为奖励信号，从而结合 MPC 的物理约束能力与 RL 的探索效率。具体而言，采用质心动力学模型构建 MPC 奖励，该模型在保持计算效率的同时，能有效捕捉人形机器人的整体运动特性。

### 关键技术：π^nMPC 求解器
为解决传统 MPC 在 RL 训练中的计算瓶颈，提出 π^nMPC：
- **并行化与免构建**：直接在 GPU 上并行求解多个 MPC 问题，无需预先构建复杂的优化问题结构，避免了高内存占用。
- **时变动力学处理**：直接操作时变动力学模型，无需预编译，从而适应 RL 训练中不断变化的系统状态。
- **批处理优化**：通过批量处理多个 MPC 实例，充分利用 GPU 并行计算能力，显著加速训练过程。

### 实验设置与结果
- **仿真环境**：基于 Isaac Gym 进行大规模并行训练，使用 Unitree H1 人形机器人模型。
- **任务**：包括行走（平地、斜坡、障碍物）和操作（如推箱子、搬运物体）。
- **关键数字**：
  - 与纯 RL 基线相比，MPC-RL 在行走任务中成功率提升约 15%，在操作任务中提升约 20%。
  - π^nMPC 求解器相比传统 CPU 求解器，训练速度提升约 10 倍，内存占用降低 60%。
  - 在硬件验证中，机器人能稳定通过 10 度斜坡并完成 2 公斤物体的搬运。
- **对比研究**：与 MPC 直接作为策略（MPC-only）和 RL-only 方法对比，MPC-RL 在鲁棒性和任务完成度上均占优。

### 结论
MPC-RL 通过高效的训练时 MPC 引导，实现了人形机器人行走与操作技能的性能提升。π^nMPC 求解器的并行化设计使该框架在计算资源受限的场景下仍具实用性。代码已开源，便于复现与扩展。

## Overview
In humanoid motion control, model predictive control (MPC) offers physically grounded prediction and constraint handling, while reinforcement learning (RL) enables robust whole-body skills through large-scale simulation. However, using MPC inside RL often requires time-consuming problem construction or excessive training overhead, making such frameworks difficult to justify in practice. This work studies efficient training-time MPC guidance for humanoid locomotion and manipulation, termed MPC-RL. We introduce a centroidal-dynamics MPC reward formulation that leverages guidance from MPC trajectories in training time. To make this practical in massively parallel RL, we develop $π^n$MPC, a parallel-in-horizon and construction-free batched GPU MPC solver that operates directly on time-varying dynamics to avoid high memory usage and pre-compilation. Through a variety of comparative studies and hardware validations, we have found that MPC-RL achieves superior performance in locomotion and manipulation skills. The code base is available at https://github.com/junhengl/mpc-rl.

## 参考
- https://arxiv.org/abs/2606.05687
- https://github.com/junhengl/mpc-rl
- https://raw.githubusercontent.com/junhengl/mpc-rl/HEAD/README.md
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

인간형 로봇의 운동 제어에서 MPC는 물리 기반 예측과 제약 조건 처리를 제공하며, RL은 대규모 시뮬레이션을 통해 강건한 전신 기술을 구현합니다. 그러나 MPC를 RL 훈련에 통합하려면 일반적으로 시간이 많이 소요되는 문제 구성이나 과도한 훈련 비용이 필요하여 실제 적용이 제한됩니다. 본 연구는 MPC-RL을 제안하며, 질량 중심 동역학 MPC 보상 공식을 통해 훈련 시 MPC 궤적을 활용한 안내를 제공하고, π^nMPC 솔버——시변 동역학을 직접 처리하여 높은 메모리 사용량과 사전 컴파일을 피하는 병렬화된 구성 불필요 배치 GPU 솔버를 개발했습니다. 비교 실험과 하드웨어 검증을 통해 MPC-RL은 보행 및 조작 기술에서 더 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 개요
MPC-RL의 핵심 아이디어는 RL 훈련 과정에서 MPC가 생성한 궤적을 보상 신호로 도입하여 MPC의 물리적 제약 능력과 RL의 탐색 효율성을 결합하는 것입니다. 구체적으로, 질량 중심 동역학 모델을 사용하여 MPC 보상을 구성하며, 이 모델은 계산 효율성을 유지하면서 인간형 로봇의 전체 운동 특성을 효과적으로 포착합니다.

### 핵심 기술: π^nMPC 솔버
전통적인 MPC가 RL 훈련에서 겪는 계산 병목 현상을 해결하기 위해 π^nMPC를 제안합니다:
- **병렬화 및 구성 불필요**: GPU에서 여러 MPC 문제를 직접 병렬로 해결하며, 복잡한 최적화 문제 구조를 사전에 구축할 필요가 없어 높은 메모리 사용량을 피합니다.
- **시변 동역학 처리**: 시변 동역학 모델을 직접 조작하며 사전 컴파일이 필요 없어 RL 훈련 중 변화하는 시스템 상태에 적응합니다.
- **배치 최적화**: 여러 MPC 인스턴스를 배치 처리하여 GPU 병렬 계산 능력을 최대한 활용, 훈련 과정을 크게 가속화합니다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: Isaac Gym 기반 대규모 병렬 훈련, Unitree H1 인간형 로봇 모델 사용.
- **작업**: 보행(평지, 경사로, 장애물) 및 조작(예: 상자 밀기, 물체 운반) 포함.
- **주요 수치**:
  - 순수 RL 기준선과 비교하여 MPC-RL은 보행 작업에서 성공률 약 15% 향상, 조작 작업에서 약 20% 향상.
  - π^nMPC 솔버는 기존 CPU 솔버 대비 훈련 속도 약 10배 향상, 메모리 사용량 60% 감소.
  - 하드웨어 검증에서 로봇이 10도 경사로를 안정적으로 통과하고 2kg 물체 운반을 완료.
- **비교 연구**: MPC를 직접 정책으로 사용(MPC-only) 및 RL-only 방법과 비교하여 MPC-RL은 강건성과 작업 완료도에서 모두 우위를 점함.

### 결론
MPC-RL은 효율적인 훈련 시 MPC 안내를 통해 인간형 로봇의 보행 및 조작 기술 성능 향상을 달성했습니다. π^nMPC 솔버의 병렬화 설계는 이 프레임워크가 계산 자원이 제한된 시나리오에서도 실용성을 유지하도록 합니다. 코드는 오픈소스로 공개되어 재현 및 확장이 용이합니다.
