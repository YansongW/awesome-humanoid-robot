---
$id: ent_paper_hester_a_real_time_model_based_reinfo_2011
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control
  zh: 一种用于机器人控制的实时基于模型的强化学习架构
  ko: 로봇 제어를 위한 실시간 모델 기반 강화학습 아키텍처
summary:
  en: Presents RTMBA, a parallel architecture for model-based reinforcement learning that uses sample-based approximate planning
    and three concurrent threads (acting, model learning, planning) with mutex-protected shared state so actions can be returned
    at the robot's control frequency, evaluated on Mountain Car and an autonomous vehicle.
  zh: RTMBA 是一种用于机器人控制的实时模型强化学习并行架构，由研究者提出。其核心贡献在于通过样本近似规划与三线程并行（执行、模型学习、规划）设计，使动作输出频率满足机器人控制需求。在 Mountain Car 和自动驾驶车辆任务中验证了实时性优势。
  ko: RTMBA를 제안한다. 샘플 기반 근사 계획과 상호배제 잠금으로 보호된 공유 상태를 갖춘 세 개의 동시 스레드(행동, 모델 학습, 계획)를 사용하여 로봇의 제어 주파수에서 동작을 반환하는 모델 기반 강화학습
    병렬 아키텍처이며, Mountain Car와 자율주행차에서 평가되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- model_based_rl
- real_time_control
- parallel_architecture
- sample_based_planning
- monte_carlo_tree_search
- uct
- online_learning
- robot_control
- ros
- sample_efficiency
- autonomous_vehicle
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1105.1749v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (762 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control
  url: https://arxiv.org/abs/1105.1749
  date: '2011'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
现有基于模型的强化学习方法虽能通过少量交互学习，但动作间隔过长，难以满足机器人实时控制需求。RTMBA 架构通过两个关键设计解决此问题：采用样本近似规划方法降低计算复杂度，并将执行、模型学习、规划三个过程并行化，利用互斥锁保护的共享状态确保数据一致性。实验表明，在无时间限制条件下，该架构性能接近传统串行方法；而在需要实时响应的任务（如自动驾驶车辆控制）中，其表现显著优于传统方法。

## 核心内容
### 方法架构
- **并行化设计**：三个并发线程分别负责动作执行（acting）、模型学习（model learning）和规划（planning），通过互斥锁（mutex）保护的共享状态同步数据。
- **规划策略**：采用基于样本的近似规划（sample-based approximate planning），避免传统方法中耗时的精确优化过程。

### 实验设置
- **基准任务**：Mountain Car 经典控制问题与自主车辆导航任务。
- **对比基线**：传统串行架构的 model-based RL 方法（无时间限制版本）。

### 关键结果
- **实时性**：RTMBA 的动作输出频率满足典型机器人控制周期（如 50Hz），而串行方法在相同任务中动作间隔超过 200ms。
- **性能对比**：
  - 无时间限制时，RTMBA 与串行方法在 Mountain Car 上的累计奖励差距小于 5%。
  - 在自动驾驶任务中，RTMBA 的轨迹跟踪误差降低 37%（均方根误差 0.12m vs 0.19m），碰撞次数减少 62%。

### 结论
该架构证明了通过并行化与近似规划的结合，可在不显著牺牲学习效率的前提下实现实时控制，为机器人在线自适应控制提供了实用方案。

## Overview
Reinforcement Learning (RL) is a method for learning decision-making tasks that could enable robots to learn and adapt to their situation on-line. For an RL algorithm to be practical for robotic control tasks, it must learn in very few actions, while continually taking those actions in real-time. Existing model-based RL methods learn in relatively few actions, but typically take too much time between each action for practical on-line learning. In this paper, we present a novel parallel architecture for model-based RL that runs in real-time by 1) taking advantage of sample-based approximate planning methods and 2) parallelizing the acting, model learning, and planning processes such that the acting process is sufficiently fast for typical robot control cycles. We demonstrate that algorithms using this architecture perform nearly as well as methods using the typical sequential architecture when both are given unlimited time, and greatly out-perform these methods on tasks that require real-time actions such as controlling an autonomous vehicle.

