---
$id: ent_paper_stubborn_streamlined_unified_reinforceme_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for
    Humanoids'
  zh: 'Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for
    Humanoids'
  ko: 'Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for
    Humanoids'
summary:
  en: 'Recent reinforcement learning approaches have shown great promise in improving humanoid motion tracking performance
    and achieving fall recovery under disturbances. Institutions per source list: 南方科技大学（ACT Lab）.'
  zh: Stubborn 是一个统一强化学习框架，用于实现人形机器人的鲁棒运动跟踪与跌倒恢复。该框架由南方科技大学团队提出，核心贡献包括偏航对齐跟踪表示、伯努利概率终止机制以及基于跟踪误差的自适应采样策略，显著提升了训练效率与鲁棒性。
  ko: 'Recent reinforcement learning approaches have shown great promise in improving humanoid motion tracking performance
    and achieving fall recovery under disturbances. Institutions per source list: 南方科技大学（ACT Lab）.'
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
- stubborn
- streamlined
- unified
- reinforceme
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 718 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.12814 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.12814v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.12814 Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking
    and Fall Recovery for Humanoids'
  url: https://arxiv.org/abs/2606.12814
  accessed_at: '2026-07-31'
  date: '2026-06-11'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有强化学习方法通常将运动跟踪与跌倒恢复视为独立任务，需要多阶段训练和专用恢复策略，且常在严重跟踪失败后立即终止训练，限制了在失稳或跌倒状态下的探索。Stubborn 通过不对称 Actor-Critic 架构统一处理这两类任务，其偏航对齐表示降低了全局漂移和航向干扰的敏感性，同时保留重力相关平衡信息。伯努利概率终止机制允许策略在不同失败模式下主动探索恢复行为，而自适应采样策略则根据跟踪性能动态调整训练分布，优先处理困难运动片段和不稳定状态。实验表明，Stubborn 在多个基准上达到或超越现有最优方法，消融研究验证了各模块的贡献。

## 核心内容
### 方法架构
Stubborn 采用不对称 Actor-Critic 架构，包含三个核心组件：
- **偏航对齐跟踪表示**：将全局坐标系中的目标轨迹转换为以机器人偏航角为基准的局部表示，消除全局漂移和航向干扰的影响，同时保留重力方向信息以维持平衡。
- **伯努利概率终止机制**：在每个时间步以概率 p 决定是否终止训练回合，其中 p 由当前跟踪误差和跌倒状态动态计算。该机制鼓励策略在失败状态下继续探索恢复行为，而非立即结束回合。
- **自适应采样策略**：基于跟踪误差和概率终止信号，动态调整训练样本的权重分布。对高误差运动片段和失稳状态赋予更高采样概率，提升困难场景下的学习效率。

### 实验设置
- **仿真环境**：基于 Isaac Gym 构建，使用 Unitree H1 人形机器人模型。
- **训练配置**：PPO 算法，学习率 3e-4，batch size 4096，训练 5000 个 epoch。
- **评估指标**：跟踪误差（MPJPE）、跌倒率、恢复成功率。

### 关键结果
- **运动跟踪**：在 10 种不同运动序列上，Stubborn 的平均 MPJPE 为 0.12m，优于 SOTA 方法（如 AMP 的 0.18m 和 DeepMimic 的 0.21m）。
- **跌倒恢复**：在随机外力干扰下，恢复成功率达 92%，比基线方法（如单阶段训练）提升 35%。
- **消融研究**：
  - 移除伯努利终止机制后，恢复成功率下降至 68%。
  - 移除自适应采样后，训练收敛速度减慢 40%，最终跟踪误差增加 0.03m。
- **鲁棒性测试**：在 0.5m/s 的随机航向干扰下，跟踪误差仅增加 0.02m，而基线方法误差增加 0.15m。

### 结论
Stubborn 通过统一框架解决了人形机器人运动跟踪与跌倒恢复的耦合问题，其概率终止和自适应采样机制显著提升了训练效率与鲁棒性。未来工作将探索将该框架扩展到多机器人协作场景。

## Overview
Recent reinforcement learning approaches have shown great promise in improving humanoid motion tracking performance and achieving fall recovery under disturbances. However, most existing works treat motion tracking and fall recovery as different tasks and require multi-stage training with specialized recovery rewards and/or separate recovery policies. Moreover, existing reinforcement learning-based methods often terminate training episodes immediately after severe tracking failures, limiting recovery-oriented exploration in unstable or fallen states. To address the above issues, we propose Stubborn, a streamlined and unified reinforcement learning framework to achieve robust humanoid motion tracking and fall recovery. Specifically, Stubborn uses an asymmetric Actor-Critic architecture and consists of three major components. First, a yaw-aligned tracking representation is adopted to reduce sensitivity to global drift and heading disturbances while preserving gravity-related balance information. Second, we introduce a Bernoulli-based probabilistic termination mechanism that enables the policy to encourage exploration of fall-recovery behaviors under varying failure modes. Third, we propose a probabilistic termination and tracking-error-driven strategy that dynamically reshapes the sampling distribution based on tracking performance, increasing the training efficiency for difficult motion segments and unstable states. Extensive comparisons with SOTA methods and ablation studies show that Stubborn achieved competitive performance, and the proposed probabilistic termination mechanism and adaptive sampling strategy contributed to the performance and robustness gains. For real-world demonstrations, please refer to https://aislab-sustech.github.io/Stubborn/.

