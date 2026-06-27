---
$id: ent_paper_morgan_model_predictive_actor_critic_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Model Predictive Actor-Critic: Accelerating Robot Skill Acquisition with Deep
    Reinforcement Learning'
  zh: 模型预测演员-评论家：利用深度强化学习加速机器人技能获取
  ko: '모델 예측 액터-크리틱: 심층 강화학습을 통한 로봇 기능 습득 가속화'
summary:
  en: This paper introduces Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free
    reinforcement learning algorithm that combines information-theoretic model predictive
    rollouts with a maximum-entropy actor-critic policy optimizer to mitigate model
    bias while preserving exploration. It derives a performance bound for MPC with
    learned dynamics and approximate value functions, and evaluates the method on
    simulated MuJoCo tasks and on a physical Yale Openhand Model Q performing valve
    rotation and finger gaiting.
  zh: 本文提出了模型预测演员-评论家（MoPAC），一种混合模型/无模型强化学习算法，该算法将信息论模型预测 rollout 与最大熵演员-评论家策略优化器相结合，以在保持探索的同时减轻模型偏差。论文推导了基于学习动态和近似值函数的模型预测控制性能界，并在模拟
    MuJoCo 任务以及执行阀门旋转和手指步态的实体 Yale Openhand Model Q 上进行了评估。
  ko: 본 논문은 정보 이론적 모델 예측 rollout과 최대 엔트로피 액터-크리틱 정책 최적화기를 결합하여 모델 편향을 완화하면서 탐색을 유지하는
    하이브리드 모델 기반/모델 프리 강화학습 알고리즘인 MoPAC(Model Predictive Actor-Critic)을 제안한다. 학습된 동역학과
    근사 값 함수를 가진 MPC에 대한 성능 경계를 유도하고, 시뮬레이션된 MuJoCo 작업과 밸브 회전 및 손가락 게이팅을 수행하는 실제 Yale
    Openhand Model Q에서 이 방법을 평가한다.
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
- model_predictive_actor_critic
- hybrid_rl
- model_based_rl
- model_free_rl
- deep_reinforcement_learning
- sample_efficiency
- dexterous_manipulation
- robotic_hand
- real_robot_training
- mujoco
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text (arXiv:2103.13842v1); hardware details
    and baseline comparisons were verified against the paper text, but full humanoid
    evaluation is absent.
sources:
- id: src_001
  type: paper
  title: 'Model Predictive Actor-Critic: Accelerating Robot Skill Acquisition with
    Deep Reinforcement Learning'
  url: https://arxiv.org/abs/2103.13842
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Model Predictive Actor-Critic (MoPAC) addresses the tension between sample efficiency and model bias in robot reinforcement learning. Model-based reinforcement learning (MBRL) is data-efficient but tends to exploit biased learned dynamics, while model-free reinforcement learning (MFRL) explores well yet requires excessive real-world interactions that risk damaging hardware. MoPAC hybridizes the two paradigms by using information-theoretic model predictive rollouts to generate near-optimal trajectory samples and a maximum-entropy actor-critic (Soft Actor-Critic) optimizer to explore the real environment and refine the policy.

The algorithm is theoretically grounded. The authors derive a performance bound for Model Predictive Control under learned dynamics and approximate value functions, showing that sufficiently low model and value approximation errors yield near-optimal policies. They instantiate this theory in three interacting components: an ensemble of probabilistic learned dynamics models, model predictive rollouts inspired by information-theoretic MPPI, and soft policy updates over a mixture of model-generated and real-environment data.

Empirically, MoPAC is evaluated on standard MuJoCo continuous-control benchmarks—HalfCheetah-v2, Ant-v2, Hopper-v2, and Walker2d-v2—against SAC, MBPO, and an information-theoretic MBRL baseline. The authors then demonstrate real-robot learning on a Yale Openhand Model Q, performing valve rotation and in-hand finger gaiting with an apple from the YCB Object and Model Set. An AprilTag tracks the apple's pose, and the hand's four Dynamixel XM-430 actuators provide underactuated, compliant manipulation.

## Key Contributions

- Introduced Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free reinforcement learning algorithm.
- Derived a performance bound for MPC under learned dynamics and approximate value functions.
- Proposed model predictive rollouts inspired by information-theoretic MPPI to generate optimal trajectory samples.
- Demonstrated accelerated learning over SAC, MBPO, and MBRL baselines in simulated MuJoCo control tasks.
- Validated MoPAC on a physical Yale Openhand Model Q performing valve rotation and finger gaiting.

## Relevance to Humanoid Robotics

Although MoPAC is demonstrated on a robotic hand rather than a full humanoid, its contributions are directly relevant to humanoid robotics. Sample-efficient, real-robot deep reinforcement learning for dexterous manipulation is a foundational capability for humanoid controllers, enabling complex contact-rich skills—such as grasping, regrasping, and in-hand object reorientation—that are essential for versatile humanoid platforms. The hybrid model-based/model-free architecture also reduces training time and physical wear, which matters for mass production and deployment of humanoid systems.
