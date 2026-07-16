---
$id: ent_paper_liu_unified_embodied_vlm_reasoning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training
  zh: ERIQ
  ko: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training
summary:
  en: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
  zh: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
  ko: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eriq
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24125v2.
sources:
- id: src_001
  type: paper
  title: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (arXiv)
  url: https://arxiv.org/abs/2512.24125
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ERIQ source
  url: https://doi.org/10.48550/arXiv.2512.24125
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## 核心内容
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## 参考
- http://arxiv.org/abs/2512.24125v2

## Overview
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## Content
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## 개요
개방형 환경에서 작동하는 범용 로봇 시스템은 광범위한 일반화와 고정밀 동작 실행을 동시에 달성해야 하며, 이는 기존의 Vision-Language-Action(VLA) 모델에게 여전히 어려운 과제입니다. 대규모 Vision-Language 모델(VLM)이 의미론적 일반화를 향상시키지만, 체화된 추론이 부족하면 취약한 행동이 발생하고, 반대로 강력한 추론만으로는 정밀한 제어 없이는 불충분합니다. 이러한 병목 현상을 분리하여 정량적으로 평가하기 위해, 우리는 로봇 조작 분야의 대규모 체화된 추론 벤치마크인 ERIQ(Embodied Reasoning Intelligence Quotient)를 도입합니다. 이는 네 가지 추론 차원에 걸쳐 6,000개 이상의 질문-답변 쌍으로 구성됩니다. 추론과 실행을 분리함으로써 ERIQ는 체계적인 평가를 가능하게 하며, 체화된 추론 능력과 종단 간 VLA 일반화 사이에 강한 양의 상관관계를 밝혀냅니다. 추론에서 정밀한 실행으로의 격차를 해소하기 위해, 우리는 연속 제어를 이산 시퀀스로 변환하면서도 고충실도 궤적 재구성을 유지하는 흐름 매칭 기반 동작 토크나이저인 FACT를 제안합니다. 그 결과 생성된 GenieReasoner는 통합된 공간에서 추론과 동작을 공동으로 최적화하여 실제 작업에서 연속 동작 및 기존 이산 동작 기준선을 모두 능가합니다. ERIQ와 FACT는 함께 추론-정밀도 트레이드오프를 진단하고 극복하기 위한 원칙적인 프레임워크를 제공하며, 강력하고 범용적인 로봇 조작을 발전시킵니다. 프로젝트 페이지: https://geniereasoner.github.io/GenieReasoner/

## 핵심 내용
개방형 환경에서 작동하는 범용 로봇 시스템은 광범위한 일반화와 고정밀 동작 실행을 동시에 달성해야 하며, 이는 기존의 Vision-Language-Action(VLA) 모델에게 여전히 어려운 과제입니다. 대규모 Vision-Language 모델(VLM)이 의미론적 일반화를 향상시키지만, 체화된 추론이 부족하면 취약한 행동이 발생하고, 반대로 강력한 추론만으로는 정밀한 제어 없이는 불충분합니다. 이러한 병목 현상을 분리하여 정량적으로 평가하기 위해, 우리는 로봇 조작 분야의 대규모 체화된 추론 벤치마크인 ERIQ(Embodied Reasoning Intelligence Quotient)를 도입합니다. 이는 네 가지 추론 차원에 걸쳐 6,000개 이상의 질문-답변 쌍으로 구성됩니다. 추론과 실행을 분리함으로써 ERIQ는 체계적인 평가를 가능하게 하며, 체화된 추론 능력과 종단 간 VLA 일반화 사이에 강한 양의 상관관계를 밝혀냅니다. 추론에서 정밀한 실행으로의 격차를 해소하기 위해, 우리는 연속 제어를 이산 시퀀스로 변환하면서도 고충실도 궤적 재구성을 유지하는 흐름 매칭 기반 동작 토크나이저인 FACT를 제안합니다. 그 결과 생성된 GenieReasoner는 통합된 공간에서 추론과 동작을 공동으로 최적화하여 실제 작업에서 연속 동작 및 기존 이산 동작 기준선을 모두 능가합니다. ERIQ와 FACT는 함께 추론-정밀도 트레이드오프를 진단하고 극복하기 위한 원칙적인 프레임워크를 제공하며, 강력하고 범용적인 로봇 조작을 발전시킵니다. 프로젝트 페이지: https://geniereasoner.github.io/GenieReasoner/
