---
$id: ent_paper_lee_diff_dagger_uncertainty_estima_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation'
  zh: Diff-DAgger：面向机器人操作的扩散策略不确定性估计
  ko: 'Diff-DAgger: 로봇 조작을 위한 확산 정책의 불확실성 추정'
summary:
  en: Diff-DAgger is a robot-gated DAgger algorithm that uses the diffusion policy
    training loss as an uncertainty signal to decide when a robot should request expert
    intervention during online rollout. Evaluations on simulated and real manipulation
    tasks show that it improves task-failure prediction, task completion rate, and
    wall-clock training time compared to ensemble-based DAgger baselines.
  zh: Diff-DAgger是一种机器人门控DAgger算法，将扩散策略的训练损失作为不确定信号，用于在在线展开过程中决定机器人何时请求专家干预。在仿真和真实操作任务上的评估表明，与基于集成的DAgger基线相比，它提高了任务失败预测、任务完成率并缩短了训练挂钟时间。
  ko: Diff-DAgger는 확산 정책의 훈련 손실을 불확실성 신호로 사용하여 온라인 롤아웃 중 로봇이 전문가 개입을 요청해야 하는 시점을 결정하는
    로봇 게이트 DAgger 알고리즘이다. 시뮬레이션 및 실제 조작 작업에 대한 평가에서 앙상블 기반 DAgger 기준과 비교하여 작업 실패 예측,
    작업 완료율 및 훈련 벽시계 시간을 개선한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- daggar
- robot_gated_dagger
- interactive_imitation_learning
- uncertainty_estimation
- visuomotor_policy
- out_of_distribution_detection
- manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation'
  url: https://arxiv.org/abs/2410.14868
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Imitation learning for manipulation must handle long-horizon decisions, high precision, and dynamic environments. While diffusion policy has achieved strong results on multi-modal behavior-cloning tasks by generating action sequences through a denoising diffusion process, it remains prone to out-of-distribution failures caused by compounding errors and limited extrapolation. Robot-gated DAgger methods address this by letting the robot request expert help during rollout, but ensemble-based approaches estimate uncertainty from action variance and therefore confuse in-distribution multi-modal choices with true OOD states.

Diff-DAgger introduces a query rule that uses the diffusion policy's own training loss as the uncertainty signal. During deployment the policy denoises an action for the current observation, then computes the expected diffusion loss over sampled noise and diffusion timesteps. If that loss exceeds the α-quantile of expected losses on the training data for K consecutive steps, the robot asks an expert to take over; otherwise it executes the action. After each batch of expert interventions the aggregated data is used to retrain the policy and reset the threshold.

The authors evaluate Diff-DAgger in the ManiSkill simulator on stacking, pushing, and plugging tasks, and in the real world on stacking and loading with a Franka Research 3 robot and three RealSense D435 cameras. Both state-based and image-based observations are tested; the image-based policy uses an R3M ResNet18 encoder and a U-Net policy head with FiLM conditioning. Baselines include behavior cloning, Ensemble-DAgger, and ThriftyDAgger.

## Key Contributions

- A robot-gated query system that uses diffusion loss to distinguish true OOD failures from in-distribution multi-modal decisions.
- Quantitative evaluation showing improved task-failure prediction, task completion, and wall-clock training time over behavior cloning, Ensemble-DAgger, and ThriftyDAgger.
- Design choices and analysis for accelerating policy learning and improving convergence in interactive imitation learning.

## Relevance to Humanoid Robotics

Humanoid robots operating in unstructured industrial or mass-production settings need visuomotor policies that can recognize their own limitations and request human guidance efficiently. Diff-DAgger provides a scalable interactive imitation-learning mechanism that reduces the expert supervision burden while improving failure prediction and recovery behavior. Its image-based policy architecture and real-robot deployment pipeline are directly transferable to humanoid manipulation platforms that require long-horizon, contact-rich, and precision tasks.
