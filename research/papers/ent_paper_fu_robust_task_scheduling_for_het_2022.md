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
  zh: This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment,
    and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams
    with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems
    with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing
    range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2106.12111v3.
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
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 核心内容
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 参考
- http://arxiv.org/abs/2106.12111v3

## Overview
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## Content
This paper develops a stochastic programming framework for multi-agent systems where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed sub-tasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Due to their inherent flexibility and robustness, multi-agent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multi-agent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk (CVaR) is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.

## 개요
본 논문은 다중 에이전트 시스템에서 작업 분해, 할당 및 일정 계획 문제를 동시에 최적화하는 확률적 프로그래밍 프레임워크를 개발한다. 이 프레임워크는 분산된 하위 작업을 가진 이기종 모바일 로봇 팀에 적용될 수 있다. 예를 들어, 팬데믹 로봇 서비스 조정, 탐색 및 구조, 이기종 차량을 사용한 배송 시스템 등이 있다. 다중 에이전트 시스템은 본질적인 유연성과 견고성 덕분에 이기종 작업과 불확실한 정보를 포함하는 실제 문제에 점점 더 많이 적용되고 있다. 대부분의 이전 연구는 작업을 에이전트에 할당할 수 있는 역할로 분해하는 고정된 방식을 가정한다. 이러한 가정은 역할이 다양하고 여러 분해 구조가 존재할 수 있는 복잡한 작업에는 유효하지 않다. 또한, 다중 에이전트 시스템 환경에서 작업 요구사항과 에이전트 능력의 불확실성을 체계적으로 정량화하고 최적화하는 방법은 명확하지 않다. 복잡한 작업에 대한 표현이 제안된다: 에이전트 능력은 무작위 분포의 벡터로 표현되고, 작업 요구사항은 일반화 가능한 이진 함수로 검증된다. 조건부 위험 가치(CVaR)는 강건한 계획을 생성하기 위해 목적 함수의 지표로 선택된다. 모델을 해결하기 위한 효율적인 알고리즘이 설명되며, 전체 프레임워크는 두 가지 실제 테스트 사례(깃발 잡기 및 팬데믹(예: COVID-19) 상황에서의 로봇 서비스 조정)에서 평가된다. 결과는 프레임워크가 일반화 가능하며, 예시 테스트 사례에서 최대 140개의 에이전트와 40개의 작업까지 확장 가능하고, 높은 성공 확률을 보장하는 저비용 계획을 제공함을 보여준다.

## 핵심 내용
본 논문은 다중 에이전트 시스템에서 작업 분해, 할당 및 일정 계획 문제를 동시에 최적화하는 확률적 프로그래밍 프레임워크를 개발한다. 이 프레임워크는 분산된 하위 작업을 가진 이기종 모바일 로봇 팀에 적용될 수 있다. 예를 들어, 팬데믹 로봇 서비스 조정, 탐색 및 구조, 이기종 차량을 사용한 배송 시스템 등이 있다. 다중 에이전트 시스템은 본질적인 유연성과 견고성 덕분에 이기종 작업과 불확실한 정보를 포함하는 실제 문제에 점점 더 많이 적용되고 있다. 대부분의 이전 연구는 작업을 에이전트에 할당할 수 있는 역할로 분해하는 고정된 방식을 가정한다. 이러한 가정은 역할이 다양하고 여러 분해 구조가 존재할 수 있는 복잡한 작업에는 유효하지 않다. 또한, 다중 에이전트 시스템 환경에서 작업 요구사항과 에이전트 능력의 불확실성을 체계적으로 정량화하고 최적화하는 방법은 명확하지 않다. 복잡한 작업에 대한 표현이 제안된다: 에이전트 능력은 무작위 분포의 벡터로 표현되고, 작업 요구사항은 일반화 가능한 이진 함수로 검증된다. 조건부 위험 가치(CVaR)는 강건한 계획을 생성하기 위해 목적 함수의 지표로 선택된다. 모델을 해결하기 위한 효율적인 알고리즘이 설명되며, 전체 프레임워크는 두 가지 실제 테스트 사례(깃발 잡기 및 팬데믹(예: COVID-19) 상황에서의 로봇 서비스 조정)에서 평가된다. 결과는 프레임워크가 일반화 가능하며, 예시 테스트 사례에서 최대 140개의 에이전트와 40개의 작업까지 확장 가능하고, 높은 성공 확률을 보장하는 저비용 계획을 제공함을 보여준다.
