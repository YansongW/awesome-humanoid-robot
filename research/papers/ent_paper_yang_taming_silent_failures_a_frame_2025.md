---
$id: ent_paper_yang_taming_silent_failures_a_frame_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Taming Silent Failures: A Framework for Verifiable AI Reliability'
  zh: 驯服静默失效：可验证人工智能可靠性框架
  ko: '조용한 실패 다루기: 검증 가능한 AI 신뢰성을 위한 프레임워크'
summary:
  en: This paper introduces FAME (Formal Assurance and Monitoring Environment), a framework that combines offline formal synthesis
    with online runtime monitoring to detect silent failures in AI components within safety-critical systems, demonstrated
    on an autonomous vehicle perception system using CARLA and YOLOv4.
  zh: 本文提出FAME（形式化保证与监控环境）框架，结合离线形式化综合与在线运行时监控，检测安全关键系统中AI组件的静默失效，并在基于CARLA和YOLOv4的自动驾驶感知系统上进行了验证。
  ko: 본 논문은 오프라인 형식적 종합과 온라인 실행 시점 모니터링을 결합하여 안임계 시스템의 AI 구성 요소에서 조용한 실패를 탐지하는 FAME(Formal Assurance and Monitoring Environment)
    프레임워크를 제안하고, CARLA 및 YOLOv4를 사용한 자율주행 인지 시스템에서 검증하였다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
- 12_policy_regulation_ethics
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- runtime_monitoring
- silent_failure_detection
- formal_verification
- signal_temporal_logic
- runtime_assurance
- ai_safety
- perception_safety
- iso_26262
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22224v1.
sources:
- id: src_001
  type: paper
  title: 'Taming Silent Failures: A Framework for Verifiable AI Reliability'
  url: https://arxiv.org/abs/2510.22224
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
The integration of Artificial Intelligence (AI) into safety-critical systems introduces a new reliability paradigm: silent failures, where AI produces confident but incorrect outputs that can be dangerous. This paper introduces the Formal Assurance and Monitoring Environment (FAME), a novel framework that confronts this challenge. FAME synergizes the mathematical rigor of offline formal synthesis with the vigilance of online runtime monitoring to create a verifiable safety net around opaque AI components. We demonstrate its efficacy in an autonomous vehicle perception system, where FAME successfully detected 93.5% of critical safety violations that were otherwise silent. By contextualizing our framework within the ISO 26262 and ISO/PAS 8800 standards, we provide reliability engineers with a practical, certifiable pathway for deploying trustworthy AI. FAME represents a crucial shift from accepting probabilistic performance to enforcing provable safety in next-generation systems.

## 核心内容
The integration of Artificial Intelligence (AI) into safety-critical systems introduces a new reliability paradigm: silent failures, where AI produces confident but incorrect outputs that can be dangerous. This paper introduces the Formal Assurance and Monitoring Environment (FAME), a novel framework that confronts this challenge. FAME synergizes the mathematical rigor of offline formal synthesis with the vigilance of online runtime monitoring to create a verifiable safety net around opaque AI components. We demonstrate its efficacy in an autonomous vehicle perception system, where FAME successfully detected 93.5% of critical safety violations that were otherwise silent. By contextualizing our framework within the ISO 26262 and ISO/PAS 8800 standards, we provide reliability engineers with a practical, certifiable pathway for deploying trustworthy AI. FAME represents a crucial shift from accepting probabilistic performance to enforcing provable safety in next-generation systems.

## 参考
- http://arxiv.org/abs/2510.22224v1

