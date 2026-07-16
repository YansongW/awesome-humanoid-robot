---
$id: ent_paper_learning_whole_body_humanoid_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
  zh: 复杂地形里，参考动作要在线生成
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
summary:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
  zh: Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need
    for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with
    reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn
    more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt
    them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion
    framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion
    model on retargeted human motions for real-time prediction of terrain-awar
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.17335v2.
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking (arXiv)
  url: https://arxiv.org/abs/2604.17335
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 复杂地形里，参考动作要在线生成 project page
  url: https://wholebodylocomotion.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 核心内容
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 参考
- http://arxiv.org/abs/2604.17335v2

## Overview
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## Content
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 개요
전신 휴머노이드 보행은 고차원 제어, 형태적 불안정성, 그리고 탑재된 인식을 통한 다양한 지형에 대한 실시간 적응의 필요성으로 인해 어려운 과제입니다. 보상 형성(reward shaping)을 이용한 강화 학습(RL)을 휴머노이드 보행에 직접 적용하면 종종 하체 중심의 행동이 나타나는 반면, 모방 기반 RL은 더 조화로운 전신 기술을 학습할 수 있지만 일반적으로 참조 동작을 재생하는 데 국한되어 지형 인식 보행을 위해 인식으로부터 온라인으로 적응하는 메커니즘이 없습니다. 이러한 격차를 해결하기 위해, 우리는 참조 동작에서 학습된 기술과 지형 인식 적응을 결합한 전신 휴머노이드 보행 프레임워크를 제안합니다. 먼저, 리타겟팅된 인간 동작에 대해 확산 모델을 학습시켜 지형 인식 참조 동작을 실시간으로 예측합니다. 동시에, 이 동작 데이터를 사용하여 RL로 전신 참조 추적기를 학습시킵니다. 불완전하게 생성된 참조 하에서의 강건성을 향상시키기 위해, 폐루프 설정에서 고정된 동작 생성기로 추적기를 추가 미세 조정합니다. 결과 시스템은 지형 인식 전신 적응을 통한 방향성 목표 도달 제어를 지원하며, 탑재된 인식 및 연산을 갖춘 Unitree G1 휴머노이드 로봇에 배포할 수 있습니다. 하드웨어 실험은 상자, 허들, 계단 및 혼합 지형 조합을 성공적으로 통과함을 보여줍니다. 정량적 결과는 또한 온라인 동작 생성 통합 및 동작 추적기 미세 조정이 일반화 및 강건성 향상에 기여함을 보여줍니다.

## 핵심 내용
전신 휴머노이드 보행은 고차원 제어, 형태적 불안정성, 그리고 탑재된 인식을 통한 다양한 지형에 대한 실시간 적응의 필요성으로 인해 어려운 과제입니다. 보상 형성(reward shaping)을 이용한 강화 학습(RL)을 휴머노이드 보행에 직접 적용하면 종종 하체 중심의 행동이 나타나는 반면, 모방 기반 RL은 더 조화로운 전신 기술을 학습할 수 있지만 일반적으로 참조 동작을 재생하는 데 국한되어 지형 인식 보행을 위해 인식으로부터 온라인으로 적응하는 메커니즘이 없습니다. 이러한 격차를 해결하기 위해, 우리는 참조 동작에서 학습된 기술과 지형 인식 적응을 결합한 전신 휴머노이드 보행 프레임워크를 제안합니다. 먼저, 리타겟팅된 인간 동작에 대해 확산 모델을 학습시켜 지형 인식 참조 동작을 실시간으로 예측합니다. 동시에, 이 동작 데이터를 사용하여 RL로 전신 참조 추적기를 학습시킵니다. 불완전하게 생성된 참조 하에서의 강건성을 향상시키기 위해, 폐루프 설정에서 고정된 동작 생성기로 추적기를 추가 미세 조정합니다. 결과 시스템은 지형 인식 전신 적응을 통한 방향성 목표 도달 제어를 지원하며, 탑재된 인식 및 연산을 갖춘 Unitree G1 휴머노이드 로봇에 배포할 수 있습니다. 하드웨어 실험은 상자, 허들, 계단 및 혼합 지형 조합을 성공적으로 통과함을 보여줍니다. 정량적 결과는 또한 온라인 동작 생성 통합 및 동작 추적기 미세 조정이 일반화 및 강건성 향상에 기여함을 보여줍니다.
