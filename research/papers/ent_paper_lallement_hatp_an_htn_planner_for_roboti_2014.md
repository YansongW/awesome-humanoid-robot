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
  en: HATP is a robotics-specific Hierarchical Task Network planning framework that
    introduces an agent-centered domain language, social-rule plan filtering, user-defined
    cost functions, and interleaved symbolic-geometric planning validated in 3D environments.
  zh: HATP是一个面向机器人学的层次任务网络规划框架，引入了以智能体为中心的领域语言、基于社会规则的计划过滤、用户自定义代价函数，以及在三維环境中验证的符号-几何交错规划。
  ko: HATP는 로봇공학을 위한 계층적 작업 네트워크 계획 프레임워크로, 에이전트 중심의 도메인 언어, 사회 규칙에 기반한 계획 필터링, 사용자
    정의 비용 함수, 그리고 3D 환경에서 검증된 기호-기하학적 교차 계획을 도입합니다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification required
    before promotion to verified.; approved by autonomous review workflow.
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

## Overview

HATP (Hierarchical Agent-based Task Planner) is an HTN planning framework designed to make classical task planning more accessible and useful for roboticists. It preserves the core benefit of HTN planning—reduced search through user-supplied hierarchical domain knowledge—while extending the representation language so that agents become first-class entities. The framework also allows users to encode social rules that characterize acceptable or unacceptable behavior, and to attach C++ cost functions so that the planner can search for least-cost plans among generated candidates. A distinctive feature is the coupling of symbolic HTN planning with geometric reasoning: HATP invokes a Geometric Task Planner through evaluable predicates to validate actions online against a detailed 3D world model.

The paper positions HATP against classical HTN planners such as SHOP, emphasizing that traditional HTN formalisms are not well suited to robotic domains because they do not explicitly represent agents, multi-agent interactions, or geometric feasibility. To address this, HATP provides an object-oriented domain description, supports method preconditions and effects with an agent-oriented syntax, and splits the final plan into synchronized execution streams for multiple agents. The framework is implemented and demonstrated on a PR2 robot interacting with a human in a shared workspace.

## Key Contributions

- An agent-first-class HTN representation language tailored for roboticists, including object-oriented domain modeling and agent-oriented syntax.
- Social rules for filtering primitive plans according to criteria such as wasted time, effort balancing, intricacy, and undesirable action sequences.
- Least-cost HTN plan search using user-supplied C++ cost functions.
- Interleaving of symbolic HTN planning with geometric task planning through evaluable predicates, enabling online validation in a 3D geometric world.
- Automatic splitting of generated solutions into synchronised multi-agent execution streams.

## Relevance to Humanoid Robotics

HATP is directly relevant to humanoid robotics because it provides a scalable, agent-aware task-planning architecture capable of coordinating complex multi-agent activities involving humans and robots. The explicit modeling of agents and the inclusion of social rules allow a planner to enforce behavior that is acceptable in shared workspaces, which is critical for humanoid robots deployed in factories, homes, or collaborative environments. Moreover, the integration of symbolic planning with geometric validation ensures that plans are not only logically sound but also physically feasible in a 3D world, addressing a key requirement for full-body humanoid motion and manipulation.
