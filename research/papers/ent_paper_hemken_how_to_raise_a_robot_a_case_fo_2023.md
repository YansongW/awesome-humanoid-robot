---
$id: ent_paper_hemken_how_to_raise_a_robot_a_case_fo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: How to Raise a Robot — A Case for Neuro-Symbolic AI in Constrained Task Planning
    for Humanoid Assistive Robots
  zh: 如何培养机器人——面向人形辅助机器人约束任务规划的神经符号人工智能案例
  ko: 로봇을 기르는 방법—인간형 보조 로봇의 제약 조건 하 작업 계획을 위한 신경-기호 AI의 사례
summary:
  en: This paper argues that humanoid assistive robots require a neuro-symbolic hybrid
    approach to task planning in order to simultaneously satisfy privacy, security,
    and access-control constraints while retaining scalability and common-sense reasoning.
  zh: 本文主张，人形辅助机器人需要采用神经符号混合方法进行任务规划，以在保持可扩展性和常识推理能力的同时满足隐私、安全和访问控制约束。
  ko: 본 논문은 인간형 보조 로봇이 확장성과 상식 추론을 유지하면서 프라이버시, 보안 및 접근 제어 제약을 동시에 충족하기 위해 작업 계획을
    위한 신경-기호 하이브리드 접근법이 필요하다고 주장한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 12_policy_regulation_ethics
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- humanoid
- assistive_robot
- task_planning
- neuro_symbolic_ai
- access_control
- privacy
- security
- large_language_models
- pddl
- constraint_satisfaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full text before final verification.
sources:
- id: src_001
  type: paper
  title: How to Raise a Robot — A Case for Neuro-Symbolic AI in Constrained Task Planning
    for Humanoid Assistive Robots
  url: https://arxiv.org/abs/2312.08820
  date: '2023'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Humanoid robots are expected to assist humans in daily life, but their autonomy raises challenges in enforcing constraints such as privacy, security, and access control. The paper surveys three planning paradigms—classical symbolic planning with PDDL and Activity-Centric Access Control (ACAC), deep-learned neural planning, and large language model (LLM)-based planning—to identify their respective trade-offs. Based on this analysis, the authors argue that a neuro-symbolic hybrid approach is necessary to combine the formal constraint guarantees of symbolic methods with the scalability and common-sense knowledge of neural and LLM-based approaches.

The paper presents preliminary results and conceptual mappings rather than large-scale experiments. It maps Kautz's six levels of neuro-symbolic integration onto constrained robot task planning and identifies core challenges for deep neuro-symbolic integration of constraint satisfaction and task planning. The authors conclude that hybrid neuro-symbolic designs are essential for building task-universal, safe humanoid assistive robots.

The work frames its contribution as opening a new application domain for neuro-symbolic AI, emphasizing that assistive robots operating in care homes and human living spaces must be able to learn, explore, and plan while respecting diverse normative constraints.

## Key Contributions

- Compares symbolic constraint-ensuring planning, neural constraint-observing planning, and LLM-based planning for assistive robots.
- Demonstrates that LLMs can act as both planner and common-sense knowledge base for social-norm constraints.
- Maps Kautz's six levels of neuro-symbolic integration to constrained robot task planning.
- Identifies core challenges for deep neuro-symbolic integration of constraint satisfaction and task planning.
- Argues that hybrid neuro-symbolic designs are necessary for task-universal, safe humanoid assistive robots.

## Relevance to Humanoid Robotics

The paper directly addresses task planning for autonomous humanoid assistive robots in sensitive human environments such as care homes. Its focus on privacy, security, and access-control constraints is highly relevant to the safe, large-scale deployment of humanoid robots in human living spaces. The proposed neuro-symbolic methods target the combination of formal safety guarantees and adaptive, scalable reasoning that is seen as essential for real-world humanoid assistance.
