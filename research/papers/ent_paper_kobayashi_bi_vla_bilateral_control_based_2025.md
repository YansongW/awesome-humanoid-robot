---
$id: ent_paper_kobayashi_bi_vla_bilateral_control_based_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation'
  zh: Bi-VLA 2025
  ko: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation'
summary:
  en: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
  zh: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
  ko: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bi_vla_2025
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18865v1.
sources:
- id: src_001
  type: paper
  title: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (arXiv)'
  url: https://arxiv.org/abs/2509.18865
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Bi-VLA 2025 source
  url: https://doi.org/10.48550/arXiv.2509.18865
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## 核心内容
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## 参考
- http://arxiv.org/abs/2509.18865v1

## Overview
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## Content
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## 개요
본 논문에서는 양방향 제어 기반 모방 학습을 확장하여 단일 모델 내에서 여러 작업을 처리할 수 있는 새로운 프레임워크인 Bi-VLA(Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation)를 제안합니다. 기존의 양방향 제어 방법은 정밀한 조작을 위해 관절 각도, 속도, 토크 및 시각 정보를 활용하지만 작업별 모델이 필요하여 일반성이 제한됩니다. Bi-VLA는 SigLIP 및 FiLM 기반 융합을 통해 리더-팔로워 양방향 제어의 로봇 관절 각도, 속도, 토크 데이터를 시각 특징 및 자연어 명령과 함께 활용하여 이러한 한계를 극복합니다. 우리는 보조 언어 단서가 필요한 작업 유형과 시각만으로 구별 가능한 작업 유형, 두 가지에 대해 Bi-VLA를 검증했습니다. 실제 로봇 실험 결과, Bi-VLA가 시각-언어 조합을 성공적으로 해석하고 기존 양방향 제어 기반 모방 학습에 비해 작업 성공률을 향상시키는 것으로 나타났습니다. 본 Bi-VLA는 기존 양방향 접근법의 단일 작업 한계를 해결하며, 시각과 언어의 결합이 다양성을 크게 향상시킨다는 실증적 증거를 제공합니다. 실험 결과는 실제 작업에서 Bi-VLA의 효과성을 입증합니다. 추가 자료는 웹사이트 https://mertcookimg.github.io/bi-vla/ 를 방문해 주십시오.

## 핵심 내용
본 논문에서는 양방향 제어 기반 모방 학습을 확장하여 단일 모델 내에서 여러 작업을 처리할 수 있는 새로운 프레임워크인 Bi-VLA(Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation)를 제안합니다. 기존의 양방향 제어 방법은 정밀한 조작을 위해 관절 각도, 속도, 토크 및 시각 정보를 활용하지만 작업별 모델이 필요하여 일반성이 제한됩니다. Bi-VLA는 SigLIP 및 FiLM 기반 융합을 통해 리더-팔로워 양방향 제어의 로봇 관절 각도, 속도, 토크 데이터를 시각 특징 및 자연어 명령과 함께 활용하여 이러한 한계를 극복합니다. 우리는 보조 언어 단서가 필요한 작업 유형과 시각만으로 구별 가능한 작업 유형, 두 가지에 대해 Bi-VLA를 검증했습니다. 실제 로봇 실험 결과, Bi-VLA가 시각-언어 조합을 성공적으로 해석하고 기존 양방향 제어 기반 모방 학습에 비해 작업 성공률을 향상시키는 것으로 나타났습니다. 본 Bi-VLA는 기존 양방향 접근법의 단일 작업 한계를 해결하며, 시각과 언어의 결합이 다양성을 크게 향상시킨다는 실증적 증거를 제공합니다. 실험 결과는 실제 작업에서 Bi-VLA의 효과성을 입증합니다. 추가 자료는 웹사이트 https://mertcookimg.github.io/bi-vla/ 를 방문해 주십시오.
