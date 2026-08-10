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
  zh: RoboBallet 提出一种基于图神经网络（GNN）与深度强化学习（RL）的框架，用于多机器人在共享、障碍密集工作单元中的联合任务分配、调度与无碰撞运动规划。该策略在程序化生成的环境上训练，可零样本泛化至未见过的布局，并支持实时推理。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05397v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (854 chars, DeepSeek).'
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
现代机器人制造中，多机器人在共享且障碍密集的工作空间内协调完成大量任务，其联合任务分配、调度与运动规划在时空约束下对经典方法而言计算上难以处理。现有工业多臂系统依赖人工经验手动设计轨迹，过程繁琐。RoboBallet 通过强化学习训练图神经网络策略，在包含八台机器人执行四十个到达任务的障碍密集环境中进行测试，任何机器人可任意顺序执行任何任务。该策略在程序化生成的不同障碍布局、机器人配置与任务分布上训练，采用场景图表示与图策略网络，联合求解任务分配、调度与运动规划子问题。训练后的策略可零样本泛化至机器人位置、障碍几何与任务姿态均变化的新场景，其高速能力还可用于工作单元布局优化，并支持容错规划与基于感知的在线重规划。

## 核心内容
### 方法
- 采用**图神经网络（GNN）** 作为策略网络，将场景表示为图：节点代表机器人与任务目标，边编码空间关系与约束。
- 通过**深度强化学习（RL）** 训练策略，在程序化生成的环境上学习联合决策，环境包含多样化的障碍布局、机器人配置与任务分布。
- 策略输出多机器人轨迹，同时解决三个子问题：任务分配（哪个机器人执行哪个任务）、调度（任务执行顺序）与运动规划（无碰撞路径）。

### 实验设置
- 测试环境：共享工作空间中部署**八台机器人**，需完成**四十个到达任务**，工作空间内布满障碍物。
- 任何机器人可执行任何任务，且任务顺序不限，增加了组合复杂度。
- 训练在仿真中进行，使用大规模随机生成的任务集，确保策略的泛化能力。

### 关键结果
- **零样本泛化**：训练后的策略可直接应用于未见过的场景，包括不同的机器人位置、障碍物几何形状与任务姿态，无需重新训练。
- **实时推理**：策略推理速度极快，支持实时在线应用。
- **布局优化**：高速求解能力可用于工作单元布局优化，显著缩短方案设计时间。
- **扩展能力**：支持容错规划（如机器人故障时快速重分配任务）与基于感知的在线重规划，适应动态任务集变化。

## Overview
Modern robotic manufacturing requires collision-free coordination of multiple robots to complete numerous tasks in shared, obstacle-rich workspaces. Although individual tasks may be simple in isolation, automated joint task allocation, scheduling, and motion planning under spatio-temporal constraints remain computationally intractable for classical methods at real-world scales. Existing multi-arm systems deployed in the industry rely on human intuition and experience to design feasible trajectories manually in a labor-intensive process. To address this challenge, we propose a reinforcement learning (RL) framework to achieve automated task and motion planning, tested in an obstacle-rich environment with eight robots performing 40 reaching tasks in a shared workspace, where any robot can perform any task in any order. Our approach builds on a graph neural network (GNN) policy trained via RL on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. It employs a graph representation of scenes and a graph policy neural network trained through reinforcement learning to generate trajectories of multiple robots, jointly solving the sub-problems of task allocation, scheduling, and motion planning. Trained on large randomly generated task sets in simulation, our policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses. We further demonstrate that the high-speed capability of our solution enables its use in workcell layout optimization, improving solution times. The speed and scalability of our planner also open the door to new capabilities such as fault-tolerant planning and online perception-based re-planning, where rapid adaptation to dynamic task sets is required.

## 参考
- http://arxiv.org/abs/2509.05397v1

## 개요
현대 로봇 제조에서 다중 로봇이 공유되고 장애물이 밀집된 작업 공간 내에서 대량의 작업을 조정하여 수행할 때, 결합된 작업 할당, 스케줄링 및 운동 계획은 시공간 제약 하에서 기존 방법으로는 계산적으로 다루기 어렵습니다. 기존 산업용 다중 암 시스템은 수동 경험에 의존하여 궤적을 수동으로 설계하며, 그 과정은 번거롭습니다. RoboBallet은 강화 학습을 통해 그래프 신경망 정책을 훈련하며, 여덟 대의 로봇이 40개의 도달 작업을 수행하는 장애물 밀집 환경에서 테스트되며, 어떤 로봇이든 임의의 순서로 어떤 작업이든 수행할 수 있습니다. 이 정책은 프로그램 방식으로 생성된 다양한 장애물 배치, 로봇 구성 및 작업 분포에서 훈련되며, 장면 그래프 표현과 그래프 정책 네트워크를 사용하여 작업 할당, 스케줄링 및 운동 계획 하위 문제를 결합하여 해결합니다. 훈련된 정책은 로봇 위치, 장애물 기하학 및 작업 자세가 모두 변화하는 새로운 장면에 제로샷 일반화할 수 있으며, 그 고속 능력은 작업 셀 레이아웃 최적화에도 사용될 수 있고, 내결함성 계획 및 인식 기반 온라인 재계획을 지원합니다.

## 핵심 내용
### 방법
- **그래프 신경망(GNN)** 을 정책 네트워크로 사용하여 장면을 그래프로 표현합니다: 노드는 로봇과 작업 목표를 나타내고, 엣지는 공간 관계와 제약을 인코딩합니다.
- **심층 강화 학습(RL)** 을 통해 정책을 훈련하며, 프로그램 방식으로 생성된 환경에서 결합 의사 결정을 학습합니다. 환경은 다양한 장애물 배치, 로봇 구성 및 작업 분포를 포함합니다.
- 정책은 다중 로봇 궤적을 출력하며, 세 가지 하위 문제를 동시에 해결합니다: 작업 할당(어떤 로봇이 어떤 작업을 수행할지), 스케줄링(작업 실행 순서) 및 운동 계획(충돌 없는 경로).

### 실험 설정
- 테스트 환경: 공유 작업 공간에 **여덟 대의 로봇**이 배치되며, **40개의 도달 작업**을 완료해야 하고, 작업 공간에는 장애물이 가득합니다.
- 어떤 로봇이든 어떤 작업이든 수행할 수 있으며, 작업 순서도 제한이 없어 조합 복잡도가 증가합니다.
- 훈련은 시뮬레이션에서 수행되며, 대규모 무작위 생성 작업 세트를 사용하여 정책의 일반화 능력을 보장합니다.

### 주요 결과
- **제로샷 일반화**: 훈련된 정책은 재훈련 없이 보지 못한 장면에 직접 적용할 수 있으며, 다른 로봇 위치, 장애물 기하학적 형태 및 작업 자세를 포함합니다.
- **실시간 추론**: 정책 추론 속도가 매우 빨라 실시간 온라인 응용을 지원합니다.
- **레이아웃 최적화**: 고속 해결 능력은 작업 셀 레이아웃 최적화에 사용될 수 있어 설계 시간을 크게 단축합니다.
- **확장 능력**: 내결함성 계획(예: 로봇 고장 시 빠른 작업 재할당) 및 인식 기반 온라인 재계획을 지원하여 동적 작업 세트 변화에 적응합니다.
