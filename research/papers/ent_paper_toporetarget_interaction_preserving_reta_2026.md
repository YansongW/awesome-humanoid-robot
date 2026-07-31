---
$id: ent_paper_toporetarget_interaction_preserving_reta_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation'
  zh: 'TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation'
  ko: 'TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation'
summary:
  en: 'Human hand-object demonstrations provide dense reference motions for training dexterous manipulation reinforcement
    learning (RL) policies through reference tracking. Institutions per source list: IIIS、Tsinghua University.'
  zh: TopoRetarget 是由研究团队提出的交互保持重定向框架，用于将人类手部演示转化为灵巧机器人手的参考运动。其核心贡献在于通过稀疏交互图和拉普拉斯变形优化，在保持手-物体接触结构的同时，实现跨不同重定向条件的单参数集适配。
  ko: 'Human hand-object demonstrations provide dense reference motions for training dexterous manipulation reinforcement
    learning (RL) policies through reference tracking. Institutions per source list: IIIS、Tsinghua University.'
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
- toporetarget
- interaction
- preserving
- reta
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 803 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.16272v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.16272 TopoRetarget: Interaction-Preserving Retargeting for Dexterous Manipulation'
  url: https://arxiv.org/abs/2606.16272
  accessed_at: '2026-07-31'
  date: '2026-06-15'
- id: src_002
  type: website
  title: Project page
  url: https://toporetarget2026.github.io/TopoRetarget/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

TopoRetarget 针对灵巧操作中的重定向问题，提出了一种保持交互的框架。该方法通过构建手和物体关键点之间的稀疏交互图，并优化距离加权拉普拉斯变形，同时考虑方向一致性、运动学约束和穿透处理，从而在重定向过程中保留任务相关的手-物体接触结构。实验表明，该方法在 ContactPose 数据集上实现了最佳的接触精度和对齐效果，将 Pen-Spin 训练成功率提升 40.6 个百分点，并实现了到 Wuji Hand 硬件的零样本迁移。

## 核心内容
### 方法架构
TopoRetarget 的核心是一个保持交互的重定向框架，其关键组件包括：
- **稀疏交互图构建**：在手和物体的关键点之间构建稀疏图，用于捕捉任务相关的接触结构。
- **距离加权拉普拉斯变形**：通过优化距离加权的拉普拉斯变形，保持手-物体交互的几何一致性。
- **方向一致性约束**：确保重定向后的手部姿态与原始演示的方向一致。
- **运动学约束**：考虑灵巧机器人手的运动学限制，避免不可行的姿态。
- **穿透处理**：检测并修正手与物体之间的穿透问题，确保物理合理性。

### 实验设置
- **数据集**：使用 ContactPose 数据集进行评估，该数据集包含多种手-物体交互场景。
- **基线方法**：与现有重定向方法进行对比，包括基于几何和基于学习的方法。
- **评估指标**：包括接触精度、对齐误差以及下游 RL 策略的成功率。

### 关键结果
- **接触精度**：TopoRetarget 在 ContactPose 数据集上实现了最佳的接触精度和对齐效果，优于所有基线方法。
- **Pen-Spin 训练**：在笔旋转任务中，TopoRetarget 将训练成功率提升 40.6 个百分点，从基线方法的较低水平显著提高。
- **零样本迁移**：在立方体重定向和笔旋转任务中，TopoRetarget 实现了到 Wuji Hand 硬件的零样本迁移，无需额外微调。

### 结论
TopoRetarget 通过保持手-物体交互结构，显著提升了灵巧操作中参考运动的质量，从而改善了下游 RL 策略的学习效果。该方法在多个任务和硬件平台上展示了其通用性和有效性。

