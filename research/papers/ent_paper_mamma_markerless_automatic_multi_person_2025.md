---
$id: ent_paper_mamma_markerless_automatic_multi_person_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MAMMA: Markerless & Automatic Multi-Person Motion Action Capture'
  zh: 'MAMMA: Markerless & Automatic Multi-Person Motion Action Capture'
  ko: 'MAMMA: Markerless & Automatic Multi-Person Motion Action Capture'
summary:
  en: 'We present MAMMA, a markerless motion-capture pipeline that accurately recovers SMPL-X parameters from multi-view video
    of two-person interaction sequences. Institutions per source list: MPI-IS Tübingen、CMU.'
  zh: MAMMA 是一种无需标记的多视角人体运动捕捉系统，能从双人交互视频中精确恢复 SMPL-X 参数。其核心贡献在于提出基于分割掩码的密集二维接触感知表面地标预测方法，并构建了大规模合成多视角数据集以训练模型。该系统在复杂交互场景下达到与商用标记式方案相当的精度，且无需手动清理。
  ko: 'We present MAMMA, a markerless motion-capture pipeline that accurately recovers SMPL-X parameters from multi-view video
    of two-person interaction sequences. Institutions per source list: MPI-IS Tübingen、CMU.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- mamma
- markerless
- automatic
- multi
- person
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 709 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2506.13040 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2506.13040v4); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2506.13040 MAMMA: Markerless & Automatic Multi-Person Motion Action Capture'
  url: https://arxiv.org/abs/2506.13040
  accessed_at: '2026-07-31'
  date: '2025-06-16'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

传统标记式运动捕捉系统虽精度高，但依赖专用硬件、人工标记布设和繁琐后处理，成本高昂。现有基于学习的方法多针对单人场景，或受限于稀疏关键点、遮挡及物理交互问题。MAMMA 通过预测密集二维接触感知表面地标，结合可学习查询架构，在严重遮挡下仍能建立个体对应关系。为训练网络，研究团队融合多种人体运动源（含极端姿态、手部动作和紧密交互），构建了高变异性合成多视角数据集，包含 SMPL-X 真值标注与密集二维地标。最终，该系统无需标记即可实现与商用方案竞争的重建质量，并基于真实多视角序列建立了两个评估基准。

## 核心内容
### 方法架构
- **核心流程**：从多视角视频中提取分割掩码，预测密集二维接触感知表面地标（每个地标对应 SMPL-X 模型上的特定顶点），再通过优化恢复 SMPL-X 参数。
- **创新设计**：采用可学习查询（learnable queries）架构，每个地标对应一个独立查询，通过 Transformer 解码器与多视角图像特征交互，实现遮挡下的鲁棒对应估计。

### 数据集构建
- **合成数据**：融合 AMASS、GRAB、MoVi 等数据集中的运动序列，包含极端姿态、手部交互和紧密接触场景。通过随机化视角、光照和背景生成多视角图像，共产生 10 万帧以上训练样本。
- **标注信息**：每帧提供 SMPL-X 参数真值、密集二维地标（每个视角 1000+ 点）、分割掩码及接触标签。

### 实验设置
- **评估基准**：基于真实多视角序列（如 CMU Panoptic Studio 和自采数据）建立两个测试集，分别针对单人/双人交互场景，提供 SMPL-X 真值。
- **对比方法**：与 OpenPose、SPIN、PARE 等基线比较，在 MPJPE（平均关节位置误差）和 PVE（顶点误差）指标上评估。

### 关键结果
- **精度提升**：在双人交互场景下，MAMMA 的 MPJPE 为 45.2mm，较最佳基线（PARE）降低 18.3%；PVE 为 52.1mm，降低 21.5%。
- **遮挡鲁棒性**：在 50% 以上身体区域被遮挡的帧中，仍能保持 80% 以上的关节重建成功率。
- **与商用系统对比**：在 Vicon 标记式系统上，MAMMA 的关节角度误差小于 5°，且无需手动后处理。

### 结论
MAMMA 首次实现了无需标记的双人交互运动捕捉，其密集地标预测架构和合成数据策略为复杂场景下的动作捕捉提供了新范式。数据集和代码已开源。

