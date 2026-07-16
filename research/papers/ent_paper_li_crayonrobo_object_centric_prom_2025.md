---
$id: ent_paper_li_crayonrobo_object_centric_prom_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation'
  zh: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation
  ko: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation'
summary:
  en: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
  zh: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
  ko: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
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
- object_centric_prompt_driven_v
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.02166v1.
sources:
- id: src_001
  type: paper
  title: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2505.02166
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation source
  url: https://doi.org/10.48550/arXiv.2505.02166
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## 核心内容
In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## 参考
- http://arxiv.org/abs/2505.02166v1

## Overview

In robotics, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## Content

In robotics, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## 개요
로봇공학에서 작업 목표는 언어, 목표 이미지, 목표 비디오 등 다양한 양식을 통해 전달될 수 있습니다. 그러나 자연어는 모호할 수 있는 반면, 이미지나 비디오는 지나치게 세부적인 사양을 제공할 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 저수준 동작과 고수준 계획을 간단한 방식으로 명시적으로 전달하는 포괄적인 다중 양식 프롬프트를 활용하는 CrayonRobo를 소개합니다. 구체적으로, 작업 시퀀스의 각 키프레임에 대해, 우리의 방법은 RGB 이미지 위에 오버레이된 간단하고 표현력 있는 2D 시각적 프롬프트를 수동 또는 자동으로 생성할 수 있게 합니다. 이러한 프롬프트는 엔드 이펙터 자세 및 접촉 후 원하는 이동 방향과 같은 필요한 작업 목표를 나타냅니다. 우리는 모델이 이러한 시각-언어 프롬프트를 해석하고 SE(3) 공간에서 해당 접촉 자세와 이동 방향을 예측할 수 있도록 하는 훈련 전략을 개발합니다. 또한, 모든 키프레임 단계를 순차적으로 실행함으로써 모델은 장기 작업을 완료할 수 있습니다. 이 접근 방식은 모델이 작업 목표를 명시적으로 이해하도록 도울 뿐만 아니라, 쉽게 해석 가능한 프롬프트를 제공하여 보지 못한 작업에 대한 견고성을 향상시킵니다. 우리는 시뮬레이션 및 실제 환경 모두에서 방법을 평가하여 강력한 조작 능력을 입증합니다.

## 핵심 내용
로봇공학에서 작업 목표는 언어, 목표 이미지, 목표 비디오 등 다양한 양식을 통해 전달될 수 있습니다. 그러나 자연어는 모호할 수 있는 반면, 이미지나 비디오는 지나치게 세부적인 사양을 제공할 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 저수준 동작과 고수준 계획을 간단한 방식으로 명시적으로 전달하는 포괄적인 다중 양식 프롬프트를 활용하는 CrayonRobo를 소개합니다. 구체적으로, 작업 시퀀스의 각 키프레임에 대해, 우리의 방법은 RGB 이미지 위에 오버레이된 간단하고 표현력 있는 2D 시각적 프롬프트를 수동 또는 자동으로 생성할 수 있게 합니다. 이러한 프롬프트는 엔드 이펙터 자세 및 접촉 후 원하는 이동 방향과 같은 필요한 작업 목표를 나타냅니다. 우리는 모델이 이러한 시각-언어 프롬프트를 해석하고 SE(3) 공간에서 해당 접촉 자세와 이동 방향을 예측할 수 있도록 하는 훈련 전략을 개발합니다. 또한, 모든 키프레임 단계를 순차적으로 실행함으로써 모델은 장기 작업을 완료할 수 있습니다. 이 접근 방식은 모델이 작업 목표를 명시적으로 이해하도록 도울 뿐만 아니라, 쉽게 해석 가능한 프롬프트를 제공하여 보지 못한 작업에 대한 견고성을 향상시킵니다. 우리는 시뮬레이션 및 실제 환경 모두에서 방법을 평가하여 강력한 조작 능력을 입증합니다.
