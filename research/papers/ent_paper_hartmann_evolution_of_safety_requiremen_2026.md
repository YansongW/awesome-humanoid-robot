---
$id: ent_paper_hartmann_evolution_of_safety_requiremen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and
    Integration of ISO/TS 15066'
  zh: 工业机器人安全要求的演进：ISO 10218-1/2（2011 vs. 2025）比较分析及 ISO/TS 15066 的整合
  ko: '산업용 로봇 안전 요구사항의 진화: ISO 10218-1/2(2011 대 2025) 비교 분석 및 ISO/TS 15066 통합'
summary:
  en: This paper compares ISO 10218-1/2:2011 with their 2025 revisions and analyzes the normative integration of ISO/TS 15066,
    highlighting expanded functional safety, cybersecurity, software validation, and new robot classification requirements.
  zh: 本文对比分析了工业机器人安全标准ISO 10218-1/2的2011版与2025修订版，并探讨了ISO/TS 15066的规范性整合。核心贡献在于揭示了新版标准在功能安全、网络安全、软件验证及机器人分类要求上的显著扩展，为现代机器人系统设计提供了综合框架。
  ko: 본 논문은 ISO 10218-1/2:2011과 2025년 개정판을 비교하고 ISO/TS 15066의 규범적 통합을 분석하며, 확장된 기능 안전, 사이버 보안, 소프트웨어 검증 및 새로운 로봇 분류 요구사항을
    강조한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.17822v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and
    Integration of ISO/TS 15066'
  url: https://arxiv.org/abs/2602.17822
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
本文系统比较了ISO 10218-1/2:2011与2025修订版在结构、术语、技术要求和附录上的演变。研究发现，新版标准大幅强化了功能安全与网络安全要求，引入了针对机器人和协作应用的新分类，并将技术规范ISO/TS 15066纳入规范性框架。这些变化反映了工业机器人从大规模制造向人机协作范式转变的安全需求，最终将机械、功能和数字安全要求整合为一个统一体系。

## 核心内容
### 研究背景与动机
- 工业机器人已成为大规模制造的核心，同时协作机器人正推动人机交互新范式。
- 这些进步要求安全标准全面修订，特别是针对网络化机器人系统的网络安全和未授权访问防护。

### 标准对比分析
- **结构演变**：2025版重新组织了章节结构，术语定义更精确，技术要求和附录内容大幅扩充。
- **功能安全扩展**：新版显著提升了功能安全要求，涵盖更复杂的控制逻辑和故障响应机制。
- **网络安全新增**：首次系统性地纳入网络安全要求，包括防止未授权访问、数据完整性和通信安全。
- **软件验证强化**：对机器人控制软件的验证和确认提出了更严格的规定，确保软件可靠性。

### 关键变化
- **机器人分类**：2025版引入了新的机器人分类体系，区分不同风险等级和应用场景。
- **协作应用分类**：针对协作机器人，定义了更细化的应用类别，如安全监控停止、手动引导、速度和力限制等。
- **ISO/TS 15066整合**：将原本作为技术规范的ISO/TS 15066（协作机器人安全要求）提升为规范性引用，成为标准核心组成部分。

### 结论
- 2025版ISO 10218-1/2将机械、功能和数字安全要求综合为一个统一框架，覆盖从设计到运行的完整生命周期。
- 这一演变反映了工业机器人从传统隔离操作向人机协作、网络化智能系统转型的安全需求。

## Overview
Industrial robotics has established itself as an integral component of large-scale manufacturing enterprises. Simultaneously, collaborative robotics is gaining prominence, introducing novel paradigms of human-machine interaction. These advancements have necessitated a comprehensive revision of safety standards, specifically incorporating requirements for cybersecurity and protection against unauthorized access in networked robotic systems. This article presents a comparative analysis of the ISO 10218:2011 and ISO 10218:2025 standards, examining the evolution of their structure, terminology, technical requirements, and annexes. The analysis reveals significant expansions in functional safety and cybersecurity, the introduction of new classifications for robots and collaborative applications, and the normative integration of the technical specification ISO/TS 15066. Consequently, the new edition synthesizes mechanical, functional, and digital safety requirements, establishing a comprehensive framework for the design and operation of modern robotic systems.

## 개요
산업용 로봇 공학은 대규모 제조 기업의 필수 구성 요소로 자리 잡았습니다. 동시에 협동 로봇 공학이 부상하며 인간-기계 상호작용의 새로운 패러다임을 도입하고 있습니다. 이러한 발전은 안전 표준의 포괄적인 개정을 필요로 하게 했으며, 특히 네트워크화된 로봇 시스템에서 사이버 보안 및 무단 접근 방지 요구 사항을 포함하게 되었습니다. 본 논문은 ISO 10218:2011과 ISO 10218:2025 표준의 비교 분석을 제시하며, 구조, 용어, 기술 요구 사항 및 부속서의 변화를 검토합니다. 분석 결과, 기능 안전과 사이버 보안의 상당한 확장, 로봇 및 협동 애플리케이션에 대한 새로운 분류 도입, 기술 사양 ISO/TS 15066의 규범적 통합이 드러났습니다. 결과적으로, 새 판은 기계적, 기능적, 디지털 안전 요구 사항을 종합하여 현대 로봇 시스템의 설계 및 운영을 위한 포괄적인 프레임워크를 구축합니다.

## 핵심 내용
산업용 로봇 공학은 대규모 제조 기업의 필수 구성 요소로 자리 잡았습니다. 동시에 협동 로봇 공학이 부상하며 인간-기계 상호작용의 새로운 패러다임을 도입하고 있습니다. 이러한 발전은 안전 표준의 포괄적인 개정을 필요로 하게 했으며, 특히 네트워크화된 로봇 시스템에서 사이버 보안 및 무단 접근 방지 요구 사항을 포함하게 되었습니다. 본 논문은 ISO 10218:2011과 ISO 10218:2025 표준의 비교 분석을 제시하며, 구조, 용어, 기술 요구 사항 및 부속서의 변화를 검토합니다. 분석 결과, 기능 안전과 사이버 보안의 상당한 확장, 로봇 및 협동 애플리케이션에 대한 새로운 분류 도입, 기술 사양 ISO/TS 15066의 규범적 통합이 드러났습니다. 결과적으로, 새 판은 기계적, 기능적, 디지털 안전 요구 사항을 종합하여 현대 로봇 시스템의 설계 및 운영을 위한 포괄적인 프레임워크를 구축합니다.

## 参考
- http://arxiv.org/abs/2602.17822v1
