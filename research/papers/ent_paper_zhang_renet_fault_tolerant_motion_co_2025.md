---
$id: ent_paper_zhang_renet_fault_tolerant_motion_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant Estimator Networks under Visual Collapse'
  zh: RENet：视觉崩溃下基于冗余估计器网络的四足机器人容错运动控制
  ko: 'RENet: 시각 붕괴 하에서 중복 추정기 네트워크를 통한 사족 로봇의 결허용 운동 제어'
summary:
  en: This paper proposes RENet, a single-stage end-to-end framework that trains a vision-plus-proprioception estimator and
    a proprioception-only estimator jointly with a low-level policy, and switches between them online using a CNN autoencoder
    anomaly detector when depth images become unreliable. Real-world outdoor experiments on a Unitree GO1 robot demonstrate
    direct sim-to-real transfer without fine-tuning.
  zh: 本文提出RENet，一种单阶段端到端框架，联合训练视觉-本体感知估计器与纯本体感知估计器及底层策略，并通过CNN自编码器异常检测器在深度图像不可靠时在线切换估计器。在Unitree GO1机器人上的真实室外实验验证了无需微调的直接仿真到现实迁移。
  ko: 본 논문은 시각-고유수용성 추정기와 고유수용성 전용 추정기를 저수준 정책과 함께 단일 단계로 종단간 학습하고, 깊이 이미지가 불안정해질 때 CNN 오토인코더 이상 탐지기를 통해 온라인으로 전환하는 RENet을
    제안한다. Unitree GO1 로봇을 이용한 실제 야외 실험에서 미세 조정 없는 시뮬레이션-현실 직접 전이를 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vision_based_locomotion
- quadruped_robot
- state_estimation
- sensor_fusion
- fault_tolerance
- sim_to_real
- reinforcement_learning
- depth_perception
- humanoid_transfer
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09283v1.
sources:
- id: src_001
  type: paper
  title: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant Estimator Networks under Visual Collapse'
  url: https://arxiv.org/abs/2509.09283
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Vision-based locomotion in outdoor environments presents significant challenges for quadruped robots. Accurate environmental prediction and effective handling of depth sensor noise during real-world deployment remain difficult, severely restricting the outdoor applications of such algorithms. To address these deployment challenges in vision-based motion control, this letter proposes the Redundant Estimator Network (RENet) framework. The framework employs a dual-estimator architecture that ensures robust motion performance while maintaining deployment stability during onboard vision failures. Through an online estimator adaptation, our method enables seamless transitions between estimation modules when handling visual perception uncertainties. Experimental validation on a real-world robot demonstrates the framework's effectiveness in complex outdoor environments, showing particular advantages in scenarios with degraded visual perception. This framework demonstrates its potential as a practical solution for reliable robotic deployment in challenging field conditions. Project website: https://RENet-Loco.github.io/

## 核心内容
Vision-based locomotion in outdoor environments presents significant challenges for quadruped robots. Accurate environmental prediction and effective handling of depth sensor noise during real-world deployment remain difficult, severely restricting the outdoor applications of such algorithms. To address these deployment challenges in vision-based motion control, this letter proposes the Redundant Estimator Network (RENet) framework. The framework employs a dual-estimator architecture that ensures robust motion performance while maintaining deployment stability during onboard vision failures. Through an online estimator adaptation, our method enables seamless transitions between estimation modules when handling visual perception uncertainties. Experimental validation on a real-world robot demonstrates the framework's effectiveness in complex outdoor environments, showing particular advantages in scenarios with degraded visual perception. This framework demonstrates its potential as a practical solution for reliable robotic deployment in challenging field conditions. Project website: https://RENet-Loco.github.io/

## 参考
- http://arxiv.org/abs/2509.09283v1

