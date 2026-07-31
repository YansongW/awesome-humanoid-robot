---
$id: ent_paper_posescript_linking_3d_human_poses_natura_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PoseScript: Linking 3D Human Poses and Natural Language'
  zh: 'PoseScript: Linking 3D Human Poses and Natural Language'
  ko: 'PoseScript: Linking 3D Human Poses and Natural Language'
summary:
  en: Natural language plays a critical role in many computer vision applications, such as image captioning, visual question
    answering, and cross-modal retrieval, to provide fine-grained semantic information.
  zh: PoseScript 是一个将 3D 人体姿态与自然语言描述配对的数据集，由研究团队基于 AMASS 数据集构建。其核心贡献在于提供了超过 6000 个带人工标注的姿态描述，并设计了一套自动化描述生成流程，将数据规模扩展至 10 万条，从而支持跨模态检索、文本条件姿态生成和姿态描述生成等任务。
  ko: Natural language plays a critical role in many computer vision applications, such as image captioning, visual question
    answering, and cross-modal retrieval, to provide fine-grained semantic information.
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
- posescript
- linking
- 3d
- human
- poses
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 327 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2210.11795v3); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2210.11795 PoseScript: Linking 3D Human Poses and Natural Language'
  url: https://arxiv.org/abs/2210.11795
  accessed_at: '2026-07-31'
  date: '2022-10-21'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

PoseScript 数据集旨在弥补现有 3D 人体姿态数据缺乏详细语言描述的不足。该数据集从 AMASS 中选取了 6000 多个姿态，并配以人工标注的身体部位及空间关系描述。为了满足数据驱动算法的需求，研究团队提出了一种自动化描述流程：首先从 3D 关键点中提取称为“posecodes”的低层姿态信息，再通过句法规则组合成高层文本描述，从而将数据量扩展到 10 万条。基于此数据集，他们展示了三项多模态学习任务：跨模态检索、文本条件姿态生成以及姿态描述生成，验证了标注姿态的实用价值。

## 核心内容
### 数据集构建
- **人工标注**：从 AMASS 数据集中选取 6000 多个 3D 人体姿态，由标注员提供关于身体部位及其空间关系的详细描述。
- **自动化描述生成**：为扩大数据规模，设计了一套流程：
  - 从 3D 关键点中提取低层姿态信息，即“posecodes”，基于简单但通用的规则。
  - 利用句法规则将 posecodes 组合成高层文本描述。
  - 最终生成 10 万条自动标注数据，用于预训练深度模型，再微调至人工标注数据。

### 多模态学习任务
- **跨模态检索**：构建一个将 3D 姿态和文本描述映射到联合嵌入空间的管道，支持从大规模数据集中检索相关姿态。
- **文本条件姿态生成**：建立基线模型，根据文本描述生成对应的 3D 人体姿态。
- **姿态描述生成**：提出一个学习过程，自动为给定姿态生成自然语言描述。

### 实验设置与关键数字
- 数据集规模：人工标注 6000+ 姿态，自动标注 10 万条。
- 任务目标：验证 PoseScript 在跨模态学习中的有效性，为后续研究提供基础。

## Overview
Natural language plays a critical role in many computer vision applications, such as image captioning, visual question answering, and cross-modal retrieval, to provide fine-grained semantic information. Unfortunately, while human pose is key to human understanding, current 3D human pose datasets lack detailed language descriptions. To address this issue, we have introduced the PoseScript dataset. This dataset pairs more than six thousand 3D human poses from AMASS with rich human-annotated descriptions of the body parts and their spatial relationships. Additionally, to increase the size of the dataset to a scale that is compatible with data-hungry learning algorithms, we have proposed an elaborate captioning process that generates automatic synthetic descriptions in natural language from given 3D keypoints. This process extracts low-level pose information, known as "posecodes", using a set of simple but generic rules on the 3D keypoints. These posecodes are then combined into higher level textual descriptions using syntactic rules. With automatic annotations, the amount of available data significantly scales up (100k), making it possible to effectively pretrain deep models for finetuning on human captions. To showcase the potential of annotated poses, we present three multi-modal learning tasks that utilize the PoseScript dataset. Firstly, we develop a pipeline that maps 3D poses and textual descriptions into a joint embedding space, allowing for cross-modal retrieval of relevant poses from large-scale datasets. Secondly, we establish a baseline for a text-conditioned model generating 3D poses. Thirdly, we present a learned process for generating pose descriptions. These applications demonstrate the versatility and usefulness of annotated poses in various tasks and pave the way for future research in the field.

## 参考
- https://arxiv.org/abs/2210.11795
- https://github.com/ImChong/Robotics_Notebooks

## 개요

PoseScript 데이터셋은 기존 3D 인체 자세 데이터에 상세한 언어 설명이 부족한 점을 보완하기 위해 설계되었습니다. 이 데이터셋은 AMASS에서 6000개 이상의 자세를 선별하고, 인체 부위 및 공간 관계에 대한 수동 주석을 추가했습니다. 데이터 기반 알고리즘의 요구를 충족하기 위해 연구팀은 자동화된 설명 파이프라인을 제안했습니다. 먼저 3D 키포인트에서 "posecodes"라는 저수준 자세 정보를 추출한 후, 구문 규칙을 통해 고수준 텍스트 설명으로 조합하여 데이터 양을 10만 개로 확장했습니다. 이 데이터셋을 기반으로 세 가지 멀티모달 학습 작업(교차 모달 검색, 텍스트 조건 자세 생성, 자세 설명 생성)을 시연하여 주석이 달린 자세의 실용적 가치를 검증했습니다.

## 핵심 내용
### 데이터셋 구축
- **수동 주석**: AMASS 데이터셋에서 6000개 이상의 3D 인체 자세를 선별하고, 주석자가 인체 부위 및 공간 관계에 대한 상세 설명을 제공했습니다.
- **자동 설명 생성**: 데이터 규모를 확장하기 위해 다음과 같은 파이프라인을 설계했습니다:
  - 3D 키포인트에서 저수준 자세 정보, 즉 "posecodes"를 추출하며, 이는 간단하지만 일반적인 규칙에 기반합니다.
  - 구문 규칙을 사용하여 posecodes를 고수준 텍스트 설명으로 조합합니다.
  - 최종적으로 10만 개의 자동 주석 데이터를 생성하여 딥 모델 사전 학습에 사용하고, 이후 수동 주석 데이터로 미세 조정합니다.

### 멀티모달 학습 작업
- **교차 모달 검색**: 3D 자세와 텍스트 설명을 공동 임베딩 공간에 매핑하는 파이프라인을 구축하여 대규모 데이터셋에서 관련 자세를 검색할 수 있도록 지원합니다.
- **텍스트 조건 자세 생성**: 텍스트 설명에 따라 해당 3D 인체 자세를 생성하는 기준 모델을 구축합니다.
- **자세 설명 생성**: 주어진 자세에 대해 자연어 설명을 자동으로 생성하는 학습 과정을 제안합니다.

### 실험 설정 및 주요 수치
- 데이터셋 규모: 수동 주석 6000개 이상의 자세, 자동 주석 10만 개.
- 작업 목표: PoseScript가 교차 모달 학습에서의 효과성을 검증하고, 후속 연구를 위한 기반을 제공합니다.
