---
$id: ent_paper_zhou_chatvla_2_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge'
  zh: ChatVLA-2
  ko: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge'
summary:
  en: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (ChatVLA-2), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea
    Group, Shanghai University, and published at NIPS25.'
  zh: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (ChatVLA-2), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea
    Group, Shanghai University, and published at NIPS25.'
  ko: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (ChatVLA-2), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea
    Group, Shanghai University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chatvla_2
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.21906v2.
sources:
- id: src_001
  type: paper
  title: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (arXiv)'
  url: https://arxiv.org/abs/2505.21906
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ChatVLA-2 source
  url: https://doi.org/10.48550/arXiv.2505.21906
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

## 核心内容
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

## 参考
- http://arxiv.org/abs/2505.21906v2

## Overview
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

## Content
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

## 개요
Vision-language-action (VLA) 모델은 로봇공학의 차세대 모델로 부상하고 있습니다. 그러나 강력한 사전 훈련된 Vision-Language Models (VLM)을 활용함에도 불구하고, 기존의 엔드투엔드 VLA 시스템은 특정 로봇 작업에 적응하기 위해 미세 조정되는 과정에서 핵심 기능을 종종 상실합니다. 우리는 일반화 가능한 VLA 모델이 VLM의 핵심 역량을 유지하고 확장해야 한다고 주장합니다: 1) 개방형 세계 구현 추론 - VLA는 VLM의 지식을 상속받아, 즉 VLM이 인식할 수 있는 모든 것을 인식하고, 수학 문제를 해결할 수 있으며, 시각-공간 지능을 보유해야 합니다, 2) 추론 따르기 - 개방형 세계 추론을 로봇이 실행 가능한 단계로 효과적으로 변환하는 것입니다. 본 연구에서는 VLM의 원래 강점을 보존하면서 실행 가능한 추론을 가능하게 하는 특화된 2단계 훈련 파이프라인과 결합된 새로운 mixture-of-expert VLA 모델인 ChatVLA-2를 소개합니다. 우리의 접근 방식을 검증하기 위해, 로봇이 화이트보드에 적힌 수학 문제를 해석하고 테이블에서 해당 숫자 카드를 집어 방정식을 푸는 수학 매칭 작업을 설계했습니다. 놀랍게도, 우리의 방법은 이러한 능력이 VLA 내에서 명시적으로 훈련되지 않았음에도 불구하고 뛰어난 수학적 추론 및 OCR 능력을 보여줍니다. 또한, VLA가 강력한 공간 추론 능력을 보유하여 이전에 본 적 없는 물체와 관련된 새로운 방향 지시를 해석할 수 있음을 입증합니다. 전반적으로, 우리의 방법은 OpenVLA, DexVLA, pi-zero와 같은 최첨단 모방 학습 방법을 크게 능가하는 추론 및 이해 능력을 보여줍니다. 이 연구는 강력한 추론 능력을 갖춘 진정으로 일반화 가능한 로봇 기반 모델을 개발하는 데 있어 중요한 진전을 나타냅니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 로봇공학의 차세대 모델로 부상하고 있습니다. 그러나 강력한 사전 훈련된 Vision-Language Models (VLM)을 활용함에도 불구하고, 기존의 엔드투엔드 VLA 시스템은 특정 로봇 작업에 적응하기 위해 미세 조정되는 과정에서 핵심 기능을 종종 상실합니다. 우리는 일반화 가능한 VLA 모델이 VLM의 핵심 역량을 유지하고 확장해야 한다고 주장합니다: 1) 개방형 세계 구현 추론 - VLA는 VLM의 지식을 상속받아, 즉 VLM이 인식할 수 있는 모든 것을 인식하고, 수학 문제를 해결할 수 있으며, 시각-공간 지능을 보유해야 합니다, 2) 추론 따르기 - 개방형 세계 추론을 로봇이 실행 가능한 단계로 효과적으로 변환하는 것입니다. 본 연구에서는 VLM의 원래 강점을 보존하면서 실행 가능한 추론을 가능하게 하는 특화된 2단계 훈련 파이프라인과 결합된 새로운 mixture-of-expert VLA 모델인 ChatVLA-2를 소개합니다. 우리의 접근 방식을 검증하기 위해, 로봇이 화이트보드에 적힌 수학 문제를 해석하고 테이블에서 해당 숫자 카드를 집어 방정식을 푸는 수학 매칭 작업을 설계했습니다. 놀랍게도, 우리의 방법은 이러한 능력이 VLA 내에서 명시적으로 훈련되지 않았음에도 불구하고 뛰어난 수학적 추론 및 OCR 능력을 보여줍니다. 또한, VLA가 강력한 공간 추론 능력을 보유하여 이전에 본 적 없는 물체와 관련된 새로운 방향 지시를 해석할 수 있음을 입증합니다. 전반적으로, 우리의 방법은 OpenVLA, DexVLA, pi-zero와 같은 최첨단 모방 학습 방법을 크게 능가하는 추론 및 이해 능력을 보여줍니다. 이 연구는 강력한 추론 능력을 갖춘 진정으로 일반화 가능한 로봇 기반 모델을 개발하는 데 있어 중요한 진전을 나타냅니다.
