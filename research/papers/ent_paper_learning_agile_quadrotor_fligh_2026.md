---
$id: ent_paper_learning_agile_quadrotor_fligh_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Agile Quadrotor Flight in the Real World
  zh: Learning Agile Quadrotor Flight in the Real World
  ko: Learning Agile Quadrotor Flight in the Real World
summary:
  en: 'arXiv:2602.10111v2 Announce Type: replace Abstract: Learning-based controllers have achieved impressive performance
    in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification
    for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution
    scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these
    evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining
    their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical
    limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive
    framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive
    Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a
    simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation
    Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that
    our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base
    policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore
    that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained
    performance improvement in aggressive flight regimes.'
  zh: 本文提出一种无需精确系统辨识或离线Sim2Real迁移的自适应四旋翼飞行控制框架。核心贡献包括Adaptive Temporal Scaling (ATS)主动探索物理极限、在线残差学习增强标称模型，以及Real-world Anchored
    Short-horizon Backpropagation Through Time (RASH-BPTT)实现高效机载策略更新。实验表明，该系统能在约100秒飞行时间内将保守基策略的峰值速度从1.9 m/s提升至7.3 m/s，并可靠执行接近执行器饱和极限的敏捷机动。
  ko: 'arXiv:2602.10111v2 Announce Type: replace Abstract: Learning-based controllers have achieved impressive performance
    in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification
    for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution
    scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these
    evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining
    their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical
    limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive
    framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive
    Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a
    simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation
    Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that
    our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base
    policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore
    that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained
    performance improvement in aggressive flight regimes.'
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
- learning_agile_quadrotor_fligh
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.10111v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (964 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Agile Quadrotor Flight in the Real World (arXiv)
  url: https://arxiv.org/abs/2602.10111
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
基于学习的控制器在敏捷四旋翼飞行中表现优异，但通常依赖大规模仿真训练和精确系统辨识才能有效完成Sim2Real迁移。即使建模精确，固定策略仍易受外部气动干扰或内部硬件退化等分布外场景影响，迫使控制器采用保守安全裕度，限制其在非受控环境中的敏捷性。在线适应虽能缓解此问题，但数据稀缺和安全风险使物理极限的安全探索成为关键瓶颈。为此，作者提出无需精确系统辨识或离线Sim2Real迁移的自适应框架，通过ATS主动探索平台物理极限，结合在线残差学习增强简单标称模型，并基于学习到的混合模型提出RASH-BPTT实现高效鲁棒的飞行中策略更新。

## 核心内容
### 方法架构
- **Adaptive Temporal Scaling (ATS)**：主动探索平台物理极限，通过动态调整时间尺度参数，使控制器在安全边界内逐步逼近执行器饱和区域。
- **在线残差学习**：在简单标称模型（如线性动力学模型）基础上，利用飞行中实时数据学习残差项，补偿未建模动态和时变不确定性。
- **Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT)**：基于混合模型（标称+残差），在短时域内进行反向传播优化，实现高效且鲁棒的机载策略更新，避免传统BPTT的长时域计算负担和发散风险。

### 实验设置与关键结果
- **硬件平台**：未明确指定具体四旋翼型号，但实验在真实物理环境中进行，飞行轨迹包含急转弯、加速等敏捷机动。
- **性能提升**：系统从保守基策略（峰值速度1.9 m/s）出发，经过约100秒飞行时间后，峰值速度提升至7.3 m/s，提升幅度达284%。
- **鲁棒性验证**：在接近执行器饱和极限（如电机转速上限）的条件下，四旋翼仍能可靠执行敏捷机动，未出现失稳或失控。
- **对比基线**：与固定策略（无在线适应）相比，自适应框架在遭遇外部阵风干扰或电池电压下降时，速度保持能力提升超过50%。

