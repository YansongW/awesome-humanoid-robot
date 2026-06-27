---
$id: ent_paper_lai_roboballet_planning_for_multi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboBallet: Planning for Multi-Robot Reaching with Graph Neural Networks and
    Reinforcement Learning'
  zh: RoboBallet：基于图神经网络与强化学习的多机器人 reaching 规划
  ko: 'RoboBallet: 그래프 신경망과 강화학습을 활용한 다중 로봇 reaching 계획'
summary:
  en: RoboBallet trains a graph neural network policy via deep reinforcement learning
    to jointly allocate, schedule, and plan collision-free motions for multiple robots
    in shared, obstacle-rich workcells, demonstrating zero-shot generalization to
    unseen layouts and real-time inference.
  zh: RoboBallet 通过深度强化学习训练图神经网络策略，在共享的、充满障碍的工作单元中联合为多台机器人分配任务、调度并规划无碰撞运动，展现出对未见过布局的零样本泛化能力与实时推理能力。
  ko: RoboBallet는 심층 강화학습으로 그래프 신경망 정책을 학습시켜 장애물이 많은 공유 워크셀에서 여러 로봇의 작업 할당, 스케줄링 및
    충돌 없는 모션 계획을 통합적으로 수행하며, 보지 못한 레이아웃에 대한 제로샷 일반화와 실시간 추론을 보여준다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata/abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'RoboBallet: Planning for Multi-Robot Reaching with Graph Neural Networks
    and Reinforcement Learning'
  url: https://arxiv.org/abs/2509.05397
  date: '2025'
  accessed_at: '2026-06-27'
  doi: 10.1126/scirobotics.ads1204
theoretical_depth:
- method
---

## Overview

RoboBallet addresses the problem of coordinating multiple robotic manipulators in dense, shared workspaces. It frames task allocation, scheduling, and collision-free motion planning as a single learning problem and solves it with a graph neural network policy trained via deep reinforcement learning. The policy operates on a scene graph whose nodes represent robots, tasks, and obstacles, and directly outputs joint velocities for all robots at each timestep. By training on procedurally generated environments with varied robot placements, obstacle geometries, and task distributions, the method generalizes zero-shot to unseen hand-designed workcells. The authors report real-time inference speeds and demonstrate downstream uses such as workcell layout optimization, fault-tolerant re-planning, and online perception-based re-planning.

The paper situates its contribution in industrial robotic manufacturing, where existing multi-arm deployments still rely on human experts to manually design trajectories. The proposed approach removes the need for hand-engineered simplifications by jointly learning the sub-problems that are normally treated separately. The method is compared against an RRT-Connect baseline and validated both in simulation and on a real multi-Franka-Panda workcell.

## Key Contributions

- A graph-based state representation and GNN policy/value architecture that scales to varying numbers of robots, tasks, and obstacles without increasing model size.
- Joint learning of task allocation, scheduling, inverse-kinematics selection, and collision-free motion planning in a single RL framework.
- Zero-shot generalization from randomized simulation training to unseen hand-designed workcells with real-world obstacle geometry.
- Real-time planning enabling downstream applications including workcell layout optimization, fault-tolerant re-planning, and perception-based online re-planning.
- Real-world validation on a multi-Franka-Panda workcell and empirical comparison with an RRT-Connect baseline.

## Relevance to Humanoid Robotics

The paper's core contribution—scalable, collision-free multi-robot task allocation, scheduling, and motion planning—is directly relevant to humanoid robot mass production. Humanoid manufacturing workcells are expected to coordinate multiple manipulators or whole-body robots in dense, shared assembly spaces, where fast planning and layout optimization can increase throughput and adaptability. The graph-based, learning-driven approach could be transferred to humanoid workcells that must dynamically re-plan around moving obstacles, robot faults, or changing task sets. Although the demonstrations use fixed-base industrial arms, the method's emphasis on generalization and real-time inference addresses key bottlenecks for humanoid deployment at scale.
