---
$id: ent_paper_liu_volumetric_environment_represe_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Volumetric Environment Representation for Vision-Language Navigation
  zh: VER
  ko: Volumetric Environment Representation for Vision-Language Navigation
summary:
  en: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
  zh: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
  ko: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- ver
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.14158v1.
sources:
- id: src_001
  type: website
  title: VER source
  url: https://doi.org/10.1109/CVPR52733.2024.01544
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## 核心内容
Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## 参考
- http://arxiv.org/abs/2403.14158v1

## Overview
Vision-language navigation (VLN) requires an agent to navigate through a 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle to capture 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## Content
Vision-language navigation (VLN) requires an agent to navigate through a 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle to capture 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## 개요
Vision-language navigation (VLN)은 에이전트가 시각적 관찰과 자연어 명령을 기반으로 3D 환경을 탐색해야 하는 과제입니다. 성공적인 탐색의 핵심 요소는 포괄적인 장면 이해에 있음이 분명합니다. 기존 VLN 에이전트는 단안 프레임워크를 사용하여 원근 뷰의 2D 특징을 직접 추출합니다. 직관적이지만, 3D 기하학과 의미론을 포착하는 데 어려움을 겪어 부분적이고 불완전한 환경 표현을 초래합니다. 세부 정보를 포함한 포괄적인 3D 표현을 달성하기 위해, 우리는 물리적 세계를 구조화된 3D 셀로 복셀화하는 Volumetric Environment Representation (VER)을 도입합니다. 각 셀에 대해 VER은 2D-3D 샘플링을 통해 다중 뷰 2D 특징을 통합된 3D 공간으로 집계합니다. VER에 대한 coarse-to-fine 특징 추출 및 멀티태스크 학습을 통해, 우리의 에이전트는 3D 점유, 3D 방 레이아웃, 3D 바운딩 박스를 공동으로 예측합니다. 온라인으로 수집된 VER을 기반으로, 에이전트는 볼륨 상태 추정을 수행하고 다음 단계를 예측하기 위한 일화 기억을 구축합니다. 실험 결과, 멀티태스크 학습을 통한 환경 표현이 VLN에서 뚜렷한 성능 향상을 가져옴을 보여줍니다. 우리 모델은 VLN 벤치마크(R2R, REVERIE, R4R)에서 최첨단 성능을 달성합니다.

## 핵심 내용
Vision-language navigation (VLN)은 에이전트가 시각적 관찰과 자연어 명령을 기반으로 3D 환경을 탐색해야 하는 과제입니다. 성공적인 탐색의 핵심 요소는 포괄적인 장면 이해에 있음이 분명합니다. 기존 VLN 에이전트는 단안 프레임워크를 사용하여 원근 뷰의 2D 특징을 직접 추출합니다. 직관적이지만, 3D 기하학과 의미론을 포착하는 데 어려움을 겪어 부분적이고 불완전한 환경 표현을 초래합니다. 세부 정보를 포함한 포괄적인 3D 표현을 달성하기 위해, 우리는 물리적 세계를 구조화된 3D 셀로 복셀화하는 Volumetric Environment Representation (VER)을 도입합니다. 각 셀에 대해 VER은 2D-3D 샘플링을 통해 다중 뷰 2D 특징을 통합된 3D 공간으로 집계합니다. VER에 대한 coarse-to-fine 특징 추출 및 멀티태스크 학습을 통해, 우리의 에이전트는 3D 점유, 3D 방 레이아웃, 3D 바운딩 박스를 공동으로 예측합니다. 온라인으로 수집된 VER을 기반으로, 에이전트는 볼륨 상태 추정을 수행하고 다음 단계를 예측하기 위한 일화 기억을 구축합니다. 실험 결과, 멀티태스크 학습을 통한 환경 표현이 VLN에서 뚜렷한 성능 향상을 가져옴을 보여줍니다. 우리 모델은 VLN 벤치마크(R2R, REVERIE, R4R)에서 최첨단 성능을 달성합니다.
