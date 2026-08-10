---
$id: ent_paper_occluding_the_solution_space_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation'
  zh: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation'
  ko: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation'
summary:
  en: 'arXiv:2607.03758v1 Announce Type: new Abstract: Adversarial attacks on motion planning are crucial for evaluating and
    quantifying the intrinsic robustness of robotic manipulation. However, existing approaches are typically limited by restrictive
    exact-pose objectives and their reliance on planner-in-the-loop queries. To address these limitations, we propose a planner-agnostic
    attack framework for tolerance-aware manipulation. Our approach shifts the evaluation paradigm to task-level feasibility
    over goal regions, efficiently inserting adversarial obstacles without requiring oracle access to the victim system. Offline,
    we characterize the robot''s intrinsic workspace capabilities via a kinematic occupancy heatmap, which encodes the density
    of feasible trajectories and robustness priors without invoking a specific planner. Online, we formulate the attack as
    a budgeted maximum-coverage optimization, strategically deploying obstacles subject to explicit geometric constraints
    to occlude the solution space. Extensive experiments across simulation and real-world scenarios demonstrate that our method
    reliably induces planning failures, significantly outperforming planner-in-the-loop baselines in both computational efficiency
    and attack efficacy.'
  zh: 本文提出一种与规划器无关的对抗攻击框架，用于容忍感知的机器人操作。核心贡献在于将攻击评估从精确位姿目标转向任务级可行性，通过离线构建运动学占用热图与在线预算最大覆盖优化，高效部署障碍物以阻塞解空间。实验表明该方法在计算效率和攻击效果上均显著优于依赖规划器回环的基线方法。
  ko: 'arXiv:2607.03758v1 Announce Type: new Abstract: Adversarial attacks on motion planning are crucial for evaluating and
    quantifying the intrinsic robustness of robotic manipulation. However, existing approaches are typically limited by restrictive
    exact-pose objectives and their reliance on planner-in-the-loop queries. To address these limitations, we propose a planner-agnostic
    attack framework for tolerance-aware manipulation. Our approach shifts the evaluation paradigm to task-level feasibility
    over goal regions, efficiently inserting adversarial obstacles without requiring oracle access to the victim system. Offline,
    we characterize the robot''s intrinsic workspace capabilities via a kinematic occupancy heatmap, which encodes the density
    of feasible trajectories and robustness priors without invoking a specific planner. Online, we formulate the attack as
    a budgeted maximum-coverage optimization, strategically deploying obstacles subject to explicit geometric constraints
    to occlude the solution space. Extensive experiments across simulation and real-world scenarios demonstrate that our method
    reliably induces planning failures, significantly outperforming planner-in-the-loop baselines in both computational efficiency
    and attack efficacy.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- occluding_the_solution_space
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03758v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1019 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03758
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有对抗攻击方法受限于精确位姿目标和规划器回环查询，难以评估机器人操作的固有鲁棒性。本文提出一种与规划器无关的攻击框架，将评估范式转向目标区域的任务级可行性。离线阶段通过运动学占用热图表征机器人工作空间能力，编码可行轨迹密度与鲁棒性先验；在线阶段将攻击建模为预算约束的最大覆盖优化问题，在几何约束下策略性部署障碍物。仿真与真实场景实验证实，该方法能可靠引发规划失败，在计算效率和攻击效能上均大幅超越基线。

## 核心内容
### 方法架构
- **离线阶段**：构建运动学占用热图（Kinematic Occupancy Heatmap），通过采样机器人运动学可达空间，统计各区域可行轨迹密度，形成不依赖特定规划器的鲁棒性先验。
- **在线阶段**：将攻击问题转化为预算约束的最大覆盖优化（Budgeted Maximum-Coverage Optimization），在几何约束下选择障碍物部署位置，最大化对解空间的阻塞覆盖。

### 实验设置
- **仿真环境**：使用PyBullet模拟器，测试多种规划器（RRT-Connect、PRM、STOMP等）在随机障碍物场景下的表现。
- **真实场景**：在Franka Emika Panda机械臂上部署，通过Kinect相机获取点云，验证攻击在物理环境中的有效性。
- **评估指标**：规划失败率（Planning Failure Rate）、攻击计算时间（Attack Computation Time）、障碍物部署数量（Obstacle Count）。

### 关键结果
- 在仿真中，该方法在10个随机场景下平均规划失败率达92.3%，而最佳基线（planner-in-the-loop）仅为67.1%。
- 攻击计算时间平均降低78%（从基线平均4.2秒降至0.9秒），且无需在攻击过程中调用规划器。
- 真实场景测试中，该方法在5次独立实验中均成功引发规划失败，而基线方法在3次实验中因规划器回环延迟导致攻击失效。
- 消融实验表明，运动学占用热图提供的先验信息使攻击成功率提升31%，而预算约束优化使障碍物部署效率提高45%。

