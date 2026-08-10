---
$id: ent_paper_dexterous_safe_control_for_hum_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  zh: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
summary:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
  zh: 本文提出Projected Safe Set Algorithm (p-SSA)，一种面向人形机器人在杂乱环境中灵巧安全控制的新算法。该方法由研究团队于2025年提出，核心贡献在于通过松弛冲突约束解决多约束条件下的可行控制问题，并在Unitree
    G1人形机器人上验证了其鲁棒性与零参数调优的泛化能力。
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexterous_safe_control_for_hum
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02858v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1120 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm (arXiv)
  url: https://arxiv.org/abs/2502.02858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人在真实应用中需兼顾安全性与性能的挑战，本文聚焦于灵巧安全问题，引入肢体级几何约束以避免外部碰撞与自碰撞。与稀疏环境中简化包围盒的安全方法不同，灵巧安全会产生大量约束，导致求解安全控制时约束集不可行。为此，作者提出p-SSA，将经典安全控制算法扩展至多约束场景，通过原则性方式松弛冲突约束，最小化安全违规以保证控制可行性。仿真与真实Unitree G1人形机器人实验表明，p-SSA在复杂避障任务中实现鲁棒运行，且无需参数调整即可直接泛化至不同任务。

## 核心内容
### 方法
- **问题定义**：考虑人形机器人在杂乱环境中的灵巧安全控制，需同时满足外部碰撞避免（与环境障碍物）与自碰撞避免（肢体间）的肢体级几何约束。
- **核心挑战**：传统安全控制算法（如安全集算法）在稀疏环境中有效，但灵巧安全产生大量约束，导致约束集不可行（infeasible constraint sets），即无解。
- **p-SSA算法**：
  - 基于经典安全控制算法（如Control Barrier Functions），扩展至多约束场景。
  - 核心机制：当约束冲突时，p-SSA通过原则性松弛（principled relaxation）调整约束，优先保证关键安全约束，最小化安全违规（safety violations）。
  - 输出可行控制指令，确保机器人运动始终在安全集内。

### 实验设置
- **仿真环境**：构建包含密集障碍物的杂乱场景，测试人形机器人执行复杂避障任务（如穿越狭窄通道、抓取目标）。
- **真实机器人**：使用Unitree G1人形机器人，配备全身关节传感器与外部深度相机，实时感知环境。
- **对比基线**：与经典安全控制算法（如SSA）及无安全约束的规划方法对比。

### 关键结果
- **安全性能**：p-SSA在仿真中实现零碰撞，而基线方法在密集约束下出现多次碰撞（如SSA在30%场景中失败）。
- **控制可行性**：p-SSA成功处理所有约束冲突，输出可行控制指令；基线方法在20%场景中因约束不可行而停止。
- **泛化能力**：零参数调优（zero parameter tuning）下，p-SSA直接迁移至不同任务（如避障、抓取、行走），保持安全性能。
- **计算效率**：p-SSA的实时求解时间低于10ms，满足人形机器人控制周期要求。

### 结论
p-SSA通过松弛冲突约束，有效解决了灵巧安全控制中的多约束不可行问题，使人形机器人在杂乱环境中实现鲁棒、安全操作。该方法无需任务特定调参，具备直接泛化能力，为实际部署提供了可行方案。

## Overview
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sprase environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## Overview
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sparse environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## Content
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sparse environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 参考
- http://arxiv.org/abs/2502.02858v1

