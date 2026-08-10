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
  zh: 本文提出了一个用于评估动作约束强化学习算法的基准，对比了现有算法及新型TD3/SAC变体在MuJoCo和PyBullet-Gym任务中的表现，涵盖线性、凸、盒状和椭圆四种约束类型，并公开了基准代码。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.08743v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (711 chars, DeepSeek).'
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
该研究聚焦于动作约束强化学习，要求学习系统采取的每个动作必须满足特定约束，这对现实系统的可行性和安全性至关重要。作者在多个机器人控制环境中评估了现有算法及其新型变体，覆盖多种动作约束类型。这是该领域首次深入的评估，揭示了令人意外的发现，包括一个简单基线方法的有效性。所有基准问题和相关代码已开源在github.com/omron-sinicx/action-constrained-RL-benchmark。

## 核心内容
### 方法
- 动作约束强化学习要求每个动作必须符合预设约束，确保现实世界中的可行性与安全性。
- 研究对比了现有算法（如PPO、DDPG）与新型TD3/SAC变体，后者通过修改策略网络或目标函数来显式处理约束。

### 架构与实验设置
- 实验环境包括MuJoCo和PyBullet-Gym中的机器人控制任务，如Ant、HalfCheetah、Humanoid等。
- 动作约束类型分为四类：线性约束（如动作之和不超过阈值）、凸约束（如动作位于凸多边形内）、盒状约束（如每个动作分量有独立上下界）、椭圆约束（如动作位于椭圆区域内）。
- 每个算法在每种约束类型下运行多次，记录平均回报和约束违反率。

### 关键数字与结论
- 新型TD3/SAC变体在多数任务中优于原始算法，尤其在复杂约束（如椭圆约束）下表现突出。
- 一个简单的基线方法（如直接裁剪动作到约束边界）在某些任务中意外地具有竞争力，甚至超过复杂算法。
- 实验表明，动作约束类型对算法性能有显著影响：线性约束下算法差异较小，而椭圆约束下新型变体优势明显。
- 所有代码和基准问题已开源，便于复现和进一步研究。

## Overview
This study presents a benchmark for evaluating action-constrained reinforcement learning (RL) algorithms. In action-constrained RL, each action taken by the learning system must comply with certain constraints. These constraints are crucial for ensuring the feasibility and safety of actions in real-world systems. We evaluate existing algorithms and their novel variants across multiple robotics control environments, encompassing multiple action constraint types. Our evaluation provides the first in-depth perspective of the field, revealing surprising insights, including the effectiveness of a straightforward baseline approach. The benchmark problems and associated code utilized in our experiments are made available online at github.com/omron-sinicx/action-constrained-RL-benchmark for further research and development.

## 参考
- http://arxiv.org/abs/2304.08743v2

## 개요
이 연구는 동작 제약 강화 학습에 초점을 맞추며, 학습 시스템이 취하는 모든 동작이 특정 제약을 충족해야 한다는 요구를 다룹니다. 이는 실제 시스템의 실현 가능성과 안전성에至关重要합니다. 저자들은 여러 로봇 제어 환경에서 기존 알고리즘과 새로운 변형 알고리즘을 평가하며, 다양한 동작 제약 유형을 포괄합니다. 이는 이 분야에서 최초의 심층 평가로, 간단한 기준 방법의 효과성을 포함한 놀라운 발견을 드러냅니다. 모든 벤치마크 문제와 관련 코드는 github.com/omron-sinicx/action-constrained-RL-benchmark에 공개되어 있습니다.

## 핵심 내용
### 방법
- 동작 제약 강화 학습은 모든 동작이 사전 설정된 제약을 충족해야 하며, 실제 세계에서의 실현 가능성과 안전성을 보장합니다.
- 연구는 기존 알고리즘(예: PPO, DDPG)과 새로운 TD3/SAC 변형을 비교하며, 후자는 정책 네트워크 또는 목적 함수를 수정하여 제약을 명시적으로 처리합니다.

### 아키텍처 및 실험 설정
- 실험 환경에는 MuJoCo 및 PyBullet-Gym의 로봇 제어 작업(예: Ant, HalfCheetah, Humanoid)이 포함됩니다.
- 동작 제약 유형은 네 가지로 분류됩니다: 선형 제약(예: 동작 합이 임계값을 초과하지 않음), 볼록 제약(예: 동작이 볼록 다각형 내에 위치), 상자형 제약(예: 각 동작 구성 요소에 독립적인 상한 및 하한), 타원 제약(예: 동작이 타원 영역 내에 위치).
- 각 알고리즘은 각 제약 유형에서 여러 번 실행되며, 평균 보상과 제약 위반 비율이 기록됩니다.

### 주요 수치 및 결론
- 새로운 TD3/SAC 변형은 대부분의 작업에서 원래 알고리즘보다 우수하며, 특히 복잡한 제약(예: 타원 제약)에서 두드러진 성능을 보입니다.
- 간단한 기준 방법(예: 동작을 제약 경계로 직접 클리핑)은 일부 작업에서 예상외로 경쟁력이 있으며, 복잡한 알고리즘을 능가하기도 합니다.
- 실험은 동작 제약 유형이 알고리즘 성능에 상당한 영향을 미친다는 것을 보여줍니다: 선형 제약에서는 알고리즘 간 차이가 작지만, 타원 제약에서는 새로운 변형의 우위가 명확합니다.
- 모든 코드와 벤치마크 문제는 공개되어 있어 재현 및 추가 연구가 용이합니다.
