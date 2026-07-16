---
$id: ent_paper_toward_reliable_sim_to_real_pr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  zh: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
summary:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
  zh: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
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
- toward_reliable_sim_to_real_pr
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.00678v4.
sources:
- id: src_001
  type: paper
  title: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion (arXiv)
  url: https://arxiv.org/abs/2602.00678
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 核心内容
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 参考
- http://arxiv.org/abs/2602.00678v4

## Overview
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## Content
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 개요
강화 학습은 고유 감각(proprioception)만을 활용한 센싱에서도 사족 보행 로봇의 민첩한 이동에 강력한 가능성을 보여주고 있습니다. 그러나 실제 환경에서는 시뮬레이션-실제 간극(sim-to-real gap)과 복잡한 지형에서의 보상 과적합(reward overfitting)으로 인해 정책이 전이에 실패할 수 있으며, 물리적 검증은 여전히 위험하고 비효율적입니다. 이러한 문제를 해결하기 위해, 우리는 로버스트한 다중 지형 표현을 위한 Mixture-of-Experts(MoE) 이동 정책과 시뮬레이션-실제 전이 가능성을 정량화하는 예측 평가 도구인 RoboGauge를 포함하는 통합 프레임워크를 소개합니다. MoE 정책은 게이트(gated) 방식의 전문가 집합을 활용하여 잠재 지형 및 명령 모델링을 분해함으로써, 고유 감각만으로도 뛰어난 배포 로버스트성과 일반화를 달성합니다. RoboGauge는 지형, 난이도, 도메인 무작위화에 걸친 시뮬레이션-시뮬레이션 테스트를 통해 다차원의 고유 감각 기반 메트릭을 제공하여, 광범위한 물리적 실험 없이도 신뢰할 수 있는 MoE 정책 선택을 가능하게 합니다. Unitree Go2에서의 실험은 눈, 모래, 계단, 경사로, 30cm 장애물 등 보지 못한 도전적인 지형에서 로버스트한 이동을 입증했습니다. 전용 고속 테스트에서 로봇은 4m/s에 도달했으며, 고속에서 안정성 향상과 관련된 좁은 폭의 보행(narrow-width gait)이 나타났습니다.

## 핵심 내용
강화 학습은 고유 감각(proprioception)만을 활용한 센싱에서도 사족 보행 로봇의 민첩한 이동에 강력한 가능성을 보여주고 있습니다. 그러나 실제 환경에서는 시뮬레이션-실제 간극(sim-to-real gap)과 복잡한 지형에서의 보상 과적합(reward overfitting)으로 인해 정책이 전이에 실패할 수 있으며, 물리적 검증은 여전히 위험하고 비효율적입니다. 이러한 문제를 해결하기 위해, 우리는 로버스트한 다중 지형 표현을 위한 Mixture-of-Experts(MoE) 이동 정책과 시뮬레이션-실제 전이 가능성을 정량화하는 예측 평가 도구인 RoboGauge를 포함하는 통합 프레임워크를 소개합니다. MoE 정책은 게이트(gated) 방식의 전문가 집합을 활용하여 잠재 지형 및 명령 모델링을 분해함으로써, 고유 감각만으로도 뛰어난 배포 로버스트성과 일반화를 달성합니다. RoboGauge는 지형, 난이도, 도메인 무작위화에 걸친 시뮬레이션-시뮬레이션 테스트를 통해 다차원의 고유 감각 기반 메트릭을 제공하여, 광범위한 물리적 실험 없이도 신뢰할 수 있는 MoE 정책 선택을 가능하게 합니다. Unitree Go2에서의 실험은 눈, 모래, 계단, 경사로, 30cm 장애물 등 보지 못한 도전적인 지형에서 로버스트한 이동을 입증했습니다. 전용 고속 테스트에서 로봇은 4m/s에 도달했으며, 고속에서 안정성 향상과 관련된 좁은 폭의 보행(narrow-width gait)이 나타났습니다.
