---
$id: ent_paper_choi_embodied_cot_distillation_from_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  zh: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents
summary:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
  zh: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_cot_distillation_from
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11499v1.
sources:
- id: src_001
  type: paper
  title: Embodied CoT Distillation From LLM To Off-the-shelf Agents source
  url: https://openreview.net/forum?id=M4Htd52HMH
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 核心内容
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 参考
- http://arxiv.org/abs/2412.11499v1

## Overview
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## Content
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 개요
본 연구는 대규모 언어 모델(LLM)을 활용하여 복잡한 구현형 과제를 해결하는 문제를 다룹니다. 특히 의사 결정 시스템이 용량이 제한된 기성 기기에서 실시간으로 작동해야 하는 환경을 대상으로 합니다. 우리는 LLM의 구현형 추론 능력을 분해하고 증류하여 효율적인 소형 언어 모델(sLM) 기반 정책으로 전환하는 프레임워크인 DeDer를 제안합니다. DeDer에서 LLM 기반 전략의 의사 결정 과정은 추론 정책과 계획 정책으로 구성된 계층 구조로 재구성됩니다. 추론 정책은 LLM의 구현형 맥락 학습과 자체 검증을 통해 생성된 데이터로부터 증류되어 효과적인 근거를 생성할 수 있습니다. 계획 정책은 이러한 근거에 따라 최적화된 계획을 효율적으로 수립합니다. 결과적으로 DeDer는 두 정책 모두에 sLM을 채택하여 기성 기기에 배포할 수 있게 합니다. 또한 구현형 과제에 특화된 중간 근거의 품질을 향상시키기 위해 구현형 지식 그래프를 설계하고, 단일 추론을 통해 여러 근거를 신속하게 생성하기 위해 대조적 프롬프트 주의 모델을 사용합니다. ALFRED 벤치마크 실험 결과, DeDer는 최신 언어 계획 및 증류 접근법을 능가하며, DeDer를 통해 도출된 sLM 기반 구현형 정책의 적용 가능성과 효율성을 입증합니다.

## 핵심 내용
본 연구는 대규모 언어 모델(LLM)을 활용하여 복잡한 구현형 과제를 해결하는 문제를 다룹니다. 특히 의사 결정 시스템이 용량이 제한된 기성 기기에서 실시간으로 작동해야 하는 환경을 대상으로 합니다. 우리는 LLM의 구현형 추론 능력을 분해하고 증류하여 효율적인 소형 언어 모델(sLM) 기반 정책으로 전환하는 프레임워크인 DeDer를 제안합니다. DeDer에서 LLM 기반 전략의 의사 결정 과정은 추론 정책과 계획 정책으로 구성된 계층 구조로 재구성됩니다. 추론 정책은 LLM의 구현형 맥락 학습과 자체 검증을 통해 생성된 데이터로부터 증류되어 효과적인 근거를 생성할 수 있습니다. 계획 정책은 이러한 근거에 따라 최적화된 계획을 효율적으로 수립합니다. 결과적으로 DeDer는 두 정책 모두에 sLM을 채택하여 기성 기기에 배포할 수 있게 합니다. 또한 구현형 과제에 특화된 중간 근거의 품질을 향상시키기 위해 구현형 지식 그래프를 설계하고, 단일 추론을 통해 여러 근거를 신속하게 생성하기 위해 대조적 프롬프트 주의 모델을 사용합니다. ALFRED 벤치마크 실험 결과, DeDer는 최신 언어 계획 및 증류 접근법을 능가하며, DeDer를 통해 도출된 sLM 기반 구현형 정책의 적용 가능성과 효율성을 입증합니다.
