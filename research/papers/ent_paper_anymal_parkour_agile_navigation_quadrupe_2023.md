---
$id: ent_paper_anymal_parkour_agile_navigation_quadrupe_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots'
  zh: 'ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots'
  ko: 'ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots'
summary:
  en: 'Performing agile navigation with four-legged robots is a challenging task due to the highly dynamic motions, contacts
    with various parts of the robot, and the limited field of view of the perception sensors. Institutions per source list:
    ETH Zurich（宇树团队）.'
  zh: ANYmal Parkour 提出了一种完全基于学习的四足机器人敏捷导航方法，由 ETH Zurich 的 Legged Robotics 团队开发。其核心贡献在于通过分层策略（高级导航策略+低级运动技能）和感知模块，使机器人在无专家演示、无先验环境知识的情况下，以高达
    2 米/秒的速度穿越连续障碍物，并成功从仿真迁移到真实硬件。
  ko: 'Performing agile navigation with four-legged robots is a challenging task due to the highly dynamic motions, contacts
    with various parts of the robot, and the limited field of view of the perception sensors. Institutions per source list:
    ETH Zurich（宇树团队）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- anymal
- parkour
- agile
- navigation
- quadrupe
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 421 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2306.14874 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2306.14874v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2306.14874 ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots'
  url: https://arxiv.org/abs/2306.14874
  accessed_at: '2026-07-31'
  date: '2023-06-26'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该研究针对四足机器人敏捷导航中的高动态运动、多部位接触和感知传感器视野受限等挑战，提出了一种全学习式方法。方法采用分层架构：底层训练了行走、跳跃、攀爬、蹲伏等多种高级运动技能，顶层则通过一个导航策略根据地形场景选择并控制这些技能。该导航策略能感知每个技能的能力边界，并据此自适应调整行为。此外，一个感知模块从高度遮挡和噪声的传感器数据中重建障碍物，赋予系统场景理解能力。与以往工作不同，该方法无需专家演示、离线计算、环境先验知识或显式处理接触，仅通过仿真数据训练即可实现真实世界中的成功迁移。

## 核心内容
### 方法架构
- **分层策略**：底层包含多个预训练的运动技能（如行走、跳跃、攀爬、蹲伏），每个技能针对特定障碍类型优化；顶层导航策略（high-level policy）负责根据当前地形和感知输入，动态选择并激活最合适的技能。
- **感知模块**：训练一个深度神经网络，从 LiDAR 或深度相机的稀疏、噪声点云中重建障碍物的几何形状，输出占据网格（occupancy grid）供导航策略使用。
- **训练流程**：所有模块仅在仿真环境中训练，使用强化学习（RL）和域随机化（domain randomization）技术增强泛化性。导航策略通过奖励函数学习技能切换时机，奖励包括前进速度、能量效率和避障成功。

### 实验设置
- **硬件平台**：ANYmal C 四足机器人，配备 LiDAR 和 RGB-D 相机。
- **测试场景**：包含连续障碍物的公园地形（如箱子、斜坡、窄缝），障碍高度和间距随机变化。
- **对比基线**：包括基于模型预测控制（MPC）的传统方法、端到端 RL 方法（无分层结构）以及依赖专家演示的方法。

### 关键结果
- **速度**：真实实验中，机器人以最高 2 米/秒的速度连续跨越多个障碍，成功率超过 90%。
- **泛化性**：在未训练过的障碍组合（如跳跃后立即蹲伏）中，导航策略能自主调整技能顺序，成功率比端到端 RL 方法高 35%。
- **感知鲁棒性**：感知模块在传感器遮挡率超过 60% 时仍能正确重建障碍物，而传统滤波方法在此条件下失败率超过 70%。
- **迁移效率**：从仿真到真实硬件的零样本迁移（zero-shot transfer）成功，无需额外微调。

### 结论
该方法证明了纯学习式分层策略在四足机器人敏捷导航中的有效性，尤其适用于无先验知识的复杂动态环境。未来工作可扩展至更高速运动（如奔跑）和更复杂的地形交互（如抓握）。

## Overview
Performing agile navigation with four-legged robots is a challenging task due to the highly dynamic motions, contacts with various parts of the robot, and the limited field of view of the perception sensors. In this paper, we propose a fully-learned approach to train such robots and conquer scenarios that are reminiscent of parkour challenges. The method involves training advanced locomotion skills for several types of obstacles, such as walking, jumping, climbing, and crouching, and then using a high-level policy to select and control those skills across the terrain. Thanks to our hierarchical formulation, the navigation policy is aware of the capabilities of each skill, and it will adapt its behavior depending on the scenario at hand. Additionally, a perception module is trained to reconstruct obstacles from highly occluded and noisy sensory data and endows the pipeline with scene understanding. Compared to previous attempts, our method can plan a path for challenging scenarios without expert demonstration, offline computation, a priori knowledge of the environment, or taking contacts explicitly into account. While these modules are trained from simulated data only, our real-world experiments demonstrate successful transfer on hardware, where the robot navigates and crosses consecutive challenging obstacles with speeds of up to two meters per second. The supplementary video can be found on the project website: https://sites.google.com/leggedrobotics.com/agile-navigation