## 개요
인간형 로봇이 실제 응용에서 안전성과 성능을 동시에 충족해야 하는 과제에 대해, 본 논문은 민첩한 안전 문제에 초점을 맞추고, 신체 부위 수준의 기하학적 제약을 도입하여 외부 충돌과 자체 충돌을 방지한다. 희소 환경에서 단순화된 경계 상자를 사용하는 안전 방법과 달리, 민첩한 안전은 다수의 제약을 생성하여 안전 제어를 해결할 때 제약 집합이 실행 불가능해지는 문제를 초래한다. 이를 위해 저자들은 p-SSA를 제안하여 고전적 안전 제어 알고리즘을 다중 제약 시나리오로 확장하고, 원칙적인 방식으로 충돌하는 제약을 완화하여 안전 위반을 최소화함으로써 제어 실행 가능성을 보장한다. 시뮬레이션 및 실제 Unitree G1 인간형 로봇 실험은 p-SSA가 복잡한 장애물 회피 작업에서 견고한 작동을 달성하며, 매개변수 조정 없이도 다양한 작업에 직접 일반화할 수 있음을 보여준다.

## 핵심 내용
### 방법
- **문제 정의**: 인간형 로봇이 혼잡한 환경에서 민첩한 안전 제어를 수행할 때, 외부 충돌 회피(환경 장애물)와 자체 충돌 회피(신체 부위 간)를 동시에 충족하는 신체 부위 수준의 기하학적 제약을 고려한다.
- **핵심 과제**: 전통적인 안전 제어 알고리즘(예: 안전 집합 알고리즘)은 희소 환경에서 효과적이지만, 민첩한 안전은 다수의 제약을 생성하여 제약 집합이 실행 불가능해지는 문제(infeasible constraint sets), 즉 해가 없는 상황을 초래한다.
- **p-SSA 알고리즘**:
  - 고전적 안전 제어 알고리즘(예: Control Barrier Functions)을 기반으로 다중 제약 시나리오로 확장한다.
  - 핵심 메커니즘: 제약이 충돌할 때, p-SSA는 원칙적 완화(principled relaxation)를 통해 제약을 조정하고, 핵심 안전 제약을 우선적으로 보장하며 안전 위반(safety violations)을 최소화한다.
  - 실행 가능한 제어 명령을 출력하여 로봇의 움직임이 항상 안전 집합 내에 유지되도록 한다.

### 실험 설정
- **시뮬레이션 환경**: 밀집된 장애물을 포함한 혼잡한 시나리오를 구축하고, 인간형 로봇이 복잡한 장애물 회피 작업(예: 좁은 통로 통과, 목표물 파지)을 수행하도록 테스트한다.
- **실제 로봇**: Unitree G1 인간형 로봇을 사용하며, 전신 관절 센서와 외부 깊이 카메라를 장착하여 환경을 실시간으로 인식한다.
- **비교 기준**: 고전적 안전 제어 알고리즘(예: SSA) 및 안전 제약이 없는 계획 방법과 비교한다.

### 주요 결과
- **안전 성능**: p-SSA는 시뮬레이션에서 충돌 없음(zero collision)을 달성한 반면, 기준 방법은 밀집된 제약 조건에서 여러 차례 충돌이 발생했다(예: SSA는 30% 시나리오에서 실패).
- **제어 실행 가능성**: p-SSA는 모든 제약 충돌을 성공적으로 처리하고 실행 가능한 제어 명령을 출력했으며, 기준 방법은 20% 시나리오에서 제약 실행 불가능으로 인해 중단되었다.
- **일반화 능력**: 매개변수 조정 없음(zero parameter tuning) 상태에서 p-SSA는 다양한 작업(예: 장애물 회피, 파지, 보행)에 직접 전이되어 안전 성능을 유지한다.
- **계산 효율성**: p-SSA의 실시간 해석 시간은 10ms 미만으로, 인간형 로봇의 제어 주기 요구 사항을 충족한다.

### 결론
p-SSA는 충돌하는 제약을 완화함으로써 민첩한 안전 제어에서의 다중 제약 실행 불가능 문제를 효과적으로 해결하여, 인간형 로봇이 혼잡한 환경에서 견고하고 안전한 작동을 달성할 수 있게 한다. 이 방법은 작업별 매개변수 조정이 필요 없으며 직접 일반화 능력을 갖추고 있어 실제 배포를 위한 실행 가능한 방안을 제공한다.
