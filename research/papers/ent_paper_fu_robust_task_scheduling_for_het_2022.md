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
  en: Proposes CTAS, a stochastic mixed-integer programming framework that jointly
    optimizes task decomposition, assignment, and scheduling for heterogeneous robot
    teams under capability and requirement uncertainty, using CVaR to quantify non-completion
    risk.
  zh: 提出CTAS，一种随机混合整数规划框架，在能力和需求不确定下联合优化异构机器人团队的任务分解、分配与调度，并使用条件风险价值（CVaR）量化未完成任务的风险。
  ko: 능력 및 요구사항 불확실성 하에서 이종 로봇 팀의 작업 분해, 할당 및 스케줄링을 동시에 최적화하고 CVaR을 사용하여 미완료 위험을 정량화하는
    CTAS 확률 혼합정수계획 프레임워크를 제안함.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    needed before promotion to verified.
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

## Overview

This paper develops CTAS, a stochastic mixed-integer programming framework for coordinating heterogeneous robot teams. Unlike prior work that assumes a single fixed task decomposition into roles, CTAS jointly optimizes task decomposition, assignment, and scheduling while representing agent capabilities and task requirements as random vectors. Task requirements are verified by a generalizable binary function, allowing the framework to handle multiple decomposition structures for complex tasks.

The objective function combines energy, time, and a conditional value at risk (CVaR) term that quantifies the risk of task non-completion under uncertainty. The authors solve the resulting model via sample average approximation and an L-shaped decomposition method, followed by network-flow rounding and splitting to generate individual agent routes and schedules. The framework is evaluated in two practical scenarios: a capture-the-flag game and pandemic robotic service coordination (e.g., COVID-19), demonstrating scalability up to 140 agents and 40 tasks in the reported test cases.

## Key Contributions

- A modeling framework that captures uncertainties in both task requirements and agent capabilities.
- A cost function incorporating conditional value at risk (CVaR) to quantify and minimize task non-completion risk.
- A scalable reformulation using species-level network flows and a flow decomposition subproblem.
- A capture-the-flag simulation comparing CTAS against the STRATA baseline.
- A pandemic robotic service coordination case study demonstrating generalizability and scalability.

## Relevance to Humanoid Robotics

Although the paper studies general heterogeneous robot teams rather than humanoids specifically, its methods for robust task decomposition, assignment, and scheduling under capability uncertainty are directly applicable to coordinating fleets of humanoid robots with diverse skills. Service, logistics, and emergency-response deployments involving humanoids can use similar stochastic programming formulations to allocate complex tasks while accounting for uncertain robot capabilities and task requirements.
