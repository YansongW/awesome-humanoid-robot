---
$id: ent_paper_brown_optimal_sequential_task_assign_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimal Sequential Task Assignment and Path Finding for Multi-Agent Robotic Assembly Planning
  zh: 多机器人装配规划中的最优顺序任务分配与路径规划
  ko: 다중 에이전트 로봇 조립 계획을 위한 최적 순차 작업 할당 및 경로 탐색
summary:
  en: Proposes a hierarchical optimal solver for precedence-constrained multi-agent task assignment and path finding (PC-TAPF),
    integrating MILP-based assignment, conflict-based search, incremental slack-prioritized search, and slack-aware A* to
    minimize makespan in robotic assembly.
  zh: 本文提出一种面向机器人装配规划中具有任务间先后约束的多智能体任务分配与路径规划（PC-TAPF）的分层最优求解器。该方法融合基于MILP的任务分配、冲突搜索、增量松弛优先搜索及松弛感知A*算法，以最小化总完工时间（makespan）。实验在随机生成的工厂网格环境中验证，并在高保真仿真中展示了非完整差速驱动机器人的无碰撞轨迹生成能力。
  ko: 선행 제약 조건이 있는 다중 에이전트 작업 할당 및 경로 탐색(PC-TAPF) 문제를 해결하기 위해 MILP 기반 할당, 충돌 기반 탐색, 증분형 여유 우선 탐색, 여유 인지 A*를 통합한 계층적 최적 솔버를
    제안한다.
