---
$id: ent_paper_hartmann_evolution_of_safety_requiremen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis
    of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066'
  zh: 工业机器人安全要求的演进：ISO 10218-1/2（2011 vs. 2025）比较分析及 ISO/TS 15066 的整合
  ko: '산업용 로봇 안전 요구사항의 진화: ISO 10218-1/2(2011 대 2025) 비교 분석 및 ISO/TS 15066 통합'
summary:
  en: This paper compares ISO 10218-1/2:2011 with their 2025 revisions and analyzes
    the normative integration of ISO/TS 15066, highlighting expanded functional safety,
    cybersecurity, software validation, and new robot classification requirements.
  zh: 本文比较了 ISO 10218-1/2:2011 与其 2025 年修订版，并分析了 ISO/TS 15066 的规范性整合，重点阐述了功能安全、网络安全、软件验证以及新型机器人分类要求的扩展。
  ko: 본 논문은 ISO 10218-1/2:2011과 2025년 개정판을 비교하고 ISO/TS 15066의 규범적 통합을 분석하며, 확장된 기능
    안전, 사이버 보안, 소프트웨어 검증 및 새로운 로봇 분류 요구사항을 강조한다.
domains:
- 12_policy_regulation_ethics
- 03_manufacturing_processes
- 04_assembly_integration_testing
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- policy
tags:
- industrial_robot_safety
- iso_10218
- iso_ts_15066
- collaborative_robotics
- functional_safety
- cybersecurity
- human_robot_collaboration
- robot_certification
- safety_standards
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full text was not independently
    consulted. Requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis
    of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066'
  url: https://arxiv.org/abs/2602.17822
  date: '2026'
  accessed_at: '2026-06-26'
---


## Overview

Industrial robotics is now central to large-scale manufacturing, while collaborative robotics introduces new forms of human-machine interaction that the 2011 editions of ISO 10218-1/2 did not fully address. This paper conducts a comparative content analysis of ISO 10218-1:2011 versus ISO 10218-1:2025, ISO 10218-2:2011 versus ISO 10218-2:2025, and ISO/TS 15066:2016, classifying changes as technical, structural/methodological, or terminological. The authors find that the 2025 revisions substantially expand functional safety and cybersecurity requirements, introduce new robot classifications (Class I/II) and terminology for collaborative applications/tasks, and normatively integrate ISO/TS 15066 into ISO 10218-2:2025. The result is a unified framework covering mechanical, functional, and digital safety for the design and operation of modern robotic systems.

The analysis covers structure, terminology, technical requirements, and annexes across the standards. Key technical additions include requirements for cybersecurity, protection against unauthorized access in networked robotic systems, software parameterization and validation, cableless teach pendants, 3-position enabling devices, sensitive protective equipment (SPE), and force and pressure measurement devices (PFMD). The paper also discusses practical impacts on system design, integration, certification timelines, and cost.

The authors note that the new edition synthesizes mechanical, functional, and digital safety requirements, establishing a comprehensive framework for the design and operation of modern robotic systems.

## Key Contributions

- Comparative analysis of ISO 10218-1/2 (2011 vs. 2025) covering structure, terminology, technical requirements, and annexes.
- Identification of expanded functional safety, cybersecurity, and software parameterization/validation requirements in the 2025 revisions.
- Analysis of new robot classification (Class I/II) and collaborative application/task terminology.
- Evaluation of the normative integration of ISO/TS 15066:2016 into ISO 10218-2:2025.
- Discussion of practical impacts on robot design, integration, certification, commissioning time, and cost.

## Relevance to Humanoid Robotics

Although the paper focuses on industrial rather than humanoid robots, the updated ISO 10218-1/2:2025 framework is directly relevant to humanoid deployment in manufacturing. The standards' treatment of collaborative applications, biomechanical contact limits, functional safety, cybersecurity, and software validation provides a regulatory foundation that humanoid robots must satisfy to enter industrial settings at scale. As humanoid robots are increasingly designed for human-robot collaboration on factory floors, the classifications, verification methods, and safety limits in ISO 10218-1/2:2025 and ISO/TS 15066 will shape certification pathways and market adoption.