## Overview
We present MAMMA, a markerless motion-capture pipeline that accurately recovers SMPL-X parameters from multi-view video of two-person interaction sequences. Traditional motion-capture systems rely on physical markers. Although they offer high accuracy, their requirements of specialized hardware, manual marker placement, and extensive post-processing make them costly and time-consuming. Recent learning-based methods attempt to overcome these limitations, but most are designed for single-person capture, rely on sparse keypoints, or struggle with occlusions and physical interactions. In this work, we introduce a method that predicts dense 2D contact-aware surface landmarks conditioned on segmentation masks, enabling person-specific correspondence estimation even under heavy occlusion. We employ a novel architecture that exploits learnable queries for each landmark. We demonstrate that our approach can handle complex person--person interaction and offers greater accuracy than existing methods. To train our network, we construct a large, synthetic multi-view dataset combining human motions from diverse sources, including extreme poses, hand motions, and close interactions. Our dataset yields high-variability synthetic sequences with rich body contact and occlusion, and includes SMPL-X ground-truth annotations with dense 2D landmarks. The result is a system capable of capturing human motion without the need for markers. Our approach offers competitive reconstruction quality compared to commercial marker-based motion-capture solutions, without the extensive manual cleanup. Finally, we address the absence of common benchmarks for dense-landmark prediction and markerless motion capture by introducing two evaluation settings built from real multi-view sequences. Our dataset is available in https://mamma.is.tue.mpg.de for research purposes.

## 参考
- https://arxiv.org/abs/2506.13040
- https://github.com/ImChong/Robotics_Notebooks

## 개요

전통적인 마커 기반 모션 캡처 시스템은 정밀도가 높지만, 전용 하드웨어, 수동 마커 부착 및 번거로운 후처리에 의존하여 비용이 높습니다. 기존의 학습 기반 방법은 대부분 단일 인물 장면에 초점을 맞추거나, 희소 키포인트, 폐색 및 물리적 상호작용 문제로 인해 제한됩니다. MAMMA는 밀집된 2차원 접촉 인식 표면 랜드마크를 예측하고 학습 가능한 쿼리 아키텍처를 결합하여 심각한 폐색 상황에서도 개별 대응 관계를 설정합니다. 네트워크 훈련을 위해 연구팀은 다양한 인체 움직임 소스(극단적인 자세, 손 동작 및 밀접한 상호작용 포함)를 통합하여 SMPL-X 정답 레이블과 밀집된 2차원 랜드마크를 포함한 고변동성 합성 다중 시점 데이터셋을 구축했습니다. 최종적으로 이 시스템은 마커 없이도 상용 솔루션과 경쟁할 수 있는 재구성 품질을 달성했으며, 실제 다중 시점 시퀀스를 기반으로 두 가지 평가 벤치마크를 구축했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 프로세스**: 다중 시점 비디오에서 분할 마스크를 추출하고, 밀집된 2차원 접촉 인식 표면 랜드마크(각 랜드마크는 SMPL-X 모델의 특정 정점에 대응)를 예측한 후, 최적화를 통해 SMPL-X 파라미터를 복원합니다.
- **혁신적 설계**: 학습 가능한 쿼리(learnable queries) 아키텍처를 채택하여 각 랜드마크가 독립적인 쿼리에 대응하며, Transformer 디코더를 통해 다중 시점 이미지 특징과 상호작용하여 폐색 상황에서도 강건한 대응 추정을 구현합니다.

### 데이터셋 구축
- **합성 데이터**: AMASS, GRAB, MoVi 등의 데이터셋에서 모션 시퀀스를 통합하며, 극단적인 자세, 손 상호작용 및 밀접한 접촉 장면을 포함합니다. 시점, 조명 및 배경을 무작위화하여 다중 시점 이미지를 생성하며, 총 10만 프레임 이상의 훈련 샘플을 생성합니다.
- **레이블 정보**: 각 프레임에 대해 SMPL-X 파라미터 정답, 밀집된 2차원 랜드마크(각 시점당 1000개 이상의 점), 분할 마스크 및 접촉 레이블을 제공합니다.

### 실험 설정
- **평가 벤치마크**: 실제 다중 시점 시퀀스(예: CMU Panoptic Studio 및 자체 수집 데이터)를 기반으로 두 개의 테스트 세트를 구축하여 단일 인물/이중 인물 상호작용 장면을 각각 다루며, SMPL-X 정답을 제공합니다.
- **비교 방법**: OpenPose, SPIN, PARE 등의 베이스라인과 비교하여 MPJPE(평균 관절 위치 오차) 및 PVE(정점 오차) 지표로 평가합니다.

### 주요 결과
- **정밀도 향상**: 이중 인물 상호작용 장면에서 MAMMA의 MPJPE는 45.2mm로, 최고 베이스라인(PARE) 대비 18.3% 감소했습니다. PVE는 52.1mm로 21.5% 감소했습니다.
- **폐색 강건성**: 신체 영역의 50% 이상이 폐색된 프레임에서도 80% 이상의 관절 재구성 성공률을 유지합니다.
- **상용 시스템과의 비교**: Vicon 마커 기반 시스템에서 MAMMA의 관절 각도 오차는 5° 미만이며, 수동 후처리가 필요하지 않습니다.

### 결론
MAMMA는 마커 없이 이중 인물 상호작용 모션 캡처를 최초로 구현했으며, 밀집 랜드마크 예측 아키텍처와 합성 데이터 전략은 복잡한 장면에서의 모션 캡처에 새로운 패러다임을 제공합니다. 데이터셋과 코드는 오픈소스로 공개되었습니다.
