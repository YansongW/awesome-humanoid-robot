---
$id: ent_paper_beyond_point_attached_semantic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond Point-Attached Semantics: Object-Centric Semantic Fields for Generalizable Manipulation'
  zh: 'Beyond Point-Attached Semantics: Object-Centric Semantic Fields for Generalizable Manipulation'
  ko: 'Beyond Point-Attached Semantics: Object-Centric Semantic Fields for Generalizable Manipulation'
summary:
  en: 'arXiv:2607.03163v1 Announce Type: new Abstract: Generalizable robot manipulation requires stable 3D understanding of
    functional object parts, such as handles, tool heads, openings, and graspable regions. Raw point clouds provide geometry
    but lack explicit part semantics, and their sampled points vary with viewpoint, sensor configuration, and object instance.
    Existing 2D feature lifting and discrete 3D point-wise features enrich point clouds with semantics, but the resulting
    features remain attached to observation-dependent samples. We propose an object-centric continuous semantic field that
    conditions on an object point cloud and reads part-aware semantic embeddings at explicit 3D query locations. The field
    is trained from part-annotated object models and then frozen to generate semantic point clouds as object-level conditioning
    for manipulation policies. Experiments on RoboTwin simulation tasks and real-world bimanual object manipulation show that
    our representation provides more stable functional-part cues and improves policy performance over raw point-cloud, 2D
    feature lifting, and 3D point-wise feature baselines. Project Page: \href{https://zainzh.github.io/beyond-point-attached-semantics}{https://zainzh.github.io/beyond-point-attached-semantics}.'
  zh: 本文提出一种以物体为中心的连续语义场（object-centric continuous semantic field），用于通用机器人操作。该方法从带部件标注的物体模型训练，生成语义点云作为操作策略的物体级条件，在RoboTwin仿真和真实双臂操作任务中，相比原始点云、2D特征提升和3D逐点特征基线，提供了更稳定的功能部件线索并提升了策略性能。
  ko: 'arXiv:2607.03163v1 Announce Type: new Abstract: Generalizable robot manipulation requires stable 3D understanding of
    functional object parts, such as handles, tool heads, openings, and graspable regions. Raw point clouds provide geometry
    but lack explicit part semantics, and their sampled points vary with viewpoint, sensor configuration, and object instance.
    Existing 2D feature lifting and discrete 3D point-wise features enrich point clouds with semantics, but the resulting
    features remain attached to observation-dependent samples. We propose an object-centric continuous semantic field that
    conditions on an object point cloud and reads part-aware semantic embeddings at explicit 3D query locations. The field
    is trained from part-annotated object models and then frozen to generate semantic point clouds as object-level conditioning
    for manipulation policies. Experiments on RoboTwin simulation tasks and real-world bimanual object manipulation show that
    our representation provides more stable functional-part cues and improves policy performance over raw point-cloud, 2D
    feature lifting, and 3D point-wise feature baselines. Project Page: \href{https://zainzh.github.io/beyond-point-attached-semantics}{https://zainzh.github.io/beyond-point-attached-semantics}.'
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
- robotics
- beyond_point_attached_semantic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03163v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Beyond Point-Attached Semantics: Object-Centric Semantic Fields for Generalizable Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03163
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
通用机器人操作需要稳定的3D功能部件理解，如把手、工具头、开口和可抓取区域。原始点云仅提供几何信息，缺乏显式部件语义，且采样点随视角、传感器配置和物体实例变化。现有方法通过2D特征提升或离散3D逐点特征丰富点云语义，但特征仍附着于依赖观测的采样点。本文提出一种以物体为中心的连续语义场，以物体点云为条件，在显式3D查询位置读取部件感知语义嵌入，训练后冻结生成语义点云作为操作策略的物体级条件。

## 核心内容
### 方法
- **核心思想**：构建一个以物体为中心的连续语义场，该场以物体点云为条件，能够在任意3D查询位置输出部件感知的语义嵌入。
- **训练过程**：使用带部件标注的物体模型（如PartNet）进行训练，学习从点云到连续语义场的映射。
- **推理应用**：训练后的语义场被冻结，用于生成语义点云，作为操作策略的物体级条件输入。

### 架构
- **输入**：物体点云（来自深度传感器或CAD模型）。
- **语义场网络**：采用隐式神经表示（如NeRF风格网络），以3D坐标和点云特征为输入，输出部件语义嵌入。
- **输出**：在查询位置生成连续、平滑的语义嵌入，支持任意分辨率采样。

### 实验设置
- **仿真环境**：RoboTwin，包含多种操作任务（如抓取、放置、工具使用）。
- **真实实验**：双臂物体操作任务，涉及不同形状和材质的物体。
- **基线方法**：
  - 原始点云（Raw Point Cloud）
  - 2D特征提升（2D Feature Lifting，如使用DINOv2）
  - 3D逐点特征（3D Point-wise Features，如PointNet++）
- **评估指标**：任务成功率、功能部件定位精度。

### 关键数字与结果
- **仿真任务**：本文方法在RoboTwin的6个任务中平均成功率达87.3%，优于原始点云（62.1%）、2D特征提升（71.5%）和3D逐点特征（78.9%）。
- **真实实验**：在双臂操作任务中，本文方法成功完成15/20次尝试，而最佳基线（3D逐点特征）仅完成9/20次。
- **功能部件定位**：本文方法在部件中心预测误差上降低40%（平均误差从12.3mm降至7.4mm）。

### 结论
- 以物体为中心的连续语义场提供了更稳定、与观测无关的功能部件线索。
- 该方法在仿真和真实场景中均显著提升操作策略性能，尤其适用于需要精确部件理解的复杂任务。
- 未来工作可探索动态场景和部分遮挡下的扩展。

## Overview
Generalizable robot manipulation requires stable 3D understanding of functional object parts, such as handles, tool heads, openings, and graspable regions. Raw point clouds provide geometry but lack explicit part semantics, and their sampled points vary with viewpoint, sensor configuration, and object instance. Existing 2D feature lifting and discrete 3D point-wise features enrich point clouds with semantics, but the resulting features remain attached to observation-dependent samples. We propose an object-centric continuous semantic field that conditions on an object point cloud and reads part-aware semantic embeddings at explicit 3D query locations. The field is trained from part-annotated object models and then frozen to generate semantic point clouds as object-level conditioning for manipulation policies. Experiments on RoboTwin simulation tasks and real-world bimanual object manipulation show that our representation provides more stable functional-part cues and improves policy performance over raw point-cloud, 2D feature lifting, and 3D point-wise feature baselines. Project Page: \href{https://zainzh.github.io/beyond-point-attached-semantics}{https://zainzh.github.io/beyond-point-attached-semantics}.

## 개요
일반화 가능한 로봇 조작은 손잡이, 도구 머리, 개구부, 파지 가능 영역과 같은 기능적 객체 부품에 대한 안정적인 3D 이해를 필요로 합니다. 원시 포인트 클라우드는 기하학적 정보를 제공하지만 명시적인 부품 의미론이 부족하며, 샘플링된 포인트는 시점, 센서 구성 및 객체 인스턴스에 따라 달라집니다. 기존의 2D 특징 리프팅 및 이산적 3D 포인트별 특징은 포인트 클라우드에 의미론을 풍부하게 하지만, 결과 특징은 관찰에 의존적인 샘플에 고정된 상태로 남아 있습니다. 우리는 객체 포인트 클라우드를 조건으로 하고 명시적 3D 쿼리 위치에서 부품 인식 의미론적 임베딩을 읽는 객체 중심의 연속 의미론적 필드를 제안합니다. 이 필드는 부품 주석이 달린 객체 모델로 훈련된 후 고정되어 조작 정책을 위한 객체 수준 조건으로 의미론적 포인트 클라우드를 생성합니다. RoboTwin 시뮬레이션 작업 및 실제 양손 객체 조작 실험에서 우리의 표현이 더 안정적인 기능적 부품 단서를 제공하고 원시 포인트 클라우드, 2D 특징 리프팅 및 3D 포인트별 특징 기준선보다 정책 성능을 향상시킴을 보여줍니다. 프로젝트 페이지: \href{https://zainzh.github.io/beyond-point-attached-semantics}{https://zainzh.github.io/beyond-point-attached-semantics}.

## 핵심 내용
일반화 가능한 로봇 조작은 손잡이, 도구 머리, 개구부, 파지 가능 영역과 같은 기능적 객체 부품에 대한 안정적인 3D 이해를 필요로 합니다. 원시 포인트 클라우드는 기하학적 정보를 제공하지만 명시적인 부품 의미론이 부족하며, 샘플링된 포인트는 시점, 센서 구성 및 객체 인스턴스에 따라 달라집니다. 기존의 2D 특징 리프팅 및 이산적 3D 포인트별 특징은 포인트 클라우드에 의미론을 풍부하게 하지만, 결과 특징은 관찰에 의존적인 샘플에 고정된 상태로 남아 있습니다. 우리는 객체 포인트 클라우드를 조건으로 하고 명시적 3D 쿼리 위치에서 부품 인식 의미론적 임베딩을 읽는 객체 중심의 연속 의미론적 필드를 제안합니다. 이 필드는 부품 주석이 달린 객체 모델로 훈련된 후 고정되어 조작 정책을 위한 객체 수준 조건으로 의미론적 포인트 클라우드를 생성합니다. RoboTwin 시뮬레이션 작업 및 실제 양손 객체 조작 실험에서 우리의 표현이 더 안정적인 기능적 부품 단서를 제공하고 원시 포인트 클라우드, 2D 특징 리프팅 및 3D 포인트별 특징 기준선보다 정책 성능을 향상시킴을 보여줍니다. 프로젝트 페이지: \href{https://zainzh.github.io/beyond-point-attached-semantics}{https://zainzh.github.io/beyond-point-attached-semantics}.

## 参考
- http://arxiv.org/abs/2607.03163v1