domains:
- 04_assembly_integration_testing
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- multi_agent_planning
- task_assignment
- path_planning
- precedence_constraints
- collision_free_routing
- makespan_optimization
- robotic_assembly
- conflict_based_search
- differential_drive_robots
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2006.08845v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (982 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Optimal Sequential Task Assignment and Path Finding for Multi-Agent Robotic Assembly Planning
  url: https://arxiv.org/abs/2006.08845
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究针对机器人制造装配中常见的先后约束任务（如任务A和B必须完成后才能开始任务C）下的多机器人协同问题，提出分层最优求解框架。核心方法包括：上层通过混合整数线性规划（MILP）进行任务分配，下层结合基于冲突的搜索（CBS）与增量松弛优先搜索（ISPS）处理路径冲突，并引入松弛感知A*（slack-aware A*）优化路径规划。实验在工厂网格环境中随机生成实例，验证了算法在最小化完工时间方面的有效性，同时通过高保真仿真展示了非完整差速驱动机器人的无碰撞轨迹生成能力。

## 核心内容
### 问题定义
- 研究问题：具有任务间先后约束的多智能体任务分配与路径规划（PC-TAPF），即机器人需在满足任务先后顺序（如子装配体必须完成后才能组合成最终产品）的前提下，完成序列任务分配与无碰撞路径规划。
- 优化目标：最小化总完工时间（makespan）。

### 方法架构
- **分层求解框架**：
  - **上层**：基于混合整数线性规划（MILP）的任务分配模块，将任务分配给各机器人，同时满足先后约束。
  - **下层**：路径规划模块，包含：
    - **基于冲突的搜索（CBS）**：处理多机器人路径冲突。
    - **增量松弛优先搜索（ISPS）**：通过优先级排序逐步解决冲突。
    - **松弛感知A*（slack-aware A*）**：在路径搜索中考虑任务的时间松弛度，优化路径质量。

### 实验设置
- **环境**：工厂网格世界（grid world），机器人需在站点间运输物体。
- **实例生成**：随机生成具有先后约束的任务集。
- **评估指标**：完工时间（makespan）最优性。
- **仿真验证**：使用高保真仿真器，验证非完整差速驱动机器人（non-holonomic differential-drive robots）的无碰撞轨迹生成。

### 关键结果
- 算法在随机实例上能有效求解makespan最优解。
- 高保真仿真表明，算法输出的路径可直接用于生成实际机器人的无碰撞轨迹，无需额外后处理。

### 结论
本文提出的分层求解器为具有先后约束的多机器人装配规划提供了理论最优解框架，并在仿真中验证了其实际可行性。未来工作可扩展至动态环境或更复杂的机器人运动学模型。

## Overview
We study the problem of sequential task assignment and collision-free routing for large teams of robots in applications with inter-task precedence constraints (e.g., task $A$ and task $B$ must both be completed before task $C$ may begin). Such problems commonly occur in assembly planning for robotic manufacturing applications, in which sub-assemblies must be completed before they can be combined to form the final product. We propose a hierarchical algorithm for computing makespan-optimal solutions to the problem. The algorithm is evaluated on a set of randomly generated problem instances where robots must transport objects between stations in a "factory "grid world environment. In addition, we demonstrate in high-fidelity simulation that the output of our algorithm can be used to generate collision-free trajectories for non-holonomic differential-drive robots.

## Overview
We study the problem of sequential task assignment and collision-free routing for large teams of robots in applications with inter-task precedence constraints (e.g., task $A$ and task $B$ must both be completed before task $C$ may begin). Such problems commonly occur in assembly planning for robotic manufacturing applications, in which sub-assemblies must be completed before they can be combined to form the final product. We propose a hierarchical algorithm for computing makespan-optimal solutions to the problem. The algorithm is evaluated on a set of randomly generated problem instances where robots must transport objects between stations in a "factory" grid world environment. In addition, we demonstrate in high-fidelity simulation that the output of our algorithm can be used to generate collision-free trajectories for non-holonomic differential-drive robots.

## Content
We study the problem of sequential task assignment and collision-free routing for large teams of robots in applications with inter-task precedence constraints (e.g., task $A$ and task $B$ must both be completed before task $C$ may begin). Such problems commonly occur in assembly planning for robotic manufacturing applications, in which sub-assemblies must be completed before they can be combined to form the final product. We propose a hierarchical algorithm for computing makespan-optimal solutions to the problem. The algorithm is evaluated on a set of randomly generated problem instances where robots must transport objects between stations in a "factory" grid world environment. In addition, we demonstrate in high-fidelity simulation that the output of our algorithm can be used to generate collision-free trajectories for non-holonomic differential-drive robots.

## 参考
- http://arxiv.org/abs/2006.08845v1

## 개요
본 연구는 로봇 제조 조립에서 흔히 발생하는 순차적 제약이 있는 작업(예: 작업 A와 B가 완료되어야 작업 C를 시작할 수 있는 경우) 하의 다중 로봇 협업 문제를 대상으로, 계층적 최적 해법 프레임워크를 제안한다. 핵심 방법은 다음과 같다: 상위 계층에서는 혼합 정수 선형 계획법(MILP)을 통해 작업 할당을 수행하고, 하위 계층에서는 충돌 기반 탐색(CBS)과 증분 완화 우선 탐색(ISPS)을 결합하여 경로 충돌을 처리하며, 완화 인지 A*(slack-aware A*)를 도입하여 경로 계획을 최적화한다. 실험은 공장 그리드 환경에서 무작위로 생성된 인스턴스를 사용하여 알고리즘이 완료 시간 최소화 측면에서 효과적임을 검증했으며, 고충실도 시뮬레이션을 통해 비홀로노믹 차동 구동 로봇의 무충돌 궤적 생성 능력을 보여준다.

## 핵심 내용
### 문제 정의
- 연구 문제: 작업 간 순차적 제약이 있는 다중 에이전트 작업 할당 및 경로 계획(PC-TAPF), 즉 로봇이 작업 순서(예: 하위 조립체가 완료되어야 최종 제품으로 조립될 수 있는 경우)를 충족하면서 순차적 작업 할당과 무충돌 경로 계획을 수행해야 하는 문제.
- 최적화 목표: 총 완료 시간(makespan) 최소화.

### 방법 구조
- **계층적 해법 프레임워크**:
  - **상위 계층**: 혼합 정수 선형 계획법(MILP) 기반 작업 할당 모듈로, 순차적 제약을 충족하면서 작업을 각 로봇에 할당한다.
  - **하위 계층**: 경로 계획 모듈로, 다음을 포함한다:
    - **충돌 기반 탐색(CBS)**: 다중 로봇 경로 충돌 처리.
    - **증분 완화 우선 탐색(ISPS)**: 우선순위 정렬을 통해 충돌을 점진적으로 해결.
    - **완화 인지 A*(slack-aware A*)**: 경로 탐색에서 작업의 시간 완화도를 고려하여 경로 품질을 최적화.

### 실험 설정
- **환경**: 공장 그리드 월드(grid world)로, 로봇은 스테이션 간 물체를 운반해야 한다.
- **인스턴스 생성**: 순차적 제약이 있는 작업 집합을 무작위로 생성.
- **평가 지표**: 완료 시간(makespan) 최적성.
- **시뮬레이션 검증**: 고충실도 시뮬레이터를 사용하여 비홀로노믹 차동 구동 로봇(non-holonomic differential-drive robots)의 무충돌 궤적 생성을 검증.

### 주요 결과
- 알고리즘은 무작위 인스턴스에서 makespan 최적 해를 효과적으로 도출할 수 있다.
- 고충실도 시뮬레이션은 알고리즘이 출력한 경로가 추가 후처리 없이 실제 로봇의 무충돌 궤적 생성에 직접 사용될 수 있음을 보여준다.

### 결론
본 논문에서 제안한 계층적 해법은 순차적 제약이 있는 다중 로봇 조립 계획에 이론적 최적 해법 프레임워크를 제공하며, 시뮬레이션에서 실제 적용 가능성을 검증했다. 향후 연구는 동적 환경이나 더 복잡한 로봇 운동학 모델로 확장할 수 있다.
