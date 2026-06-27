---
$id: ent_paper_mckay_learning_the_p2d_model_for_lit_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
  zh: 具有SOH检测的锂离子电池P2D模型学习
  ko: SOH 감지를 위한 리튬 이온 배터리 P2D 모델 학습
summary:
  en: This paper proposes a Convolutional Neural Network surrogate trained on synthetic
    P2D battery simulations to replace the computationally expensive Pseudo Two Dimensional
    electrochemical model for 100-second-ahead state prediction, and introduces a
    single-parameter State of Health adjustment estimated by voltage-discrepancy grid
    search.
  zh: 本文提出了一种在合成P2D电池模拟数据上训练的卷积神经网络代理模型，用于替代计算昂贵的伪二维电化学模型，实现未来100秒的状态预测，并引入了一种通过电压差异网格搜索估计的单参数健康状态调整方法。
  ko: 본 논문은 합성 P2D 배터리 시뮬레이션 데이터로 학습된 컨볼루션 신경망 서로게이트 모델을 제안하여, 계산 비용이 높은 의사이차원 전기화학
    모델을 대체하고 100초 선행 상태 예측을 수행하며, 전압 불일치 그리드 서치를 통해 추정되는 단일 매개변수 SOH 조정을 도입한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- battery_management_system
- state_of_health_estimation
- convolutional_neural_network
- surrogate_model
- electrochemical_model
- power_system
- lithium_ion_battery
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
  url: https://arxiv.org/abs/2502.14147
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Lithium-ion batteries are central to mobile power systems, yet the high-fidelity Pseudo Two Dimensional (P2D) electrochemical model is too expensive to solve in real time inside a battery management system (BMS). This paper addresses that gap by training a Convolutional Neural Network (CNN) surrogate on synthetic data generated with PyBaMM over random high-current driving cycles. The learned model predicts battery states 100 seconds ahead while preserving the spatial concentration information encoded in the P2D formulation.

The authors structure the surrogate to accept past current and voltage sequences along with internal concentration profiles, and they use a CNN architecture to capture the two-dimensional electrode-field structure. They compare models trained on constant-current profiles against those trained on variable driving cycles, concluding that variable-current training is necessary for accurate high-current operation. Finally, they augment the surrogate with a single State of Health (SOH) parameter representing degraded active particle area and current density, estimating it through a grid search that minimizes the discrepancy between predicted and observed voltage.

The reported CPU runtime is approximately 350 times faster than PyBaMM P2D simulation for K-step predictions, while still reproducing relevant concentration and voltage dynamics.

## Key Contributions

- Replaces the P2D electrochemical model with a CNN surrogate for 100-second-ahead battery state prediction.
- Demonstrates that CNNs are well suited to capturing two-dimensional Li-ion concentration profiles in electrodes.
- Shows that variable-current driving-cycle training is necessary for accurate high-current operation prediction, whereas constant-current training is insufficient.
- Incorporates a simple SOH parameter into the surrogate framework and estimates it via grid search over predicted-vs-observed voltage discrepancies.
- Achieves ~350x speedup over PyBaMM P2D simulation for K-step predictions on CPU.

## Relevance to Humanoid Robotics

Mobile humanoid robots rely on high-discharge battery packs to power actuators, compute, and sensors during dynamic locomotion and manipulation tasks. Fast, accurate battery state prediction and State of Health monitoring are therefore essential for safe mission planning, thermal management, and long-duration autonomy. This paper's CNN surrogate directly addresses the real-time constraint that prevents full electrochemical models from running onboard a BMS, making it relevant to humanoid power-system component technology. Nevertheless, the work is generic to Li-ion batteries and does not examine humanoid-specific integration, form factor, load profile, or safety certification.
