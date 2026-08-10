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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22224v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (696 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.22224v1

## 개요
FAME 프레임워크는 오프라인 형식적 종합을 통해 엄격한 안전 사양을 생성하고, 온라인 런타임 모니터링을 결합하여 AI 출력의 이상을 실시간으로 감지함으로써, AI가 안전 필수 시스템에서 자신 있지만 잘못된 출력을 생성하는 정적 장애 문제를 해결합니다. 자율주행 인식 시스템 실험에서 FAME은 93.5%의 정적 안전 위반을 성공적으로 식별했습니다. 이 프레임워크는 또한 ISO 26262 및 ISO/PAS 8800 표준을 참조하여 설계되었으며, 신뢰성 엔지니어에게 인증 가능한 실용적 경로를 제공하여 확률적 성능에서 증명 가능한 안전으로의 전환을 촉진합니다.

## 핵심 내용
### 방법
FAME 프레임워크는 두 가지 핵심 모듈로 구성됩니다:
- **오프라인 형식적 종합**: 시스템 모델과 안전 사양을 기반으로 형식적 검증 조건을 자동 생성하여, AI 구성 요소가 이상적인 환경에서 기대에 부합하는 동작을 보장합니다.
- **온라인 런타임 모니터링**: 시스템 실행 중 AI 출력과 형식적 조건 간의 편차를 실시간으로 모니터링하며, 정적 장애가 감지되면 즉시 경보를 발동합니다.

### 실험 설정
- **플랫폼**: CARLA 시뮬레이터를 사용하여 자율주행 시나리오를 구축했으며, 인식 시스템은 YOLOv4 객체 탐지 모델을 채택했습니다.
- **테스트 시나리오**: 보행자 횡단, 차량 가림, 조명 변화 등 전형적인 안전 필수 시나리오를 포함합니다.
- **평가 지표**: 안전 위반 탐지율(즉, 정적 장애가 성공적으로 식별된 비율)을 주요 지표로 사용합니다.

### 주요 수치
- **탐지율**: FAME은 93.5%의 정적 안전 위반을 성공적으로 탐지했습니다.
- **표준 정렬**: 프레임워크 설계는 ISO 26262(도로 차량 기능 안전) 및 ISO/PAS 8800(AI 안전) 표준을 따릅니다.

### 결론
FAME은 형식적 방법과 런타임 모니터링의 결합을 통해 AI가 안전 필수 시스템에 배포될 때 검증 가능한 신뢰성 보장을 제공합니다. 실험 결과 정적 장애 위험을 효과적으로 줄일 수 있으며, AI 시스템 인증을 위한 표준화된 경로를 제공합니다. 향후 작업은 더 많은 AI 구성 요소와 복잡한 시나리오로 확장될 것입니다.
