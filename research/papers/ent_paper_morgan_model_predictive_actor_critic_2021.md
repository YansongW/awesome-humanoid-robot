---
$id: ent_paper_morgan_model_predictive_actor_critic_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Model Predictive Actor-Critic: Accelerating Robot Skill Acquisition with Deep Reinforcement Learning'
  zh: 模型预测演员-评论家：利用深度强化学习加速机器人技能获取
  ko: '모델 예측 액터-크리틱: 심층 강화학습을 통한 로봇 기능 습득 가속화'
summary:
  en: This paper introduces Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free reinforcement learning
    algorithm that combines information-theoretic model predictive rollouts with a maximum-entropy actor-critic policy optimizer
    to mitigate model bias while preserving exploration. It derives a performance bound for MPC with learned dynamics and
    approximate value functions, and evaluates the method on simulated MuJoCo tasks and on a physical Yale Openhand Model
    Q performing valve rotation and finger gaiting.
  zh: 本文提出了模型预测演员-评论家（MoPAC），一种混合模型/无模型强化学习算法，该算法将信息论模型预测 rollout 与最大熵演员-评论家策略优化器相结合，以在保持探索的同时减轻模型偏差。论文推导了基于学习动态和近似值函数的模型预测控制性能界，并在模拟
    MuJoCo 任务以及执行阀门旋转和手指步态的实体 Yale Openhand Model Q 上进行了评估。
  ko: 본 논문은 정보 이론적 모델 예측 rollout과 최대 엔트로피 액터-크리틱 정책 최적화기를 결합하여 모델 편향을 완화하면서 탐색을 유지하는 하이브리드 모델 기반/모델 프리 강화학습 알고리즘인 MoPAC(Model
    Predictive Actor-Critic)을 제안한다. 학습된 동역학과 근사 값 함수를 가진 MPC에 대한 성능 경계를 유도하고, 시뮬레이션된 MuJoCo 작업과 밸브 회전 및 손가락 게이팅을 수행하는 실제 Yale
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.13842v1.
sources:
- id: src_001
  type: paper
  title: 'Model Predictive Actor-Critic: Accelerating Robot Skill Acquisition with Deep Reinforcement Learning'
  url: https://arxiv.org/abs/2103.13842
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Substantial advancements to model-based reinforcement learning algorithms have been impeded by the model-bias induced by the collected data, which generally hurts performance. Meanwhile, their inherent sample efficiency warrants utility for most robot applications, limiting potential damage to the robot and its environment during training. Inspired by information theoretic model predictive control and advances in deep reinforcement learning, we introduce Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free method that combines model predictive rollouts with policy optimization as to mitigate model bias. MoPAC leverages optimal trajectories to guide policy learning, but explores via its model-free method, allowing the algorithm to learn more expressive dynamics models. This combination guarantees optimal skill learning up to an approximation error and reduces necessary physical interaction with the environment, making it suitable for real-robot training. We provide extensive results showcasing how our proposed method generally outperforms current state-of-the-art and conclude by evaluating MoPAC for learning on a physical robotic hand performing valve rotation and finger gaiting--a task that requires grasping, manipulation, and then regrasping of an object.

## 核心内容
Substantial advancements to model-based reinforcement learning algorithms have been impeded by the model-bias induced by the collected data, which generally hurts performance. Meanwhile, their inherent sample efficiency warrants utility for most robot applications, limiting potential damage to the robot and its environment during training. Inspired by information theoretic model predictive control and advances in deep reinforcement learning, we introduce Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free method that combines model predictive rollouts with policy optimization as to mitigate model bias. MoPAC leverages optimal trajectories to guide policy learning, but explores via its model-free method, allowing the algorithm to learn more expressive dynamics models. This combination guarantees optimal skill learning up to an approximation error and reduces necessary physical interaction with the environment, making it suitable for real-robot training. We provide extensive results showcasing how our proposed method generally outperforms current state-of-the-art and conclude by evaluating MoPAC for learning on a physical robotic hand performing valve rotation and finger gaiting--a task that requires grasping, manipulation, and then regrasping of an object.

## 参考
- http://arxiv.org/abs/2103.13842v1

## Overview
Substantial advancements to model-based reinforcement learning algorithms have been impeded by the model-bias induced by the collected data, which generally hurts performance. Meanwhile, their inherent sample efficiency warrants utility for most robot applications, limiting potential damage to the robot and its environment during training. Inspired by information theoretic model predictive control and advances in deep reinforcement learning, we introduce Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free method that combines model predictive rollouts with policy optimization as to mitigate model bias. MoPAC leverages optimal trajectories to guide policy learning, but explores via its model-free method, allowing the algorithm to learn more expressive dynamics models. This combination guarantees optimal skill learning up to an approximation error and reduces necessary physical interaction with the environment, making it suitable for real-robot training. We provide extensive results showcasing how our proposed method generally outperforms current state-of-the-art and conclude by evaluating MoPAC for learning on a physical robotic hand performing valve rotation and finger gaiting--a task that requires grasping, manipulation, and then regrasping of an object.

