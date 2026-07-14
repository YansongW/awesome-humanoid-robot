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
  en: This paper proposes a Convolutional Neural Network surrogate trained on synthetic P2D battery simulations to replace
    the computationally expensive Pseudo Two Dimensional electrochemical model for 100-second-ahead state prediction, and
    introduces a single-parameter State of Health adjustment estimated by voltage-discrepancy grid search.
  zh: 本文提出了一种在合成P2D电池模拟数据上训练的卷积神经网络代理模型，用于替代计算昂贵的伪二维电化学模型，实现未来100秒的状态预测，并引入了一种通过电压差异网格搜索估计的单参数健康状态调整方法。
  ko: 본 논문은 합성 P2D 배터리 시뮬레이션 데이터로 학습된 컨볼루션 신경망 서로게이트 모델을 제안하여, 계산 비용이 높은 의사이차원 전기화학 모델을 대체하고 100초 선행 상태 예측을 수행하며, 전압 불일치 그리드
    서치를 통해 추정되는 단일 매개변수 SOH 조정을 도입한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.14147v1.
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
## 概述
Lithium ion batteries are widely used in many applications. Battery management systems control their optimal use and charging and predict when the battery will cease to deliver the required output on a planned duty or driving cycle. Such systems use a simulation of a mathematical model of battery performance. These models can be electrochemical or data-driven. Electrochemical models for batteries running at high currents are mathematically and computationally complex. In this work, we show that a well-regarded electrochemical model, the Pseudo Two Dimensional (P2D) model, can be replaced by a computationally efficient Convolutional Neural Network (CNN) surrogate model fit to accurately simulated data from a class of random driving cycles. We demonstrate that a CNN is an ideal choice for accurately capturing Lithium ion concentration profiles. Additionally, we show how the neural network model can be adjusted to correspond to battery changes in State of Health (SOH).

## 核心内容
Lithium ion batteries are widely used in many applications. Battery management systems control their optimal use and charging and predict when the battery will cease to deliver the required output on a planned duty or driving cycle. Such systems use a simulation of a mathematical model of battery performance. These models can be electrochemical or data-driven. Electrochemical models for batteries running at high currents are mathematically and computationally complex. In this work, we show that a well-regarded electrochemical model, the Pseudo Two Dimensional (P2D) model, can be replaced by a computationally efficient Convolutional Neural Network (CNN) surrogate model fit to accurately simulated data from a class of random driving cycles. We demonstrate that a CNN is an ideal choice for accurately capturing Lithium ion concentration profiles. Additionally, we show how the neural network model can be adjusted to correspond to battery changes in State of Health (SOH).

## 参考
- http://arxiv.org/abs/2502.14147v1

