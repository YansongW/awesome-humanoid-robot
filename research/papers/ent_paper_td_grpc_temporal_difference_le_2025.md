---
$id: ent_paper_td_grpc_temporal_difference_le_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
  zh: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
  ko: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
summary:
  en: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  zh: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  ko: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
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
- td_grpc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.13549v1.
sources:
- id: src_001
  type: paper
  title: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.13549
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## 核心内容
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## 参考
- http://arxiv.org/abs/2505.13549v1

## Overview
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## Content
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## 개요
휴머노이드 보행과 같은 고차원 제어 환경에서의 로봇 학습은 불안정한 동역학, 복잡한 접촉 상호작용, 훈련 중 분포 변화에 대한 민감성으로 인해 강화 학습(RL) 알고리즘에 지속적인 도전 과제를 제시합니다. 모델 기반 방법, 예를 들어 시간차 모델 예측 제어(TD-MPC)는 단기 계획과 가치 기반 학습을 결합하여 기본 보행 작업에 대한 효율적인 솔루션을 가능하게 함으로써 유망한 결과를 보여주었습니다. 그러나 이러한 접근 방식은 오프-폴리시 업데이트로 인해 발생하는 정책 불일치와 불안정성을 해결하는 데 여전히 효과적이지 않습니다. 따라서 본 연구에서는 그룹 상대 정책 최적화(GRPO)와 명시적 정책 제약(PC)을 통합하는 TD-MPC 프레임워크의 확장인 시간차 그룹 상대 정책 제약(TD-GRPC)을 소개합니다. TD-GRPC는 잠재 정책 공간에서 신뢰 영역 제약을 적용하여 계획 사전 정보와 학습된 롤아웃 간의 일관성을 유지하는 동시에, 그룹 상대 순위를 활용하여 후보 궤적의 물리적 실현 가능성을 평가하고 보존합니다. 이전 방법과 달리 TD-GRPC는 기본 계획기를 수정하지 않고도 강건한 동작을 달성하여 유연한 계획 및 정책 학습을 가능하게 합니다. 우리는 26자유도(DoF) Unitree H1-2 휴머노이드 로봇에서 기본 걷기부터 고도로 동적인 움직임까지 다양한 보행 작업 세트에 걸쳐 방법을 검증합니다. 시뮬레이션 결과를 통해 TD-GRPC는 복잡한 휴머노이드 제어 작업을 훈련하는 동안 샘플 효율성과 함께 안정성 및 정책 강건성에서의 개선을 입증합니다.

## 핵심 내용
휴머노이드 보행과 같은 고차원 제어 환경에서의 로봇 학습은 불안정한 동역학, 복잡한 접촉 상호작용, 훈련 중 분포 변화에 대한 민감성으로 인해 강화 학습(RL) 알고리즘에 지속적인 도전 과제를 제시합니다. 모델 기반 방법, 예를 들어 시간차 모델 예측 제어(TD-MPC)는 단기 계획과 가치 기반 학습을 결합하여 기본 보행 작업에 대한 효율적인 솔루션을 가능하게 함으로써 유망한 결과를 보여주었습니다. 그러나 이러한 접근 방식은 오프-폴리시 업데이트로 인해 발생하는 정책 불일치와 불안정성을 해결하는 데 여전히 효과적이지 않습니다. 따라서 본 연구에서는 그룹 상대 정책 최적화(GRPO)와 명시적 정책 제약(PC)을 통합하는 TD-MPC 프레임워크의 확장인 시간차 그룹 상대 정책 제약(TD-GRPC)을 소개합니다. TD-GRPC는 잠재 정책 공간에서 신뢰 영역 제약을 적용하여 계획 사전 정보와 학습된 롤아웃 간의 일관성을 유지하는 동시에, 그룹 상대 순위를 활용하여 후보 궤적의 물리적 실현 가능성을 평가하고 보존합니다. 이전 방법과 달리 TD-GRPC는 기본 계획기를 수정하지 않고도 강건한 동작을 달성하여 유연한 계획 및 정책 학습을 가능하게 합니다. 우리는 26자유도(DoF) Unitree H1-2 휴머노이드 로봇에서 기본 걷기부터 고도로 동적인 움직임까지 다양한 보행 작업 세트에 걸쳐 방법을 검증합니다. 시뮬레이션 결과를 통해 TD-GRPC는 복잡한 휴머노이드 제어 작업을 훈련하는 동안 샘플 효율성과 함께 안정성 및 정책 강건성에서의 개선을 입증합니다.
