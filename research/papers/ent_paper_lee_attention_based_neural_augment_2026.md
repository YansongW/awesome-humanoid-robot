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
  en: Proposes AttenNKF, an Invariant Extended Kalman Filter augmented with a cross-attention neural compensator that estimates
    slip-induced error from a continuous foot-slip level and applies it as a post-update correction to improve legged-robot
    state estimation under slip.
  zh: 提出 AttenNKF，一种用交叉注意力神经补偿器增强的不变扩展卡尔曼滤波器；该补偿器根据连续足端打滑程度估计打滑引起的误差，并在滤波更新后作为补偿量施加，以改善打滑条件下足式机器人的状态估计。
  ko: 지속적인 발 미끄러짐 수준으로부터 미끄러짐에 의한 오차를 추정하는 교차 주의 신경 보상기로 Invariant Extended Kalman Filter를 확장한 AttenNKF를 제안하여, 미끄러짐이 발생하는
    조건에서 다족 보행 로봇의 상태 추정 성능을 향상시킨다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.18569v2.
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
## 概述
In this letter, we propose an Attention-Based Neural-Augmented Kalman Filter (AttenNKF) for state estimation in legged robots. Foot slip is a major source of estimation error: when slip occurs, kinematic measurements violate the no-slip assumption and inject bias during the update step. Our objective is to estimate this slip-induced error and compensate for it. To this end, we augment an Invariant Extended Kalman Filter (InEKF) with a neural compensator that uses an attention mechanism to infer error conditioned on foot-slip severity and then applies this estimate as a post-update compensation to the InEKF state (i.e., after the filter update). The compensator is trained in a latent space, which aims to reduce sensitivity to raw input scales and encourages structured slip-conditioned compensations, while preserving the InEKF recursion. Experiments demonstrate improved performance compared to existing legged-robot state estimators, particularly under slip-prone conditions.

## 核心内容
In this letter, we propose an Attention-Based Neural-Augmented Kalman Filter (AttenNKF) for state estimation in legged robots. Foot slip is a major source of estimation error: when slip occurs, kinematic measurements violate the no-slip assumption and inject bias during the update step. Our objective is to estimate this slip-induced error and compensate for it. To this end, we augment an Invariant Extended Kalman Filter (InEKF) with a neural compensator that uses an attention mechanism to infer error conditioned on foot-slip severity and then applies this estimate as a post-update compensation to the InEKF state (i.e., after the filter update). The compensator is trained in a latent space, which aims to reduce sensitivity to raw input scales and encourages structured slip-conditioned compensations, while preserving the InEKF recursion. Experiments demonstrate improved performance compared to existing legged-robot state estimators, particularly under slip-prone conditions.

## 参考
- http://arxiv.org/abs/2601.18569v2

