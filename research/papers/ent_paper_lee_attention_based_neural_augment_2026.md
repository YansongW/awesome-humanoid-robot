---
$id: ent_paper_lee_attention_based_neural_augment_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation
  zh: 基于注意力机制的神经增强卡尔曼滤波用于足式机器人状态估计
  ko: 다족 보행 로봇 상태 추정을 위한 주의 기반 신경 증강 칼만 필터
summary:
  en: Proposes AttenNKF, an Invariant Extended Kalman Filter augmented with a cross-attention
    neural compensator that estimates slip-induced error from a continuous foot-slip
    level and applies it as a post-update correction to improve legged-robot state
    estimation under slip.
  zh: 提出 AttenNKF，一种用交叉注意力神经补偿器增强的不变扩展卡尔曼滤波器；该补偿器根据连续足端打滑程度估计打滑引起的误差，并在滤波更新后作为补偿量施加，以改善打滑条件下足式机器人的状态估计。
  ko: 지속적인 발 미끄러짐 수준으로부터 미끄러짐에 의한 오차를 추정하는 교차 주의 신경 보상기로 Invariant Extended Kalman
    Filter를 확장한 AttenNKF를 제안하여, 미끄러짐이 발생하는 조건에서 다족 보행 로봇의 상태 추정 성능을 향상시킨다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- state_estimation
- legged_robotics
- kalman_filter
- neural_compensator
- attention_mechanism
- foot_slip
- invariant_ekf
- proprioceptive_sensing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification needed before
    promotion to verified.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation
  url: https://arxiv.org/abs/2601.18569
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Foot slip is a dominant source of error in proprioceptive state estimators for legged robots because kinematic measurements typically assume no slip at contact points. When slip occurs, this assumption is violated and bias is injected during the filter update. This paper proposes the Attention-Based Neural-Augmented Kalman Filter (AttenNKF), which retains a conventional Invariant Extended Kalman Filter (InEKF) recursion but augments it with a neural compensator that runs after the update step.

The neural compensator is conditioned on a continuous foot-slip level derived from foot velocity and estimated contact state. Using cross-attention between a slip query and latent InEKF key/value representations, the network infers a slip-induced error and applies it as a post-update correction to the InEKF state. The compensator is trained in a latent space to reduce sensitivity to raw input scales and to encourage structured, slip-conditioned corrections. The authors report reduced relative estimation error compared to Slip Rejection, Learned Contact, and InNKF baselines on indoor experiments and roughly 100 m outdoor traverses.

The method is primarily relevant to legged and humanoid locomotion because maintaining accurate proprioceptive state estimates under slip directly affects closed-loop control stability, safety, and the reliability of deployment on industrial or low-friction floors.

## Key Contributions

- Define a continuous foot slip level from foot velocity and estimated contact state, and validate its correlation with estimation error.
- Propose a slip-conditioned Neural Compensator that uses cross-attention between a slip query and InEKF key/value latents.
- Design the Attention-Based Neural-Augmented Kalman Filter (AttenNKF) that preserves the InEKF recursion while adding learned post-update compensation.
- Demonstrate reduced Relative Error over Slip Rejection, Learned Contact, and InNKF baselines on indoor and approximately 100 m outdoor terrains.

## Relevance to Humanoid Robotics

Reliable proprioceptive state estimation under foot slip is a prerequisite for stable closed-loop locomotion in bipedal and humanoid robots. The paper explicitly connects slip compensation to control, safety, and deployment reliability on varied or low-friction industrial floors, which are critical concerns for humanoid systems operating outside of controlled laboratories.

Although the experiments are performed on a quadruped (Unitree Go1), the underlying estimation problem—fusing IMU and kinematic measurements while rejecting slip-induced bias—is identical for bipedal platforms. The learned post-update compensation and attention-based conditioning are therefore transferable design patterns for humanoid state estimation pipelines.
