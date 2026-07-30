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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11709v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
조작을 위한 모방 학습은 잘 알려진 데이터 부족 문제를 겪고 있습니다. 자연어 및 2D 컴퓨터 비전과 달리, 정교한 조작을 위한 인터넷 규모의 데이터 코퍼스는 존재하지 않습니다. 한 가지 매력적인 대안은 수동적으로 확장 가능한 데이터 소스인 자기중심적 인간 비디오입니다. 그러나 Ego4D와 같은 기존의 대규모 데이터셋은 기본적인 손 자세 주석이 없으며 객체 조작에 초점을 맞추지 않습니다. 이에 따라, 우리는 Apple Vision Pro를 사용하여 EgoDex를 수집했습니다: 현재까지 가장 크고 다양한 정교한 인간 조작 데이터셋입니다. EgoDex는 829시간의 자기중심적 비디오와 녹화 시점에 수집된 3D 손 및 손가락 추적 데이터를 포함하며, 여러 보정된 카메라와 기기 내 SLAM을 사용하여 각 손의 모든 관절 자세를 정밀하게 추적할 수 있습니다. 이 데이터셋은 신발 끈 묶기부터 빨래 개기까지 194가지 다양한 탁상 작업에서 일상적인 가정용 물체를 사용한 다양한 조작 행동을 포괄합니다. 또한, 우리는 데이터셋에서 손 궤적 예측을 위한 모방 학습 정책을 훈련하고 체계적으로 평가하며, 이 점점 더 중요해지는 분야의 진전을 측정하기 위한 지표와 벤치마크를 도입합니다. 이 대규모 데이터셋을 공개함으로써 로봇 공학, 컴퓨터 비전 및 기초 모델의 경계를 넓히기를 희망합니다. EgoDex는 https://github.com/apple/ml-egodex에서 공개적으로 다운로드 가능합니다.

## 핵심 내용
조작을 위한 모방 학습은 잘 알려진 데이터 부족 문제를 겪고 있습니다. 자연어 및 2D 컴퓨터 비전과 달리, 정교한 조작을 위한 인터넷 규모의 데이터 코퍼스는 존재하지 않습니다. 한 가지 매력적인 대안은 수동적으로 확장 가능한 데이터 소스인 자기중심적 인간 비디오입니다. 그러나 Ego4D와 같은 기존의 대규모 데이터셋은 기본적인 손 자세 주석이 없으며 객체 조작에 초점을 맞추지 않습니다. 이에 따라, 우리는 Apple Vision Pro를 사용하여 EgoDex를 수집했습니다: 현재까지 가장 크고 다양한 정교한 인간 조작 데이터셋입니다. EgoDex는 829시간의 자기중심적 비디오와 녹화 시점에 수집된 3D 손 및 손가락 추적 데이터를 포함하며, 여러 보정된 카메라와 기기 내 SLAM을 사용하여 각 손의 모든 관절 자세를 정밀하게 추적할 수 있습니다. 이 데이터셋은 신발 끈 묶기부터 빨래 개기까지 194가지 다양한 탁상 작업에서 일상적인 가정용 물체를 사용한 다양한 조작 행동을 포괄합니다. 또한, 우리는 데이터셋에서 손 궤적 예측을 위한 모방 학습 정책을 훈련하고 체계적으로 평가하며, 이 점점 더 중요해지는 분야의 진전을 측정하기 위한 지표와 벤치마크를 도입합니다. 이 대규모 데이터셋을 공개함으로써 로봇 공학, 컴퓨터 비전 및 기초 모델의 경계를 넓히기를 희망합니다. EgoDex는 https://github.com/apple/ml-egodex에서 공개적으로 다운로드 가능합니다.

## 参考
- http://arxiv.org/abs/2505.11709v3
