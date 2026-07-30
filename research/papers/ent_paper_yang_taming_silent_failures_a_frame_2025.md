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
  zh: FAME（Formal Assurance and Monitoring Environment）是一个结合离线形式化综合与在线运行时监控的框架，旨在检测安全关键系统中AI组件的静默故障。该框架由论文作者提出，在基于CARLA和YOLOv4的自动驾驶感知系统上验证，成功检测出93.5%的关键安全违规行为。其核心贡献在于为不可解释的AI组件提供可验证的安全保障，并符合ISO
    26262和ISO/PAS 8800标准。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22224v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
FAME框架通过离线形式化综合生成严格的安全规范，再结合在线运行时监控实时检测AI输出的异常，从而解决AI在安全关键系统中产生自信但错误输出的静默故障问题。在自动驾驶感知系统的实验中，FAME成功识别了93.5%的静默安全违规行为。该框架还参照ISO 26262和ISO/PAS 8800标准设计，为可靠性工程师提供了一条可认证的实用路径，推动从概率性能向可证明安全的转变。

## 核心内容
### 方法
FAME框架由两个核心模块组成：
- **离线形式化综合**：基于系统模型和安全规范，自动生成形式化验证条件，确保AI组件在理想环境下的行为符合预期。
- **在线运行时监控**：在系统运行过程中，实时监测AI输出与形式化条件的偏差，一旦检测到静默故障立即触发警报。

### 实验设置
- **平台**：使用CARLA模拟器构建自动驾驶场景，感知系统采用YOLOv4目标检测模型。
- **测试场景**：包括行人横穿、车辆遮挡、光照变化等典型安全关键场景。
- **评估指标**：以安全违规检测率（即静默故障被成功识别的比例）为主要指标。

### 关键数字
- **检测率**：FAME成功检测出93.5%的静默安全违规行为。
- **标准对齐**：框架设计遵循ISO 26262（道路车辆功能安全）和ISO/PAS 8800（AI安全）标准。

### 结论
FAME通过形式化方法与运行时监控的结合，为AI在安全关键系统中的部署提供了可验证的可靠性保障。实验证明其能有效降低静默故障风险，并为AI系统的认证提供了标准化路径。未来工作将扩展至更多AI组件和复杂场景。

## Overview
The integration of Artificial Intelligence (AI) into safety-critical systems introduces a new reliability paradigm: silent failures, where AI produces confident but incorrect outputs that can be dangerous. This paper introduces the Formal Assurance and Monitoring Environment (FAME), a novel framework that confronts this challenge. FAME synergizes the mathematical rigor of offline formal synthesis with the vigilance of online runtime monitoring to create a verifiable safety net around opaque AI components. We demonstrate its efficacy in an autonomous vehicle perception system, where FAME successfully detected 93.5% of critical safety violations that were otherwise silent. By contextualizing our framework within the ISO 26262 and ISO/PAS 8800 standards, we provide reliability engineers with a practical, certifiable pathway for deploying trustworthy AI. FAME represents a crucial shift from accepting probabilistic performance to enforcing provable safety in next-generation systems.

## 개요
인공지능(AI)을 안전 필수 시스템에 통합하면 새로운 신뢰성 패러다임, 즉 AI가 확신을 가지고 있지만 잘못된 출력을 생성하여 위험을 초래할 수 있는 '침묵 실패(silent failures)'가 도입됩니다. 본 논문은 이러한 문제에 대응하는 새로운 프레임워크인 FAME(Formal Assurance and Monitoring Environment)을 소개합니다. FAME은 오프라인 형식 합성의 수학적 엄밀성과 온라인 런타임 모니터링의 경계를 결합하여 불투명한 AI 구성 요소 주변에 검증 가능한 안전망을 구축합니다. 우리는 자율주행 차량 인식 시스템에서 FAME의 효용성을 입증했으며, FAME은 그렇지 않으면 침묵했을 치명적 안전 위반의 93.5%를 성공적으로 탐지했습니다. ISO 26262 및 ISO/PAS 8800 표준 내에서 프레임워크를 맥락화함으로써, 신뢰성 엔지니어에게 신뢰할 수 있는 AI를 배포하기 위한 실용적이고 인증 가능한 경로를 제공합니다. FAME은 차세대 시스템에서 확률적 성능을 수용하는 것에서 증명 가능한 안전을 강제하는 것으로의 중요한 전환을 나타냅니다.

## 핵심 내용
인공지능(AI)을 안전 필수 시스템에 통합하면 새로운 신뢰성 패러다임, 즉 AI가 확신을 가지고 있지만 잘못된 출력을 생성하여 위험을 초래할 수 있는 '침묵 실패(silent failures)'가 도입됩니다. 본 논문은 이러한 문제에 대응하는 새로운 프레임워크인 FAME(Formal Assurance and Monitoring Environment)을 소개합니다. FAME은 오프라인 형식 합성의 수학적 엄밀성과 온라인 런타임 모니터링의 경계를 결합하여 불투명한 AI 구성 요소 주변에 검증 가능한 안전망을 구축합니다. 우리는 자율주행 차량 인식 시스템에서 FAME의 효용성을 입증했으며, FAME은 그렇지 않으면 침묵했을 치명적 안전 위반의 93.5%를 성공적으로 탐지했습니다. ISO 26262 및 ISO/PAS 8800 표준 내에서 프레임워크를 맥락화함으로써, 신뢰성 엔지니어에게 신뢰할 수 있는 AI를 배포하기 위한 실용적이고 인증 가능한 경로를 제공합니다. FAME은 차세대 시스템에서 확률적 성능을 수용하는 것에서 증명 가능한 안전을 강제하는 것으로의 중요한 전환을 나타냅니다.

## 参考
- http://arxiv.org/abs/2510.22224v1
