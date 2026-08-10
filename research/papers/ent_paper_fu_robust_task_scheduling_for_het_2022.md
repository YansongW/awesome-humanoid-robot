---
$id: ent_paper_fu_robust_task_scheduling_for_het_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Task Scheduling for Heterogeneous Robot Teams under Capability Uncertainty
  zh: 能力不确定下异构机器人团队的鲁棒任务调度
  ko: 능력 불확실성 하에서 이종 로봇 팀을 위한 강건한 작업 스케줄링
summary:
  en: Proposes CTAS, a stochastic mixed-integer programming framework that jointly optimizes task decomposition, assignment,
    and scheduling for heterogeneous robot teams under capability and requirement uncertainty, using CVaR to quantify non-completion
    risk.
  zh: 本文提出CTAS框架，一个随机混合整数规划模型，用于异构机器人团队在能力与需求不确定下的任务分解、分配与调度联合优化。该框架采用条件风险价值（CVaR）量化任务未完成风险，并在两个实际案例中验证了其可扩展性与鲁棒性。
  ko: 능력 및 요구사항 불확실성 하에서 이종 로봇 팀의 작업 분해, 할당 및 스케줄링을 동시에 최적화하고 CVaR을 사용하여 미완료 위험을 정량화하는 CTAS 확률 혼합정수계획 프레임워크를 제안함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- task_allocation
- task_scheduling
- heterogeneous_robot_teams
- multi_agent_systems
- stochastic_programming
- cvar
- robust_planning
- pandemic_service_robots
- capture_the_flag
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2106.12111v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_fu_robust_task_scheduling_for_het_2022 into this card (rules: same_arxiv). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (794 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Robust Task Scheduling for Heterogeneous Robot Teams under Capability Uncertainty
  url: https://arxiv.org/abs/2106.12111
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对异构多机器人系统中任务分解结构可变且存在能力与需求不确定性的问题，本文提出了CTAS框架。该框架将任务分解、分配与调度作为联合优化问题，用随机分布向量表示机器人能力，用通用二元函数验证任务需求，并以CVaR作为目标函数中的风险度量指标。实验在夺旗与疫情机器人服务协调两个场景中展开，结果显示框架可扩展至140个机器人与40个任务，且能生成低成本、高成功概率的鲁棒计划。

## 核心内容
### 方法
- **问题建模**：将异构机器人团队的任务规划建模为随机混合整数规划，同时优化任务分解（将复杂任务拆分为可变角色）、分配（角色到机器人）与调度（执行顺序）。
- **不确定性表示**：机器人能力用随机分布向量描述，任务需求通过通用二元函数验证，允许能力与需求存在概率性偏差。
- **风险量化**：目标函数采用条件风险价值（CVaR）作为风险度量，以生成对能力不确定性鲁棒的规划方案。

### 算法
- 提出一种高效求解算法，通过分解与剪枝策略降低混合整数规划的计算复杂度，支持大规模问题实例。

### 实验设置
- **测试案例**：两个实际场景——夺旗任务（Capture-the-flag）与疫情（如COVID-19）机器人服务协调。
- **规模**：框架可扩展至140个机器人与40个任务，验证了其可扩展性。

### 关键结果
- **可泛化性**：框架在不同任务类型与不确定性分布下均能生成有效计划。
- **成本与成功率**：相比基线方法，CTAS在保持低成本的同时，显著提升了任务成功概率（高概率成功）。
- **鲁棒性**：CVaR的引入使计划对能力不确定性具有更强的抗干扰能力。

### 结论
CTAS框架为异构机器人团队在不确定性下的任务规划提供了统一解决方案，兼顾了分解灵活性、分配效率与调度鲁棒性，适用于探索救援、物流配送等实际场景。

## Overview
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 参考
- http://arxiv.org/abs/2106.12111v3

## 개요
이질적 다중 로봇 시스템에서 작업 분해 구조가 가변적이고 능력 및 수요 불확실성이 존재하는 문제를 해결하기 위해, 본 논문은 CTAS 프레임워크를 제안한다. 이 프레임워크는 작업 분해, 할당 및 일정 계획을 결합 최적화 문제로 간주하며, 로봇 능력을 확률 분포 벡터로 표현하고, 작업 수요를 일반 이진 함수로 검증하며, CVaR을 목적 함수의 위험 측정 지표로 사용한다. 실험은 깃발 뺏기(Capture-the-flag)와 팬데믹 로봇 서비스 조정 두 시나리오에서 수행되었으며, 결과는 프레임워크가 140개의 로봇과 40개의 작업으로 확장 가능하고, 저비용·고성공 확률의 강건한 계획을 생성할 수 있음을 보여준다.

## 핵심 내용
### 방법
- **문제 모델링**: 이질적 로봇 팀의 작업 계획을 확률적 혼합 정수 계획법으로 모델링하며, 작업 분해(복잡한 작업을 가변 역할로 분할), 할당(역할에서 로봇으로), 일정 계획(실행 순서)을 동시에 최적화한다.
- **불확실성 표현**: 로봇 능력은 확률 분포 벡터로 설명되고, 작업 수요는 일반 이진 함수를 통해 검증되어 능력과 수요 간의 확률적 편차를 허용한다.
- **위험 정량화**: 목적 함수는 조건부 위험 가치(CVaR)를 위험 측정 지표로 사용하여 능력 불확실성에 강건한 계획 방안을 생성한다.

### 알고리즘
- 분해 및 가지치기 전략을 통해 혼합 정수 계획법의 계산 복잡도를 낮추는 고효율 해법 알고리즘을 제안하며, 대규모 문제 인스턴스를 지원한다.

### 실험 설정
- **테스트 사례**: 두 실제 시나리오——깃발 뺏기 작업(Capture-the-flag)과 팬데믹(예: COVID-19) 로봇 서비스 조정.
- **규모**: 프레임워크는 140개의 로봇과 40개의 작업으로 확장 가능하며, 확장성을 검증한다.

### 주요 결과
- **일반화 가능성**: 프레임워크는 다양한 작업 유형과 불확실성 분포에서 효과적인 계획을 생성할 수 있다.
- **비용 및 성공률**: 기준 방법과 비교하여 CTAS는 낮은 비용을 유지하면서 작업 성공 확률(고확률 성공)을 크게 향상시킨다.
- **강건성**: CVaR 도입으로 계획이 능력 불확실성에 대해 더 강한 간섭 저항력을 갖는다.

### 결론
CTAS 프레임워크는 불확실성 하에서 이질적 로봇 팀의 작업 계획을 위한 통합 솔루션을 제공하며, 분해 유연성, 할당 효율성 및 일정 강건성을 모두 고려하여 탐사 구조, 물류 배송 등 실제 시나리오에 적합하다.
