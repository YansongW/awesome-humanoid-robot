---
$id: ent_paper_zhang_coc_vla_delving_into_adversari_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
  zh: CoC-VLA
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
summary:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
  zh: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coc_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19914v1.
sources:
- id: src_001
  type: paper
  title: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (arXiv)'
  url: https://arxiv.org/abs/2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoC-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 核心内容
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 参考
- http://arxiv.org/abs/2511.19914v1

## Overview
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## Content
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 개요
자율주행은 인공지능의 대표적인 응용 분야입니다. 최근 접근 방식은 일반적인 시나리오에만 집중하던 것에서 미묘한 인간 행동, 교통 사고, 비정상적인 운전 패턴과 같은 복잡한 롱테일(long-tail) 상황을 다루는 방향으로 전환되었습니다. 대규모 언어 모델(LLM)이 시각적 및 자연어 입력을 이해하고 지시를 따르는 능력을 입증함에 따라, 최근 방법들은 LLM을 자율주행 시스템에 통합하여 다양한 시나리오에서 추론, 해석 가능성 및 성능을 향상시키고 있습니다. 그러나 기존 방법들은 일반적으로 산업 배포에 적합한 실제 데이터나 희귀하거나 어려운 사례에 맞춰진 시뮬레이션 데이터 중 하나에 의존합니다. 두 데이터 소스의 상호 보완적 장점을 효과적으로 통합하는 접근 방식은 거의 없습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션에서 실제 배포로 롱테일 처리 능력을 전이하는 새로운 VLM 기반 종단간 적대적 전이 프레임워크인 CoC-VLA를 제안합니다. 이 프레임워크는 교사 VLM 모델, 학생 VLM 모델, 그리고 판별기로 구성됩니다. 교사 및 학생 VLM 모델은 모두 Chain-of-Causality Visual-Language Model(CoC VLM)이라는 공유 기본 아키텍처를 사용하며, 이는 종단간 텍스트 어댑터를 통해 시간 정보를 통합합니다. 이 아키텍처는 복잡한 운전 논리를 추론하기 위한 사고 사슬(chain-of-thought) 추론을 지원합니다. 교사 및 학생 VLM 모델은 각각 시뮬레이션 및 실제 데이터셋에서 사전 훈련됩니다. 판별기는 새로운 역전파 전략을 사용하여 학생 VLM 모델이 시뮬레이션 환경에서 실제 환경으로 롱테일 처리 능력을 전이하도록 적대적으로 훈련됩니다.

## 핵심 내용
자율주행은 인공지능의 대표적인 응용 분야입니다. 최근 접근 방식은 일반적인 시나리오에만 집중하던 것에서 미묘한 인간 행동, 교통 사고, 비정상적인 운전 패턴과 같은 복잡한 롱테일(long-tail) 상황을 다루는 방향으로 전환되었습니다. 대규모 언어 모델(LLM)이 시각적 및 자연어 입력을 이해하고 지시를 따르는 능력을 입증함에 따라, 최근 방법들은 LLM을 자율주행 시스템에 통합하여 다양한 시나리오에서 추론, 해석 가능성 및 성능을 향상시키고 있습니다. 그러나 기존 방법들은 일반적으로 산업 배포에 적합한 실제 데이터나 희귀하거나 어려운 사례에 맞춰진 시뮬레이션 데이터 중 하나에 의존합니다. 두 데이터 소스의 상호 보완적 장점을 효과적으로 통합하는 접근 방식은 거의 없습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션에서 실제 배포로 롱테일 처리 능력을 전이하는 새로운 VLM 기반 종단간 적대적 전이 프레임워크인 CoC-VLA를 제안합니다. 이 프레임워크는 교사 VLM 모델, 학생 VLM 모델, 그리고 판별기로 구성됩니다. 교사 및 학생 VLM 모델은 모두 Chain-of-Causality Visual-Language Model(CoC VLM)이라는 공유 기본 아키텍처를 사용하며, 이는 종단간 텍스트 어댑터를 통해 시간 정보를 통합합니다. 이 아키텍처는 복잡한 운전 논리를 추론하기 위한 사고 사슬(chain-of-thought) 추론을 지원합니다. 교사 및 학생 VLM 모델은 각각 시뮬레이션 및 실제 데이터셋에서 사전 훈련됩니다. 판별기는 새로운 역전파 전략을 사용하여 학생 VLM 모델이 시뮬레이션 환경에서 실제 환경으로 롱테일 처리 능력을 전이하도록 적대적으로 훈련됩니다.
