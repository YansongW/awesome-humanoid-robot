---
$id: ent_paper_lallement_hatp_an_htn_planner_for_roboti_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HATP: An HTN Planner for Robotics'
  zh: HATP：面向机器人学的HTN规划器
  ko: 'HATP: 로보틱스를 위한 HTN 플래너'
summary:
  en: HATP is a robotics-specific Hierarchical Task Network planning framework that introduces an agent-centered domain language,
    social-rule plan filtering, user-defined cost functions, and interleaved symbolic-geometric planning validated in 3D environments.
  zh: HATP是一个面向机器人学的层次任务网络规划框架，引入了以智能体为中心的领域语言、基于社会规则的计划过滤、用户自定义代价函数，以及在三維环境中验证的符号-几何交错规划。
  ko: HATP는 로봇공학을 위한 계층적 작업 네트워크 계획 프레임워크로, 에이전트 중심의 도메인 언어, 사회 규칙에 기반한 계획 필터링, 사용자 정의 비용 함수, 그리고 3D 환경에서 검증된 기호-기하학적 교차 계획을
    도입합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- htn_planning
- task_planning
- multi_agent_planning
- human_robot_interaction
- geometric_reasoning
- social_rules
- robotic_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1405.5345v2.
sources:
- id: src_001
  type: paper
  title: 'HATP: An HTN Planner for Robotics'
  url: https://arxiv.org/abs/1405.5345
  date: '2014'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Hierarchical Task Network (HTN) planning is a popular approach that cuts down on the classical planning search space by relying on a given hierarchical library of domain control knowledge. This provides an intuitive methodology for specifying high-level instructions on how robots and agents should perform tasks, while also giving the planner enough flexibility to choose the lower-level steps and their ordering. In this paper we present the HATP (Hierarchical Agent-based Task Planner) planning framework which extends the traditional HTN planning domain representation and semantics by making them more suitable for roboticists, and treating agents as "first class" entities in the language. The former is achieved by allowing "social rules" to be defined which specify what behaviour is acceptable/unacceptable by the agents/robots in the domain, and interleaving planning with geometric reasoning in order to validate online -with respect to a detailed geometric 3D world- the human/robot actions currently being pursued by HATP.

## 核心内容
Hierarchical Task Network (HTN) planning is a popular approach that cuts down on the classical planning search space by relying on a given hierarchical library of domain control knowledge. This provides an intuitive methodology for specifying high-level instructions on how robots and agents should perform tasks, while also giving the planner enough flexibility to choose the lower-level steps and their ordering. In this paper we present the HATP (Hierarchical Agent-based Task Planner) planning framework which extends the traditional HTN planning domain representation and semantics by making them more suitable for roboticists, and treating agents as "first class" entities in the language. The former is achieved by allowing "social rules" to be defined which specify what behaviour is acceptable/unacceptable by the agents/robots in the domain, and interleaving planning with geometric reasoning in order to validate online -with respect to a detailed geometric 3D world- the human/robot actions currently being pursued by HATP.

## 参考
- http://arxiv.org/abs/1405.5345v2

## Overview
Hierarchical Task Network (HTN) planning is a popular approach that cuts down on the classical planning search space by relying on a given hierarchical library of domain control knowledge. This provides an intuitive methodology for specifying high-level instructions on how robots and agents should perform tasks, while also giving the planner enough flexibility to choose the lower-level steps and their ordering. In this paper we present the HATP (Hierarchical Agent-based Task Planner) planning framework which extends the traditional HTN planning domain representation and semantics by making them more suitable for roboticists, and treating agents as "first class" entities in the language. The former is achieved by allowing "social rules" to be defined which specify what behaviour is acceptable/unacceptable by the agents/robots in the domain, and interleaving planning with geometric reasoning in order to validate online -with respect to a detailed geometric 3D world- the human/robot actions currently being pursued by HATP.

## Content
Hierarchical Task Network (HTN) planning is a popular approach that cuts down on the classical planning search space by relying on a given hierarchical library of domain control knowledge. This provides an intuitive methodology for specifying high-level instructions on how robots and agents should perform tasks, while also giving the planner enough flexibility to choose the lower-level steps and their ordering. In this paper we present the HATP (Hierarchical Agent-based Task Planner) planning framework which extends the traditional HTN planning domain representation and semantics by making them more suitable for roboticists, and treating agents as "first class" entities in the language. The former is achieved by allowing "social rules" to be defined which specify what behaviour is acceptable/unacceptable by the agents/robots in the domain, and interleaving planning with geometric reasoning in order to validate online -with respect to a detailed geometric 3D world- the human/robot actions currently being pursued by HATP.

## 개요
계층적 작업 네트워크(HTN) 계획은 주어진 계층적 도메인 제어 지식 라이브러리에 의존하여 고전적 계획 탐색 공간을 줄이는 인기 있는 접근 방식입니다. 이는 로봇과 에이전트가 작업을 수행하는 방법에 대한 상위 수준 지침을 지정하는 직관적인 방법론을 제공하는 동시에, 계획자가 하위 수준 단계와 그 순서를 선택할 수 있는 충분한 유연성을 제공합니다. 본 논문에서는 전통적인 HTN 계획 도메인 표현과 의미론을 로봇 공학자에게 더 적합하도록 확장하고, 언어에서 에이전트를 "일급" 개체로 취급하는 HATP(계층적 에이전트 기반 작업 계획자) 계획 프레임워크를 제시합니다. 전자는 도메인 내 에이전트/로봇의 허용 가능/허용 불가능한 행동을 지정하는 "사회적 규칙"을 정의할 수 있도록 하고, HATP가 현재 추구하는 인간/로봇 행동을 상세한 기하학적 3D 세계와 관련하여 온라인으로 검증하기 위해 계획과 기하학적 추론을 인터리빙함으로써 달성됩니다.

## 핵심 내용
계층적 작업 네트워크(HTN) 계획은 주어진 계층적 도메인 제어 지식 라이브러리에 의존하여 고전적 계획 탐색 공간을 줄이는 인기 있는 접근 방식입니다. 이는 로봇과 에이전트가 작업을 수행하는 방법에 대한 상위 수준 지침을 지정하는 직관적인 방법론을 제공하는 동시에, 계획자가 하위 수준 단계와 그 순서를 선택할 수 있는 충분한 유연성을 제공합니다. 본 논문에서는 전통적인 HTN 계획 도메인 표현과 의미론을 로봇 공학자에게 더 적합하도록 확장하고, 언어에서 에이전트를 "일급" 개체로 취급하는 HATP(계층적 에이전트 기반 작업 계획자) 계획 프레임워크를 제시합니다. 전자는 도메인 내 에이전트/로봇의 허용 가능/허용 불가능한 행동을 지정하는 "사회적 규칙"을 정의할 수 있도록 하고, HATP가 현재 추구하는 인간/로봇 행동을 상세한 기하학적 3D 세계와 관련하여 온라인으로 검증하기 위해 계획과 기하학적 추론을 인터리빙함으로써 달성됩니다.
