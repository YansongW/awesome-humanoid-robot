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

