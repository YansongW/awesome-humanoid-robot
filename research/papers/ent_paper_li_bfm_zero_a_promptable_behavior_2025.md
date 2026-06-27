---
$id: ent_paper_li_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using
    Unsupervised Reinforcement Learning'
  zh: BFM-Zero：基于无监督强化学习的可提示人形机器人行为基础模型
  ko: 'BFM-Zero: 비지도 강화학습을 이용한 프롬프트 가능한 휴머노이드 제어 행동 기초 모델'
summary:
  en: BFM-Zero trains a single promptable foundation policy for whole-body humanoid
    control using off-policy unsupervised reinforcement learning and Forward-Backward
    representations, enabling zero-shot motion tracking, goal reaching, reward optimization,
    and few-shot latent-space adaptation on a real Unitree G1.
  zh: BFM-Zero基于离策略无监督强化学习与Forward-Backward表示，训练单一可提示的全身人形控制基础策略，可在真实Unitree G1上实现零样本运动跟踪、目标到达、奖励优化及少样本潜在空间自适应。
  ko: BFM-Zero는 오프폴리시 비지도 강화학습과 Forward-Backward 표현을 활용해 단일 프롬프트 가능한 전신 휴머노이드 제어 기초
    정책을 학습하며, 실제 Unitree G1에서 제로샷 동작 추적, 목표 도달, 보상 최적화 및 소수 샘플 잠재 공간 적응을 가능하게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- promptable_policy
- unsupervised_reinforcement_learning
- forward_backward_representation
- sim_to_real
- whole_body_control
- unitree_g1
- booster_t1
- zero_shot_humanoid_control
- latent_space_control
- motion_tracking
- goal_reaching
- reward_optimization
- few_shot_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv PDF; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control
    Using Unsupervised Reinforcement Learning'
  url: https://arxiv.org/abs/2511.04131
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

BFM-Zero addresses the problem of building a Behavioral Foundation Model (BFM) for whole-body humanoid control. Existing approaches are either confined to simulated characters or trained for narrow tasks such as motion tracking. The paper proposes an off-policy unsupervised reinforcement-learning framework that learns a shared latent space embedding motions, goals, and rewards, and uses this space to prompt a single policy for diverse downstream tasks without task-specific retraining. The policy is trained on a 29-degree-of-freedom humanoid in simulation and transferred to a real Unitree G1 robot.

The method builds on Forward-Backward (FB) representations and the recent FB-CPR algorithm, which combines FB learning with online training and motion-capture regularization. BFM-Zero extends this foundation with sim-to-real ingredients: asymmetric history-dependent training (policy observes history while critics access privileged state), domain randomization of physical parameters and sensor noise, auxiliary rewards for safety and physical feasibility, and massively parallel off-policy training. The resulting model supports zero-shot inference modes for reward optimization, single-frame goal reaching, and motion tracking, as well as few-shot latent-space adaptation via cross-entropy or sampling-based trajectory optimization.

The authors validate the approach through quantitative simulation ablations, sim-to-sim transfer to MuJoCo, out-of-distribution evaluation on the AMASS dataset, and real-world deployment on a Unitree G1. They also show preliminary generalization to a Booster T1 humanoid.

## Key Contributions

- Proposes the first behavioral foundation model deployed on a real humanoid (Unitree G1) that can be prompted in zero-shot for motion tracking, goal reaching, and reward optimization.
- Extends Forward-Backward unsupervised RL with sim-to-real components: asymmetric history-dependent training, domain randomization, reward regularization, and massively parallel off-policy training.
- Demonstrates diverse zero-shot inference modes and few-shot latent-space adaptation on real hardware, with quantitative simulation ablations validating the key design choices.
- Provides systematic evaluation across simulation (IsaacLab), sim-to-sim transfer (MuJoCo), out-of-distribution motions (AMASS), and a second humanoid platform (Booster T1).

## Relevance to Humanoid Robotics

BFM-Zero is highly relevant to scalable humanoid control because it replaces multiple task-specific policies with a single promptable foundation policy. This unification directly supports the control scalability needed for mass production and field deployment, where retraining or redesigning controllers for each task is impractical. The sim-to-real transfer results on a real Unitree G1 demonstrate that off-policy unsupervised RL can produce robust whole-body behaviors under hardware constraints. Although the few-shot adaptation remains preliminary, the framework points toward a generalist control layer that could simplify integration, reduce per-task engineering, and accelerate deployment of humanoid robots in real-world applications.
