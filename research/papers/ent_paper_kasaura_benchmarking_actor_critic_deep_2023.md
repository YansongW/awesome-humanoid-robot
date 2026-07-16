---
$id: ent_paper_kasaura_benchmarking_actor_critic_deep_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Actor-Critic Deep Reinforcement Learning Algorithms for Robotics Control with Action Constraints
  zh: 动作约束下机器人控制的演员-评论家深度强化学习算法基准测试
  ko: 동작 제약 조건 하의 로봇 제어를 위한 액터-크리틱 심층 강화학습 알고리즘 벤치마킹
summary:
  en: This paper introduces a benchmark for action-constrained reinforcement learning, comparing existing algorithms and novel
    TD3/SAC variants on MuJoCo and PyBullet-Gym tasks under linear, convex, box, and elliptical action constraints, and releases
    the benchmark code.
  zh: 本研究提出了一个动作约束强化学习算法评估基准，在线性、凸、盒型和椭圆型动作约束下，对MuJoCo与PyBullet-Gym任务中的现有算法及新型TD3/SAC变体进行了比较，并公开了基准代码。
  ko: 본 연구는 선형, 볼록, 박스, 타원형 동작 제약 조건 하에서 MuJoCo 및 PyBullet-Gym 작업의 기존 알고리즘과 새로운 TD3/SAC 변형을 비교하고 벤치마크 코드를 공개하는 동작 제약 강화학습
    평가 기준을 제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.08743v2.
sources:
- id: src_001
  type: paper
  title: Benchmarking Actor-Critic Deep Reinforcement Learning Algorithms for Robotics Control with Action Constraints
  url: https://arxiv.org/abs/2304.08743
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This study presents a benchmark for evaluating action-constrained reinforcement learning (RL) algorithms. In action-constrained RL, each action taken by the learning system must comply with certain constraints. These constraints are crucial for ensuring the feasibility and safety of actions in real-world systems. We evaluate existing algorithms and their novel variants across multiple robotics control environments, encompassing multiple action constraint types. Our evaluation provides the first in-depth perspective of the field, revealing surprising insights, including the effectiveness of a straightforward baseline approach. The benchmark problems and associated code utilized in our experiments are made available online at github.com/omron-sinicx/action-constrained-RL-benchmark for further research and development.

## 核心内容
This study presents a benchmark for evaluating action-constrained reinforcement learning (RL) algorithms. In action-constrained RL, each action taken by the learning system must comply with certain constraints. These constraints are crucial for ensuring the feasibility and safety of actions in real-world systems. We evaluate existing algorithms and their novel variants across multiple robotics control environments, encompassing multiple action constraint types. Our evaluation provides the first in-depth perspective of the field, revealing surprising insights, including the effectiveness of a straightforward baseline approach. The benchmark problems and associated code utilized in our experiments are made available online at github.com/omron-sinicx/action-constrained-RL-benchmark for further research and development.

## 参考
- http://arxiv.org/abs/2304.08743v2

## Overview
This study presents a benchmark for evaluating action-constrained reinforcement learning (RL) algorithms. In action-constrained RL, each action taken by the learning system must comply with certain constraints. These constraints are crucial for ensuring the feasibility and safety of actions in real-world systems. We evaluate existing algorithms and their novel variants across multiple robotics control environments, encompassing multiple action constraint types. Our evaluation provides the first in-depth perspective of the field, revealing surprising insights, including the effectiveness of a straightforward baseline approach. The benchmark problems and associated code utilized in our experiments are made available online at github.com/omron-sinicx/action-constrained-RL-benchmark for further research and development.

## Content
This study presents a benchmark for evaluating action-constrained reinforcement learning (RL) algorithms. In action-constrained RL, each action taken by the learning system must comply with certain constraints. These constraints are crucial for ensuring the feasibility and safety of actions in real-world systems. We evaluate existing algorithms and their novel variants across multiple robotics control environments, encompassing multiple action constraint types. Our evaluation provides the first in-depth perspective of the field, revealing surprising insights, including the effectiveness of a straightforward baseline approach. The benchmark problems and associated code utilized in our experiments are made available online at github.com/omron-sinicx/action-constrained-RL-benchmark for further research and development.

## 개요
본 연구는 행동 제약 강화 학습(RL) 알고리즘을 평가하기 위한 벤치마크를 제시합니다. 행동 제약 RL에서 학습 시스템이 수행하는 각 행동은 특정 제약 조건을 준수해야 합니다. 이러한 제약 조건은 실제 시스템에서 행동의 실행 가능성과 안전성을 보장하는 데 중요합니다. 우리는 여러 로봇 제어 환경에서 다양한 행동 제약 유형을 포함하여 기존 알고리즘과 그 새로운 변형을 평가합니다. 본 평가는 해당 분야에 대한 최초의 심층적 관점을 제공하며, 간단한 기준 접근법의 효과성을 포함한 놀라운 통찰력을 드러냅니다. 실험에 사용된 벤치마크 문제와 관련 코드는 추가 연구 및 개발을 위해 github.com/omron-sinicx/action-constrained-RL-benchmark에서 온라인으로 제공됩니다.

## 핵심 내용
본 연구는 행동 제약 강화 학습(RL) 알고리즘을 평가하기 위한 벤치마크를 제시합니다. 행동 제약 RL에서 학습 시스템이 수행하는 각 행동은 특정 제약 조건을 준수해야 합니다. 이러한 제약 조건은 실제 시스템에서 행동의 실행 가능성과 안전성을 보장하는 데 중요합니다. 우리는 여러 로봇 제어 환경에서 다양한 행동 제약 유형을 포함하여 기존 알고리즘과 그 새로운 변형을 평가합니다. 본 평가는 해당 분야에 대한 최초의 심층적 관점을 제공하며, 간단한 기준 접근법의 효과성을 포함한 놀라운 통찰력을 드러냅니다. 실험에 사용된 벤치마크 문제와 관련 코드는 추가 연구 및 개발을 위해 github.com/omron-sinicx/action-constrained-RL-benchmark에서 온라인으로 제공됩니다.
