---
$id: ent_paper_walker_desiderata_for_planning_system_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Desiderata for Planning Systems in General-Purpose Service Robots
  zh: 通用服务机器人规划系统的期望特性
  ko: 범용 서비스 로봇 계획 시스템을 위한 요구사항
summary:
  en: Proposes desiderata for planning and reasoning systems to support general-purpose
    service robots operating in homes and offices, emphasizing natural human interfaces
    and robust fallback methods.
  zh: 提出针对在家庭和办公室环境中运行的通用服务机器人的规划与推理系统的期望特性，强调自然人机交互与鲁棒的回退方法。
  ko: 가정과 사무실에서 동작하는 범용 서비스 로봇을 지원하기 위한 계획 및 추론 시스템의 요구사항을 제안하며, 자연스러운 인간-로봇 상호작용과
    강건한 폴백 방법을 강조한다.
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
- service_robot_planning
- task_planning
- human_robot_interaction
- fallback_strategies
- knowledge_representation
- general_purpose_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text citation locations
    and relationship details require human review before full verification.; approved
    by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: Desiderata for Planning Systems in General-Purpose Service Robots
  url: https://arxiv.org/abs/1907.02300
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This position paper addresses the absence of a unified view on what features knowledge representation and planning systems should provide for general-purpose service robots. Drawing on experience with service robots in home and office environments, the authors organize their requirements around three factors: users, the environment, and the robot system. The paper argues that diverging assumptions about these factors have slowed integrated progress and calls for planning systems that explicitly support the full set of needs arising in real-world service deployments.

The proposed desiderata emphasize two cross-cutting concerns: natural human interfaces that allow non-expert users to task and interact with robots flexibly, and robust fallback methods that maintain useful behavior when human interactions or environmental assumptions fail. The authors survey relevant work in planning and robotics, identify gaps between existing systems and the proposed desiderata, and advocate for integrated approaches that address the complete set rather than optimizing individual capabilities in isolation.

Although the paper does not present new empirical results or a new robot implementation, it provides a structured framing that can guide future research and system design for user-facing autonomous robots.

## Key Contributions

- Proposes a unified set of desiderata for planning and reasoning systems in general-purpose service robots.
- Organizes requirements around three factors: users, environment, and robot system.
- Emphasizes natural human interfaces and robust fallback methods as essential cross-cutting requirements.
- Surveys relevant work and identifies gaps between existing planning systems and the proposed desiderata.
- Advocates for integrated approaches that address the full set of desiderata rather than isolated capabilities.

## Relevance to Humanoid Robotics

The desiderata are directly relevant to humanoid robot deployment because mass-produced humanoids are expected to operate as general-purpose service robots in unstructured human environments. Planning systems that support natural tasking, environmental uncertainty, and graceful degradation are foundational AI capabilities for such products. The paper's framing helps bridge academic planning research and the practical requirements of user-facing humanoid systems in homes, offices, and public spaces.
