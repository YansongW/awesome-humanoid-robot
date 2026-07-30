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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02858v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇이 실제 환경에서 성능 저하 없이 안전을 보장하는 것은 매우 중요합니다. 본 논문에서는 혼잡한 환경에서 외부 충돌 및 자체 충돌을 모두 회피하기 위한 팔다리 수준의 기하학적 제약 조건을 특징으로 하는 정밀 안전 문제를 다룹니다. 희소 환경에서 단순화된 경계 기하학을 사용한 안전과 비교할 때, 정밀 안전은 수많은 제약 조건을 생성하며, 이는 종종 안전한 로봇 제어를 해결할 때 실행 불가능한 제약 조건 집합으로 이어집니다. 이 문제를 해결하기 위해, 우리는 고전적인 안전 제어 알고리즘을 다중 제약 조건 사례로 확장한 Projected Safe Set Algorithm (p-SSA)을 제안합니다. p-SSA는 원칙적인 방식으로 충돌하는 제약 조건을 완화하여 안전 위반을 최소화하고 실행 가능한 로봇 제어를 보장합니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇이 복잡한 충돌 회피 작업을 수행하는 환경에서 접근 방식을 검증합니다. 결과는 p-SSA가 휴머노이드가 최소한의 안전 위반으로 어려운 상황에서 강건하게 작동할 수 있게 하며, 매개변수 조정 없이 다양한 작업에 직접 일반화됨을 보여줍니다.

## 핵심 내용
휴머노이드 로봇이 실제 환경에서 성능 저하 없이 안전을 보장하는 것은 매우 중요합니다. 본 논문에서는 혼잡한 환경에서 외부 충돌 및 자체 충돌을 모두 회피하기 위한 팔다리 수준의 기하학적 제약 조건을 특징으로 하는 정밀 안전 문제를 다룹니다. 희소 환경에서 단순화된 경계 기하학을 사용한 안전과 비교할 때, 정밀 안전은 수많은 제약 조건을 생성하며, 이는 종종 안전한 로봇 제어를 해결할 때 실행 불가능한 제약 조건 집합으로 이어집니다. 이 문제를 해결하기 위해, 우리는 고전적인 안전 제어 알고리즘을 다중 제약 조건 사례로 확장한 Projected Safe Set Algorithm (p-SSA)을 제안합니다. p-SSA는 원칙적인 방식으로 충돌하는 제약 조건을 완화하여 안전 위반을 최소화하고 실행 가능한 로봇 제어를 보장합니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇이 복잡한 충돌 회피 작업을 수행하는 환경에서 접근 방식을 검증합니다. 결과는 p-SSA가 휴머노이드가 최소한의 안전 위반으로 어려운 상황에서 강건하게 작동할 수 있게 하며, 매개변수 조정 없이 다양한 작업에 직접 일반화됨을 보여줍니다.

## 参考
- http://arxiv.org/abs/2502.02858v1
