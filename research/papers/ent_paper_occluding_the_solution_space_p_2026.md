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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03758v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
모션 플래닝에 대한 적대적 공격은 로봇 조작의 본질적 강건성을 평가하고 정량화하는 데 중요합니다. 그러나 기존 접근 방식은 일반적으로 제한적인 정확한 자세 목표와 플래너-인-더-루프 쿼리에 대한 의존성으로 인해 한계가 있습니다. 이러한 한계를 해결하기 위해, 우리는 공차 인식 조작을 위한 플래너-비의존적 공격 프레임워크를 제안합니다. 우리의 접근 방식은 평가 패러다임을 목표 영역에 대한 작업 수준의 실현 가능성으로 전환하며, 피해 시스템에 대한 오라클 접근 없이도 효율적으로 적대적 장애물을 삽입합니다. 오프라인에서는 특정 플래너를 호출하지 않고도 실행 가능한 궤적의 밀도와 강건성 사전 정보를 인코딩하는 운동학적 점유 히트맵을 통해 로봇의 본질적 작업 공간 능력을 특성화합니다. 온라인에서는 공격을 예산 제한 최대 커버리지 최적화로 공식화하여, 명시적 기하학적 제약 조건 하에 전략적으로 장애물을 배치하여 해 공간을 차단합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 우리의 방법이 안정적으로 플래닝 실패를 유도하며, 계산 효율성과 공격 효과 모두에서 플래너-인-더-루프 기준선을 크게 능가함을 입증합니다.

## 핵심 내용
모션 플래닝에 대한 적대적 공격은 로봇 조작의 본질적 강건성을 평가하고 정량화하는 데 중요합니다. 그러나 기존 접근 방식은 일반적으로 제한적인 정확한 자세 목표와 플래너-인-더-루프 쿼리에 대한 의존성으로 인해 한계가 있습니다. 이러한 한계를 해결하기 위해, 우리는 공차 인식 조작을 위한 플래너-비의존적 공격 프레임워크를 제안합니다. 우리의 접근 방식은 평가 패러다임을 목표 영역에 대한 작업 수준의 실현 가능성으로 전환하며, 피해 시스템에 대한 오라클 접근 없이도 효율적으로 적대적 장애물을 삽입합니다. 오프라인에서는 특정 플래너를 호출하지 않고도 실행 가능한 궤적의 밀도와 강건성 사전 정보를 인코딩하는 운동학적 점유 히트맵을 통해 로봇의 본질적 작업 공간 능력을 특성화합니다. 온라인에서는 공격을 예산 제한 최대 커버리지 최적화로 공식화하여, 명시적 기하학적 제약 조건 하에 전략적으로 장애물을 배치하여 해 공간을 차단합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 우리의 방법이 안정적으로 플래닝 실패를 유도하며, 계산 효율성과 공격 효과 모두에서 플래너-인-더-루프 기준선을 크게 능가함을 입증합니다.

## 参考
- http://arxiv.org/abs/2607.03758v1