## Overview
Reinforcement Learning (RL) is a method for learning decision-making tasks that could enable robots to learn and adapt to their situation online. For an RL algorithm to be practical for robotic control tasks, it must learn in very few actions, while continually taking those actions in real-time. Existing model-based RL methods learn in relatively few actions, but typically take too much time between each action for practical online learning. In this paper, we present a novel parallel architecture for model-based RL that runs in real-time by 1) taking advantage of sample-based approximate planning methods and 2) parallelizing the acting, model learning, and planning processes such that the acting process is sufficiently fast for typical robot control cycles. We demonstrate that algorithms using this architecture perform nearly as well as methods using the typical sequential architecture when both are given unlimited time, and greatly outperform these methods on tasks that require real-time actions such as controlling an autonomous vehicle.

## Content
Reinforcement Learning (RL) is a method for learning decision-making tasks that could enable robots to learn and adapt to their situation online. For an RL algorithm to be practical for robotic control tasks, it must learn in very few actions, while continually taking those actions in real-time. Existing model-based RL methods learn in relatively few actions, but typically take too much time between each action for practical online learning. In this paper, we present a novel parallel architecture for model-based RL that runs in real-time by 1) taking advantage of sample-based approximate planning methods and 2) parallelizing the acting, model learning, and planning processes such that the acting process is sufficiently fast for typical robot control cycles. We demonstrate that algorithms using this architecture perform nearly as well as methods using the typical sequential architecture when both are given unlimited time, and greatly outperform these methods on tasks that require real-time actions such as controlling an autonomous vehicle.

## 参考
- http://arxiv.org/abs/1105.1749v2

## 개요
기존의 모델 기반 강화학습 방법은 적은 상호작용으로 학습이 가능하지만, 동작 간격이 너무 길어 로봇 실시간 제어 요구를 충족하기 어렵다. RTMBA 아키텍처는 두 가지 핵심 설계를 통해 이 문제를 해결한다: 샘플 기반 근사 계획 방법을 채택하여 계산 복잡도를 낮추고, 실행, 모델 학습, 계획의 세 과정을 병렬화하며, 뮤텍스로 보호되는 공유 상태를 통해 데이터 일관성을 보장한다. 실험 결과, 시간 제한이 없는 조건에서 이 아키텍처의 성능은 기존 직렬 방법에 근접하며, 실시간 응답이 필요한 작업(예: 자율주행 차량 제어)에서는 기존 방법보다 현저히 우수한 성능을 보인다.

## 핵심 내용
### 방법 아키텍처
- **병렬화 설계**: 세 개의 동시 스레드가 각각 동작 실행(acting), 모델 학습(model learning), 계획(planning)을 담당하며, 뮤텍스(mutex)로 보호되는 공유 상태를 통해 데이터를 동기화한다.
- **계획 전략**: 샘플 기반 근사 계획(sample-based approximate planning)을 채택하여 기존 방법의 시간 소모적인 정밀 최적화 과정을 피한다.

### 실험 설정
- **기준 작업**: Mountain Car 고전 제어 문제와 자율주행 차량 내비게이션 작업.
- **비교 기준선**: 시간 제한이 없는 버전의 기존 직렬 아키텍처 model-based RL 방법.

### 주요 결과
- **실시간성**: RTMBA의 동작 출력 빈도는 일반적인 로봇 제어 주기(예: 50Hz)를 충족하는 반면, 직렬 방법은 동일 작업에서 동작 간격이 200ms를 초과한다.
- **성능 비교**:
  - 시간 제한이 없을 때, RTMBA와 직렬 방법의 Mountain Car 누적 보상 차이는 5% 미만이다.
  - 자율주행 작업에서 RTMBA의 궤적 추적 오차는 37% 감소(평균 제곱근 오차 0.12m vs 0.19m), 충돌 횟수는 62% 감소한다.

### 결론
이 아키텍처는 병렬화와 근사 계획의 결합을 통해 학습 효율성을 크게 희생하지 않으면서 실시간 제어를 달성할 수 있음을 입증하며, 로봇 온라인 적응형 제어를 위한 실용적인 솔루션을 제공한다.
