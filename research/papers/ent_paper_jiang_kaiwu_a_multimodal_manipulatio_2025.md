---
$id: ent_paper_jiang_kaiwu_a_multimodal_manipulatio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning and Human-Robot Interaction'
  zh: Kaiwu：用于机器人学习与人和机器人交互的多模态操作数据集与框架
  ko: 'Kaiwu: 로봇 학습 및 인간-로봇 상호작용을 위한 다중감각 조작 데이터셋과 프레임워크'
summary:
  en: Kaiwu is a large-scale, real-world multimodal manipulation dataset and collection framework for industrial assembly,
    providing synchronized vision, force, sound, gaze, EMG, and motion-capture recordings with fine-grained spatio-temporal
    annotations for robot learning and human-robot interaction research.
  zh: Kaiwu是一个面向工业装配的大规模真实世界多模态操作数据集与采集框架，由研究团队构建，提供同步的视觉、力觉、声音、眼动、肌电和动作捕捉记录，并带有细粒度时空标注，旨在支持机器人学习与人机交互研究。
  ko: Kaiwu는 산업 조립을 위한 대규모 실제 다중감각 조작 데이터셋 및 수집 프레임워크로, 로봇 학습과 인간-로봇 상호작용 연구를 위해 시각, 힘, 소리, 시선, 근전도 및 모션 캡처 기록을 동기화하여 세밀한
    시공간 주석과 함께 제공한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- multimodal_dataset
- imitation_learning
- human_robot_interaction
- assembly
- motion_capture
- emg
- eye_tracking
- robot_learning
- fine_grained_annotation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05231v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (626 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning and Human-Robot Interaction'
  url: https://arxiv.org/abs/2503.05231
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Kaiwu数据集针对复杂装配场景中真实世界同步多模态数据缺失的问题，首次整合了人、环境与机器人的数据采集框架。该数据集包含20名受试者和30个交互对象，共产生11,664个集成动作实例。每个演示都记录了手部运动、操作压力、装配过程声音、多视角视频、高精度动作捕捉信息、第一人称视频中的眼动以及肌电信号。数据集还基于绝对时间戳进行了细粒度多级标注和语义分割标注，旨在推动机器人学习、灵巧操作、人类意图研究与人机协作等领域的发展。

## 核心内容
### 背景与动机
前沿机器人学习技术（如基础模型和从人类模仿学习）对大规模、高质量数据集有巨大需求，这构成了通用智能机器人领域的瓶颈之一。Kaiwu数据集旨在解决复杂装配场景中，特别是包含动态信息及其细粒度标注的真实世界同步多模态数据缺失问题。

### 数据集框架与规模
- 首次提供了整合人类、环境和机器人的数据采集框架。
- 包含20名受试者，使用30个交互对象，共产生11,664个集成动作实例。

### 多模态数据记录
每个演示均同步记录以下模态：
- 手部运动
- 操作压力
- 装配过程声音
- 多视角视频
- 高精度动作捕捉信息
- 第一人称视频中的眼动
- 肌电信号

### 标注方法
- 基于绝对时间戳进行细粒度多级标注。
- 执行语义分割标注。

### 应用目标
Kaiwu数据集旨在促进以下研究方向：
- 机器人学习
- 灵巧操作
- 人类意图研究
- 人机协作

## Overview
Cutting-edge robot learning techniques including foundation models and imitation learning from humans all pose huge demands on large-scale and high-quality datasets which constitute one of the bottleneck in the general intelligent robot fields. This paper presents the Kaiwu multimodal dataset to address the missing real-world synchronized multimodal data problems in the sophisticated assembling scenario,especially with dynamics information and its fine-grained labelling. The dataset first provides an integration of human,environment and robot data collection framework with 20 subjects and 30 interaction objects resulting in totally 11,664 instances of integrated actions. For each of the demonstration,hand motions,operation pressures,sounds of the assembling process,multi-view videos, high-precision motion capture information,eye gaze with first-person videos,electromyography signals are all recorded. Fine-grained multi-level annotation based on absolute timestamp,and semantic segmentation labelling are performed. Kaiwu dataset aims to facilitate robot learning,dexterous manipulation,human intention investigation and human-robot collaboration research.

## 参考
- http://arxiv.org/abs/2503.05231v2

## 개요
Kaiwu 데이터셋은 복잡한 조립 현장에서 실제 세계의 동기화된 다중 모달 데이터가 부족한 문제를 해결하기 위해, 인간, 환경, 로봇의 데이터 수집 프레임워크를 최초로 통합했습니다. 이 데이터셋은 20명의 피험자와 30개의 상호작용 객체를 포함하며, 총 11,664개의 통합 동작 인스턴스를 생성합니다. 각 데모는 손 움직임, 조작 압력, 조립 과정 소리, 다중 시점 비디오, 고정밀 모션 캡처 정보, 1인칭 비디오의 시선 추적, 그리고 근전도 신호를 기록합니다. 데이터셋은 또한 절대 타임스탬프를 기반으로 세분화된 다중 수준 주석과 의미론적 분할 주석을 제공하며, 로봇 학습, 정밀 조작, 인간 의도 연구, 인간-로봇 협력 분야의 발전을 촉진하는 것을 목표로 합니다.

## 핵심 내용
### 배경 및 동기
최첨단 로봇 학습 기술(예: 기초 모델 및 인간 모방 학습)은 대규모 고품질 데이터셋에 대한 막대한 수요가 있으며, 이는 범용 지능 로봇 분야의 병목 현상 중 하나입니다. Kaiwu 데이터셋은 복잡한 조립 현장, 특히 동적 정보와 세분화된 주석을 포함한 실제 세계의 동기화된 다중 모달 데이터 부족 문제를 해결하는 것을 목표로 합니다.

### 데이터셋 프레임워크 및 규모
- 인간, 환경, 로봇을 통합한 데이터 수집 프레임워크를 최초로 제공합니다.
- 20명의 피험자와 30개의 상호작용 객체를 포함하며, 총 11,664개의 통합 동작 인스턴스를 생성합니다.

### 다중 모달 데이터 기록
각 데모는 다음 모달을 동기화하여 기록합니다:
- 손 움직임
- 조작 압력
- 조립 과정 소리
- 다중 시점 비디오
- 고정밀 모션 캡처 정보
- 1인칭 비디오의 시선 추적
- 근전도 신호

### 주석 방법
- 절대 타임스탬프를 기반으로 세분화된 다중 수준 주석을 수행합니다.
- 의미론적 분할 주석을 실행합니다.

### 응용 목표
Kaiwu 데이터셋은 다음 연구 방향을 촉진하는 것을 목표로 합니다:
- 로봇 학습
- 정밀 조작
- 인간 의도 연구
- 인간-로봇 협력