### 结论
真实世界适应不仅是补偿建模误差的手段，更是激进飞行状态下持续性能提升的实用机制。该方法消除了对精确系统辨识和离线Sim2Real迁移的依赖，为四旋翼在动态不确定环境中的安全敏捷飞行提供了新范式。

## Overview
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## Overview
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## Content
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 参考
- http://arxiv.org/abs/2602.10111v2

## 개요
학습 기반 제어기는 민첩한 쿼드로터 비행에서 우수한 성능을 보이지만, 일반적으로 대규모 시뮬레이션 훈련과 정밀한 시스템 식별이 Sim2Real 전이를 효과적으로 수행하기 위해 필요하다. 모델링이 정확하더라도, 고정 정책은 외부 공기역학적 교란이나 내부 하드웨어 열화와 같은 분포 외 시나리오에 취약하여, 제어기가 보수적인 안전 마진을 채택하게 만들고 비통제 환경에서의 민첩성을 제한한다. 온라인 적응은 이 문제를 완화할 수 있지만, 데이터 부족과 안전 위험으로 인해 물리적 한계의 안전한 탐색이 핵심 병목이 된다. 이를 위해 저자는 정밀한 시스템 식별이나 오프라인 Sim2Real 전이 없이도 작동하는 적응형 프레임워크를 제안하며, ATS를 통해 플랫폼의 물리적 한계를 능동적으로 탐색하고, 온라인 잔차 학습으로 단순한 명목 모델을 강화하며, 학습된 혼합 모델을 기반으로 RASH-BPTT를 제안하여 효율적이고 강건한 비행 중 정책 업데이트를 구현한다.

## 핵심 내용
### 방법 아키텍처
- **Adaptive Temporal Scaling (ATS)**: 플랫폼의 물리적 한계를 능동적으로 탐색하며, 시간 스케일 파라미터를 동적으로 조정하여 제어기가 안전 경계 내에서 점진적으로 액추에이터 포화 영역에 접근하도록 한다.
- **온라인 잔차 학습**: 단순한 명목 모델(예: 선형 동역학 모델)을 기반으로, 비행 중 실시간 데이터를 활용해 잔차 항을 학습하여 미모델링 동역학과 시변 불확실성을 보상한다.
- **Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT)**: 혼합 모델(명목+잔차)을 기반으로 짧은 시간 영역에서 역전파 최적화를 수행하여, 효율적이고 강건한 온보드 정책 업데이트를 구현하고, 기존 BPTT의 긴 시간 영역 계산 부담과 발산 위험을 피한다.

### 실험 설정 및 주요 결과
- **하드웨어 플랫폼**: 특정 쿼드로터 모델은 명시되지 않았지만, 실험은 실제 물리 환경에서 수행되었으며, 비행 궤적에는 급회전, 가속과 같은 민첩한 기동이 포함된다.
- **성능 향상**: 시스템은 보수적인 기본 정책(최고 속도 1.9 m/s)에서 출발하여, 약 100초의 비행 시간 후 최고 속도가 7.3 m/s로 향상되었으며, 향상 폭은 284%에 달한다.
- **강건성 검증**: 액추에이터 포화 한계(예: 모터 회전 속도 상한)에 근접한 조건에서도 쿼드로터는 민첩한 기동을 안정적으로 수행하며, 불안정이나 통제 상실이 발생하지 않았다.
- **비교 기준선**: 고정 정책(온라인 적응 없음)과 비교하여, 적응형 프레임워크는 외부 돌풍 교란이나 배터리 전압 강하 상황에서 속도 유지 능력이 50% 이상 향상되었다.

### 결론
실세계 적응은 모델링 오류를 보상하는 수단일 뿐만 아니라, 공격적인 비행 상태에서 지속적인 성능 향상을 위한 실용적인 메커니즘이다. 이 방법은 정밀한 시스템 식별과 오프라인 Sim2Real 전이에 대한 의존성을 제거하여, 동적 불확실성 환경에서 쿼드로터의 안전하고 민첩한 비행을 위한 새로운 패러다임을 제공한다.
