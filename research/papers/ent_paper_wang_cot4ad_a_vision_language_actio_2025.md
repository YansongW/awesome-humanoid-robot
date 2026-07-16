---
$id: ent_paper_wang_cot4ad_a_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
  zh: CoT4AD
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
summary:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
  zh: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot4ad
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22532v1.
sources:
- id: src_001
  type: paper
  title: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoT4AD source
  url: https://doi.org/10.48550/arXiv.2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 核心内容
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 参考
- http://arxiv.org/abs/2511.22532v1

## Overview
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## Content
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 개요
Vision-Language-Action (VLA) 모델은 강력한 추론 능력과 풍부한 세계 지식으로 인해 최근 엔드투엔드 자율주행 분야에서 주목받고 있습니다. 그러나 기존 VLA는 종종 제한된 수치 추론 능력과 지나치게 단순화된 입출력 매핑으로 인해 단계적 인과 추론이 필요한 복잡한 주행 시나리오에서 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 우리는 CoT4AD라는 새로운 VLA 프레임워크를 제안합니다. 이는 자율주행을 위한 Chain-of-Thought (CoT) 추론을 도입하여 Vision-Language Models (VLMs)의 수치 및 인과 추론을 모두 향상시킵니다. CoT4AD는 시각적 관찰과 언어 명령을 통합하여 의미 추론, 장면 이해 및 궤적 계획을 수행합니다. 훈련 중에는 인식-질문-예측-행동 CoT를 명시적으로 모델링하여 여러 주행 작업에서 추론 공간과 행동 공간을 정렬합니다. 추론 중에는 암시적 CoT 추론을 수행하여 동적 환경에서 일관된 수치 추론과 강건한 의사 결정을 가능하게 합니다. nuScenes 및 Bench2Drive를 포함한 실제 및 시뮬레이션 벤치마크에서의 광범위한 실험을 통해 CoT4AD가 개방 루프 및 폐쇄 루프 평가 모두에서 최첨단 성능을 달성함을 입증했습니다. 코드는 논문 채택 시 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 강력한 추론 능력과 풍부한 세계 지식으로 인해 최근 엔드투엔드 자율주행 분야에서 주목받고 있습니다. 그러나 기존 VLA는 종종 제한된 수치 추론 능력과 지나치게 단순화된 입출력 매핑으로 인해 단계적 인과 추론이 필요한 복잡한 주행 시나리오에서 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 우리는 CoT4AD라는 새로운 VLA 프레임워크를 제안합니다. 이는 자율주행을 위한 Chain-of-Thought (CoT) 추론을 도입하여 Vision-Language Models (VLMs)의 수치 및 인과 추론을 모두 향상시킵니다. CoT4AD는 시각적 관찰과 언어 명령을 통합하여 의미 추론, 장면 이해 및 궤적 계획을 수행합니다. 훈련 중에는 인식-질문-예측-행동 CoT를 명시적으로 모델링하여 여러 주행 작업에서 추론 공간과 행동 공간을 정렬합니다. 추론 중에는 암시적 CoT 추론을 수행하여 동적 환경에서 일관된 수치 추론과 강건한 의사 결정을 가능하게 합니다. nuScenes 및 Bench2Drive를 포함한 실제 및 시뮬레이션 벤치마크에서의 광범위한 실험을 통해 CoT4AD가 개방 루프 및 폐쇄 루프 평가 모두에서 최첨단 성능을 달성함을 입증했습니다. 코드는 논문 채택 시 공개될 예정입니다.
