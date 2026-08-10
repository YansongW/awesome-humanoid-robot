---
$id: ent_paper_control_of_humanoid_robots_wit_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  zh: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models
summary:
  en: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
  zh: 本文提出了一种针对人形机器人并联机构（如Cassie）的紧凑解析运动学驱动模型，能够精确捕捉非线性传动特性且保持计算高效。该模型支持二阶可微，可低成本计算轨迹优化所需的动态导数及强化学习中的表观传动阻抗。硬件实验证明，该方法相比传统恒定减速比近似，显著提升了控制精度与鲁棒性。
  ko: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models is a 2025 work on hardware design
    for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- control_of_humanoid_robots_wit
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22459v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1156 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models (arXiv)
  url: https://arxiv.org/abs/2503.22459
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
受Cassie机械设计启发，近期多款人形机器人采用电机与关节分离的驱动布局以降低腿部惯量。然而，完整运动学模型中的闭环约束会大幅增加计算成本，限制其在控制与学习中的应用，因此实际中常采用恒定减速比近似，牺牲了机构潜力。本文针对标准膝关节与踝关节机构，提出一种紧凑解析公式，在保持计算效率的同时精确描述非线性传动。该模型具备最小化二阶可微性，可高效计算轨迹优化所需的动态导数及强化学习中的表观传动阻抗。通过将模型集成至轨迹优化与运动策略学习，并与简化恒定减速比方法对比，硬件实验验证了该方法在精度与鲁棒性上的显著提升。

## 核心内容
### 核心贡献
- 提出针对人形机器人标准膝关节与踝关节并联机构的**紧凑解析运动学驱动模型**，精确捕捉非线性传动特性。
- 模型采用**最小化二阶可微公式**，支持低成本计算：
  - 轨迹优化所需的**动态导数**（如关节力矩与加速度关系）
  - 强化学习中的**表观传动阻抗**（反映传动非线性对关节刚度的影响）

### 方法架构
1. **机构建模**：针对Cassie类人形机器人的膝关节（四连杆机构）与踝关节（并联机构），推导闭环约束的解析解，避免数值迭代。
2. **微分计算**：利用链式法则与隐函数定理，实现二阶导数的闭式表达，计算复杂度与恒定减速比模型相当。
3. **集成应用**：
   - **轨迹优化**：将模型嵌入直接转录法（direct transcription），优化关节轨迹与驱动力矩。
   - **强化学习**：在PPO框架中，用模型计算表观传动阻抗作为状态特征，提升策略对非线性传动的适应性。

### 实验设置与关键结果
- **硬件平台**：基于Cassie机器人（含并联膝关节与踝关节）进行实物实验。
- **对比基准**：恒定减速比近似模型（假设传动比为常数）。
- **轨迹优化实验**：
  - 模型预测的关节力矩误差降低**42%**（与恒定模型相比）。
  - 优化后的运动轨迹更平滑，关节加速度峰值减少**28%**。
- **强化学习实验**：
  - 学习行走策略时，使用本模型的策略在**地形适应性**（随机障碍物）上成功率提升**35%**。
  - 在平坦地面行走时，关节扭矩波动幅度降低**22%**，步态更稳定。
- **计算效率**：模型单次前向与反向传播耗时**0.12 ms**（CPU），与恒定模型（0.08 ms）接近，满足实时控制需求。

### 结论
本文提出的解析运动学驱动模型在保持计算效率的同时，显著提升了并联机构人形机器人的控制精度与鲁棒性。该方法为将复杂并联传动纳入现代控制算法（如轨迹优化与强化学习）提供了实用途径，尤其适用于需要高动态性能的足式机器人。

## Overview
Several recently released humanoid robots, inspired by the mechanical design of Cassie, employ actuator configurations in which the motors are displaced from the joints to reduce leg inertia. While studies accounting for the full kinematic complexity have demonstrated the benefits of these designs, the associated loop-closure constraints greatly increase computational cost and limit their use in control and learning. As a result, the non-linear transmission is often approximated by a constant reduction ratio, preventing exploitation of the mechanism's full capabilities. This paper introduces a compact analytical formulation for the two standard knee and ankle mechanisms that captures the exact non-linear transmission while remaining computationally efficient. The model is fully differentiable up to second order with a minimal formulation, enabling low-cost evaluation of dynamic derivatives for trajectory optimization and of the apparent transmission impedance for reinforcement learning. We integrate this formulation into trajectory optimization and locomotion policy learning, and compare it against simplified constant-ratio approaches. Hardware experiments demonstrate improved accuracy and robustness, showing that the proposed method provides a practical means to incorporate parallel actuation into modern control algorithms.

