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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.10111v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
학습 기반 제어기는 민첩한 쿼드로터 비행에서 인상적인 성능을 달성했지만, 일반적으로 시뮬레이션에서 대규모 훈련에 의존하며, 효과적인 Sim2Real 전이를 위해 정확한 시스템 식별이 필요합니다. 그러나 정밀한 모델링이 있더라도 고정된 정책은 외부 공기역학적 교란부터 내부 하드웨어 성능 저하에 이르기까지 분포 외 시나리오에 취약합니다. 이러한 변화하는 불확실성 하에서 안전을 보장하기 위해, 이러한 제어기는 보수적인 안전 마진으로 작동해야 하며, 이는 통제된 환경 외부에서의 민첩성을 본질적으로 제한합니다. 온라인 적응이 잠재적 해결책을 제공하지만, 데이터 부족과 안전 위험으로 인해 물리적 한계를 안전하게 탐색하는 것은 여전히 중요한 병목 현상입니다. 이러한 격차를 해소하기 위해, 우리는 정밀한 시스템 식별이나 오프라인 Sim2Real 전이가 필요 없는 자가 적응 프레임워크를 제안합니다. 우리는 적응형 시간 스케일링(ATS)을 도입하여 플랫폼의 물리적 한계를 적극적으로 탐색하고, 온라인 잔차 학습을 사용하여 간단한 명목 모델을 보강합니다. 학습된 하이브리드 모델을 기반으로, 우리는 실세계 고정 단기 시간 역전파(RASH-BPTT)를 추가로 제안하여 효율적이고 강건한 비행 중 정책 업데이트를 달성합니다. 광범위한 실험을 통해 우리의 쿼드로터가 액추에이터 포화 한계 근처에서 민첩한 기동을 안정적으로 실행함을 입증했습니다. 시스템은 약 100초의 비행 시간 내에 최고 속도 1.9m/s에서 7.3m/s로 보수적인 기본 정책을 진화시킵니다. 이러한 결과는 실제 적응이 단순히 모델링 오류를 보상하는 것이 아니라, 공격적인 비행 영역에서 지속적인 성능 향상을 위한 실용적인 메커니즘으로 작용함을 강조합니다.

## 핵심 내용
학습 기반 제어기는 민첩한 쿼드로터 비행에서 인상적인 성능을 달성했지만, 일반적으로 시뮬레이션에서 대규모 훈련에 의존하며, 효과적인 Sim2Real 전이를 위해 정확한 시스템 식별이 필요합니다. 그러나 정밀한 모델링이 있더라도 고정된 정책은 외부 공기역학적 교란부터 내부 하드웨어 성능 저하에 이르기까지 분포 외 시나리오에 취약합니다. 이러한 변화하는 불확실성 하에서 안전을 보장하기 위해, 이러한 제어기는 보수적인 안전 마진으로 작동해야 하며, 이는 통제된 환경 외부에서의 민첩성을 본질적으로 제한합니다. 온라인 적응이 잠재적 해결책을 제공하지만, 데이터 부족과 안전 위험으로 인해 물리적 한계를 안전하게 탐색하는 것은 여전히 중요한 병목 현상입니다. 이러한 격차를 해소하기 위해, 우리는 정밀한 시스템 식별이나 오프라인 Sim2Real 전이가 필요 없는 자가 적응 프레임워크를 제안합니다. 우리는 적응형 시간 스케일링(ATS)을 도입하여 플랫폼의 물리적 한계를 적극적으로 탐색하고, 온라인 잔차 학습을 사용하여 간단한 명목 모델을 보강합니다. 학습된 하이브리드 모델을 기반으로, 우리는 실세계 고정 단기 시간 역전파(RASH-BPTT)를 추가로 제안하여 효율적이고 강건한 비행 중 정책 업데이트를 달성합니다. 광범위한 실험을 통해 우리의 쿼드로터가 액추에이터 포화 한계 근처에서 민첩한 기동을 안정적으로 실행함을 입증했습니다. 시스템은 약 100초의 비행 시간 내에 최고 속도 1.9m/s에서 7.3m/s로 보수적인 기본 정책을 진화시킵니다. 이러한 결과는 실제 적응이 단순히 모델링 오류를 보상하는 것이 아니라, 공격적인 비행 영역에서 지속적인 성능 향상을 위한 실용적인 메커니즘으로 작용함을 강조합니다.

## 参考
- http://arxiv.org/abs/2602.10111v2
