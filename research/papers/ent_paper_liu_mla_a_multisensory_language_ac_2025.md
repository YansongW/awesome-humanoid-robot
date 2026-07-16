---
$id: ent_paper_liu_mla_a_multisensory_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
  zh: MLA
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
summary:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
  zh: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
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
- mla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26642v2.
sources:
- id: src_001
  type: paper
  title: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MLA source
  url: https://doi.org/10.48550/arXiv.2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 核心内容
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 参考
- http://arxiv.org/abs/2509.26642v2

## Overview
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## Content
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 개요
Vision-language-action models (VLAs)는 vision-language models (VLMs)로부터 상속받은 일반화 능력과 행동 생성을 학습하여 로봇 조작 작업에서 일반화 능력을 보여주고 있습니다. 대부분의 VLA 모델은 시각과 언어를 해석하여 행동을 생성하는 데 초점을 맞추는 반면, 로봇은 공간적 물리적 세계 내에서 인지하고 상호작용해야 합니다. 이러한 격차는 복잡하고 접촉이 많은 제어를 달성하는 데 필수적인 로봇 특화 다중 감각 정보에 대한 포괄적인 이해의 필요성을 강조합니다. 이를 위해, 우리는 이질적인 감각 양식을 협력적으로 인지하고 미래의 다중 감각 목표를 예측하여 물리적 세계 모델링을 촉진하는 다중 감각 언어-행동(multisensory language-action, MLA) 모델을 소개합니다. 구체적으로, 지각 표현을 향상시키기 위해, 우리는 인코더 없는 다중 모드 정렬 방식을 제안합니다. 이 방식은 대규모 언어 모델 자체를 혁신적으로 지각 모듈로 재활용하여, 2D 이미지, 3D 포인트 클라우드, 촉각 토큰을 위치 대응을 통해 정렬함으로써 다중 모드 신호를 직접 해석합니다. MLA의 물리적 역학에 대한 이해를 더욱 강화하기 위해, 우리는 미래 다중 감각 생성 사후 훈련 전략을 설계하여 MLA가 의미, 기하학, 상호작용 정보를 추론할 수 있게 하고, 행동 생성을 위한 더 강력한 조건을 제공합니다. 평가 결과, MLA 모델은 복잡하고 접촉이 많은 실제 작업에서 이전 최첨단 2D 및 3D VLA 방법보다 각각 12% 및 24% 더 뛰어난 성능을 보였으며, 보이지 않는 구성에 대한 일반화 능력도 향상되었습니다.

## 핵심 내용
Vision-language-action models (VLAs)는 vision-language models (VLMs)로부터 상속받은 일반화 능력과 행동 생성을 학습하여 로봇 조작 작업에서 일반화 능력을 보여주고 있습니다. 대부분의 VLA 모델은 시각과 언어를 해석하여 행동을 생성하는 데 초점을 맞추는 반면, 로봇은 공간적 물리적 세계 내에서 인지하고 상호작용해야 합니다. 이러한 격차는 복잡하고 접촉이 많은 제어를 달성하는 데 필수적인 로봇 특화 다중 감각 정보에 대한 포괄적인 이해의 필요성을 강조합니다. 이를 위해, 우리는 이질적인 감각 양식을 협력적으로 인지하고 미래의 다중 감각 목표를 예측하여 물리적 세계 모델링을 촉진하는 다중 감각 언어-행동(multisensory language-action, MLA) 모델을 소개합니다. 구체적으로, 지각 표현을 향상시키기 위해, 우리는 인코더 없는 다중 모드 정렬 방식을 제안합니다. 이 방식은 대규모 언어 모델 자체를 혁신적으로 지각 모듈로 재활용하여, 2D 이미지, 3D 포인트 클라우드, 촉각 토큰을 위치 대응을 통해 정렬함으로써 다중 모드 신호를 직접 해석합니다. MLA의 물리적 역학에 대한 이해를 더욱 강화하기 위해, 우리는 미래 다중 감각 생성 사후 훈련 전략을 설계하여 MLA가 의미, 기하학, 상호작용 정보를 추론할 수 있게 하고, 행동 생성을 위한 더 강력한 조건을 제공합니다. 평가 결과, MLA 모델은 복잡하고 접촉이 많은 실제 작업에서 이전 최첨단 2D 및 3D VLA 방법보다 각각 12% 및 24% 더 뛰어난 성능을 보였으며, 보이지 않는 구성에 대한 일반화 능력도 향상되었습니다.
