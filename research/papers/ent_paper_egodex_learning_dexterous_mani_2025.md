---
$id: ent_paper_egodex_learning_dexterous_mani_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
  zh: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
  ko: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
summary:
  en: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
  zh: EgoDex 是 Apple 团队于 2025 年提出的最大规模灵巧操作数据集，包含 829 小时第一人称视频与同步的 3D 手部及手指关节追踪数据。该数据集覆盖 194 种桌面任务，并提供了手部轨迹预测的模仿学习基准与评估指标，旨在解决灵巧操作领域的数据稀缺问题。
  ko: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egodex
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11709v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (814 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2505.11709
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EgoDex 利用 Apple Vision Pro 的头戴式摄像头与设备端 SLAM 技术，在录制时同步采集多视角校准视频与每根手指关节的精确 3D 位姿，避免了传统数据集缺乏手部标注或仅关注非操作场景的局限。数据集涵盖从系鞋带到折叠衣物等 194 种日常物品操作任务，总时长 829 小时，是目前规模最大、多样性最丰富的灵巧操作数据集。基于该数据，作者训练并系统评估了手部轨迹预测的模仿学习策略，并引入了新的度量标准与基准测试，以推动机器人学、计算机视觉与基础模型在该领域的发展。

## 核心内容
### 数据稀缺问题与解决方案
- 灵巧操作的模仿学习长期受困于数据不足，与自然语言和 2D 视觉领域不同，缺乏互联网规模的操作数据。
- 第一人称人类视频（egocentric video）是潜在的可扩展数据源，但现有大规模数据集（如 Ego4D）缺少原生手部姿态标注，且未聚焦于物体操作。

### EgoDex 数据集构建
- **采集设备**：使用 Apple Vision Pro，其配备多个校准摄像头与设备端 SLAM，可在录制时实时追踪每只手的每个关节的 3D 位姿。
- **规模与多样性**：包含 829 小时视频，覆盖 194 种桌面任务，涉及日常家居物品（如系鞋带、折叠衣物等）。
- **数据特点**：所有手部追踪数据与视频同步采集，无需后期标注，保证了精度与一致性。

### 实验设置与基准
- **任务**：基于数据集训练模仿学习策略，预测手部轨迹。
- **评估指标**：引入新的度量标准与基准测试，用于衡量手部轨迹预测的进展。
- **结论**：EgoDex 为灵巧操作研究提供了大规模、高质量的数据基础，有望推动机器人学、计算机视觉与基础模型的前沿发展。

### 开源与访问
- EgoDex 已公开下载：https://github.com/apple/ml-egodex

## Overview
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 参考
- http://arxiv.org/abs/2505.11709v3

## 개요
EgoDex는 Apple Vision Pro의 헤드 장착 카메라와 온디바이스 SLAM 기술을 활용하여, 녹화 시점에 다중 시점 보정 영상과 각 손가락 관절의 정밀한 3D 포즈를 동시에 수집합니다. 이는 기존 데이터셋이 손에 대한 주석이 부족하거나 비조작 장면에만 초점을 맞춘 한계를 피합니다. 데이터셋은 신발 끈 묶기부터 옷 접기까지 194가지 일상 사물 조작 작업을 포함하며, 총 829시간 분량으로 현재 가장 크고 다양성이 풍부한 손재주 조작 데이터셋입니다. 이 데이터를 기반으로 저자들은 손 궤적 예측을 위한 모방 학습 정책을 훈련하고 체계적으로 평가했으며, 로봇 공학, 컴퓨터 비전 및 기초 모델의 해당 분야 발전을 촉진하기 위해 새로운 평가 지표와 벤치마크를 도입했습니다.

## 핵심 내용
### 데이터 부족 문제와 해결 방안
- 손재주 조작의 모방 학습은 오랫동안 데이터 부족에 시달려 왔으며, 자연어 및 2D 비전 분야와 달리 인터넷 규모의 조작 데이터가 부족합니다.
- 일인칭 인간 비디오(egocentric video)는 잠재적으로 확장 가능한 데이터 소스이지만, 기존 대규모 데이터셋(예: Ego4D)에는 기본 손 포즈 주석이 없고 사물 조작에 초점을 맞추지 않았습니다.

### EgoDex 데이터셋 구축
- **수집 장치**: Apple Vision Pro를 사용하며, 여러 보정 카메라와 온디바이스 SLAM을 갖추고 있어 녹화 중 각 손의 모든 관절 3D 포즈를 실시간으로 추적합니다.
- **규모와 다양성**: 829시간의 비디오를 포함하며, 일상 가정용품을 다루는 194가지 데스크톱 작업(신발 끈 묶기, 옷 접기 등)을 포괄합니다.
- **데이터 특징**: 모든 손 추적 데이터는 비디오와 동기화되어 수집되며, 사후 주석이 필요 없어 정밀도와 일관성을 보장합니다.

### 실험 설정 및 벤치마크
- **작업**: 데이터셋을 기반으로 모방 학습 정책을 훈련하여 손 궤적을 예측합니다.
- **평가 지표**: 손 궤적 예측의 진전을 측정하기 위한 새로운 평가 지표와 벤치마크를 도입합니다.
- **결론**: EgoDex는 손재주 조작 연구를 위한 대규모 고품질 데이터 기반을 제공하며, 로봇 공학, 컴퓨터 비전 및 기초 모델의 최첨단 발전을 촉진할 것으로 기대됩니다.

### 오픈소스 및 접근
- EgoDex는 공개 다운로드 가능: https://github.com/apple/ml-egodex
