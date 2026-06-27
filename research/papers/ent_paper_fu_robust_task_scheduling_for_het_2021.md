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
  en: Proposes a stochastic programming framework (CTAS) that jointly optimizes task
    decomposition, assignment, and scheduling for heterogeneous robot teams under
    uncertain task requirements and agent capabilities, using conditional value at
    risk (CVaR) to generate risk-aware plans.
  zh: 提出了一种随机规划框架（CTAS），在任务需求和智能体能力不确定的情况下，联合优化异构机器人团队的任务分解、分配和调度，并使用条件风险价值（CVaR）生成风险感知计划。
  ko: 작업 요구사항과 에이전트 능력이 불확실한 상황에서 이종 로봇 팀의 작업 분해, 할당, 스케줄링을 동시에 최적화하는 확률적 계획법 프레임워크(CTAS)를
    제안하고 CVaR을 사용하여 위험 인식 계획을 생성한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and arXiv abstract; requires human review
    before full verification.
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

## Overview

This paper develops a stochastic programming framework for multi-agent systems in which task decomposition, assignment, and scheduling are optimized simultaneously. It targets heterogeneous mobile robot teams executing distributed sub-tasks, with motivating examples that include pandemic robotic service coordination, explore-and-rescue missions, and heterogeneous-vehicle delivery systems.

The authors argue that prior work typically assumes a single fixed task-to-role decomposition, which is unrealistic for complex tasks that admit multiple decomposition structures and varying roles. To address this, they represent agent capabilities as a vector of random distributions and task requirements as a generalizable binary function. The conditional value at risk (CVaR) is adopted in the objective to obtain robust plans, and a scalable two-stage algorithm—using sample average approximation and a flow-decomposition subproblem—is described for solving the resulting model.

## Key Contributions

- A stochastic modeling framework that explicitly captures uncertain task requirements and agent capabilities.
- A CVaR-based cost function that directly incorporates the risk of task failure into plan generation.
- A scalable reformulation of the heterogeneous teaming problem using species-level flows and a flow-decomposition subproblem.
- Experimental validation on capture-the-flag and pandemic robotic service scenarios, demonstrating scalability up to 140 agents and 40 tasks.

## Relevance to Humanoid Robotics

Although the paper does not focus exclusively on humanoid robots, its framework is directly applicable to coordinating fleets of humanoid robots during mass deployment. Logistics, service, and emergency-response operations all require task decomposition, assignment, and scheduling under uncertain capability estimates, which is precisely the problem CTAS addresses.

By providing a risk-aware, scalable method for heterogeneous robot teams, the work supports downstream humanoid-robot applications where mixed teams of humanoids and other vehicles must be reliably scheduled in dynamic, uncertain environments.
