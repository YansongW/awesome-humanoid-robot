---
$id: ent_paper_liu_vla_pruner_temporal_aware_dual_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
  zh: VLA-Pruner
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
summary:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
  zh: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_pruner
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16449v5.
sources:
- id: src_001
  type: paper
  title: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (arXiv)'
  url: https://arxiv.org/abs/2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Pruner source
  url: https://doi.org/10.48550/arXiv.2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 核心内容
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 参考
- http://arxiv.org/abs/2511.16449v5

## Overview
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## Content
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 개요
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 행동 실행을 통합하여 임베디드 AI에서 큰 잠재력을 보여주고 있습니다. 실시간 배포에서 이러한 모델은 연속적인 시각적 스트림을 처리해야 하므로 상당한 계산 오버헤드가 발생합니다. 시각적 토큰 가지치기(Visual token pruning)는 중요 토큰을 유지하고 중복 토큰을 제거하여 Vision-Language Models (VLM)를 가속화하는 주류 기술로, 이 문제에 대한 자연스러운 해결책을 제공합니다. 그러나 VLM 중심의 가지치기 방법을 VLA 추론에 직접 적용하면 조작 성능이 심각하게 저하될 수 있습니다. 우리의 분석은 이러한 저하가 핵심 불일치에 기인한다고 설명합니다: VLA 추론은 비전-언어 프리필(prefill) 단계와 행동 디코드(action-decode) 단계에서 서로 다른 주의 패턴을 보이므로, 컨텍스트 프리필의 의미적 중요도(semantic salience)만을 기반으로 가지치기를 하면 의미적 단서에 편향되어 행동에 중요한 시각적 토큰이 제거될 수 있습니다. 이러한 관찰에 동기 부여되어, 우리는 VLA 추론의 시각적 요구 사항에 기반한 효과적인 플러그 앤 플레이 토큰 가지치기 방법인 VLA-Pruner를 제안하며, 로봇 조작의 시간적 연속성을 추가로 활용합니다. 구체적으로, VLA-Pruner는 의미적 프리필링과 시간적으로 평활화된 행동 관련성(temporally smoothed action relevance) 모두에서 시각적 토큰 중요도를 추정한 다음, Combine-then-Filter 전략을 적용하여 계산 예산 내에서 간결하고 중복되지 않는 토큰을 유지합니다. 실험 결과, VLA-Pruner는 여러 VLA 아키텍처에서 최첨단 접근 방식을 능가하며, 비슷한 조작 품질로 최대 1.99배의 속도 향상을 달성합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 행동 실행을 통합하여 임베디드 AI에서 큰 잠재력을 보여주고 있습니다. 실시간 배포에서 이러한 모델은 연속적인 시각적 스트림을 처리해야 하므로 상당한 계산 오버헤드가 발생합니다. 시각적 토큰 가지치기(Visual token pruning)는 중요 토큰을 유지하고 중복 토큰을 제거하여 Vision-Language Models (VLM)를 가속화하는 주류 기술로, 이 문제에 대한 자연스러운 해결책을 제공합니다. 그러나 VLM 중심의 가지치기 방법을 VLA 추론에 직접 적용하면 조작 성능이 심각하게 저하될 수 있습니다. 우리의 분석은 이러한 저하가 핵심 불일치에 기인한다고 설명합니다: VLA 추론은 비전-언어 프리필(prefill) 단계와 행동 디코드(action-decode) 단계에서 서로 다른 주의 패턴을 보이므로, 컨텍스트 프리필의 의미적 중요도(semantic salience)만을 기반으로 가지치기를 하면 의미적 단서에 편향되어 행동에 중요한 시각적 토큰이 제거될 수 있습니다. 이러한 관찰에 동기 부여되어, 우리는 VLA 추론의 시각적 요구 사항에 기반한 효과적인 플러그 앤 플레이 토큰 가지치기 방법인 VLA-Pruner를 제안하며, 로봇 조작의 시간적 연속성을 추가로 활용합니다. 구체적으로, VLA-Pruner는 의미적 프리필링과 시간적으로 평활화된 행동 관련성(temporally smoothed action relevance) 모두에서 시각적 토큰 중요도를 추정한 다음, Combine-then-Filter 전략을 적용하여 계산 예산 내에서 간결하고 중복되지 않는 토큰을 유지합니다. 실험 결과, VLA-Pruner는 여러 VLA 아키텍처에서 최첨단 접근 방식을 능가하며, 비슷한 조작 품질로 최대 1.99배의 속도 향상을 달성합니다.
