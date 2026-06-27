---
$id: ent_paper_shin_infusing_model_predictive_cont_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Infusing Model Predictive Control into Meta-Reinforcement Learning for Mobile
    Robots in Dynamic Environments
  zh: 将模型预测控制融入动态环境下移动机器人的元强化学习
  ko: 동적 환경에서 모바일 로봇을 위한 메타 강화 학습에 모델 예측 제어 통합
summary:
  en: Proposes MPC-PEARL, an algorithm that combines off-policy meta-reinforcement
    learning with event-triggered, randomized model predictive control for safe navigation
    of mobile robots among dynamic obstacles and pedestrians.
  zh: 提出MPC-PEARL算法，将离线策略元强化学习与事件触发、随机化的模型预测控制相结合，用于移动机器人在动态障碍物和行人中的安全导航。
  ko: 오프폴리시 메타 강화 학습과 사건 기반 무작위 모델 예측 제어를 결합하여 동적 장애물 및 보행자 환경에서 모바일 로봇의 안전한 내비게이션을
    위한 MPC-PEARL 알고리즘을 제안한다.
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
- meta_reinforcement_learning
- model_predictive_control
- mobile_robot_navigation
- dynamic_obstacles
- pedestrian_avoidance
- cvar_safety
- online_adaptation
- event_triggered_control
- gaussian_process_regression
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before final verification.
sources:
- id: src_001
  type: paper
  title: Infusing Model Predictive Control into Meta-Reinforcement Learning for Mobile
    Robots in Dynamic Environments
  url: https://arxiv.org/abs/2109.07120
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper proposes MPC-PEARL, a hybrid algorithm that infuses model predictive control (MPC) into an off-policy meta-reinforcement learning (meta-RL) framework for mobile robots operating in dynamic environments. The key idea is to switch randomly and in an event-triggered manner between a meta-learned policy and an MPC controller during training. When the robot detects events that can be effectively handled by MPC—such as nearby dynamic obstacles—the MPC module generates transition samples using its explicit robot-dynamics model, and these samples are used to train the meta-RL policy. During meta-testing, the MPC module is deactivated to reduce computation time, while an online latent-context adaptation scheme enables the robot to infer and adapt to a new task within a single trajectory.

The MPC module uses Gaussian process regression to predict obstacle motions and incorporates conditional value-at-risk (CVaR) constraints to manage collision risk. The randomized switching is designed to compensate for suboptimal actions caused by the MPC's limited prediction horizon: when MPC is active too often, the policy may lose diversity and performance can degrade, so the activation probability is a tunable hyperparameter. Experiments are conducted in simulation with a nonlinear car-like vehicle model, first with synthetic obstacle movements and then with real pedestrian trajectories from the UCY dataset in restaurant and sidewalk scenarios.

## Key Contributions

- Randomized, event-triggered infusion of MPC-generated transitions into off-policy meta-RL training.
- Learning-based MPC using Gaussian process regression for obstacle motion prediction and CVaR constraints for collision-risk management.
- Online latent-context adaptation scheme enabling task inference and adaptation within a single trajectory.
- MPC deactivation at meta-test time to reduce real-time computation while retaining navigation performance.
- Empirical validation in restaurant and sidewalk simulations using synthetic obstacles and real pedestrian data.

## Relevance to Humanoid Robotics

Although the experiments are performed on a simulated nonlinear car-like robot, the core contribution—an adaptive meta-RL/MPC navigation framework that reasons explicitly about robot dynamics, predicts moving obstacles, and enforces safety constraints—is conceptually transferable to humanoid locomotion in cluttered, human-shared environments. Humanoids operating alongside pedestrians or in dynamic indoor spaces face similar requirements for rapid adaptation, collision avoidance, and real-time decision making. The online latent-context adaptation mechanism in particular aligns with the need for humanoid platforms to infer task context from a short interaction history. However, the paper does not validate transfer to humanoids or address platform-specific concerns such as balance, contact dynamics, real-time operating systems, or scheduling.
