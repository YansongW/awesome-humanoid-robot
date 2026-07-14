---
$id: ent_paper_fu_robust_task_scheduling_for_het_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Task Scheduling for Heterogeneous Robot Teams under Capability Uncertainty
  zh: 能力不确定性下异构机器人团队的鲁棒任务调度
  ko: 능력 불확실성 하에서 이종 로봇 팀의 강건한 작업 스케줄링
summary:
  en: Proposes a stochastic programming framework (CTAS) that jointly optimizes task decomposition, assignment, and scheduling
    for heterogeneous robot teams under uncertain task requirements and agent capabilities, using conditional value at risk
    (CVaR) to generate risk-aware plans.
  zh: 提出了一种随机规划框架（CTAS），在任务需求和智能体能力不确定的情况下，联合优化异构机器人团队的任务分解、分配和调度，并使用条件风险价值（CVaR）生成风险感知计划。
  ko: 작업 요구사항과 에이전트 능력이 불확실한 상황에서 이종 로봇 팀의 작업 분해, 할당, 스케줄링을 동시에 최적화하는 확률적 계획법 프레임워크(CTAS)를 제안하고 CVaR을 사용하여 위험 인식 계획을 생성한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- task_scheduling
- multi_agent_systems
- heterogeneous_robots
- stochastic_programming
- cvar
- risk_aware_planning
- task_assignment
- task_decomposition
- pandemic_service_robots
- capture_the_flag
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2106.12111v3.
sources:
- id: src_001
  type: paper
  title: Robust Task Scheduling for Heterogeneous Robot Teams under Capability Uncertainty
  url: https://arxiv.org/abs/2106.12111
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 核心内容
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 参考
- http://arxiv.org/abs/2106.12111v3

