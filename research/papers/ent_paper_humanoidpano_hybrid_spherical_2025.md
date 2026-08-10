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
  zh: HumanoidPano 是2025年提出的一种面向人形机器人的混合球形全景-LiDAR跨模态感知框架。该工作由相关研究团队完成，核心贡献在于通过球形视觉Transformer实现全景视觉与LiDAR深度测量的几何感知对齐，并在360BEV-Matterport基准上取得最优性能。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09010v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (631 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2503.09010
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人因自身结构限制存在严重自遮挡和视野受限问题。HumanoidPano通过球形几何感知约束（SGC）、空间可变形注意力（SDA）和全景增强（AUG）三大模块，实现了360°全景图像与LiDAR点云的高效融合。该方法在360BEV-Matterport基准测试中达到领先水平，并在真实人形机器人平台上验证了其生成精确BEV分割图的能力，可直接支持复杂环境中的导航任务。

## 核心内容
### 方法架构
HumanoidPano 框架包含三个核心模块：
- **球形几何感知约束（SGC）**：利用全景相机射线特性引导畸变正则化采样偏移，实现几何对齐。
- **空间可变形注意力（SDA）**：通过球形偏移聚合层次化3D特征，实现高效的360°到BEV融合，生成几何完整的物体表征。
- **全景增强（AUG）**：结合跨视角变换与语义对齐，在数据增强过程中提升BEV-全景特征一致性。

### 实验设置
- **基准测试**：在360BEV-Matterport数据集上进行评估。
- **部署平台**：真实人形机器人平台。

### 关键结果
- 在360BEV-Matterport基准上达到最先进性能（state-of-the-art）。
- 真实部署验证了系统能够通过全景-LiDAR协同感知生成精确的BEV分割图。

### 结论
HumanoidPano 为人形机器人的具身感知建立了新范式，直接支持复杂环境中的下游导航任务。

## Overview
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360 visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## Overview
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360° visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## Content
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360° visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 参考
- http://arxiv.org/abs/2503.09010v2

## 개요
휴머노이드 로봇은 구조적 한계로 인해 심각한 자가 폐색 및 시야 제한 문제를 겪는다. HumanoidPano는 구형 기하학 인식 제약(SGC), 공간 변형 가능 어텐션(SDA), 파노라마 증강(AUG)의 세 가지 모듈을 통해 360° 파노라마 이미지와 LiDAR 포인트 클라우드의 효율적인 융합을 구현한다. 이 방법은 360BEV-Matterport 벤치마크에서 최고 수준에 도달했으며, 실제 휴머노이드 로봇 플랫폼에서 정밀한 BEV 분할 맵 생성 능력을 검증하여 복잡한 환경에서의 내비게이션 작업을 직접 지원할 수 있다.

## 핵심 내용
### 방법 아키텍처
HumanoidPano 프레임워크는 세 가지 핵심 모듈로 구성된다:
- **구형 기하학 인식 제약(SGC)**: 파노라마 카메라의 광선 특성을 활용하여 왜곡 정규화 샘플링 오프셋을 유도하고 기하학적 정렬을 구현한다.
- **공간 변형 가능 어텐션(SDA)**: 구형 오프셋을 통해 계층적 3D 특징을 집계하여 효율적인 360°에서 BEV로의 융합을 구현하고, 기하학적으로 완전한 객체 표현을 생성한다.
- **파노라마 증강(AUG)**: 교차 시점 변환과 의미 정렬을 결합하여 데이터 증강 과정에서 BEV-파노라마 특징 일관성을 향상시킨다.

### 실험 설정
- **벤치마크 테스트**: 360BEV-Matterport 데이터셋에서 평가를 수행한다.
- **배포 플랫폼**: 실제 휴머노이드 로봇 플랫폼.

### 주요 결과
- 360BEV-Matterport 벤치마크에서 최첨단 성능(state-of-the-art)을 달성했다.
- 실제 배포를 통해 시스템이 파노라마-LiDAR 협동 인식을 통해 정밀한 BEV 분할 맵을 생성할 수 있음을 검증했다.

### 결론
HumanoidPano는 휴머노이드 로봇의 체화 인식에 새로운 패러다임을 확립하며, 복잡한 환경에서의 하위 내비게이션 작업을 직접 지원한다.
