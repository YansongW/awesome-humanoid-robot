---
$id: ent_paper_spectral_normalization_for_lip_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
  zh: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
  ko: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion
summary:
  en: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
  zh: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
  ko: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.
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
- spectral_normalization_for_lip
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.08246v1.
sources:
- id: src_001
  type: paper
  title: Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2504.08246
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth.   Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## 核心内容
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth.   Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## 参考
- http://arxiv.org/abs/2504.08246v1

## Overview
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth. Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## Content
Reinforcement learning (RL) has shown great potential in training agile and adaptable controllers for legged robots, enabling them to learn complex locomotion behaviors directly from experience. However, policies trained in simulation often fail to transfer to real-world robots due to unrealistic assumptions such as infinite actuator bandwidth and the absence of torque limits. These conditions allow policies to rely on abrupt, high-frequency torque changes, which are infeasible for real actuators with finite bandwidth. Traditional methods address this issue by penalizing aggressive motions through regularization rewards, such as joint velocities, accelerations, and energy consumption, but they require extensive hyperparameter tuning. Alternatively, Lipschitz-Constrained Policies (LCP) enforce finite bandwidth action control by penalizing policy gradients, but their reliance on gradient calculations introduces significant GPU memory overhead. To overcome this limitation, this work proposes Spectral Normalization (SN) as an efficient replacement for enforcing Lipschitz continuity. By constraining the spectral norm of network weights, SN effectively limits high-frequency policy fluctuations while significantly reducing GPU memory usage. Experimental evaluations in both simulation and real-world humanoid robot show that SN achieves performance comparable to gradient penalty methods while enabling more efficient parallel training.

## 개요
강화 학습(RL)은 다리 로봇을 위한 민첩하고 적응 가능한 제어기를 훈련하는 데 큰 잠재력을 보여주며, 경험을 통해 직접 복잡한 보행 동작을 학습할 수 있게 합니다. 그러나 시뮬레이션에서 훈련된 정책은 무한한 액추에이터 대역폭과 토크 제한 부재와 같은 비현실적인 가정으로 인해 실제 로봇에 전이되지 못하는 경우가 많습니다. 이러한 조건은 정책이 급격하고 고주파의 토크 변화에 의존하게 하며, 이는 유한한 대역폭을 가진 실제 액추에이터에서는 실현 불가능합니다. 전통적인 방법은 관절 속도, 가속도 및 에너지 소비와 같은 정규화 보상을 통해 공격적인 움직임을 제재함으로써 이 문제를 해결하지만, 광범위한 하이퍼파라미터 튜닝이 필요합니다. 대안으로, Lipschitz 제약 정책(LCP)은 정책 기울기를 제재하여 유한 대역폭 동작 제어를 강제하지만, 기울기 계산에 의존하여 상당한 GPU 메모리 오버헤드를 초래합니다. 이 한계를 극복하기 위해, 본 연구는 Lipschitz 연속성을 강제하기 위한 효율적인 대안으로 스펙트럼 정규화(SN)를 제안합니다. 네트워크 가중치의 스펙트럼 노름을 제약함으로써, SN은 고주파 정책 변동을 효과적으로 제한하면서 GPU 메모리 사용량을 크게 줄입니다. 시뮬레이션 및 실제 인간형 로봇에서의 실험 평가는 SN이 기울기 패널티 방법과 유사한 성능을 달성하면서 더 효율적인 병렬 훈련을 가능하게 함을 보여줍니다.

## 핵심 내용
강화 학습(RL)은 다리 로봇을 위한 민첩하고 적응 가능한 제어기를 훈련하는 데 큰 잠재력을 보여주며, 경험을 통해 직접 복잡한 보행 동작을 학습할 수 있게 합니다. 그러나 시뮬레이션에서 훈련된 정책은 무한한 액추에이터 대역폭과 토크 제한 부재와 같은 비현실적인 가정으로 인해 실제 로봇에 전이되지 못하는 경우가 많습니다. 이러한 조건은 정책이 급격하고 고주파의 토크 변화에 의존하게 하며, 이는 유한한 대역폭을 가진 실제 액추에이터에서는 실현 불가능합니다. 전통적인 방법은 관절 속도, 가속도 및 에너지 소비와 같은 정규화 보상을 통해 공격적인 움직임을 제재함으로써 이 문제를 해결하지만, 광범위한 하이퍼파라미터 튜닝이 필요합니다. 대안으로, Lipschitz 제약 정책(LCP)은 정책 기울기를 제재하여 유한 대역폭 동작 제어를 강제하지만, 기울기 계산에 의존하여 상당한 GPU 메모리 오버헤드를 초래합니다. 이 한계를 극복하기 위해, 본 연구는 Lipschitz 연속성을 강제하기 위한 효율적인 대안으로 스펙트럼 정규화(SN)를 제안합니다. 네트워크 가중치의 스펙트럼 노름을 제약함으로써, SN은 고주파 정책 변동을 효과적으로 제한하면서 GPU 메모리 사용량을 크게 줄입니다. 시뮬레이션 및 실제 인간형 로봇에서의 실험 평가는 SN이 기울기 패널티 방법과 유사한 성능을 달성하면서 더 효율적인 병렬 훈련을 가능하게 함을 보여줍니다.
