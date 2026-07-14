---
$id: ent_paper_berdica_towards_reinforcement_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Reinforcement Learning Controllers for Soft Robots using Learned Environments
  zh: 基于学习环境的软体机器人强化学习控制器研究
  ko: 학습된 환경을 사용한 소프트 로봇용 강화 학습 컨트롤러 연구
summary:
  en: This paper presents a model-based reinforcement learning pipeline for soft pneumatic manipulators that learns a recurrent
    forward-dynamics model from safe actuation-space exploration and trains PPO actor-critic policies inside a parallel JAX/Gymnax
    learned environment on GPU.
  zh: 本文提出了一种面向软体气动机械臂的基于模型的强化学习流程，通过安全驱动空间探索学习循环前向动力学模型，并在 GPU 上的并行 JAX/Gymnax 学习环境中训练 PPO 演员-评论家策略。
  ko: 본 논문은 안전한 구동 공간 탐색으로부터 순환 전진 동역학 모델을 학습하고 GPU에서 병렬 JAX/Gymnax 학습 환경 내에서 PPO 액터-크리틱 정책을 훈련하는 소프트 공압 매니퓰레이터를 위한 모델 기반
    강화 학습 파이프라인을 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robotics
- reinforcement_learning
- model_based_rl
- ppo
- actor_critic
- lstm
- learned_dynamics
- jax
- gymnax
- pneumatic_actuator
- gpu_training
- closed_loop_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.18519v2.
sources:
- id: src_001
  type: paper
  title: Towards Reinforcement Learning Controllers for Soft Robots using Learned Environments
  url: https://arxiv.org/abs/2410.18519
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Soft robotic manipulators offer operational advantage due to their compliant and deformable structures. However, their inherently nonlinear dynamics presents substantial challenges. Traditional analytical methods often depend on simplifying assumptions, while learning-based techniques can be computationally demanding and limit the control policies to existing data. This paper introduces a novel approach to soft robotic control, leveraging state-of-the-art policy gradient methods within parallelizable synthetic environments learned from data. We also propose a safety oriented actuation space exploration protocol via cascaded updates and weighted randomness. Specifically, our recurrent forward dynamics model is learned by generating a training dataset from a physically safe \textit{mean reverting} random walk in actuation space to explore the partially-observed state-space. We demonstrate a reinforcement learning approach towards closed-loop control through state-of-the-art actor-critic methods, which efficiently learn high-performance behaviour over long horizons. This approach removes the need for any knowledge regarding the robot's operation or capabilities and sets the stage for a comprehensive benchmarking tool in soft robotics control.

## 核心内容
Soft robotic manipulators offer operational advantage due to their compliant and deformable structures. However, their inherently nonlinear dynamics presents substantial challenges. Traditional analytical methods often depend on simplifying assumptions, while learning-based techniques can be computationally demanding and limit the control policies to existing data. This paper introduces a novel approach to soft robotic control, leveraging state-of-the-art policy gradient methods within parallelizable synthetic environments learned from data. We also propose a safety oriented actuation space exploration protocol via cascaded updates and weighted randomness. Specifically, our recurrent forward dynamics model is learned by generating a training dataset from a physically safe \textit{mean reverting} random walk in actuation space to explore the partially-observed state-space. We demonstrate a reinforcement learning approach towards closed-loop control through state-of-the-art actor-critic methods, which efficiently learn high-performance behaviour over long horizons. This approach removes the need for any knowledge regarding the robot's operation or capabilities and sets the stage for a comprehensive benchmarking tool in soft robotics control.

## 参考
- http://arxiv.org/abs/2410.18519v2

