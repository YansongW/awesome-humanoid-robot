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
  en: Diffusion Policy represents robot visuomotor policies as conditional denoising diffusion processes over the action space,
    learning the score gradient of action distributions and iteratively denoising actions via stochastic Langevin dynamics
    conditioned on visual observations. Evaluated across 15 tasks from four manipulation benchmarks and real-world robot setups,
    it outperforms prior state-of-the-art robot learning methods by an average of 46.9%.
  zh: 扩散策略将机器人视觉运动策略表示为动作空间上的条件去噪扩散过程，学习动作分布的分数梯度，并在视觉观测条件下通过随机朗之万动力学迭代去噪生成动作。该文在四个操作基准的15项任务以及真实机器人系统上进行了评估，平均比之前最优的机器人学习方法高出46.9%。
  ko: 디퓨전 정책은 로봇의 시각운동 정책을 동작 공간에 대한 조건부 노이즈 제거 확산 과정으로 모델링하여, 시각 관찰을 조건으로 행동 분포의 점수 기울기를 학습하고 확률적 랑주뱅 동역학을 통해 반복적으로 노이즈를
    제거한다. 4개의 조작 벤치마크에서 15개 작업과 실제 로봇 설정에서 평가한 결과, 기존 최신 로봇 학습 방법보다 평균 46.9% 향상된 성능을 보였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.04137v5.
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 12 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer. We hope this work will help motivate a new generation of policy learning techniques that are able to leverage the powerful generative modeling capabilities of diffusion models. Code, data, and training details is publicly available diffusion-policy.cs.columbia.edu

## 核心内容
This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 12 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer. We hope this work will help motivate a new generation of policy learning techniques that are able to leverage the powerful generative modeling capabilities of diffusion models. Code, data, and training details is publicly available diffusion-policy.cs.columbia.edu

## 参考
- http://arxiv.org/abs/2303.04137v5