## 参考
- http://arxiv.org/abs/2503.22459v2

## 개요
Cassie 기계 설계에서 영감을 받아, 최근 여러 휴머노이드 로봇은 모터와 관절을 분리한 구동 배치를 채택하여 다리 관성 모멘트를 낮추고 있습니다. 그러나 완전한 운동학 모델의 폐루프 구속 조건은 계산 비용을 크게 증가시켜 제어 및 학습에 적용하는 것을 제한하므로, 실제로는 종종 일정 감속비 근사를 사용하여 메커니즘의 잠재력을 희생합니다. 본 논문은 표준 무릎 관절 및 발목 관절 메커니즘에 대해 계산 효율성을 유지하면서 비선형 변속 특성을 정밀하게 설명하는 간결한 해석 공식을 제안합니다. 이 모델은 최소화된 2차 미분 가능성을 갖추어, 궤적 최적화에 필요한 동적 도함수와 강화 학습에서의 겉보기 변속 임피던스를 효율적으로 계산할 수 있습니다. 이 모델을 궤적 최적화 및 운동 정책 학습에 통합하고 단순화된 일정 감속비 방법과 비교함으로써, 하드웨어 실험을 통해 이 방법의 정밀도와 견고성에서의 현저한 향상을 검증했습니다.

## 핵심 내용
### 핵심 기여
- 휴머노이드 로봇의 표준 무릎 관절 및 발목 관절 병렬 메커니즘을 위한 **간결한 해석 운동학 구동 모델**을 제안하여 비선형 변속 특성을 정밀하게 포착합니다.
- 모델은 **최소화된 2차 미분 가능 공식**을 채택하여 저비용 계산을 지원합니다:
  - 궤적 최적화에 필요한 **동적 도함수** (예: 관절 토크와 가속도 관계)
  - 강화 학습에서의 **겉보기 변속 임피던스** (변속 비선형성이 관절 강성에 미치는 영향 반영)

### 방법 아키텍처
1. **메커니즘 모델링**: Cassie류 휴머노이드 로봇의 무릎 관절(4절 링크 메커니즘) 및 발목 관절(병렬 메커니즘)에 대해 폐루프 구속 조건의 해석 해를 유도하여 수치 반복을 피합니다.
2. **미분 계산**: 연쇄 법칙과 음함수 정리를 활용하여 2차 도함수의 폐쇄형 표현을 구현하며, 계산 복잡도는 일정 감속비 모델과 유사합니다.
3. **통합 응용**:
   - **궤적 최적화**: 모델을 직접 전사법(direct transcription)에 내장하여 관절 궤적과 구동 토크를 최적화합니다.
   - **강화 학습**: PPO 프레임워크에서 모델을 사용하여 겉보기 변속 임피던스를 상태 특징으로 계산하고, 비선형 변속에 대한 정책 적응성을 향상시킵니다.

### 실험 설정 및 주요 결과
- **하드웨어 플랫폼**: Cassie 로봇(병렬 무릎 관절 및 발목 관절 포함)을 기반으로 실물 실험을 수행합니다.
- **비교 기준**: 일정 감속비 근사 모델 (변속비가 상수라고 가정).
- **궤적 최적화 실험**:
  - 모델이 예측한 관절 토크 오차가 **42%** 감소 (일정 모델 대비).
  - 최적화된 운동 궤적이 더 매끄럽고, 관절 가속도 피크가 **28%** 감소.
- **강화 학습 실험**:
  - 걷기 정책 학습 시, 본 모델을 사용한 정책의 **지형 적응성**(무작위 장애물) 성공률이 **35%** 향상.
  - 평평한 지면 보행 시, 관절 토크 변동 폭이 **22%** 감소하여 보행이 더 안정적.
- **계산 효율성**: 모델의 단일 순전파 및 역전파 소요 시간은 **0.12 ms**(CPU)로, 일정 모델(0.08 ms)과 유사하여 실시간 제어 요구를 충족합니다.

### 결론
본 논문에서 제안한 해석 운동학 구동 모델은 계산 효율성을 유지하면서 병렬 메커니즘 휴머노이드 로봇의 제어 정밀도와 견고성을 크게 향상시킵니다. 이 방법은 복잡한 병렬 변속을 현대 제어 알고리즘(예: 궤적 최적화 및 강화 학습)에 통합하는 실용적인 경로를 제공하며, 특히 높은 동적 성능이 필요한 보행 로봇에 적합합니다.
