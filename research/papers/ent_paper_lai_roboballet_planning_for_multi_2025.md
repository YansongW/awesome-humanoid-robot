---
$id: ent_paper_lai_roboballet_planning_for_multi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboBallet: Planning for Multi-Robot Reaching with Graph Neural Networks and Reinforcement Learning'
  zh: RoboBallet：基于图神经网络与强化学习的多机器人 reaching 规划
  ko: 'RoboBallet: 그래프 신경망과 강화학습을 활용한 다중 로봇 reaching 계획'
summary:
  en: RoboBallet trains a graph neural network policy via deep reinforcement learning to jointly allocate, schedule, and plan
    collision-free motions for multiple robots in shared, obstacle-rich workcells, demonstrating zero-shot generalization
    to unseen layouts and real-time inference.
  zh: RoboBallet 通过深度强化学习训练图神经网络策略，在共享的、充满障碍的工作单元中联合为多台机器人分配任务、调度并规划无碰撞运动，展现出对未见过布局的零样本泛化能力与实时推理能力。
  ko: RoboBallet는 심층 강화학습으로 그래프 신경망 정책을 학습시켜 장애물이 많은 공유 워크셀에서 여러 로봇의 작업 할당, 스케줄링 및 충돌 없는 모션 계획을 통합적으로 수행하며, 보지 못한 레이아웃에 대한
    제로샷 일반화와 실시간 추론을 보여준다.
domains:
- 07_ai_models_algorithms
- 03_manufacturing_processes
- 05_mass_production
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_coordination
- graph_neural_network
- reinforcement_learning
- task_and_motion_planning
- collision_avoidance
- robotic_manufacturing
- zero_shot_generalization
- workcell_layout_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05397v1.
sources:
- id: src_001
  type: paper
  title: 'RoboBallet: Planning for Multi-Robot Reaching with Graph Neural Networks and Reinforcement Learning'
  url: https://arxiv.org/abs/2509.05397
  date: '2025'
  accessed_at: '2026-06-27'
  doi: 10.1126/scirobotics.ads1204
theoretical_depth:
- method
---
## 概述
Modern robotic manufacturing requires collision-free coordination of multiple robots to complete numerous tasks in shared, obstacle-rich workspaces. Although individual tasks may be simple in isolation, automated joint task allocation, scheduling, and motion planning under spatio-temporal constraints remain computationally intractable for classical methods at real-world scales. Existing multi-arm systems deployed in the industry rely on human intuition and experience to design feasible trajectories manually in a labor-intensive process. To address this challenge, we propose a reinforcement learning (RL) framework to achieve automated task and motion planning, tested in an obstacle-rich environment with eight robots performing 40 reaching tasks in a shared workspace, where any robot can perform any task in any order. Our approach builds on a graph neural network (GNN) policy trained via RL on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. It employs a graph representation of scenes and a graph policy neural network trained through reinforcement learning to generate trajectories of multiple robots, jointly solving the sub-problems of task allocation, scheduling, and motion planning. Trained on large randomly generated task sets in simulation, our policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses. We further demonstrate that the high-speed capability of our solution enables its use in workcell layout optimization, improving solution times. The speed and scalability of our planner also open the door to new capabilities such as fault-tolerant planning and online perception-based re-planning, where rapid adaptation to dynamic task sets is required.

## 核心内容
Modern robotic manufacturing requires collision-free coordination of multiple robots to complete numerous tasks in shared, obstacle-rich workspaces. Although individual tasks may be simple in isolation, automated joint task allocation, scheduling, and motion planning under spatio-temporal constraints remain computationally intractable for classical methods at real-world scales. Existing multi-arm systems deployed in the industry rely on human intuition and experience to design feasible trajectories manually in a labor-intensive process. To address this challenge, we propose a reinforcement learning (RL) framework to achieve automated task and motion planning, tested in an obstacle-rich environment with eight robots performing 40 reaching tasks in a shared workspace, where any robot can perform any task in any order. Our approach builds on a graph neural network (GNN) policy trained via RL on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. It employs a graph representation of scenes and a graph policy neural network trained through reinforcement learning to generate trajectories of multiple robots, jointly solving the sub-problems of task allocation, scheduling, and motion planning. Trained on large randomly generated task sets in simulation, our policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses. We further demonstrate that the high-speed capability of our solution enables its use in workcell layout optimization, improving solution times. The speed and scalability of our planner also open the door to new capabilities such as fault-tolerant planning and online perception-based re-planning, where rapid adaptation to dynamic task sets is required.

## 参考
- http://arxiv.org/abs/2509.05397v1

## Overview
Modern robotic manufacturing requires collision-free coordination of multiple robots to complete numerous tasks in shared, obstacle-rich workspaces. Although individual tasks may be simple in isolation, automated joint task allocation, scheduling, and motion planning under spatio-temporal constraints remain computationally intractable for classical methods at real-world scales. Existing multi-arm systems deployed in the industry rely on human intuition and experience to design feasible trajectories manually in a labor-intensive process. To address this challenge, we propose a reinforcement learning (RL) framework to achieve automated task and motion planning, tested in an obstacle-rich environment with eight robots performing 40 reaching tasks in a shared workspace, where any robot can perform any task in any order. Our approach builds on a graph neural network (GNN) policy trained via RL on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. It employs a graph representation of scenes and a graph policy neural network trained through reinforcement learning to generate trajectories of multiple robots, jointly solving the sub-problems of task allocation, scheduling, and motion planning. Trained on large randomly generated task sets in simulation, our policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses. We further demonstrate that the high-speed capability of our solution enables its use in workcell layout optimization, improving solution times. The speed and scalability of our planner also open the door to new capabilities such as fault-tolerant planning and online perception-based re-planning, where rapid adaptation to dynamic task sets is required.

