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
  zh: 提出了RTMBA，一种基于模型的强化学习并行架构，利用基于样本的近似规划和三个并发线程（执行、模型学习、规划），并通过互斥锁保护共享状态，从而能够以机器人的控制频率返回动作；在Mountain Car和自主车辆上进行了评估。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1105.1749v2.
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
Reinforcement Learning (RL) is a method for learning decision-making tasks that could enable robots to learn and adapt to their situation on-line. For an RL algorithm to be practical for robotic control tasks, it must learn in very few actions, while continually taking those actions in real-time. Existing model-based RL methods learn in relatively few actions, but typically take too much time between each action for practical on-line learning. In this paper, we present a novel parallel architecture for model-based RL that runs in real-time by 1) taking advantage of sample-based approximate planning methods and 2) parallelizing the acting, model learning, and planning processes such that the acting process is sufficiently fast for typical robot control cycles. We demonstrate that algorithms using this architecture perform nearly as well as methods using the typical sequential architecture when both are given unlimited time, and greatly out-perform these methods on tasks that require real-time actions such as controlling an autonomous vehicle.

## 核心内容
Reinforcement Learning (RL) is a method for learning decision-making tasks that could enable robots to learn and adapt to their situation on-line. For an RL algorithm to be practical for robotic control tasks, it must learn in very few actions, while continually taking those actions in real-time. Existing model-based RL methods learn in relatively few actions, but typically take too much time between each action for practical on-line learning. In this paper, we present a novel parallel architecture for model-based RL that runs in real-time by 1) taking advantage of sample-based approximate planning methods and 2) parallelizing the acting, model learning, and planning processes such that the acting process is sufficiently fast for typical robot control cycles. We demonstrate that algorithms using this architecture perform nearly as well as methods using the typical sequential architecture when both are given unlimited time, and greatly out-perform these methods on tasks that require real-time actions such as controlling an autonomous vehicle.

## 参考
- http://arxiv.org/abs/1105.1749v2

