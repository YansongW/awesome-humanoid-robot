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
  en: This paper presents a model-based reinforcement learning pipeline for soft pneumatic
    manipulators that learns a recurrent forward-dynamics model from safe actuation-space
    exploration and trains PPO actor-critic policies inside a parallel JAX/Gymnax
    learned environment on GPU.
  zh: 本文提出了一种面向软体气动机械臂的基于模型的强化学习流程，通过安全驱动空间探索学习循环前向动力学模型，并在 GPU 上的并行 JAX/Gymnax 学习环境中训练
    PPO 演员-评论家策略。
  ko: 본 논문은 안전한 구동 공간 탐색으로부터 순환 전진 동역학 모델을 학습하고 GPU에서 병렬 JAX/Gymnax 학습 환경 내에서 PPO
    액터-크리틱 정책을 훈련하는 소프트 공압 매니퓰레이터를 위한 모델 기반 강화 학습 파이프라인을 제시한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    of section-level citations not performed.
sources:
- id: src_001
  type: paper
  title: Towards Reinforcement Learning Controllers for Soft Robots using Learned
    Environments
  url: https://arxiv.org/abs/2410.18519
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Soft robotic manipulators can operate safely around humans because of their compliant, deformable structures, but their highly nonlinear continuum dynamics make precise closed-loop control difficult. Traditional analytical models often rely on simplifying assumptions that fail to capture real behavior, while purely data-driven approaches can be computationally expensive and restrict control policies to the distribution of previously collected data. This paper proposes a pipeline that learns a recurrent LSTM forward-dynamics model directly from a physically safe exploration dataset and then uses that model as a parallelizable synthetic environment for GPU-based reinforcement learning.

The training dataset is generated through a constrained mean-reverting random walk in actuation space, which is designed to explore the partially observed state-space without exposing the hardware to unsafe pressures or motions. The learned recurrent model is wrapped in a JAX/Gymnax environment, enabling large-scale parallel rollouts and PPO actor-critic training entirely on GPU. The authors compare feed-forward and recurrent PPO policies over long-horizon reaching tasks and report that recurrent policies achieve stronger performance.

The work is positioned as a step toward a broader benchmarking tool for soft-robot control: by removing the need for analytical models or manually designed trajectories, the same pipeline could in principle be applied to a variety of soft robotic platforms once appropriate hardware data are available.

## Key Contributions

- A data-driven pipeline that learns soft-robot forward dynamics without analytical models or guiding trajectories.
- A safe actuation-space exploration protocol using a constrained mean-reverting random walk.
- A JAX/Gymnax learned-environment implementation enabling fully GPU-based parallel PPO training.
- An empirical comparison of feed-forward and recurrent PPO policies for long-horizon soft-robot reaching.

## Relevance to Humanoid Robotics

Although the experiments focus on a single soft pneumatic actuator rather than a full humanoid, the underlying methods are directly relevant to future humanoid systems. Compliant soft actuators and flexible limbs are promising for safe human-robot interaction and low-cost end-effectors, but their control remains an open problem. The paper's combination of learned recurrent dynamics, safe exploration, and GPU-accelerated model-based RL provides a reusable control methodology that could be scaled to soft joints, fingers, or continuum arms in humanoid robots. The approach also reduces dependence on accurate physics simulators, which is valuable when soft-body dynamics are hard to model analytically.