## Content
Substantial advancements to model-based reinforcement learning algorithms have been impeded by the model-bias induced by the collected data, which generally hurts performance. Meanwhile, their inherent sample efficiency warrants utility for most robot applications, limiting potential damage to the robot and its environment during training. Inspired by information theoretic model predictive control and advances in deep reinforcement learning, we introduce Model Predictive Actor-Critic (MoPAC), a hybrid model-based/model-free method that combines model predictive rollouts with policy optimization as to mitigate model bias. MoPAC leverages optimal trajectories to guide policy learning, but explores via its model-free method, allowing the algorithm to learn more expressive dynamics models. This combination guarantees optimal skill learning up to an approximation error and reduces necessary physical interaction with the environment, making it suitable for real-robot training. We provide extensive results showcasing how our proposed method generally outperforms current state-of-the-art and conclude by evaluating MoPAC for learning on a physical robotic hand performing valve rotation and finger gaiting--a task that requires grasping, manipulation, and then regrasping of an object.

## 개요
모델 기반 강화 학습 알고리즘의 실질적인 발전은 수집된 데이터로 인해 발생하는 모델 편향(model-bias)에 의해 저해되어 왔으며, 이는 일반적으로 성능을 저하시킵니다. 한편, 모델 기반 방법의 본질적인 샘플 효율성은 대부분의 로봇 응용 분야에서 유용성을 보장하며, 훈련 중 로봇과 환경에 대한 잠재적 손상을 제한합니다. 정보 이론적 모델 예측 제어와 심층 강화 학습의 발전에서 영감을 받아, 우리는 모델 예측 롤아웃(model predictive rollouts)과 정책 최적화를 결합하여 모델 편향을 완화하는 하이브리드 모델 기반/모델 프리 방법인 Model Predictive Actor-Critic (MoPAC)을 소개합니다. MoPAC은 최적 궤적을 활용하여 정책 학습을 안내하지만, 모델 프리 방법을 통해 탐색함으로써 알고리즘이 더 표현력 있는 동역학 모델을 학습할 수 있도록 합니다. 이 조합은 근사 오차까지 최적의 기술 학습을 보장하고 환경과의 필요한 물리적 상호작용을 줄여, 실제 로봇 훈련에 적합하게 만듭니다. 우리는 제안된 방법이 일반적으로 최신 기술보다 우수함을 보여주는 광범위한 결과를 제공하며, 밸브 회전과 핑거 게이팅(finger gaiting)을 수행하는 물리적 로봇 손에서의 학습을 평가하는 것으로 마무리합니다. 이 작업은 물체를 잡고, 조작한 후 다시 잡는 작업을 필요로 합니다.

## 핵심 내용
모델 기반 강화 학습 알고리즘의 실질적인 발전은 수집된 데이터로 인해 발생하는 모델 편향(model-bias)에 의해 저해되어 왔으며, 이는 일반적으로 성능을 저하시킵니다. 한편, 모델 기반 방법의 본질적인 샘플 효율성은 대부분의 로봇 응용 분야에서 유용성을 보장하며, 훈련 중 로봇과 환경에 대한 잠재적 손상을 제한합니다. 정보 이론적 모델 예측 제어와 심층 강화 학습의 발전에서 영감을 받아, 우리는 모델 예측 롤아웃(model predictive rollouts)과 정책 최적화를 결합하여 모델 편향을 완화하는 하이브리드 모델 기반/모델 프리 방법인 Model Predictive Actor-Critic (MoPAC)을 소개합니다. MoPAC은 최적 궤적을 활용하여 정책 학습을 안내하지만, 모델 프리 방법을 통해 탐색함으로써 알고리즘이 더 표현력 있는 동역학 모델을 학습할 수 있도록 합니다. 이 조합은 근사 오차까지 최적의 기술 학습을 보장하고 환경과의 필요한 물리적 상호작용을 줄여, 실제 로봇 훈련에 적합하게 만듭니다. 우리는 제안된 방법이 일반적으로 최신 기술보다 우수함을 보여주는 광범위한 결과를 제공하며, 밸브 회전과 핑거 게이팅(finger gaiting)을 수행하는 물리적 로봇 손에서의 학습을 평가하는 것으로 마무리합니다. 이 작업은 물체를 잡고, 조작한 후 다시 잡는 작업을 필요로 합니다.
