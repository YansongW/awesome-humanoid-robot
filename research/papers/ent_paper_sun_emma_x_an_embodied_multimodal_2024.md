---
$id: ent_paper_sun_emma_x_an_embodied_multimodal_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning'
  zh: Emma-X
  ko: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning'
summary:
  en: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning (Emma-X),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by SUTD, Google DeepMind, and published
    at ACL 2024.'
  zh: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning (Emma-X),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by SUTD, Google DeepMind, and published
    at ACL 2024.'
  ko: 'Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning (Emma-X),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by SUTD, Google DeepMind, and published
    at ACL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emma_x
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11974v2.
sources:
- id: src_001
  type: website
  title: Emma-X source
  url: https://aclanthology.org/2025.acl-long.695/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, Emma-X. Emma-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that Emma-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

## 核心内容
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, Emma-X. Emma-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that Emma-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

## 参考
- http://arxiv.org/abs/2412.11974v2

## Overview
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, Emma-X. Emma-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that Emma-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

## Content
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, Emma-X. Emma-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that Emma-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

## 개요
전통적인 강화 학습 기반 로봇 제어 방법은 종종 특정 작업에 국한되어 다양한 환경이나 보지 못한 물체 및 명령에 일반화되지 못합니다. 시각 언어 모델(VLM)은 강력한 장면 이해 및 계획 능력을 보여주지만, 특정 로봇 체형에 맞춰 실행 가능한 정책을 생성하는 능력은 부족합니다. 이를 해결하기 위해 시각-언어-행동(VLA) 모델이 등장했지만, 장기적인 공간 추론 및 기반 작업 계획에서 어려움을 겪고 있습니다. 본 연구에서는 Grounded Chain of Thought 및 Look-ahead Spatial Reasoning을 갖춘 체화된 다중 모달 행동 모델인 Emma-X를 제안합니다. Emma-X는 BridgeV2를 기반으로 구축된 계층적 체화 데이터셋을 활용하며, 이 데이터셋은 60,000개의 로봇 조작 궤적을 포함하며, 기반 작업 추론 및 공간 안내로 자동 주석 처리되었습니다. 또한, 그리퍼 상태와 운동 궤적에 기반한 궤적 분할 전략을 도입하여 기반 하위 작업 추론 생성에서의 환각을 완화하는 데 도움을 줍니다. 실험 결과, Emma-X는 경쟁 기준선보다 우수한 성능을 보였으며, 특히 공간 추론이 필요한 실제 로봇 작업에서 두드러집니다.

## 핵심 내용
전통적인 강화 학습 기반 로봇 제어 방법은 종종 특정 작업에 국한되어 다양한 환경이나 보지 못한 물체 및 명령에 일반화되지 못합니다. 시각 언어 모델(VLM)은 강력한 장면 이해 및 계획 능력을 보여주지만, 특정 로봇 체형에 맞춰 실행 가능한 정책을 생성하는 능력은 부족합니다. 이를 해결하기 위해 시각-언어-행동(VLA) 모델이 등장했지만, 장기적인 공간 추론 및 기반 작업 계획에서 어려움을 겪고 있습니다. 본 연구에서는 Grounded Chain of Thought 및 Look-ahead Spatial Reasoning을 갖춘 체화된 다중 모달 행동 모델인 Emma-X를 제안합니다. Emma-X는 BridgeV2를 기반으로 구축된 계층적 체화 데이터셋을 활용하며, 이 데이터셋은 60,000개의 로봇 조작 궤적을 포함하며, 기반 작업 추론 및 공간 안내로 자동 주석 처리되었습니다. 또한, 그리퍼 상태와 운동 궤적에 기반한 궤적 분할 전략을 도입하여 기반 하위 작업 추론 생성에서의 환각을 완화하는 데 도움을 줍니다. 실험 결과, Emma-X는 경쟁 기준선보다 우수한 성능을 보였으며, 특히 공간 추론이 필요한 실제 로봇 작업에서 두드러집니다.