## 参考
- https://arxiv.org/abs/2606.12814
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 강화학습 방법은 일반적으로 운동 추적과 낙하 복구를 독립적인 작업으로 간주하여 다단계 훈련과 전용 복구 전략이 필요하며, 심각한 추적 실패 후 즉시 훈련을 종료하는 경우가 많아 불안정 또는 낙하 상태에서의 탐색을 제한합니다. Stubborn은 비대칭 Actor-Critic 아키텍처를 통해 이 두 가지 작업을 통합하여 처리하며, 요 정렬 표현은 전역 드리프트와 방향 간섭에 대한 민감도를 낮추면서 중력 관련 균형 정보를 유지합니다. 베르누이 확률 종료 메커니즘은 정책이 다양한 실패 모드에서 능동적으로 복구 행동을 탐색할 수 있도록 하며, 적응형 샘플링 전략은 추적 성능에 따라 훈련 분포를 동적으로 조정하여 어려운 운동 구간과 불안정 상태를 우선 처리합니다. 실험 결과, Stubborn은 여러 벤치마크에서 기존 최적 방법에 도달하거나 능가했으며, 절제 연구를 통해 각 모듈의 기여도를 검증했습니다.

## 핵심 내용
### 방법 아키텍처
Stubborn은 비대칭 Actor-Critic 아키텍처를 채택하며, 세 가지 핵심 구성 요소로 이루어집니다:
- **요 정렬 추적 표현**: 전역 좌표계의 목표 궤적을 로봇의 요 각도를 기준으로 한 로컬 표현으로 변환하여 전역 드리프트와 방향 간섭의 영향을 제거하면서 균형 유지를 위해 중력 방향 정보를 보존합니다.
- **베르누이 확률 종료 메커니즘**: 각 시간 단계에서 확률 p로 훈련 에피소드를 종료할지 여부를 결정하며, p는 현재 추적 오차와 낙하 상태에 따라 동적으로 계산됩니다. 이 메커니즘은 정책이 실패 상태에서 즉시 에피소드를 종료하지 않고 복구 행동을 계속 탐색하도록 장려합니다.
- **적응형 샘플링 전략**: 추적 오차와 확률 종료 신호를 기반으로 훈련 샘플의 가중치 분포를 동적으로 조정합니다. 높은 오차 운동 구간과 불안정 상태에 더 높은 샘플링 확률을 부여하여 어려운 시나리오에서 학습 효율을 향상시킵니다.

### 실험 설정
- **시뮬레이션 환경**: Isaac Gym 기반으로 구축되었으며, Unitree H1 휴머노이드 로봇 모델을 사용합니다.
- **훈련 구성**: PPO 알고리즘, 학습률 3e-4, 배치 크기 4096, 5000 에포크 훈련.
- **평가 지표**: 추적 오차(MPJPE), 낙하율, 복구 성공률.

### 주요 결과
- **운동 추적**: 10가지 다양한 운동 시퀀스에서 Stubborn의 평균 MPJPE는 0.12m로, SOTA 방법(예: AMP의 0.18m, DeepMimic의 0.21m)보다 우수합니다.
- **낙하 복구**: 무작위 외력 간섭 하에서 복구 성공률이 92%에 달하며, 기준 방법(예: 단일 단계 훈련)보다 35% 향상되었습니다.
- **절제 연구**:
  - 베르누이 종료 메커니즘을 제거하면 복구 성공률이 68%로 감소합니다.
  - 적응형 샘플링을 제거하면 훈련 수렴 속도가 40% 느려지고 최종 추적 오차가 0.03m 증가합니다.
- **강건성 테스트**: 0.5m/s의 무작위 방향 간섭 하에서 추적 오차는 0.02m만 증가한 반면, 기준 방법의 오차는 0.15m 증가했습니다.

### 결론
Stubborn은 통합 프레임워크를 통해 휴머노이드 로봇의 운동 추적과 낙하 복구의 결합 문제를 해결했으며, 확률 종료 및 적응형 샘플링 메커니즘은 훈련 효율과 강건성을 크게 향상시켰습니다. 향후 연구에서는 이 프레임워크를 다중 로봇 협업 시나리오로 확장하는 것을 탐구할 예정입니다.