## Overview
The integration of Artificial Intelligence (AI) into safety-critical systems introduces a new reliability paradigm: silent failures, where AI produces confident but incorrect outputs that can be dangerous. This paper introduces the Formal Assurance and Monitoring Environment (FAME), a novel framework that confronts this challenge. FAME synergizes the mathematical rigor of offline formal synthesis with the vigilance of online runtime monitoring to create a verifiable safety net around opaque AI components. We demonstrate its efficacy in an autonomous vehicle perception system, where FAME successfully detected 93.5% of critical safety violations that were otherwise silent. By contextualizing our framework within the ISO 26262 and ISO/PAS 8800 standards, we provide reliability engineers with a practical, certifiable pathway for deploying trustworthy AI. FAME represents a crucial shift from accepting probabilistic performance to enforcing provable safety in next-generation systems.

## Content
The integration of Artificial Intelligence (AI) into safety-critical systems introduces a new reliability paradigm: silent failures, where AI produces confident but incorrect outputs that can be dangerous. This paper introduces the Formal Assurance and Monitoring Environment (FAME), a novel framework that confronts this challenge. FAME synergizes the mathematical rigor of offline formal synthesis with the vigilance of online runtime monitoring to create a verifiable safety net around opaque AI components. We demonstrate its efficacy in an autonomous vehicle perception system, where FAME successfully detected 93.5% of critical safety violations that were otherwise silent. By contextualizing our framework within the ISO 26262 and ISO/PAS 8800 standards, we provide reliability engineers with a practical, certifiable pathway for deploying trustworthy AI. FAME represents a crucial shift from accepting probabilistic performance to enforcing provable safety in next-generation systems.

## 개요
인공지능(AI)을 안전 필수 시스템에 통합하면 새로운 신뢰성 패러다임, 즉 AI가 확신을 가지고 있지만 잘못된 출력을 생성하여 위험을 초래할 수 있는 '침묵 실패(silent failures)'가 도입됩니다. 본 논문은 이러한 문제에 대응하는 새로운 프레임워크인 FAME(Formal Assurance and Monitoring Environment)을 소개합니다. FAME은 오프라인 형식 합성의 수학적 엄밀성과 온라인 런타임 모니터링의 경계를 결합하여 불투명한 AI 구성 요소 주변에 검증 가능한 안전망을 구축합니다. 우리는 자율주행 차량 인식 시스템에서 FAME의 효용성을 입증했으며, FAME은 그렇지 않으면 침묵했을 치명적 안전 위반의 93.5%를 성공적으로 탐지했습니다. ISO 26262 및 ISO/PAS 8800 표준 내에서 프레임워크를 맥락화함으로써, 신뢰성 엔지니어에게 신뢰할 수 있는 AI를 배포하기 위한 실용적이고 인증 가능한 경로를 제공합니다. FAME은 차세대 시스템에서 확률적 성능을 수용하는 것에서 증명 가능한 안전을 강제하는 것으로의 중요한 전환을 나타냅니다.

## 핵심 내용
인공지능(AI)을 안전 필수 시스템에 통합하면 새로운 신뢰성 패러다임, 즉 AI가 확신을 가지고 있지만 잘못된 출력을 생성하여 위험을 초래할 수 있는 '침묵 실패(silent failures)'가 도입됩니다. 본 논문은 이러한 문제에 대응하는 새로운 프레임워크인 FAME(Formal Assurance and Monitoring Environment)을 소개합니다. FAME은 오프라인 형식 합성의 수학적 엄밀성과 온라인 런타임 모니터링의 경계를 결합하여 불투명한 AI 구성 요소 주변에 검증 가능한 안전망을 구축합니다. 우리는 자율주행 차량 인식 시스템에서 FAME의 효용성을 입증했으며, FAME은 그렇지 않으면 침묵했을 치명적 안전 위반의 93.5%를 성공적으로 탐지했습니다. ISO 26262 및 ISO/PAS 8800 표준 내에서 프레임워크를 맥락화함으로써, 신뢰성 엔지니어에게 신뢰할 수 있는 AI를 배포하기 위한 실용적이고 인증 가능한 경로를 제공합니다. FAME은 차세대 시스템에서 확률적 성능을 수용하는 것에서 증명 가능한 안전을 강제하는 것으로의 중요한 전환을 나타냅니다.