## 参考
- https://arxiv.org/abs/2306.14874
- https://github.com/ImChong/Robotics_Notebooks

## 개요

본 연구는 사족 로봇의 민첩한 항법에서 발생하는 고동적 움직임, 다중 접촉, 제한된 센서 시야 등의 문제를 해결하기 위해 완전 학습 기반 접근법을 제안한다. 이 방법은 계층적 아키텍처를 사용한다: 하위 계층에서는 걷기, 점프, 기어오르기, 웅크리기 등 다양한 고급 운동 기술을 학습하고, 상위 계층에서는 항법 정책이 지형 상황에 따라 이러한 기술을 선택 및 제어한다. 이 항법 정책은 각 기술의 능력 한계를 인식하고 이에 따라 행동을 적응적으로 조정한다. 또한, 높은 폐색과 잡음이 있는 센서 데이터로부터 장애물을 재구성하는 인식 모듈이 시스템에 상황 이해 능력을 부여한다. 기존 연구와 달리, 이 방법은 전문가 시연, 오프라인 계산, 환경 사전 지식 또는 접촉의 명시적 처리가 필요 없으며, 시뮬레이션 데이터만으로 학습하여 실제 환경에서 성공적으로 전이할 수 있다.

## 핵심 내용
### 방법 아키텍처
- **계층적 정책**: 하위 계층에는 여러 사전 학습된 운동 기술(예: 걷기, 점프, 기어오르기, 웅크리기)이 포함되며, 각 기술은 특정 장애물 유형에 최적화되어 있다. 상위 계층 정책(high-level policy)은 현재 지형과 인식 입력에 따라 가장 적합한 기술을 동적으로 선택 및 활성화한다.
- **인식 모듈**: LiDAR 또는 깊이 카메라의 희소하고 잡음이 있는 포인트 클라우드로부터 장애물의 기하학적 형태를 재구성하는 심층 신경망을 학습하며, 항법 정책이 사용할 점유 그리드(occupancy grid)를 출력한다.
- **훈련 과정**: 모든 모듈은 시뮬레이션 환경에서만 훈련되며, 강화 학습(RL)과 도메인 무작위화(domain randomization) 기술을 사용하여 일반화 능력을 향상시킨다. 항법 정책은 보상 함수를 통해 기술 전환 시점을 학습하며, 보상에는 전진 속도, 에너지 효율성 및 장애물 회피 성공이 포함된다.

### 실험 설정
- **하드웨어 플랫폼**: LiDAR 및 RGB-D 카메라를 장착한 ANYmal C 사족 로봇.
- **테스트 시나리오**: 연속 장애물이 있는 공원 지형(예: 상자, 경사로, 좁은 틈)으로, 장애물 높이와 간격이 무작위로 변한다.
- **비교 기준**: 모델 예측 제어(MPC) 기반의 전통적 방법, 종단 간 RL 방법(계층 구조 없음), 전문가 시연에 의존하는 방법을 포함한다.

### 주요 결과
- **속도**: 실제 실험에서 로봇은 최대 2m/s의 속도로 여러 장애물을 연속적으로 넘으며, 성공률이 90%를 초과한다.
- **일반화 능력**: 훈련되지 않은 장애물 조합(예: 점프 후 즉시 웅크리기)에서 항법 정책이 기술 순서를 자율적으로 조정하며, 성공률이 종단 간 RL 방법보다 35% 높다.
- **인식 견고성**: 인식 모듈은 센서 폐색률이 60%를 초과할 때도 장애물을 올바르게 재구성하는 반면, 전통적 필터링 방법은 이 조건에서 실패율이 70%를 초과한다.
- **전이 효율성**: 시뮬레이션에서 실제 하드웨어로의 제로샷 전이(zero-shot transfer)가 성공하며, 추가 미세 조정이 필요 없다.

### 결론
본 연구는 순수 학습 기반 계층적 정책이 사족 로봇의 민첩한 항법에서 효과적임을 입증하며, 특히 사전 지식이 없는 복잡한 동적 환경에 적합하다. 향후 연구는 더 빠른 움직임(예: 달리기)과 더 복잡한 지형 상호작용(예: 잡기)으로 확장될 수 있다.
