---
$id: ent_paper_hirose_omnivla_an_omni_modal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
  zh: OmniVLA
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
summary:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
  zh: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
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
- omnivla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19480v1.
sources:
- id: src_001
  type: paper
  title: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (arXiv)'
  url: https://arxiv.org/abs/2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniVLA source
  url: https://doi.org/10.48550/arXiv.2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 核心内容
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 参考
- http://arxiv.org/abs/2509.19480v1

## Overview
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## Content
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 개요
인간은 목적지로 이동할 때 언어 명령, 공간 좌표, 시각적 참조 등 다양한 목표 사양을 유연하게 해석하고 구성할 수 있습니다. 반면, 대부분의 기존 로봇 내비게이션 정책은 단일 모달리티로 훈련되어, 다양한 형태의 목표 사양이 자연스럽고 상호 보완적인 실제 환경에서의 적응성이 제한됩니다. 본 연구에서는 시각 기반 내비게이션을 위한 전모달 목표 조건화를 가능하게 하는 로봇 기초 모델 훈련 프레임워크를 제시합니다. 우리의 접근 방식은 고용량 비전-언어-행동(VLA) 백본을 활용하며, 무작위 모달리티 융합 전략을 통해 2D 포즈, 자기중심 이미지, 자연어의 세 가지 주요 목표 모달리티와 이들의 조합으로 훈련합니다. 이 설계는 사용 가능한 데이터셋 풀을 확장할 뿐만 아니라, 정책이 더 풍부한 기하학적, 의미론적, 시각적 표현을 개발하도록 장려합니다. 결과 모델인 OmniVLA는 보지 못한 환경에 대한 강력한 일반화, 희소 모달리티에 대한 견고성, 새로운 자연어 명령을 따르는 능력을 달성합니다. 우리는 OmniVLA가 모달리티 전반에서 전문가 기준선을 능가하며, 새로운 모달리티와 작업에 미세 조정할 수 있는 유연한 기반을 제공함을 입증합니다. OmniVLA가 광범위하게 일반화 가능하고 유연한 내비게이션 정책을 위한 한 걸음이며, 전모달 로봇 기초 모델 구축을 위한 확장 가능한 경로를 제공한다고 믿습니다. OmniVLA 성능을 보여주는 비디오를 제시하며, 프로젝트 페이지에서 체크포인트와 훈련 코드를 공개할 예정입니다.

## 핵심 내용
인간은 목적지로 이동할 때 언어 명령, 공간 좌표, 시각적 참조 등 다양한 목표 사양을 유연하게 해석하고 구성할 수 있습니다. 반면, 대부분의 기존 로봇 내비게이션 정책은 단일 모달리티로 훈련되어, 다양한 형태의 목표 사양이 자연스럽고 상호 보완적인 실제 환경에서의 적응성이 제한됩니다. 본 연구에서는 시각 기반 내비게이션을 위한 전모달 목표 조건화를 가능하게 하는 로봇 기초 모델 훈련 프레임워크를 제시합니다. 우리의 접근 방식은 고용량 비전-언어-행동(VLA) 백본을 활용하며, 무작위 모달리티 융합 전략을 통해 2D 포즈, 자기중심 이미지, 자연어의 세 가지 주요 목표 모달리티와 이들의 조합으로 훈련합니다. 이 설계는 사용 가능한 데이터셋 풀을 확장할 뿐만 아니라, 정책이 더 풍부한 기하학적, 의미론적, 시각적 표현을 개발하도록 장려합니다. 결과 모델인 OmniVLA는 보지 못한 환경에 대한 강력한 일반화, 희소 모달리티에 대한 견고성, 새로운 자연어 명령을 따르는 능력을 달성합니다. 우리는 OmniVLA가 모달리티 전반에서 전문가 기준선을 능가하며, 새로운 모달리티와 작업에 미세 조정할 수 있는 유연한 기반을 제공함을 입증합니다. OmniVLA가 광범위하게 일반화 가능하고 유연한 내비게이션 정책을 위한 한 걸음이며, 전모달 로봇 기초 모델 구축을 위한 확장 가능한 경로를 제공한다고 믿습니다. OmniVLA 성능을 보여주는 비디오를 제시하며, 프로젝트 페이지에서 체크포인트와 훈련 코드를 공개할 예정입니다.
