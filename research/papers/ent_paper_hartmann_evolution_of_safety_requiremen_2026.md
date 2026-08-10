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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.17822v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (789 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.17822v1

## 개요
본 논문은 ISO 10218-1/2:2011과 2025 개정판의 구조, 용어, 기술 요구사항 및 부록에서의 변화를 체계적으로 비교한다. 연구 결과, 새 버전은 기능 안전과 사이버 보안 요구사항을 크게 강화하고, 로봇 및 협동 애플리케이션에 대한 새로운 분류를 도입했으며, 기술 사양서 ISO/TS 15066을 규범적 프레임워크에 포함시켰다. 이러한 변화는 산업용 로봇이 대규모 제조에서 인간-로봇 협업 패러다임으로 전환되는 과정에서의 안전 요구를 반영하며, 궁극적으로 기계적, 기능적, 디지털 안전 요구사항을 하나의 통합 체계로 결합한다.

## 핵심 내용
### 연구 배경 및 동기
- 산업용 로봇은 대규모 제조의 핵심이 되었으며, 동시에 협동 로봇은 인간-로봇 상호작용의 새로운 패러다임을 추진하고 있다.
- 이러한 발전은 안전 표준의 전면적인 개정을 요구하며, 특히 네트워크화된 로봇 시스템의 사이버 보안과 무단 접근 방지에 중점을 둔다.

### 표준 비교 분석
- **구조 변화**: 2025 버전은 장(chapter) 구조를 재구성하고, 용어 정의를 더 정밀하게 했으며, 기술 요구사항과 부록 내용을 크게 확장했다.
- **기능 안전 확장**: 새 버전은 기능 안전 요구사항을 현저히 강화하여, 더 복잡한 제어 로직과 고장 대응 메커니즘을 포함한다.
- **사이버 보안 신설**: 무단 접근 방지, 데이터 무결성, 통신 보안을 포함한 사이버 보안 요구사항을 처음으로 체계적으로 포함한다.
- **소프트웨어 검증 강화**: 로봇 제어 소프트웨어의 검증 및 확인에 대해 더 엄격한 규정을 도입하여 소프트웨어 신뢰성을 보장한다.

### 주요 변화
- **로봇 분류**: 2025 버전은 새로운 로봇 분류 체계를 도입하여, 다양한 위험 수준과 적용 시나리오를 구분한다.
- **협동 애플리케이션 분류**: 협동 로봇에 대해 안전 모니터링 정지, 수동 유도, 속도 및 힘 제한 등과 같은 더 세분화된 애플리케이션 범주를 정의한다.
- **ISO/TS 15066 통합**: 원래 기술 사양서였던 ISO/TS 15066(협동 로봇 안전 요구사항)을 규범적 참조로 승격시켜, 표준의 핵심 구성 요소로 만든다.

### 결론
- 2025 버전 ISO 10218-1/2는 기계적, 기능적, 디지털 안전 요구사항을 설계부터 운영까지의 전체 수명 주기를 포괄하는 하나의 통합 프레임워크로 결합한다.
- 이러한 변화는 산업용 로봇이 전통적인 격리 운영에서 인간-로봇 협업, 네트워크화된 지능형 시스템으로 전환되는 과정에서의 안전 요구를 반영한다.
