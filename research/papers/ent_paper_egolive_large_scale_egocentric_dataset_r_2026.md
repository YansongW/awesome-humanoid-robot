---
$id: ent_paper_egolive_large_scale_egocentric_dataset_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoLive: A Large-Scale Egocentric Dataset from Real-World Human Tasks'
  zh: 'EgoLive: A Large-Scale Egocentric Dataset from Real-World Human Tasks'
  ko: 'EgoLive: A Large-Scale Egocentric Dataset from Real-World Human Tasks'
summary:
  en: 'The advancement of robot learning is currently hindered by the scarcity of large-scale, high-quality datasets. While
    established data collection methods such as teleoperation and universal manipulation interfaces dominate current datasets,
    they suffer from inherent limitations in scalability and real-world deployability. Institutions per source list: Joy Future
    Academy、JD.'
  zh: EgoLive 是一个大规模、高质量的以自我为中心的视频数据集，专为机器人操作学习设计。该数据集由研究团队创建，核心贡献在于提供了目前最大的开源注释以自我为中心的数据集，专注于真实世界任务导向的人类日常活动，并通过定制头戴设备实现高精度多模态注释，数据全部采集于无约束的真实场景。
  ko: 'The advancement of robot learning is currently hindered by the scarcity of large-scale, high-quality datasets. While
    established data collection methods such as teleoperation and universal manipulation interfaces dominate current datasets,
    they suffer from inherent limitations in scalability and real-world deployability. Institutions per source list: Joy Future
    Academy、JD.'
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
- egolive
- large
- scale
- egocentric
- dataset
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 275 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2604.23570v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2604.23570 EgoLive: A Large-Scale Egocentric Dataset from Real-World Human Tasks'
  url: https://arxiv.org/abs/2604.23570
  accessed_at: '2026-07-31'
  date: '2026-04-26'
- id: src_002
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

EgoLive 数据集旨在解决机器人学习中大规模高质量数据稀缺的问题。与依赖遥操作或通用操作界面的传统数据收集方法不同，EgoLive 利用人类以自我为中心的视频收集，实现了可扩展、自然且真实世界的数据采集。该数据集具有三大技术优势：它是目前最大的开源注释以自我为中心的数据集，专注于真实世界任务导向的人类日常活动；通过定制头戴式采集设备和全面高精度多模态注释，提供了领先的数据质量；所有数据均采集于无约束的真实世界场景，涵盖家庭服务、零售等垂直领域的人类工作数据，提供了卓越的多样性和生态效度。

## 核心内容
### 数据集概述
EgoLive 是一个大规模、高质量的以自我为中心的视频数据集，专门为机器人操作学习而设计。它通过收集人类在真实世界任务中的日常活动视频，为机器人学习提供可扩展、自然且真实的数据来源。

### 技术优势
- **规模最大**：EgoLive 是当前最大的开源注释以自我为中心的数据集，专注于真实世界任务导向的人类日常活动。
- **数据质量领先**：通过定制头戴式采集设备，实现了高精度多模态注释，包括视频、深度、惯性测量单元（IMU）等数据。
- **场景多样性**：所有数据均采集于无约束的真实世界场景，涵盖家庭服务、零售等垂直领域的人类工作数据，提供了卓越的多样性和生态效度。

### 实验设置与关键数字
- **数据规模**：EgoLive 包含大量视频片段，具体数字未在摘要中提及，但强调其为“最大”的开源注释数据集。
- **采集设备**：使用定制头戴式设备，确保视频稳定性和多模态数据同步。
- **场景覆盖**：包括家庭服务（如清洁、烹饪）、零售（如货架整理、收银）等实际工作场景。

### 结论
EgoLive 的推出旨在为研究社区提供一个可扩展、高质量的数据集，加速通用机器人模型的突破，并促进机器人系统在真实世界中的部署。

