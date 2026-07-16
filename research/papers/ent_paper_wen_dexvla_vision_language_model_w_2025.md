---
$id: ent_paper_wen_dexvla_vision_language_model_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
  zh: DexVLA
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
summary:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
  zh: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05855v3.
sources:
- id: src_001
  type: paper
  title: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexVLA source
  url: https://doi.org/10.48550/arXiv.2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 核心内容
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 参考
- http://arxiv.org/abs/2502.05855v3

## Overview
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## Content
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 개요
로봇이 다양한 환경에서 여러 작업을 수행할 수 있도록 하는 것은 로봇 학습의 핵심 과제입니다. 시각-언어-행동(VLA) 모델은 일반화 가능한 로봇 기술에 대한 가능성을 보여주었지만, 그 잠재력을 최대한 발휘하려면 행동 표현과 효율적인 훈련의 한계를 해결해야 합니다. 현재 VLA 모델은 종종 시각-언어 모델(VLM) 구성 요소의 확장에 초점을 맞추는 반면, 행동 공간 표현은 여전히 중요한 병목 현상으로 남아 있습니다. 본 논문에서는 다양한 로봇 구현체에서 복잡하고 장기적인 작업을 위한 VLA의 효율성과 일반화 능력을 향상시키도록 설계된 새로운 프레임워크인 DexVLA를 소개합니다. DexVLA는 교차 구현체 학습을 위해 설계된 10억 개의 매개변수로 확장된 새로운 확산 기반 행동 전문가를 특징으로 합니다. 새로운 구현체 커리큘럼 학습 전략은 효율적인 훈련을 용이하게 합니다: (1) VLA와 분리 가능한 확산 전문가를 교차 구현체 데이터로 사전 훈련, (2) VLA 모델을 특정 구현체에 정렬, (3) 새로운 작업에 빠르게 적응하기 위한 사후 훈련. 우리는 단일 암, 양손, 정교한 손을 포함한 여러 구현체에 걸쳐 포괄적인 실험을 수행하여, 작업별 적응 없이도 어려운 작업에 대한 DexVLA의 적응성, 제한된 데이터로 새로운 구현체에서 정교한 기술을 학습하는 능력, 그리고 세탁물 접기와 같은 직접적인 언어 프롬프트만을 사용하여 복잡하고 장기적인 작업을 완료하는 능력을 입증합니다. 모든 설정에서 우리의 방법은 Octo, OpenVLA, Diffusion Policy와 같은 최첨단 모델에 비해 우수한 성능을 보여줍니다.

## 핵심 내용
로봇이 다양한 환경에서 여러 작업을 수행할 수 있도록 하는 것은 로봇 학습의 핵심 과제입니다. 시각-언어-행동(VLA) 모델은 일반화 가능한 로봇 기술에 대한 가능성을 보여주었지만, 그 잠재력을 최대한 발휘하려면 행동 표현과 효율적인 훈련의 한계를 해결해야 합니다. 현재 VLA 모델은 종종 시각-언어 모델(VLM) 구성 요소의 확장에 초점을 맞추는 반면, 행동 공간 표현은 여전히 중요한 병목 현상으로 남아 있습니다. 본 논문에서는 다양한 로봇 구현체에서 복잡하고 장기적인 작업을 위한 VLA의 효율성과 일반화 능력을 향상시키도록 설계된 새로운 프레임워크인 DexVLA를 소개합니다. DexVLA는 교차 구현체 학습을 위해 설계된 10억 개의 매개변수로 확장된 새로운 확산 기반 행동 전문가를 특징으로 합니다. 새로운 구현체 커리큘럼 학습 전략은 효율적인 훈련을 용이하게 합니다: (1) VLA와 분리 가능한 확산 전문가를 교차 구현체 데이터로 사전 훈련, (2) VLA 모델을 특정 구현체에 정렬, (3) 새로운 작업에 빠르게 적응하기 위한 사후 훈련. 우리는 단일 암, 양손, 정교한 손을 포함한 여러 구현체에 걸쳐 포괄적인 실험을 수행하여, 작업별 적응 없이도 어려운 작업에 대한 DexVLA의 적응성, 제한된 데이터로 새로운 구현체에서 정교한 기술을 학습하는 능력, 그리고 세탁물 접기와 같은 직접적인 언어 프롬프트만을 사용하여 복잡하고 장기적인 작업을 완료하는 능력을 입증합니다. 모든 설정에서 우리의 방법은 Octo, OpenVLA, Diffusion Policy와 같은 최첨단 모델에 비해 우수한 성능을 보여줍니다.
