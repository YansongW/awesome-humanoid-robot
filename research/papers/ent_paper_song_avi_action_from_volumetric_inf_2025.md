---
$id: ent_paper_song_avi_action_from_volumetric_inf_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Avi: Action from Volumetric Inference'
  zh: Avi
  ko: 'Avi: Action from Volumetric Inference'
summary:
  en: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
  zh: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
  ko: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- avi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.21746v1.
sources:
- id: src_001
  type: paper
  title: 'Avi: Action from Volumetric Inference (arXiv)'
  url: https://arxiv.org/abs/2510.21746
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Avi source
  url: https://doi.org/10.48550/arXiv.2510.21746
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## 核心内容
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## 参考
- http://arxiv.org/abs/2510.21746v1

## Overview
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## Content
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## 개요
우리는 Avi를 제안합니다. 이는 로봇 동작 생성을 저수준 정책 학습이 아닌 3D 인식 및 공간 추론 문제로 재정의하는 새로운 3D Vision-Language-Action (VLA) 아키텍처입니다. 기존 VLA 모델은 주로 2D 시각 입력을 기반으로 하며 작업별 동작 정책에 대해 종단간 학습되는 반면, Avi는 3D 포인트 클라우드와 언어 기반 장면 이해를 활용하여 고전적인 기하 변환을 통해 동작을 계산합니다. 가장 주목할 점은, Avi가 이전 동작 토큰을 학습하지 않고, 대신 3D 다중 모달 대규모 언어 모델(MLLM)을 기반으로 다음 포인트 클라우드를 생성하고 고전적 변환을 통해 동작을 명시적으로 계산한다는 것입니다. 이 접근 방식은 폐색, 카메라 포즈 변화, 시점 변경에 강건한 일반화 가능한 행동을 가능하게 합니다. 로봇 의사 결정 과정을 3D 표현에 대한 구조화된 추론 작업으로 처리함으로써, Avi는 불투명한 정책 학습 없이 고수준 언어 명령과 저수준 작동 사이의 간극을 메웁니다. 우리의 예비 결과는 확장 가능하고 강건한 로봇 시스템의 기반으로서 3D 시각-언어 추론의 잠재력을 강조합니다. 자세한 내용은 https://avi-3drobot.github.io/에서 확인하세요.

## 핵심 내용
우리는 Avi를 제안합니다. 이는 로봇 동작 생성을 저수준 정책 학습이 아닌 3D 인식 및 공간 추론 문제로 재정의하는 새로운 3D Vision-Language-Action (VLA) 아키텍처입니다. 기존 VLA 모델은 주로 2D 시각 입력을 기반으로 하며 작업별 동작 정책에 대해 종단간 학습되는 반면, Avi는 3D 포인트 클라우드와 언어 기반 장면 이해를 활용하여 고전적인 기하 변환을 통해 동작을 계산합니다. 가장 주목할 점은, Avi가 이전 동작 토큰을 학습하지 않고, 대신 3D 다중 모달 대규모 언어 모델(MLLM)을 기반으로 다음 포인트 클라우드를 생성하고 고전적 변환을 통해 동작을 명시적으로 계산한다는 것입니다. 이 접근 방식은 폐색, 카메라 포즈 변화, 시점 변경에 강건한 일반화 가능한 행동을 가능하게 합니다. 로봇 의사 결정 과정을 3D 표현에 대한 구조화된 추론 작업으로 처리함으로써, Avi는 불투명한 정책 학습 없이 고수준 언어 명령과 저수준 작동 사이의 간극을 메웁니다. 우리의 예비 결과는 확장 가능하고 강건한 로봇 시스템의 기반으로서 3D 시각-언어 추론의 잠재력을 강조합니다. 자세한 내용은 https://avi-3drobot.github.io/에서 확인하세요.
