---
$id: ent_paper_huang_tactile_vla_unlocking_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization'
  zh: Tactile-VLA
  ko: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization'
summary:
  en: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
  zh: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
  ko: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
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
- tactile_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.09160v1.
sources:
- id: src_001
  type: paper
  title: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (arXiv)'
  url: https://arxiv.org/abs/2507.09160
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Tactile-VLA source
  url: https://doi.org/10.48550/arXiv.2507.09160
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## 参考
- http://arxiv.org/abs/2507.09160v1

## Overview
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with the real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## Content
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with the real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## 개요
Vision-Language-Action (VLA) 모델은 시각-언어 구성 요소의 풍부한 암묵적 지식을 바탕으로 놀라운 성과를 보여주고 있습니다. 그러나 범용 로봇 에이전트를 구현하려면 특히 세밀한 힘 제어가 필수적인 접촉이 많은 시나리오에서 물리적 상호작용에 대한 정밀한 근거가 필요합니다. 우리는 VLA의 암묵적 지식을 '무엇을 해야 하는지' 식별하는 것을 넘어 '실제 세계와 물리적으로 상호작용하는 방법'을 안내하는 방향으로 발전시킵니다. 본 논문은 시각, 언어, 행동 및 촉각 감지를 깊이 융합하는 새로운 프레임워크인 Tactile-VLA를 소개합니다. 이 프레임워크는 모델의 의도를 정밀한 물리적 행동으로 변환하는 하이브리드 위치-힘 제어기와 로봇이 촉각 피드백에 기반하여 전략을 조정할 수 있게 하는 추론 모듈을 통합합니다. 실험은 Tactile-VLA의 효과성과 일반화 가능성을 세 가지 주요 측면에서 입증합니다: (1) 촉각 인식 명령 수행 가능, (2) 촉각 관련 상식 활용, (3) 적응형 촉각 관련 추론 촉진. 핵심 발견은 VLM의 사전 지식이 이미 물리적 상호작용에 대한 의미론적 이해를 포함하고 있으며, 이를 소수의 시연만으로 로봇의 촉각 센서에 연결하면 이 사전 지식을 활성화하여 접촉이 많은 작업에서 제로샷 일반화를 달성할 수 있다는 점입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각-언어 구성 요소의 풍부한 암묵적 지식을 바탕으로 놀라운 성과를 보여주고 있습니다. 그러나 범용 로봇 에이전트를 구현하려면 특히 세밀한 힘 제어가 필수적인 접촉이 많은 시나리오에서 물리적 상호작용에 대한 정밀한 근거가 필요합니다. 우리는 VLA의 암묵적 지식을 '무엇을 해야 하는지' 식별하는 것을 넘어 '실제 세계와 물리적으로 상호작용하는 방법'을 안내하는 방향으로 발전시킵니다. 본 논문은 시각, 언어, 행동 및 촉각 감지를 깊이 융합하는 새로운 프레임워크인 Tactile-VLA를 소개합니다. 이 프레임워크는 모델의 의도를 정밀한 물리적 행동으로 변환하는 하이브리드 위치-힘 제어기와 로봇이 촉각 피드백에 기반하여 전략을 조정할 수 있게 하는 추론 모듈을 통합합니다. 실험은 Tactile-VLA의 효과성과 일반화 가능성을 세 가지 주요 측면에서 입증합니다: (1) 촉각 인식 명령 수행 가능, (2) 촉각 관련 상식 활용, (3) 적응형 촉각 관련 추론 촉진. 핵심 발견은 VLM의 사전 지식이 이미 물리적 상호작용에 대한 의미론적 이해를 포함하고 있으며, 이를 소수의 시연만으로 로봇의 촉각 센서에 연결하면 이 사전 지식을 활성화하여 접촉이 많은 작업에서 제로샷 일반화를 달성할 수 있다는 점입니다.
