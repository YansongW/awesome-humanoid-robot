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
  en: This paper introduces FAME (Formal Assurance and Monitoring Environment), a
    framework that combines offline formal synthesis with online runtime monitoring
    to detect silent failures in AI components within safety-critical systems, demonstrated
    on an autonomous vehicle perception system using CARLA and YOLOv4.
  zh: 本文提出FAME（形式化保证与监控环境）框架，结合离线形式化综合与在线运行时监控，检测安全关键系统中AI组件的静默失效，并在基于CARLA和YOLOv4的自动驾驶感知系统上进行了验证。
  ko: 본 논문은 오프라인 형식적 종합과 온라인 실행 시점 모니터링을 결합하여 안임계 시스템의 AI 구성 요소에서 조용한 실패를 탐지하는 FAME(Formal
    Assurance and Monitoring Environment) 프레임워크를 제안하고, CARLA 및 YOLOv4를 사용한 자율주행 인지
    시스템에서 검증하였다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full paper before verification.
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

## Overview

This paper introduces the Formal Assurance and Monitoring Environment (FAME), a framework designed to address silent failures in AI components deployed in safety-critical systems. Silent failures occur when AI systems produce confident but incorrect outputs without triggering conventional diagnostics, posing serious safety risks. FAME combines offline formal synthesis with online runtime monitoring to create a verifiable safety net around opaque AI components. The framework uses Signal Temporal Logic (STL) specifications, captured through controlled natural-language templates, to synthesize lightweight runtime monitors that continuously observe AI inputs and outputs. These monitors trigger mitigations when violations are detected, and an assurance feedback loop curates violation contexts for model retraining and specification refinement.

The paper demonstrates FAME in an autonomous vehicle perception system implemented with CARLA and YOLOv4. The toolchain uses RTAMT to generate portable C++/ROS 2 monitors from STL specifications. In the reported experiments, FAME detected 93.5% of critical safety violations that were otherwise silent, with zero false positives in nominal scenarios. The work is positioned within the ISO 26262 and ISO/PAS 8800 standards to provide a certifiable pathway for deploying trustworthy AI.

FAME represents a methodological shift from accepting probabilistic performance to enforcing provable safety for AI components. While the empirical evaluation is limited to autonomous driving perception, the underlying runtime-assurance methodology is framed as applicable to other safety-critical robotic domains.

## Key Contributions

- FAME framework combining offline formal synthesis with online runtime monitoring.
- STL-based specification engineering workflow supported by controlled natural-language templates.
- Automated monitor synthesis toolchain using RTAMT to generate portable C++/ROS 2 monitors.
- Assurance feedback loop that curates violation contexts for model retraining and specification refinement.
- CARLA/YOLOv4 proof-of-concept detecting 93.5% of silent failures with zero false positives in nominal scenarios.

## Relevance to Humanoid Robotics

Although the paper evaluates FAME in autonomous driving perception, its runtime-assurance methodology is directly applicable to humanoid robot perception and control stacks. Humanoid robots increasingly rely on opaque learning-based components for vision, state estimation, and motion planning, all of which must operate safely on production platforms. The FAME approach of synthesizing lightweight STL monitors from formal specifications and wrapping them around AI components can be transferred to detect silent failures in humanoid vision systems, gait controllers, and task planners.

The framework's alignment with ISO 26262 and ISO/PAS 8800 also provides a starting point for addressing emerging safety standards for humanoid robots. However, the limitations explicitly note that cross-domain design patterns remain conceptual and require future empirical validation in humanoid or general robotics settings.
