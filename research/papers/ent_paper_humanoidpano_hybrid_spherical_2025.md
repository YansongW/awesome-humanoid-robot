---
$id: ent_paper_humanoidpano_hybrid_spherical_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
  zh: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
  ko: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
summary:
  en: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
  zh: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
  ko: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoidpano
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09010v2.
sources:
- id: src_001
  type: paper
  title: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2503.09010
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360 visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 核心内容
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360 visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 参考
- http://arxiv.org/abs/2503.09010v2

## Overview
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360° visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## Content
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360° visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 개요
휴머노이드 로봇을 위한 지각 시스템 설계는 심각한 자기 폐색과 제한된 시야(FOV)를 유발하는 고유한 구조적 제약으로 인해 독특한 과제를 제기합니다. 본 논문에서는 이러한 한계를 극복하기 위해 파노라마 비전과 LiDAR 센싱을 시너지적으로 통합하는 새로운 하이브리드 교차 모달 지각 프레임워크인 HumanoidPano를 제시합니다. 단일 카메라나 표준 다중 센서 구성을 사용하는 기존 로봇 지각 시스템과 달리, 우리의 방법은 구형 비전 트랜스포머를 통해 기하학적 인식 모달리티 정렬을 확립하여 360도 시각적 맥락과 LiDAR의 정밀한 깊이 측정을 원활하게 융합합니다. 첫째, 구형 기하학 인식 제약(SGC)은 파노라마 카메라 광선 속성을 활용하여 왜곡 정규화 샘플링 오프셋을 유도하여 기하학적 정렬을 수행합니다. 둘째, 공간 변형 가능 어텐션(SDA)은 구형 오프셋을 통해 계층적 3D 특징을 집계하여 기하학적으로 완전한 객체 표현으로 효율적인 360°-to-BEV 융합을 가능하게 합니다. 셋째, 파노라마 증강(AUG)은 교차 뷰 변환과 의미적 정렬을 결합하여 데이터 증강 중 BEV-파노라마 특징 일관성을 향상시킵니다. 광범위한 평가를 통해 360BEV-Matterport 벤치마크에서 최첨단 성능을 입증했습니다. 휴머노이드 플랫폼에서의 실제 배치는 파노라마-LiDAR 공동 지각을 통해 정확한 BEV 분할 맵을 생성하는 시스템의 능력을 검증하여 복잡한 환경에서의 하위 탐색 작업을 직접 지원합니다. 우리의 연구는 휴머노이드 로봇 공학에서 구현된 지각을 위한 새로운 패러다임을 확립합니다.

## 핵심 내용
휴머노이드 로봇을 위한 지각 시스템 설계는 심각한 자기 폐색과 제한된 시야(FOV)를 유발하는 고유한 구조적 제약으로 인해 독특한 과제를 제기합니다. 본 논문에서는 이러한 한계를 극복하기 위해 파노라마 비전과 LiDAR 센싱을 시너지적으로 통합하는 새로운 하이브리드 교차 모달 지각 프레임워크인 HumanoidPano를 제시합니다. 단일 카메라나 표준 다중 센서 구성을 사용하는 기존 로봇 지각 시스템과 달리, 우리의 방법은 구형 비전 트랜스포머를 통해 기하학적 인식 모달리티 정렬을 확립하여 360도 시각적 맥락과 LiDAR의 정밀한 깊이 측정을 원활하게 융합합니다. 첫째, 구형 기하학 인식 제약(SGC)은 파노라마 카메라 광선 속성을 활용하여 왜곡 정규화 샘플링 오프셋을 유도하여 기하학적 정렬을 수행합니다. 둘째, 공간 변형 가능 어텐션(SDA)은 구형 오프셋을 통해 계층적 3D 특징을 집계하여 기하학적으로 완전한 객체 표현으로 효율적인 360°-to-BEV 융합을 가능하게 합니다. 셋째, 파노라마 증강(AUG)은 교차 뷰 변환과 의미적 정렬을 결합하여 데이터 증강 중 BEV-파노라마 특징 일관성을 향상시킵니다. 광범위한 평가를 통해 360BEV-Matterport 벤치마크에서 최첨단 성능을 입증했습니다. 휴머노이드 플랫폼에서의 실제 배치는 파노라마-LiDAR 공동 지각을 통해 정확한 BEV 분할 맵을 생성하는 시스템의 능력을 검증하여 복잡한 환경에서의 하위 탐색 작업을 직접 지원합니다. 우리의 연구는 휴머노이드 로봇 공학에서 구현된 지각을 위한 새로운 패러다임을 확립합니다.
