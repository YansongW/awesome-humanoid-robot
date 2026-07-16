---
$id: ent_paper_maskedmimic_unified_physics_ba_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
  zh: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
  ko: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
summary:
  en: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
  zh: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
  ko: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- maskedmimic
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.14393v1.
sources:
- id: src_001
  type: paper
  title: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (arXiv)'
  url: https://arxiv.org/abs/2409.14393
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting project page'
  url: https://research.nvidia.com/labs/par/maskedmimic/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## 核心内容
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## 参考
- http://arxiv.org/abs/2409.14393v1

## Overview
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## Content
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## 개요
광범위한 시나리오에서 대화형 캐릭터에 생명을 불어넣을 수 있는 단일하고 다재다능한 물리 기반 제어기를 만드는 것은 캐릭터 애니메이션의 흥미로운 최전선을 대표합니다. 이상적인 제어기는 희소 목표 키프레임, 텍스트 명령, 장면 정보와 같은 다양한 제어 방식을 지원해야 합니다. 이전 연구에서 물리적으로 시뮬레이션된 장면 인식 제어 모델이 제안되었지만, 이러한 시스템은 주로 좁은 범위의 작업과 제어 방식에 특화된 제어기를 개발하는 데 초점을 맞추었습니다. 본 연구는 물리 기반 캐릭터 제어를 일반적인 모션 인페인팅 문제로 정식화하는 새로운 접근 방식인 MaskedMimic을 제시합니다. 우리의 핵심 통찰은 마스킹된 키프레임, 객체, 텍스트 설명 또는 이들의 조합과 같은 부분적(마스킹된) 모션 설명으로부터 모션을 합성하는 단일 통합 모델을 훈련하는 것입니다. 이는 모션 추적 데이터를 활용하고 다양한 모션 설명을 효과적으로 활용하여 일관된 애니메이션을 생성할 수 있는 확장 가능한 훈련 방법을 설계함으로써 달성됩니다. 이 과정을 통해 우리의 접근 방식은 관심 있는 모든 행동에 대해 지루한 보상 엔지니어링 없이 직관적인 제어 인터페이스를 제공하는 물리 기반 제어기를 학습합니다. 결과적으로 생성된 제어기는 광범위한 제어 방식을 지원하고 서로 다른 작업 간의 원활한 전환을 가능하게 합니다. 모션 인페인팅을 통해 캐릭터 제어를 통합함으로써 MaskedMimic은 다재다능한 가상 캐릭터를 만듭니다. 이러한 캐릭터는 복잡한 장면에 동적으로 적응하고 필요에 따라 다양한 모션을 구성하여 더욱 상호작용적이고 몰입감 있는 경험을 가능하게 합니다.

## 핵심 내용
광범위한 시나리오에서 대화형 캐릭터에 생명을 불어넣을 수 있는 단일하고 다재다능한 물리 기반 제어기를 만드는 것은 캐릭터 애니메이션의 흥미로운 최전선을 대표합니다. 이상적인 제어기는 희소 목표 키프레임, 텍스트 명령, 장면 정보와 같은 다양한 제어 방식을 지원해야 합니다. 이전 연구에서 물리적으로 시뮬레이션된 장면 인식 제어 모델이 제안되었지만, 이러한 시스템은 주로 좁은 범위의 작업과 제어 방식에 특화된 제어기를 개발하는 데 초점을 맞추었습니다. 본 연구는 물리 기반 캐릭터 제어를 일반적인 모션 인페인팅 문제로 정식화하는 새로운 접근 방식인 MaskedMimic을 제시합니다. 우리의 핵심 통찰은 마스킹된 키프레임, 객체, 텍스트 설명 또는 이들의 조합과 같은 부분적(마스킹된) 모션 설명으로부터 모션을 합성하는 단일 통합 모델을 훈련하는 것입니다. 이는 모션 추적 데이터를 활용하고 다양한 모션 설명을 효과적으로 활용하여 일관된 애니메이션을 생성할 수 있는 확장 가능한 훈련 방법을 설계함으로써 달성됩니다. 이 과정을 통해 우리의 접근 방식은 관심 있는 모든 행동에 대해 지루한 보상 엔지니어링 없이 직관적인 제어 인터페이스를 제공하는 물리 기반 제어기를 학습합니다. 결과적으로 생성된 제어기는 광범위한 제어 방식을 지원하고 서로 다른 작업 간의 원활한 전환을 가능하게 합니다. 모션 인페인팅을 통해 캐릭터 제어를 통합함으로써 MaskedMimic은 다재다능한 가상 캐릭터를 만듭니다. 이러한 캐릭터는 복잡한 장면에 동적으로 적응하고 필요에 따라 다양한 모션을 구성하여 더욱 상호작용적이고 몰입감 있는 경험을 가능하게 합니다.
