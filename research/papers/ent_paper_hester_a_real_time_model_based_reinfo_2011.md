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
  en: Presents RTMBA, a parallel architecture for model-based reinforcement learning
    that uses sample-based approximate planning and three concurrent threads (acting,
    model learning, planning) with mutex-protected shared state so actions can be
    returned at the robot's control frequency, evaluated on Mountain Car and an autonomous
    vehicle.
  zh: 提出了RTMBA，一种基于模型的强化学习并行架构，利用基于样本的近似规划和三个并发线程（执行、模型学习、规划），并通过互斥锁保护共享状态，从而能够以机器人的控制频率返回动作；在Mountain
    Car和自主车辆上进行了评估。
  ko: RTMBA를 제안한다. 샘플 기반 근사 계획과 상호배제 잠금으로 보호된 공유 상태를 갖춘 세 개의 동시 스레드(행동, 모델 학습, 계획)를
    사용하여 로봇의 제어 주파수에서 동작을 반환하는 모델 기반 강화학습 병렬 아키텍처이며, Mountain Car와 자율주행차에서 평가되었다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv full text; factual claims are sourced to the paper
    but have not been independently verified against a peer-reviewed version.
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

## Overview

The paper identifies two requirements for practical robotic reinforcement learning: sample efficiency and continual real-time action selection. It argues that existing model-based methods such as R-MAX are sample-efficient but typically require a complete model update and planning step between actions, which takes too much time for real-time robot control. To address this, the authors introduce the Real-Time Model-Based Architecture (RTMBA). RTMBA limits planning time by using sample-based approximate planners from the Monte Carlo Tree Search (MCTS) family, and it parallelizes acting, model learning, and planning into three threads. Mutex locks protect shared variables—the update list, current state, learned model, and per-state policy/value function—so the action thread can return an action immediately when requested while background threads update the model and perform rollouts.

The action thread adds a new transition to an update list, sets the agent's current state, and returns the action from the current policy. The model-learning thread batches new experiences into a copied model and atomically swaps it in. The planning thread repeatedly performs rollouts from the current state using UCT-style MCTS. Because each thread can run on a separate core, RTMBA can exploit multi-core processors common on robotic platforms. The authors evaluate the architecture against Q-Learning, DYNA, sequential value iteration, and sequential MCTS on Mountain Car, and demonstrate real-time velocity control on an Isuzu VehiCross autonomous vehicle in ROS stage simulation and on the physical robot.

## Key Contributions

- First parallel architecture for model-based RL that achieves both sample efficiency and continual real-time action selection.
- Uses sample-based approximate planning (MCTS/UCT) to bound planning time instead of exact dynamic-programming methods.
- Parallelizes model learning, planning, and acting into three threads with mutex locks protecting shared variables.
- Demonstrates real-time learning on an autonomous vehicle both in ROS stage simulation and on the physical Isuzu VehiCross.
- Shows that utilizing multiple cores improves learning performance over single-core execution.

## Relevance to Humanoid Robotics

Although RTMBA is demonstrated on a ground vehicle, the problem it solves—learning low-level control policies online while meeting hard real-time deadlines—is directly applicable to humanoid robots. Humanoid balance, locomotion, and manipulation all require controllers that can update at tens to hundreds of hertz and adapt from experience without an offline training phase. The architecture's separation of acting from model learning and planning, and its use of sample-based approximate planning, provide a domain-agnostic framework that can be instantiated for humanoid motor control. Its ROS-based implementation further eases integration with common humanoid robot software stacks.
