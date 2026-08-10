---
$id: ent_paper_autoodom_learning_auto_regress_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  zh: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
summary:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
  zh: AutoOdom 是 2025 年提出的一种用于足式机器人（特别是人形机器人）的自回归本体里程计系统。其核心贡献在于通过两阶段训练范式（大规模仿真预训练 + 少量真实数据自回归增强）有效弥合仿真到现实的差距，在 Booster T1
    人形机器人上相比 Legolas 基线在绝对轨迹误差上提升 57.2%。
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autoodom
- humanoid
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18857v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (862 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2511.18857
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对 GPS 拒止和视觉退化环境中传统视觉里程计失效的问题，现有本体里程计方法（解析滤波、混合学习-滤波、纯学习方法）分别受限于建模不确定性、仿真到现实迁移困难及数据需求大等瓶颈。AutoOdom 提出一种创新的两阶段训练策略：第一阶段利用大规模仿真数据学习足式运动中的复杂非线性动力学与快速变化的接触状态；第二阶段通过少量真实数据引入自回归增强机制，使模型从自身预测中学习以提升对传感器噪声的鲁棒性。在 Booster T1 人形机器人上的实验表明，AutoOdom 在所有评估指标上显著超越现有最优方法，消融研究还揭示了关于 IMU 加速度数据选择的反直觉发现。

## 核心内容
### 方法架构
AutoOdom 的核心是一个自回归本体里程计系统，其训练分为两个阶段：
- **Stage 1（仿真预训练）**：在大规模仿真数据上训练，学习足式运动中的非线性动力学与快速变化的接触状态。
- **Stage 2（自回归增强）**：使用少量真实世界数据，让模型从自身预测中学习，从而对传感器噪声产生抵抗力，有效弥合仿真到现实的差距。

### 实验设置
- **平台**：Booster T1 人形机器人
- **基线**：Legolas（当前最优方法）
- **评估指标**：绝对轨迹误差（ATE）、Umeyama 对齐误差、相对位姿误差（RPE）

### 关键结果
- **绝对轨迹误差**：相比 Legolas 基线提升 **57.2%**
- **Umeyama 对齐误差**：提升 **59.2%**
- **相对位姿误差**：提升 **36.2%**

### 消融研究
- **传感器模态选择**：揭示了关于 IMU 加速度数据的反直觉发现，验证了系统设计选择的合理性。
- **时序建模**：验证了自回归机制在动态环境中的鲁棒性优势。

### 结论
AutoOdom 通过两阶段自回归训练范式，在无需大量真实数据的前提下，显著提升了足式机器人在挑战性运动场景中的本体里程计精度与鲁棒性。

## Overview
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 参考
- http://arxiv.org/abs/2511.18857v1

## 개요
GPS 거부 및 시각 퇴화 환경에서 기존 시각 오도메트리가 실패하는 문제에 대해, 기존의 본체 오도메트리 방법(해석적 필터링, 하이브리드 학습-필터링, 순수 학습 방법)은 각각 모델링 불확실성, 시뮬레이션-실제 전이의 어려움, 대규모 데이터 요구 등의 병목에 제한되어 있습니다. AutoOdom은 혁신적인 2단계 훈련 전략을 제안합니다: 첫 번째 단계에서는 대규모 시뮬레이션 데이터를 활용하여 보행 운동에서의 복잡한 비선형 동역학과 빠르게 변화하는 접촉 상태를 학습합니다; 두 번째 단계에서는 소량의 실제 데이터를 통해 자기회귀 강화 메커니즘을 도입하여 모델이 자체 예측에서 학습함으로써 센서 노이즈에 대한 강건성을 향상시킵니다. Booster T1 휴머노이드 로봇에서의 실험은 AutoOdom이 모든 평가 지표에서 기존 최적 방법을 크게 능가함을 보여주며, 절제 연구는 IMU 가속도 데이터 선택에 관한 반직관적 발견을 밝혀냈습니다.

## 핵심 내용
### 방법 아키텍처
AutoOdom의 핵심은 자기회귀 본체 오도메트리 시스템으로, 훈련은 두 단계로 나뉩니다:
- **Stage 1 (시뮬레이션 사전 훈련)**: 대규모 시뮬레이션 데이터에서 훈련하여 보행 운동의 비선형 동역학과 빠르게 변화하는 접촉 상태를 학습합니다.
- **Stage 2 (자기회귀 강화)**: 소량의 실제 세계 데이터를 사용하여 모델이 자체 예측에서 학습하도록 하여 센서 노이즈에 대한 저항력을 갖추고, 시뮬레이션-실제 격차를 효과적으로 메웁니다.

### 실험 설정
- **플랫폼**: Booster T1 휴머노이드 로봇
- **기준선**: Legolas (현재 최적 방법)
- **평가 지표**: 절대 궤적 오차(ATE), Umeyama 정렬 오차, 상대 자세 오차(RPE)

### 핵심 결과
- **절대 궤적 오차**: Legolas 기준선 대비 **57.2%** 향상
- **Umeyama 정렬 오차**: **59.2%** 향상
- **상대 자세 오차**: **36.2%** 향상

### 절제 연구
- **센서 모달리티 선택**: IMU 가속도 데이터에 관한 반직관적 발견을 밝혀내며 시스템 설계 선택의 타당성을 검증합니다.
- **시계열 모델링**: 동적 환경에서 자기회귀 메커니즘의 강건성 이점을 검증합니다.

### 결론
AutoOdom은 2단계 자기회귀 훈련 패러다임을 통해 대량의 실제 데이터 없이도 보행 로봇의 도전적인 운동 시나리오에서 본체 오도메트리 정확도와 강건성을 크게 향상시킵니다.
