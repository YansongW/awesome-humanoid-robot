---
$id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  zh: 扩散策略：通过动作扩散实现视觉运动策略学习
  ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
summary:
  en: Diffusion Policy represents robot visuomotor policies as conditional denoising
    diffusion processes over the action space, learning the score gradient of action
    distributions and iteratively denoising actions via stochastic Langevin dynamics
    conditioned on visual observations. Evaluated across 15 tasks from four manipulation
    benchmarks and real-world robot setups, it outperforms prior state-of-the-art
    robot learning methods by an average of 46.9%.
  zh: 扩散策略将机器人视觉运动策略表示为动作空间上的条件去噪扩散过程，学习动作分布的分数梯度，并在视觉观测条件下通过随机朗之万动力学迭代去噪生成动作。该文在四个操作基准的15项任务以及真实机器人系统上进行了评估，平均比之前最优的机器人学习方法高出46.9%。
  ko: 디퓨전 정책은 로봇의 시각운동 정책을 동작 공간에 대한 조건부 노이즈 제거 확산 과정으로 모델링하여, 시각 관찰을 조건으로 행동 분포의
    점수 기울기를 학습하고 확률적 랑주뱅 동역학을 통해 반복적으로 노이즈를 제거한다. 4개의 조작 벤치마크에서 15개 작업과 실제 로봇 설정에서
    평가한 결과, 기존 최신 로봇 학습 방법보다 평균 46.9% 향상된 성능을 보였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- imitation_learning
- visuomotor_policy
- behavior_cloning
- robot_manipulation
- action_diffusion
- langevin_dynamics
- score_matching
- receding_horizon_control
- multimodal_actions
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from provided paper metadata and abstract; full-text verification
    not performed. Requires human review before changing status to verified.
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
---

## Overview

Diffusion Policy formulates robot visuomotor policy learning as a conditional denoising diffusion process over the action space. Instead of directly regressing actions from observations, the model learns the gradient of the action-distribution score function and iteratively refines action samples through stochastic Langevin dynamics conditioned on visual observations. This generative formulation naturally handles multimodal action distributions, high-dimensional action spaces, and training stability, which are persistent challenges in imitation learning.

The paper presents several technical contributions tailored to robotic deployment: closed-loop action-sequence prediction combined with receding-horizon control, a vision-conditioned policy that extracts visual features once per inference for real-time operation, and a time-series diffusion transformer for high-frequency and velocity-control action spaces. The method is evaluated on 15 tasks across Robomimic, Push-T, Multimodal Block Pushing, and Franka Kitchen, as well as on real-world manipulation tasks including Push-T, mug flip, sauce handling, and bimanual tasks using UR5 and Franka Panda arms with Intel RealSense D415 RGB-D cameras.

Results show that Diffusion Policy consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. It also inherits the limitations of behavior cloning, such as sensitivity to demonstration quality and quantity, and exhibits higher inference latency than simpler baselines such as LSTM-GMM.

## Key Contributions

- Closed-loop action-sequence prediction combined with receding-horizon control for robust execution.
- Vision-conditioned diffusion policy that extracts visual features once per inference for real-time control.
- Time-series diffusion transformer architecture for high-frequency and velocity-control action spaces.
- Stable training by directly learning the score gradient, avoiding normalization issues of explicit energy-based models.
- Comprehensive evaluation across 15 simulated and real-world manipulation tasks.

## Relevance to Humanoid Robotics

Diffusion Policy is directly relevant to humanoid robotics because it provides a scalable and stable imitation-learning framework for visuomotor manipulation skills. Humanoid robots must perform diverse, contact-rich tasks in unstructured environments, which requires policies that can represent multimodal, high-dimensional, and precise action distributions from visual feedback. The diffusion-based formulation addresses these requirements and can serve as a foundation for training general-purpose manipulation skills on humanoid platforms.

The real-world experiments on manipulation tasks such as Push-T, mug flipping, sauce handling, and bimanual operations demonstrate the method's applicability to the kinds of everyday tasks humanoid robots are expected to perform. While the paper focuses on manipulation rather than full-body humanoid control, its algorithmic contributions are domain-agnostic and transferable to upper-body and hand manipulation policies for humanoid systems.