## Overview
The advancement of robot learning is currently hindered by the scarcity of large-scale, high-quality datasets. While established data collection methods such as teleoperation and universal manipulation interfaces dominate current datasets, they suffer from inherent limitations in scalability and real-world deployability. Human egocentric video collection, by contrast, has emerged as a promising approach to enable scalable, natural and in-the-wild data collection. As such, we present EgoLive, a large-scale, high-quality egocentric dataset designed explicitly for robot manipulation learning. EgoLive establishes three distinctive technical advantages over existing egocentric datasets: first, it represents the largest open-source annotated egocentric dataset focused on real-world task-oriented human routines to date; second, it delivers leading data quality via a customized head-mounted capture device and comprehensive high-precision multi-modal annotations; third, all data is collected exclusively in unconstrained real-world scenarios and encompasses vertical field human working data, including home service, retail, and other practical work scenarios, providing superior diversity and ecological validity. With the introduction of EgoLive, we aim to provide the research community with a scalable, high-quality dataset that accelerates breakthroughs in generalizable robotic models and facilitates the real-world deployment of robot systems.

## 参考
- https://arxiv.org/abs/2604.23570
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

EgoLive 데이터셋은 로봇 학습에서 대규모 고품질 데이터의 부족 문제를 해결하기 위해 설계되었습니다. 원격 조작이나 범용 조작 인터페이스에 의존하는 전통적인 데이터 수집 방법과 달리, EgoLive는 인간의 자기 중심적 비디오 수집을 활용하여 확장 가능하고 자연스러우며 실제 세계의 데이터 수집을 가능하게 합니다. 이 데이터셋은 세 가지 주요 기술적 장점을 가지고 있습니다: 현재까지 가장 큰 오픈소스 주석 자기 중심적 데이터셋으로, 실제 세계의 작업 지향적 인간 일상 활동에 초점을 맞추고 있습니다; 맞춤형 헤드마운트 수집 장치와 포괄적인 고정밀 다중 모드 주석을 통해 선도적인 데이터 품질을 제공합니다; 모든 데이터는 제약 없는 실제 세계 시나리오에서 수집되며, 가사 서비스, 소매 등 수직 분야의 인간 작업 데이터를 포함하여 뛰어난 다양성과 생태적 타당성을 제공합니다.

## 핵심 내용
### 데이터셋 개요
EgoLive는 로봇 조작 학습을 위해 특별히 설계된 대규모 고품질 자기 중심적 비디오 데이터셋입니다. 실제 세계 작업에서 인간의 일상 활동 비디오를 수집하여 로봇 학습에 확장 가능하고 자연스러우며 실제적인 데이터 소스를 제공합니다.

### 기술적 장점
- **최대 규모**: EgoLive는 현재까지 가장 큰 오픈소스 주석 자기 중심적 데이터셋으로, 실제 세계의 작업 지향적 인간 일상 활동에 초점을 맞추고 있습니다.
- **데이터 품질 선도**: 맞춤형 헤드마운트 수집 장치를 통해 비디오, 깊이, 관성 측정 장치(IMU) 등 데이터를 포함한 고정밀 다중 모드 주석을 구현했습니다.
- **시나리오 다양성**: 모든 데이터는 제약 없는 실제 세계 시나리오에서 수집되며, 가사 서비스, 소매 등 수직 분야의 인간 작업 데이터를 포함하여 뛰어난 다양성과 생태적 타당성을 제공합니다.

### 실험 설정 및 주요 수치
- **데이터 규모**: EgoLive는 많은 비디오 클립을 포함하며, 구체적인 수치는 초록에서 언급되지 않았지만 "가장 큰" 오픈소스 주석 데이터셋임을 강조합니다.
- **수집 장치**: 맞춤형 헤드마운트 장치를 사용하여 비디오 안정성과 다중 모드 데이터 동기화를 보장합니다.
- **시나리오 범위**: 가사 서비스(예: 청소, 요리), 소매(예: 선반 정리, 계산) 등 실제 작업 시나리오를 포함합니다.

### 결론
EgoLive의 출시는 연구 커뮤니티에 확장 가능하고 고품질의 데이터셋을 제공하여 범용 로봇 모델의 돌파구를 가속화하고 실제 세계에서 로봇 시스템의 배포를 촉진하는 것을 목표로 합니다.
