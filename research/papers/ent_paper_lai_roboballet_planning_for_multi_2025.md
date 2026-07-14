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

