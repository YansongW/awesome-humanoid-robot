---
$id: ent_paper_mitra_mechanistic_finetuning_of_visi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
  zh: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
  ko: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
summary:
  en: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
  zh: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
  ko: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
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
- mechanistic_finetuning_of_visi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22697v1.
sources:
- id: src_001
  type: paper
  title: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (arXiv)
  url: https://arxiv.org/abs/2511.22697
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations source
  url: https://doi.org/10.48550/arXiv.2511.22697
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Action (VLAs) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## 核心内容
Vision-Language Action (VLAs) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## 参考
- http://arxiv.org/abs/2511.22697v1

## Overview
Vision-Language Action (VLA) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## Content
Vision-Language Action (VLA) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## 개요
Vision-Language Action (VLA) 모델은 비전-언어 모델(VLM)의 놀라운 성공을 로보틱스로 확장할 것을 약속합니다. 그러나 비전-언어 영역의 VLM과 달리, 로보틱스를 위한 VLA는 로봇의 구현, 환경 특성, 각 작업의 공간적 관계와 같은 다양한 물리적 요소에 대응하기 위해 미세 조정이 필요합니다. 기존의 미세 조정 방법은 작업의 시각적, 언어적, 물리적 특성과 관계없이 동일한 파라미터 세트를 적용하여 특수성이 부족합니다. 신경과학의 기능적 특수성에서 영감을 받아, 우리는 주어진 작업에 특화된 희소 모델 표현을 미세 조정하는 것이 더 효과적이라고 가정합니다. 본 연구에서는 메커니즘 해석 가능성에 기반한 미세 조정 접근법인 Robotic Steering을 소개합니다. 이는 소수의 시연을 활용하여 로봇 작업의 물리적, 시각적, 언어적 요구 사항에 부합하는 작업별 주의 헤드를 식별하고 선택적으로 미세 조정합니다. Franka Emika 로봇 팔을 사용한 포괄적인 온-로봇 평가를 통해, Robotic Steering이 LoRA보다 우수한 성능을 보이며, 작업 변동 하에서 뛰어난 강건성, 낮은 계산 비용, 그리고 다양한 로봇 작업에 VLA를 적용하기 위한 향상된 해석 가능성을 달성함을 입증합니다.

## 핵심 내용
Vision-Language Action (VLA) 모델은 비전-언어 모델(VLM)의 놀라운 성공을 로보틱스로 확장할 것을 약속합니다. 그러나 비전-언어 영역의 VLM과 달리, 로보틱스를 위한 VLA는 로봇의 구현, 환경 특성, 각 작업의 공간적 관계와 같은 다양한 물리적 요소에 대응하기 위해 미세 조정이 필요합니다. 기존의 미세 조정 방법은 작업의 시각적, 언어적, 물리적 특성과 관계없이 동일한 파라미터 세트를 적용하여 특수성이 부족합니다. 신경과학의 기능적 특수성에서 영감을 받아, 우리는 주어진 작업에 특화된 희소 모델 표현을 미세 조정하는 것이 더 효과적이라고 가정합니다. 본 연구에서는 메커니즘 해석 가능성에 기반한 미세 조정 접근법인 Robotic Steering을 소개합니다. 이는 소수의 시연을 활용하여 로봇 작업의 물리적, 시각적, 언어적 요구 사항에 부합하는 작업별 주의 헤드를 식별하고 선택적으로 미세 조정합니다. Franka Emika 로봇 팔을 사용한 포괄적인 온-로봇 평가를 통해, Robotic Steering이 LoRA보다 우수한 성능을 보이며, 작업 변동 하에서 뛰어난 강건성, 낮은 계산 비용, 그리고 다양한 로봇 작업에 VLA를 적용하기 위한 향상된 해석 가능성을 달성함을 입증합니다.
