---
$id: ent_paper_kasaura_benchmarking_actor_critic_deep_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Actor-Critic Deep Reinforcement Learning Algorithms for Robotics
    Control with Action Constraints
  zh: 动作约束下机器人控制的演员-评论家深度强化学习算法基准测试
  ko: 동작 제약 조건 하의 로봇 제어를 위한 액터-크리틱 심층 강화학습 알고리즘 벤치마킹
summary:
  en: This paper introduces a benchmark for action-constrained reinforcement learning,
    comparing existing algorithms and novel TD3/SAC variants on MuJoCo and PyBullet-Gym
    tasks under linear, convex, box, and elliptical action constraints, and releases
    the benchmark code.
  zh: 本研究提出了一个动作约束强化学习算法评估基准，在线性、凸、盒型和椭圆型动作约束下，对MuJoCo与PyBullet-Gym任务中的现有算法及新型TD3/SAC变体进行了比较，并公开了基准代码。
  ko: 본 연구는 선형, 볼록, 박스, 타원형 동작 제약 조건 하에서 MuJoCo 및 PyBullet-Gym 작업의 기존 알고리즘과 새로운 TD3/SAC
    변형을 비교하고 벤치마크 코드를 공개하는 동작 제약 강화학습 평가 기준을 제시한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- action_constrained_rl
- actor_critic
- continuous_control
- reinforcement_learning
- robotics_benchmark
- safety_constraints
- mujoco
- pybullet_gym
- humanoid_control
- actuator_limits
- td3
- sac
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the arXiv full text; factual claims are supported by the
    paper, but human review is required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Benchmarking Actor-Critic Deep Reinforcement Learning Algorithms for Robotics
    Control with Action Constraints
  url: https://arxiv.org/abs/2304.08743
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Action-constrained reinforcement learning requires every action executed by a learning agent to lie inside a feasible set defined for each state. Such constraints arise naturally in robotics, where actuator torque limits, collision-avoidance requirements, or task-specific bounds must be respected to guarantee safe and feasible control. The paper presents the first comprehensive benchmark study dedicated to actor-critic deep RL algorithms under four classes of action constraints: linear, convex, box, and elliptical. It evaluates both existing methods and new algorithmic variants, measuring learning performance as well as computational runtime.
The experiments are conducted on standard continuous-control tasks from MuJoCo (Hopper, Walker2d, HalfCheetah) and PyBullet-Gym (Reacher), all exposed through the OpenAI Gym interface. The base algorithms are TD3 and SAC, chosen for their sample efficiency. The authors compare projection-based approaches (closest-point projection, differentiable optimization layers, Neural Frank-Wolfe Policy Optimization), mapping-based approaches (alpha-projection and the newly proposed radial squashing), and a simple baseline that trains the critic with pre-projected actions while projecting only during environment transitions. Code and benchmark environments are released to support reproducible follow-up work.

## Key Contributions

- First comprehensive benchmark of action-constrained actor-critic RL algorithms spanning linear, convex, box, and elliptical constraints.
- Introduction of simple yet competitive baselines that train the critic with pre-projected actions, showing comparable performance to specialized algorithms.
- Proposal of radial squashing, a differentiable neural-network layer that maps suggested actions into feasible action sets.
- Extension of action-constrained techniques to SAC, including non-trivial entropy handling for alpha-projection and a tractable Jacobian for radial squashing.
- Public release of benchmark tasks and implementation code at github.com/omron-sinicx/action-constrained-RL-benchmark.

## Relevance to Humanoid Robotics

Humanoid robots must respect tight actuator torque and joint-limit constraints during dynamic whole-body motions. Violations can damage hardware or cause falls, so low-level motion policies and whole-body controllers are typically required to produce only feasible actions. The benchmark directly addresses this need by evaluating how deep RL agents can learn continuous controllers while enforcing action constraints during training.
The constraints studied in the paper (box bounds, linear/coupled torque limits, and elliptical feasibility regions) map closely to the torque and kinematic limits encountered in humanoid locomotion and manipulation. The finding that simple pre-projected-action baselines are competitive, and that radial squashing and alpha-projection provide efficient alternatives to expensive optimization layers, is especially relevant for deploying RL-based policies on real humanoid hardware with limited compute budgets.
