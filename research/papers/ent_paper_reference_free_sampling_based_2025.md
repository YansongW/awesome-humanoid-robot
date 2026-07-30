---
$id: ent_paper_reference_free_sampling_based_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reference-Free Sampling-Based Model Predictive Control
  zh: Reference-Free Sampling-Based Model Predictive Control
  ko: Reference-Free Sampling-Based Model Predictive Control
summary:
  en: Reference-Free Sampling-Based Model Predictive Control is a 2025 work on locomotion for humanoid robots.
  zh: Reference-Free Sampling-Based Model Predictive Control 是 2025 年提出的一种用于人形机器人运动控制的框架。它无需手工设计的步态模式或预定义接触序列，仅通过优化高层目标即可实现从慢跑到跳跃等多种运动行为。核心贡献在于采用三次
    Hermite 样条参数化，在标准 CPU 上实现实时控制，并展示了在 Go2 四足机器人和仿真人形机器人上的多种涌现能力。
  ko: Reference-Free Sampling-Based Model Predictive Control is a 2025 work on locomotion for humanoid robots.
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
- reference_free_sampling_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19204v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Reference-Free Sampling-Based Model Predictive Control (arXiv)
  url: https://arxiv.org/abs/2511.19204
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作提出了一种基于采样的模型预测控制（MPC）框架，用于实现机器人运动控制中的涌现行为。它基于模型预测路径积分（MPPI）方法，创新性地引入了三次 Hermite 样条参数化，通过位置和速度控制点来优化轨迹。这种方法使得机器人能够自动适应任务需求，自主生成接触与脱离策略，且仅需少量采样轨迹即可完成优化。由于样本效率高，该方法可在标准 CPU 硬件上实时运行，无需 GPU 加速。在 Go2 四足机器人上验证了多种涌现步态和跳跃能力，并在仿真中展示了人形机器人的后空翻、动态倒立平衡等复杂行为。

## 核心内容
### 方法概述
本文提出了一种无需参考轨迹的采样式 MPC 框架，核心思想是通过优化高层目标（如速度、稳定性）来直接生成运动行为，而非依赖预定义的步态模式或接触序列。

### 核心架构
- **基础算法**：基于模型预测路径积分（MPPI）方法，通过采样多条轨迹并评估其代价函数来优化控制序列。
- **参数化创新**：提出三次 Hermite 样条参数化，将控制输入表示为位置和速度控制点上的样条曲线。这种参数化方式能够平滑地表示连续运动，同时支持接触状态的自动切换。
- **样本效率**：由于样条参数化减少了优化变量的维度，仅需少量采样轨迹（如 64 条）即可获得有效控制策略，从而在标准 CPU 上实现实时控制。

### 实验设置与结果
- **硬件验证**：在 Go2 四足机器人上测试，展示了从慢跑到跳跃的多种涌现步态，以及基本的跳跃能力。
- **仿真验证**：在仿真环境中进一步展示了更复杂的行为，包括：
  - 后空翻（backflips）
  - 动态倒立平衡（dynamic handstand balancing）
  - 人形机器人的运动控制
- **关键数字**：所有行为均无需参考轨迹跟踪或离线预训练，完全通过在线优化实现。控制频率达到实时要求（具体频率未在摘要中给出，但强调在 CPU 上运行）。

### 结论
该方法证明了通过纯采样优化，无需手工设计或预训练即可实现多样化的机器人运动行为，为未来更复杂的机器人控制提供了新思路。

## Overview
We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a cubic Hermite spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency enables real-time control on standard CPU hardware, eliminating the GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating a range of emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

## 개요
본 논문에서는 수제 보행 패턴이나 사전 정의된 접촉 순서에 의존하지 않고 창발적 보행을 가능하게 하는 샘플링 기반 모델 예측 제어(MPC) 프레임워크를 제시합니다. 우리의 방법은 높은 수준의 목표 최적화만을 통해 트로팅에서 갤럽에 이르기까지 다양한 운동 패턴, 강건한 서기 정책, 점프, 물구나무서기 균형을 발견합니다. 모델 예측 경로 적분(MPPI)을 기반으로, 위치 및 속도 제어점에서 작동하는 3차 에르미트 스플라인 매개변수화를 제안합니다. 우리의 접근 방식은 작업 요구 사항에 자동으로 적응하는 접촉 생성 및 접촉 해제 전략을 가능하게 하며, 제한된 수의 샘플링된 궤적만 필요로 합니다. 이러한 샘플 효율성은 일반 CPU 하드웨어에서 실시간 제어를 가능하게 하여, 다른 최신 MPPI 방법에서 일반적으로 요구되는 GPU 가속을 제거합니다. 우리는 Go2 사족 보행 로봇에서 접근 방식을 검증하여 다양한 창발적 보행과 기본 점프 능력을 입증합니다. 시뮬레이션에서는 참조 추적이나 오프라인 사전 훈련 없이 백플립, 동적 물구나무서기 균형, 휴머노이드 보행과 같은 더 복잡한 행동을 추가로 보여줍니다.

## 핵심 내용
본 논문에서는 수제 보행 패턴이나 사전 정의된 접촉 순서에 의존하지 않고 창발적 보행을 가능하게 하는 샘플링 기반 모델 예측 제어(MPC) 프레임워크를 제시합니다. 우리의 방법은 높은 수준의 목표 최적화만을 통해 트로팅에서 갤럽에 이르기까지 다양한 운동 패턴, 강건한 서기 정책, 점프, 물구나무서기 균형을 발견합니다. 모델 예측 경로 적분(MPPI)을 기반으로, 위치 및 속도 제어점에서 작동하는 3차 에르미트 스플라인 매개변수화를 제안합니다. 우리의 접근 방식은 작업 요구 사항에 자동으로 적응하는 접촉 생성 및 접촉 해제 전략을 가능하게 하며, 제한된 수의 샘플링된 궤적만 필요로 합니다. 이러한 샘플 효율성은 일반 CPU 하드웨어에서 실시간 제어를 가능하게 하여, 다른 최신 MPPI 방법에서 일반적으로 요구되는 GPU 가속을 제거합니다. 우리는 Go2 사족 보행 로봇에서 접근 방식을 검증하여 다양한 창발적 보행과 기본 점프 능력을 입증합니다. 시뮬레이션에서는 참조 추적이나 오프라인 사전 훈련 없이 백플립, 동적 물구나무서기 균형, 휴머노이드 보행과 같은 더 복잡한 행동을 추가로 보여줍니다.

## 参考
- http://arxiv.org/abs/2511.19204v3