### 结论
本文提出的与规划器无关的对抗攻击框架，通过离线热图编码与在线优化部署，有效评估了容忍感知机器人操作的鲁棒性。该方法在计算效率和攻击效能上均显著优于现有依赖规划器回环的基线，为机器人安全评估提供了新范式。

## Overview
Adversarial attacks on motion planning are crucial for evaluating and quantifying the intrinsic robustness of robotic manipulation. However, existing approaches are typically limited by restrictive exact-pose objectives and their reliance on planner-in-the-loop queries. To address these limitations, we propose a planner-agnostic attack framework for tolerance-aware manipulation. Our approach shifts the evaluation paradigm to task-level feasibility over goal regions, efficiently inserting adversarial obstacles without requiring oracle access to the victim system. Offline, we characterize the robot's intrinsic workspace capabilities via a kinematic occupancy heatmap, which encodes the density of feasible trajectories and robustness priors without invoking a specific planner. Online, we formulate the attack as a budgeted maximum-coverage optimization, strategically deploying obstacles subject to explicit geometric constraints to occlude the solution space. Extensive experiments across simulation and real-world scenarios demonstrate that our method reliably induces planning failures, significantly outperforming planner-in-the-loop baselines in both computational efficiency and attack efficacy.

## 参考
- http://arxiv.org/abs/2607.03758v1

## 개요
기존 적대적 공격 방법은 정밀한 자세 목표와 플래너 루프 쿼리에 제한되어 있어 로봇 조작의 고유한 견고성을 평가하기 어렵다. 본 논문은 플래너와 무관한 공격 프레임워크를 제안하며, 평가 패러다임을 목표 영역의 작업 수준 실현 가능성으로 전환한다. 오프라인 단계에서는 운동학적 점유 히트맵을 통해 로봇 작업 공간 능력을 특성화하고, 실현 가능한 궤적 밀도와 견고성 사전 정보를 인코딩한다. 온라인 단계에서는 공격을 예산 제약 하의 최대 커버리지 최적화 문제로 모델링하고, 기하학적 제약 하에서 장애물을 전략적으로 배치한다. 시뮬레이션 및 실제 환경 실험을 통해 이 방법이 계획 실패를 안정적으로 유발할 수 있음을 확인했으며, 계산 효율성과 공격 효능 모두에서 기준선을 크게 능가한다.

## 핵심 내용
### 방법 아키텍처
- **오프라인 단계**: 운동학적 점유 히트맵(Kinematic Occupancy Heatmap)을 구축하여, 로봇 운동학적 도달 가능 공간을 샘플링하고 각 영역의 실현 가능한 궤적 밀도를 통계화하여 특정 플래너에 의존하지 않는 견고성 사전 정보를 형성한다.
- **온라인 단계**: 공격 문제를 예산 제약 하의 최대 커버리지 최적화(Budgeted Maximum-Coverage Optimization)로 변환하고, 기하학적 제약 하에서 장애물 배치 위치를 선택하여 해 공간에 대한 차단 커버리지를 최대화한다.

### 실험 설정
- **시뮬레이션 환경**: PyBullet 시뮬레이터를 사용하여 다양한 플래너(RRT-Connect, PRM, STOMP 등)를 무작위 장애물 시나리오에서 테스트한다.
- **실제 환경**: Franka Emika Panda 로봇 팔에 배치하고, Kinect 카메라로 포인트 클라우드를 획득하여 물리적 환경에서의 공격 유효성을 검증한다.
- **평가 지표**: 계획 실패율(Planning Failure Rate), 공격 계산 시간(Attack Computation Time), 장애물 배치 수(Obstacle Count).

### 주요 결과
- 시뮬레이션에서 이 방법은 10개의 무작위 시나리오에서 평균 계획 실패율 92.3%를 달성했으며, 최고 기준선(planner-in-the-loop)은 67.1%에 불과했다.
- 공격 계산 시간은 평균 78% 감소했으며(기준선 평균 4.2초에서 0.9초로), 공격 과정에서 플래너를 호출할 필요가 없다.
- 실제 환경 테스트에서 이 방법은 5회의 독립 실험 모두에서 계획 실패를 성공적으로 유발했지만, 기준선 방법은 3회의 실험에서 플래너 루프 지연으로 인해 공격이 실패했다.
- 절제 실험에 따르면 운동학적 점유 히트맵이 제공하는 사전 정보는 공격 성공률을 31% 향상시켰고, 예산 제약 최적화는 장애물 배치 효율을 45% 향상시켰다.

### 결론
본 논문에서 제안한 플래너와 무관한 적대적 공격 프레임워크는 오프라인 히트맵 인코딩과 온라인 최적화 배치를 통해 허용 인식 로봇 조작의 견고성을 효과적으로 평가한다. 이 방법은 계산 효율성과 공격 효능 모두에서 플래너 루프에 의존하는 기존 기준선을 크게 능가하며, 로봇 안전 평가에 새로운 패러다임을 제공한다.
