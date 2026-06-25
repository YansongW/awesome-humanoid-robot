---
$id: "ent_dataset_open_x_embodiment"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "dataset"

names:
  en: "Open X-Embodiment Dataset"
  zh: "Open X-Embodiment 数据集"
  ko: "Open X-Embodiment 데이터셋"

summary:
  en: "A large-scale aggregated robot-learning dataset combining demonstrations from diverse real-world robot platforms and institutions, widely used for cross-embodiment VLA pretraining."
  zh: "一个大规模聚合机器人学习数据集，整合来自多种真实机器人平台和机构的演示数据，广泛用于跨具身 VLA 预训练。"
  ko: "다양한 실제 로봇 플랫폼과 기관의 데모를 결합한 대규모 로봇 학습 데이터셋으로, cross-embodiment VLA 사전 학습에 널리 사용됨."

domains:
  - "09_data_datasets"

layers:
  - "intelligence"

functional_roles:
  - "knowledge"
  - "intelligence"

tags:
  - "robot_learning"
  - "vla"
  - "cross_embodiment"
  - "real_world_data"
  - "pretraining"
  - "demonstrations"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Dataset scope and usage are documented in the original RSS 2023 paper and confirmed by Wang et al. 2026 VLA survey."

sources:
  - id: "src_oxe_paper"
    type: "paper"
    title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models"
    url: "https://arxiv.org/abs/2310.08864"
    date: "2023-10-13"
    accessed_at: "2026-06-22"
  - id: "src_oxe_website"
    type: "website"
    title: "Open X-Embodiment Collaboration"
    url: "https://www.open-x-embodiment.org/"
    date: "2023-01-01"
    accessed_at: "2026-06-22"

related_entities:
  - id: "ent_paper_wang_vla_survey_2026"
    relationship: "cites"
    description:
      en: "Wang et al. 2026 survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset."
      zh: "Wang 等人 2026 综述将 Open X-Embodiment 引用为广泛使用的跨具身预训练数据集。"
      ko: "Wang et al. 2026 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함."
---

# Open X-Embodiment Dataset

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