## Content
Modern robotic manufacturing requires collision-free coordination of multiple robots to complete numerous tasks in shared, obstacle-rich workspaces. Although individual tasks may be simple in isolation, automated joint task allocation, scheduling, and motion planning under spatio-temporal constraints remain computationally intractable for classical methods at real-world scales. Existing multi-arm systems deployed in the industry rely on human intuition and experience to design feasible trajectories manually in a labor-intensive process. To address this challenge, we propose a reinforcement learning (RL) framework to achieve automated task and motion planning, tested in an obstacle-rich environment with eight robots performing 40 reaching tasks in a shared workspace, where any robot can perform any task in any order. Our approach builds on a graph neural network (GNN) policy trained via RL on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. It employs a graph representation of scenes and a graph policy neural network trained through reinforcement learning to generate trajectories of multiple robots, jointly solving the sub-problems of task allocation, scheduling, and motion planning. Trained on large randomly generated task sets in simulation, our policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses. We further demonstrate that the high-speed capability of our solution enables its use in workcell layout optimization, improving solution times. The speed and scalability of our planner also open the door to new capabilities such as fault-tolerant planning and online perception-based re-planning, where rapid adaptation to dynamic task sets is required.

## 개요
현대 로봇 제조는 장애물이 많은 공유 작업 공간에서 여러 로봇이 충돌 없이 협력하여 수많은 작업을 완료해야 합니다. 개별 작업은 단독으로는 단순할 수 있지만, 시공간적 제약 하에서 자동화된 공동 작업 할당, 스케줄링 및 모션 플래닝은 실제 규모에서 고전적 방법으로는 계산적으로 다루기 어렵습니다. 산업 현장에 배치된 기존 다중 암 시스템은 인간의 직관과 경험에 의존하여 노동 집약적인 과정을 통해 수동으로 실행 가능한 궤적을 설계합니다. 이 문제를 해결하기 위해 우리는 강화 학습(RL) 프레임워크를 제안하여 자동화된 작업 및 모션 플래닝을 달성하며, 8대의 로봇이 공유 작업 공간에서 40개의 도달 작업을 수행하는 장애물이 많은 환경에서 테스트되었습니다. 여기서 모든 로봇은 모든 작업을 어떤 순서로든 수행할 수 있습니다. 우리의 접근 방식은 다양한 장애물 배치, 로봇 구성 및 작업 분포를 가진 절차적으로 생성된 환경에서 RL을 통해 훈련된 그래프 신경망(GNN) 정책을 기반으로 합니다. 이는 장면의 그래프 표현과 강화 학습을 통해 훈련된 그래프 정책 신경망을 사용하여 여러 로봇의 궤적을 생성하며, 작업 할당, 스케줄링 및 모션 플래닝의 하위 문제를 공동으로 해결합니다. 시뮬레이션에서 대규모 무작위 생성 작업 세트로 훈련된 우리의 정책은 다양한 로봇 배치, 장애물 형상 및 작업 자세를 가진 보이지 않는 설정에 제로샷 일반화를 보여줍니다. 또한 우리 솔루션의 고속 기능이 작업 셀 레이아웃 최적화에 사용될 수 있음을 입증하여 솔루션 시간을 개선합니다. 플래너의 속도와 확장성은 동적 작업 세트에 대한 빠른 적응이 필요한 내결함성 플래닝 및 온라인 인식 기반 재플래닝과 같은 새로운 기능의 문을 열어줍니다.

## 핵심 내용
현대 로봇 제조는 장애물이 많은 공유 작업 공간에서 여러 로봇이 충돌 없이 협력하여 수많은 작업을 완료해야 합니다. 개별 작업은 단독으로는 단순할 수 있지만, 시공간적 제약 하에서 자동화된 공동 작업 할당, 스케줄링 및 모션 플래닝은 실제 규모에서 고전적 방법으로는 계산적으로 다루기 어렵습니다. 산업 현장에 배치된 기존 다중 암 시스템은 인간의 직관과 경험에 의존하여 노동 집약적인 과정을 통해 수동으로 실행 가능한 궤적을 설계합니다. 이 문제를 해결하기 위해 우리는 강화 학습(RL) 프레임워크를 제안하여 자동화된 작업 및 모션 플래닝을 달성하며, 8대의 로봇이 공유 작업 공간에서 40개의 도달 작업을 수행하는 장애물이 많은 환경에서 테스트되었습니다. 여기서 모든 로봇은 모든 작업을 어떤 순서로든 수행할 수 있습니다. 우리의 접근 방식은 다양한 장애물 배치, 로봇 구성 및 작업 분포를 가진 절차적으로 생성된 환경에서 RL을 통해 훈련된 그래프 신경망(GNN) 정책을 기반으로 합니다. 이는 장면의 그래프 표현과 강화 학습을 통해 훈련된 그래프 정책 신경망을 사용하여 여러 로봇의 궤적을 생성하며, 작업 할당, 스케줄링 및 모션 플래닝의 하위 문제를 공동으로 해결합니다. 시뮬레이션에서 대규모 무작위 생성 작업 세트로 훈련된 우리의 정책은 다양한 로봇 배치, 장애물 형상 및 작업 자세를 가진 보이지 않는 설정에 제로샷 일반화를 보여줍니다. 또한 우리 솔루션의 고속 기능이 작업 셀 레이아웃 최적화에 사용될 수 있음을 입증하여 솔루션 시간을 개선합니다. 플래너의 속도와 확장성은 동적 작업 세트에 대한 빠른 적응이 필요한 내결함성 플래닝 및 온라인 인식 기반 재플래닝과 같은 새로운 기능의 문을 열어줍니다.
