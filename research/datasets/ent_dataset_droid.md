---
$id: ent_dataset_droid
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: DROID
  zh: DROID 机器人操作数据集
  ko: DROID
summary:
  en: A distributed, diverse real-world robot manipulation dataset collected across multiple labs and environments, designed
    to improve visual and environmental robustness.
  zh: 一个分布式、多样化的真实世界机器人操作数据集，跨多个实验室和环境收集，旨在提升视觉与环境鲁棒性。
  ko: 여러 실험실과 환경에서 수집된 분산적이고 다양한 실제 로봇 조작 데이터셋으로, 시각 및 환경 견고성 향상을 목표로 함.
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
- real_world_data
- distributed_collection
- manipulation
- robustness
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Scope described in original DROID paper and confirmed by Wang et al. 2026 VLA survey. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_droid_paper
  type: paper
  title: 'DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset'
  url: https://arxiv.org/abs/2403.12945
  date: '2024-03-19'
  accessed_at: '2026-06-22'
- id: src_droid_website
  type: website
  title: DROID Dataset
  url: https://droid-dataset.github.io/
  date: '2024-01-01'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: cites
  description:
    en: Wang et al. 2026 survey cites DROID as a distributed real-world dataset with strong visual and environmental variation.
    zh: Wang 等人 2026 综述引用 DROID 作为具有强视觉和环境变化的分布式真实世界数据集。
    ko: Wang et al. 2026 서베이는 DROID를 강한 시각 및 환경 변화를 가진 분산 실제 데이터셋으로 인용함.
theoretical_depth:
- system
---

## 概述
一个分布式、多样化的真实世界机器人操作数据集，跨多个实验室和环境收集，旨在提升视觉与环境鲁棒性。

## 核心内容
### DROID 机器人操作数据集的定义与定位
DROID 机器人操作数据集属于 **数据集** 类型，英文名称为 *DROID*。
一个分布式、多样化的真实世界机器人操作数据集，跨多个实验室和环境收集，旨在提升视觉与环境鲁棒性。

### DROID 机器人操作数据集的关键信息
以下整理了关于DROID 机器人操作数据集的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像由全球许多摄影师在不同城市、不同光线下拍摄的“街头摄影合集”——用丰富的真实场景差异来训练一个 robust 的图像识别系统。

> **自然语言逻辑**：DROID 是一个分布式、多样化的真实世界机器人操作数据集，由多个实验室按统一协议收集；它强调视觉和环境多样性，帮助策略学习在不同背景、光照、相机视角和场景布局下都能泛化，是训练鲁棒 VLA 模型的重要真实数据来源。

## Overview

DROID is a large-scale in-the-wild robot manipulation dataset collected by multiple institutions using a shared data-collection protocol. It emphasizes visual and environmental diversity to train policies that generalize across backgrounds, lighting, and scene configurations.

## Key Characteristics

- **Distributed collection**: collected across many labs with standardized hardware and software.
- **Visual diversity**: varied backgrounds, lighting, camera viewpoints, and object arrangements.
- **Language annotations**: natural-language task descriptions for each episode.
- **High fidelity**: real-world contact dynamics and visual appearance.

## Limitations

- Primarily arm-only manipulation; limited humanoid or mobile manipulation coverage.
- Real-world collection is expensive and time-consuming, constraining scale compared to synthetic alternatives.

## Relevance to Humanoid Robotics

DROID demonstrates a scalable real-world data-collection model. For humanoids, similar distributed collection would need to additionally capture whole-body balance, locomotion, and bimanual coordination.

## 参考
- [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)
- [DROID Dataset](https://droid-dataset.github.io/)

## 개요
분산형이고 다양한 실제 세계 로봇 조작 데이터셋으로, 여러 연구실과 환경에서 수집되었으며, 시각 및 환경 강건성을 향상시키는 것을 목표로 합니다.

## 핵심 내용
### DROID 로봇 조작 데이터셋의 정의와 위치
DROID 로봇 조작 데이터셋은 **데이터셋** 유형에 속하며, 영문 명칭은 *DROID*입니다.
분산형이고 다양한 실제 세계 로봇 조작 데이터셋으로, 여러 연구실과 환경에서 수집되었으며, 시각 및 환경 강건성을 향상시키는 것을 목표로 합니다.

### DROID 로봇 조작 데이터셋의 핵심 정보
다음은 DROID 로봇 조작 데이터셋에 대한 상세 설명을 정리한 것으로, 중·영문 독자 모두 참고할 수 있습니다.

## 초록

> **생활 예시**: 마치 전 세계 많은 사진작가들이 서로 다른 도시와 다양한 조명 조건에서 촬영한 "거리 사진 컬렉션"과 같습니다. 풍부한 실제 장면 차이를 활용해 강건한 이미지 인식 시스템을 훈련하는 것입니다.

> **자연어 논리**: DROID는 분산형이고 다양한 실제 세계 로봇 조작 데이터셋으로, 여러 연구실이 통일된 프로토콜에 따라 수집했습니다. 시각 및 환경 다양성을 강조하여, 정책 학습이 다양한 배경, 조명, 카메라 시점 및 장면 레이아웃에서도 일반화될 수 있도록 돕습니다. 이는 강건한 VLA 모델을 훈련하는 중요한 실제 데이터 소스입니다.
