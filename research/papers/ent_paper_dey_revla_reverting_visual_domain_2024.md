---
$id: ent_paper_dey_revla_reverting_visual_domain_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models'
  zh: ReVLA
  ko: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models'
summary:
  en: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models (ReVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, and published at ICRA 2024.'
  zh: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models (ReVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, and published at ICRA 2024.'
  ko: 'ReVLA: Reverting Visual Domain Limitation of Robotic Foundation Models (ReVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, and published at ICRA 2024.'
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
- revla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15250v3.
sources:
- id: src_001
  type: website
  title: ReVLA source
  url: https://doi.org/10.1109/ICRA55743.2025.11128823
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A large step for the community are open Vision Language Action models which showcase strong performance in a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models, and propose a corresponding evaluation framework. Our study shows that the existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is, therefore, expected to generalize to out-of-domain experiments. However, we showcase catastrophic forgetting by DINO-v2 in OpenVLA through its failure to fulfill the task of depth regression. To overcome the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach founded on model merging. This enables OpenVLA -- which requires the adaptation of the visual backbones during initial training -- to regain its visual generalization ability. Regaining this capability enables our ReVLA model to improve over OpenVLA by a factor of 77\% and 66\% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts and model weights are available on the ReVLA Page

## 核心内容
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A large step for the community are open Vision Language Action models which showcase strong performance in a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models, and propose a corresponding evaluation framework. Our study shows that the existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is, therefore, expected to generalize to out-of-domain experiments. However, we showcase catastrophic forgetting by DINO-v2 in OpenVLA through its failure to fulfill the task of depth regression. To overcome the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach founded on model merging. This enables OpenVLA -- which requires the adaptation of the visual backbones during initial training -- to regain its visual generalization ability. Regaining this capability enables our ReVLA model to improve over OpenVLA by a factor of 77\% and 66\% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts and model weights are available on the ReVLA Page

## 参考
- http://arxiv.org/abs/2409.15250v3

## Overview
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models, transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A major step for the community is the emergence of open Vision-Language-Action models, which demonstrate strong performance across a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models and propose a corresponding evaluation framework. Our study shows that these existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is therefore expected to generalize to out-of-domain experiments. However, we demonstrate catastrophic forgetting by DINO-v2 in OpenVLA through its failure to perform depth regression. To address the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach based on model merging. This enables OpenVLA—which requires adaptation of the visual backbones during initial training—to regain its visual generalization ability. Regaining this capability allows our ReVLA model to improve over OpenVLA by 77% and 66% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts, and model weights are available on the ReVLA Page.

## Content
Recent progress in large language models and access to large-scale robotic datasets has sparked a paradigm shift in robotics models, transforming them into generalists able to adapt to various tasks, scenes, and robot modalities. A major step for the community is the emergence of open Vision-Language-Action models, which demonstrate strong performance across a wide variety of tasks. In this work, we study the visual generalization capabilities of three existing robotic foundation models and propose a corresponding evaluation framework. Our study shows that these existing models do not exhibit robustness to visual out-of-domain scenarios. This is potentially caused by limited variations in the training data and/or catastrophic forgetting, leading to domain limitations in the vision foundation models. We further explore OpenVLA, which uses two pre-trained vision foundation models and is therefore expected to generalize to out-of-domain experiments. However, we demonstrate catastrophic forgetting by DINO-v2 in OpenVLA through its failure to perform depth regression. To address the aforementioned issue of visual catastrophic forgetting, we propose a gradual backbone reversal approach based on model merging. This enables OpenVLA—which requires adaptation of the visual backbones during initial training—to regain its visual generalization ability. Regaining this capability allows our ReVLA model to improve over OpenVLA by 77% and 66% for grasping and lifting in visual OOD tasks. Comprehensive evaluations, episode rollouts, and model weights are available on the ReVLA Page.

## 개요
최근 대규모 언어 모델의 발전과 대규모 로봇 데이터셋에 대한 접근성은 로봇 모델을 다양한 작업, 장면 및 로봇 모달리티에 적응할 수 있는 제너럴리스트로 전환하는 패러다임 변화를 촉발했습니다. 커뮤니티의 큰 진전은 다양한 작업에서 강력한 성능을 보여주는 오픈 Vision Language Action 모델입니다. 본 연구에서는 기존의 세 가지 로봇 기반 모델의 시각적 일반화 능력을 조사하고, 이에 상응하는 평가 프레임워크를 제안합니다. 우리의 연구는 기존 모델이 시각적 도메인 외부(out-of-domain) 시나리오에 대한 견고성을 나타내지 않음을 보여줍니다. 이는 잠재적으로 훈련 데이터의 제한된 다양성 및/또는 치명적 망각(catastrophic forgetting)으로 인해 발생하며, 이는 시각 기반 모델의 도메인 한계로 이어집니다. 우리는 또한 OpenVLA를 추가로 탐구합니다. OpenVLA는 두 개의 사전 훈련된 시각 기반 모델을 사용하므로 도메인 외부 실험에 일반화될 것으로 예상됩니다. 그러나 우리는 OpenVLA에서 DINO-v2가 깊이 회귀(depth regression) 작업을 수행하지 못함으로써 치명적 망각을 보여줍니다. 위에서 언급한 시각적 치명적 망각 문제를 극복하기 위해, 우리는 모델 병합(model merging)에 기반한 점진적 백본 역전(gradual backbone reversal) 접근 방식을 제안합니다. 이를 통해 초기 훈련 중 시각적 백본의 적응이 필요한 OpenVLA가 시각적 일반화 능력을 회복할 수 있습니다. 이 능력을 회복함으로써 우리의 ReVLA 모델은 시각적 OOD 작업에서 그리핑(grasping) 및 리프팅(lifting)에 대해 OpenVLA 대비 각각 77% 및 66% 향상됩니다. 포괄적인 평가, 에피소드 롤아웃 및 모델 가중치는 ReVLA 페이지에서 확인할 수 있습니다.

## 핵심 내용
최근 대규모 언어 모델의 발전과 대규모 로봇 데이터셋에 대한 접근성은 로봇 모델을 다양한 작업, 장면 및 로봇 모달리티에 적응할 수 있는 제너럴리스트로 전환하는 패러다임 변화를 촉발했습니다. 커뮤니티의 큰 진전은 다양한 작업에서 강력한 성능을 보여주는 오픈 Vision Language Action 모델입니다. 본 연구에서는 기존의 세 가지 로봇 기반 모델의 시각적 일반화 능력을 조사하고, 이에 상응하는 평가 프레임워크를 제안합니다. 우리의 연구는 기존 모델이 시각적 도메인 외부 시나리오에 대한 견고성을 나타내지 않음을 보여줍니다. 이는 잠재적으로 훈련 데이터의 제한된 다양성 및/또는 치명적 망각으로 인해 발생하며, 이는 시각 기반 모델의 도메인 한계로 이어집니다. 우리는 또한 OpenVLA를 추가로 탐구합니다. OpenVLA는 두 개의 사전 훈련된 시각 기반 모델을 사용하므로 도메인 외부 실험에 일반화될 것으로 예상됩니다. 그러나 우리는 OpenVLA에서 DINO-v2가 깊이 회귀 작업을 수행하지 못함으로써 치명적 망각을 보여줍니다. 위에서 언급한 시각적 치명적 망각 문제를 극복하기 위해, 우리는 모델 병합에 기반한 점진적 백본 역전 접근 방식을 제안합니다. 이를 통해 초기 훈련 중 시각적 백본의 적응이 필요한 OpenVLA가 시각적 일반화 능력을 회복할 수 있습니다. 이 능력을 회복함으로써 우리의 ReVLA 모델은 시각적 OOD 작업에서 그리핑 및 리프팅에 대해 OpenVLA 대비 각각 77% 및 66% 향상됩니다. 포괄적인 평가, 에피소드 롤아웃 및 모델 가중치는 ReVLA 페이지에서 확인할 수 있습니다.
