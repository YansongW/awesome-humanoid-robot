---
$id: ent_dataset_open_x_embodiment
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: Open X-Embodiment Dataset
  zh: Open X-Embodiment 数据集
  ko: Open X-Embodiment 데이터셋
summary:
  en: A large-scale aggregated robot-learning dataset combining demonstrations from diverse real-world robot platforms and
    institutions, widely used for cross-embodiment VLA pretraining.
  zh: 概述 一个大规模聚合机器人学习数据集，整合来自多种真实机器人平台和机构的演示数据，广泛用于跨具身 VLA 预训练。
  ko: 다양한 실제 로봇 플랫폼과 기관의 데모를 결합한 대규모 로봇 학습 데이터셋으로, cross-embodiment VLA 사전 학습에 널리 사용됨.
domains:
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- robot_learning
- vla
- cross_embodiment
- real_world_data
- pretraining
- demonstrations
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Dataset scope and usage are documented in the original RSS 2023 paper and confirmed by Wang et al. 2026 VLA survey.
    Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_oxe_paper
  type: paper
  title: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'
  url: https://arxiv.org/abs/2310.08864
  date: '2023-10-13'
  accessed_at: '2026-06-22'
- id: src_oxe_website
  type: website
  title: Open X-Embodiment Collaboration
  url: https://www.open-x-embodiment.org/
  date: '2023-01-01'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: cites
  description:
    en: Wang et al. 2026 survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset.
    zh: Wang 等人 2026 综述将 Open X-Embodiment 引用为广泛使用的跨具身预训练数据集。
    ko: Wang et al. 2026 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함.
theoretical_depth:
- system
---

## 概述
一个大规模聚合机器人学习数据集，整合来自多种真实机器人平台和机构的演示数据，广泛用于跨具身 VLA 预训练。

## 核心内容
### Open X-Embodiment 数据集的定义与定位
Open X-Embodiment 数据集属于 **数据集** 类型，英文名称为 *Open X-Embodiment Dataset*。
一个大规模聚合机器人学习数据集，整合来自多种真实机器人平台和机构的演示数据，广泛用于跨具身 VLA 预训练。

### Open X-Embodiment 数据集的关键信息
以下整理了关于Open X-Embodiment 数据集的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像把来自不同运动项目、不同体型运动员的训练视频整合成一部“通用运动教材”，让学习者能跨项目迁移基本动作技能。

> **自然语言逻辑**：Open X-Embodiment 是目前最大的公开机器人演示数据聚合集之一，汇集了多个机构、多种机器人形态和控制接口的数据；它统一的格式支持跨具身预训练，是 OpenVLA 等通用视觉-语言-动作模型最常用的预训练语料。

## Overview

Open X-Embodiment (OXE) is one of the largest public aggregations of robot demonstration data. It pools data from multiple institutions, robot morphologies, and control interfaces into a unified format suitable for training generalist vision-language-action models.

## Key Characteristics

- **Cross-embodiment**: combines data from many robot platforms with different action spaces (EEF, joint, delta, absolute, etc.).
- **Large scale**: millions of demonstration frames across thousands of tasks.
- **Diversity**: covers manipulation tasks in multiple environments with varying camera views and language instructions.
- **Trade-offs**: the heterogeneity that enables generalization also introduces alignment challenges across embodiments.

## Format

Data is released in a standardized RLDS format with video, language instruction, robot state, and action traces.

## Relevance to Humanoid Robotics

Open X-Embodiment is the most common pretraining corpus for VLA models that may later be fine-tuned on humanoid platforms. However, humanoid-specific whole-body control and balancing data is under-represented compared to arm-only manipulation.

## 参考
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)
- [Open X-Embodiment Collaboration](https://www.open-x-embodiment.org/)

Open X-Embodiment 数据集的相关技术仍在快速发展。从系统科学角度看，它与其他dataset相互耦合，共同决定了人形机器人的整体性能。深入理解其原理、边界条件与工程约束，是将实验室样机转化为可量产产品的必要环节。

## 개요
대규모 집합 로봇 학습 데이터셋으로, 다양한 실제 로봇 플랫폼과 기관의 시연 데이터를 통합하여 교차 구현 VLA 사전 학습에 널리 사용됩니다.

## 핵심 내용
### Open X-Embodiment 데이터셋의 정의와 위치
Open X-Embodiment 데이터셋은 **데이터셋** 유형에 속하며, 영문 명칭은 *Open X-Embodiment Dataset*입니다.
대규모 집합 로봇 학습 데이터셋으로, 다양한 실제 로봇 플랫폼과 기관의 시연 데이터를 통합하여 교차 구현 VLA 사전 학습에 널리 사용됩니다.

### Open X-Embodiment 데이터셋의 주요 정보
다음은 Open X-Embodiment 데이터셋에 대한 상세 설명을 정리한 것으로, 중·영문 독자 모두 참고할 수 있습니다.

## 개요

> **생활 예시**: 마치 다양한 운동 종목과 체형의 선수 훈련 영상을 하나의 '범용 운동 교재'로 통합하여 학습자가 종목 간 기본 동작 기술을 전이할 수 있게 하는 것과 같습니다.

> **자연어 논리**: Open X-Embodiment는 현재 공개된 로봇 시연 데이터 중 가장 큰 집합체 중 하나로, 여러 기관, 다양한 로봇 형태 및 제어 인터페이스의 데이터를 수집합니다. 통일된 형식은 교차 구현 사전 학습을 지원하며, OpenVLA와 같은 범용 시각-언어-동작 모델에서 가장 많이 사용되는 사전 학습 코퍼스입니다.