## Overview
Human hand-object demonstrations provide dense reference motions for training dexterous manipulation reinforcement learning (RL) policies through reference tracking. However, to use such demonstrations for RL policy learning, retargeting must preserve hand pose and task-relevant hand-object contact structure. Otherwise, contact and feasibility artifacts can degrade downstream RL policy performance. We introduce TopoRetarget, an interaction-preserving retargeting framework that uses a single set of parameters across diverse retargeting conditions while maintaining task-relevant hand-object interaction and adapting human demonstrations to dexterous robot hands. The method constructs a sparse interaction graph over hand and object keypoints and optimizes distance-weighted Laplacian deformation with directional consistency, kinematic constraints, and penetration handling. Evaluations show that the generated references improve both interaction fidelity and policy learning: TopoRetarget achieves the best contact precision and alignment over all baselines on the ContactPose Dataset, improves Pen-Spin training success by 40.6 percentage points over the existing baseline methods, and enables zero-shot transfer to Wuji Hand hardware on cube reorientation and pen spinning.

## 参考
- https://arxiv.org/abs/2606.16272
- https://toporetarget2026.github.io/TopoRetarget/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

TopoRetarget은 정교한 조작에서의 리타게팅 문제를 해결하기 위해 상호작용을 유지하는 프레임워크를 제안한다. 이 방법은 손과 물체의 키포인트 간 희소 상호작용 그래프를 구축하고, 거리 가중 라플라시안 변형을 최적화하며, 방향 일관성, 운동학적 제약 및 관통 처리를 동시에 고려하여 리타게팅 과정에서 작업 관련 손-물체 접촉 구조를 보존한다. 실험 결과, 이 방법은 ContactPose 데이터셋에서 최고의 접촉 정밀도와 정렬 성능을 달성했으며, Pen-Spin 훈련 성공률을 40.6% 포인트 향상시키고 Wuji Hand 하드웨어로의 제로샷 전이를 구현했다.

## 핵심 내용
### 방법 아키텍처
TopoRetarget의 핵심은 상호작용을 유지하는 리타게팅 프레임워크로, 주요 구성 요소는 다음과 같다:
- **희소 상호작용 그래프 구축**: 손과 물체의 키포인트 간 희소 그래프를 구축하여 작업 관련 접촉 구조를 포착한다.
- **거리 가중 라플라시안 변형**: 거리 가중 라플라시안 변형을 최적화하여 손-물체 상호작용의 기하학적 일관성을 유지한다.
- **방향 일관성 제약**: 리타게팅된 손 자세가 원본 데모의 방향과 일치하도록 보장한다.
- **운동학적 제약**: 정교한 로봇 손의 운동학적 한계를 고려하여 실행 불가능한 자세를 방지한다.
- **관통 처리**: 손과 물체 간의 관통 문제를 감지하고 수정하여 물리적 타당성을 보장한다.

### 실험 설정
- **데이터셋**: 다양한 손-물체 상호작용 시나리오를 포함하는 ContactPose 데이터셋을 사용하여 평가한다.
- **기준 방법**: 기하학 기반 및 학습 기반 방법을 포함한 기존 리타게팅 방법과 비교한다.
- **평가 지표**: 접촉 정밀도, 정렬 오차 및 하위 RL 정책의 성공률을 포함한다.

### 주요 결과
- **접촉 정밀도**: TopoRetarget은 ContactPose 데이터셋에서 모든 기준 방법을 능가하는 최고의 접촉 정밀도와 정렬 성능을 달성했다.
- **Pen-Spin 훈련**: 펜 회전 작업에서 TopoRetarget은 훈련 성공률을 기준 방법의 낮은 수준에서 40.6% 포인트 향상시켰다.
- **제로샷 전이**: 큐브 리타게팅 및 펜 회전 작업에서 TopoRetarget은 추가 미세 조정 없이 Wuji Hand 하드웨어로의 제로샷 전이를 구현했다.

### 결론
TopoRetarget은 손-물체 상호작용 구조를 유지함으로써 정교한 조작에서 참조 동작의 품질을 크게 향상시켜 하위 RL 정책의 학습 효과를 개선한다. 이 방법은 여러 작업과 하드웨어 플랫폼에서 그 범용성과 효율성을 입증했다.
