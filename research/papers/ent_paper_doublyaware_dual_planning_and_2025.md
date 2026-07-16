---
$id: ent_paper_doublyaware_dual_planning_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
  zh: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
  ko: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
summary:
  en: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  zh: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  ko: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- doublyaware
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12095v1.
sources:
- id: src_001
  type: paper
  title: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2506.12095
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## 核心内容
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## 参考
- http://arxiv.org/abs/2506.12095v1

## Overview
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## Content
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## 개요
휴머노이드 보행을 위한 강건한 로봇 학습을 달성하는 것은 모델 기반 강화 학습(MBRL)에서 근본적인 과제이며, 환경의 확률성과 무작위성은 효율적인 탐색과 학습 안정성을 저해할 수 있습니다. 소위 우연적(aleatoric) 불확실성이라고 불리는 환경적 불확실성은 복잡한 접촉 역학을 가진 고차원 행동 공간에서 증폭될 수 있으며, 학습 단계에서 모델의 인식적(epistemic) 불확실성과 더욱 얽히게 됩니다. 본 연구에서는 DoublyAware를 제안합니다. 이는 시간차 모델 예측 제어(TD-MPC)의 불확실성 인식 확장판으로, 불확실성을 계획 불확실성과 정책 불확실성이라는 두 개의 분리 가능하고 해석 가능한 구성 요소로 명시적으로 분해합니다. 계획 불확실성을 처리하기 위해 DoublyAware는 등위 예측(conformal prediction)을 사용하여 분위수 보정 위험 경계를 통해 후보 궤적을 필터링함으로써 통계적 일관성과 확률적 역학에 대한 강건성을 보장합니다. 한편, 정책 롤아웃은 구조화된 정보 제공 사전 지식으로 활용되어 잠재 행동 공간에서 그룹 기반 적응형 신뢰 영역을 부과하는 그룹 상대 정책 제약(GRPC) 최적화기를 통해 학습 단계를 지원합니다. 이러한 원칙적 결합을 통해 로봇 에이전트는 불확실성 하에서 효과적이고 목표 지향적인 탐색을 유지하면서 높은 신뢰도와 높은 보상의 행동을 우선시할 수 있습니다. Unitree 26-DoF H1-2 휴머노이드를 사용한 HumanoidBench 보행 제품군에서 평가된 DoublyAware는 RL 기준선과 비교하여 향상된 샘플 효율성, 가속화된 수렴 및 향상된 동작 실현 가능성을 보여줍니다. 시뮬레이션 결과는 TD-MPC 기반 휴머노이드 보행 학습에서 데이터 효율적이고 신뢰할 수 있는 의사 결정을 위한 구조화된 불확실성 모델링의 중요성을 강조합니다.

## 핵심 내용
휴머노이드 보행을 위한 강건한 로봇 학습을 달성하는 것은 모델 기반 강화 학습(MBRL)에서 근본적인 과제이며, 환경의 확률성과 무작위성은 효율적인 탐색과 학습 안정성을 저해할 수 있습니다. 소위 우연적(aleatoric) 불확실성이라고 불리는 환경적 불확실성은 복잡한 접촉 역학을 가진 고차원 행동 공간에서 증폭될 수 있으며, 학습 단계에서 모델의 인식적(epistemic) 불확실성과 더욱 얽히게 됩니다. 본 연구에서는 DoublyAware를 제안합니다. 이는 시간차 모델 예측 제어(TD-MPC)의 불확실성 인식 확장판으로, 불확실성을 계획 불확실성과 정책 불확실성이라는 두 개의 분리 가능하고 해석 가능한 구성 요소로 명시적으로 분해합니다. 계획 불확실성을 처리하기 위해 DoublyAware는 등위 예측(conformal prediction)을 사용하여 분위수 보정 위험 경계를 통해 후보 궤적을 필터링함으로써 통계적 일관성과 확률적 역학에 대한 강건성을 보장합니다. 한편, 정책 롤아웃은 구조화된 정보 제공 사전 지식으로 활용되어 잠재 행동 공간에서 그룹 기반 적응형 신뢰 영역을 부과하는 그룹 상대 정책 제약(GRPC) 최적화기를 통해 학습 단계를 지원합니다. 이러한 원칙적 결합을 통해 로봇 에이전트는 불확실성 하에서 효과적이고 목표 지향적인 탐색을 유지하면서 높은 신뢰도와 높은 보상의 행동을 우선시할 수 있습니다. Unitree 26-DoF H1-2 휴머노이드를 사용한 HumanoidBench 보행 제품군에서 평가된 DoublyAware는 RL 기준선과 비교하여 향상된 샘플 효율성, 가속화된 수렴 및 향상된 동작 실현 가능성을 보여줍니다. 시뮬레이션 결과는 TD-MPC 기반 휴머노이드 보행 학습에서 데이터 효율적이고 신뢰할 수 있는 의사 결정을 위한 구조화된 불확실성 모델링의 중요성을 강조합니다.
