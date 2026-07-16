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
  zh: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11709v3.
sources:
- id: src_001
  type: paper
  title: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2505.11709
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 核心内容
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 参考
- http://arxiv.org/abs/2505.11709v3

## Overview
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## Content
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 개요
조작을 위한 모방 학습은 잘 알려진 데이터 부족 문제를 겪고 있습니다. 자연어 및 2D 컴퓨터 비전과 달리, 정교한 조작을 위한 인터넷 규모의 데이터 코퍼스는 존재하지 않습니다. 한 가지 매력적인 대안은 수동적으로 확장 가능한 데이터 소스인 자기중심적 인간 비디오입니다. 그러나 Ego4D와 같은 기존의 대규모 데이터셋은 기본적인 손 자세 주석이 없으며 객체 조작에 초점을 맞추지 않습니다. 이에 따라, 우리는 Apple Vision Pro를 사용하여 EgoDex를 수집했습니다: 현재까지 가장 크고 다양한 정교한 인간 조작 데이터셋입니다. EgoDex는 829시간의 자기중심적 비디오와 녹화 시점에 수집된 3D 손 및 손가락 추적 데이터를 포함하며, 여러 보정된 카메라와 기기 내 SLAM을 사용하여 각 손의 모든 관절 자세를 정밀하게 추적할 수 있습니다. 이 데이터셋은 신발 끈 묶기부터 빨래 개기까지 194가지 다양한 탁상 작업에서 일상적인 가정용 물체를 사용한 다양한 조작 행동을 포괄합니다. 또한, 우리는 데이터셋에서 손 궤적 예측을 위한 모방 학습 정책을 훈련하고 체계적으로 평가하며, 이 점점 더 중요해지는 분야의 진전을 측정하기 위한 지표와 벤치마크를 도입합니다. 이 대규모 데이터셋을 공개함으로써 로봇 공학, 컴퓨터 비전 및 기초 모델의 경계를 넓히기를 희망합니다. EgoDex는 https://github.com/apple/ml-egodex에서 공개적으로 다운로드 가능합니다.

## 핵심 내용
조작을 위한 모방 학습은 잘 알려진 데이터 부족 문제를 겪고 있습니다. 자연어 및 2D 컴퓨터 비전과 달리, 정교한 조작을 위한 인터넷 규모의 데이터 코퍼스는 존재하지 않습니다. 한 가지 매력적인 대안은 수동적으로 확장 가능한 데이터 소스인 자기중심적 인간 비디오입니다. 그러나 Ego4D와 같은 기존의 대규모 데이터셋은 기본적인 손 자세 주석이 없으며 객체 조작에 초점을 맞추지 않습니다. 이에 따라, 우리는 Apple Vision Pro를 사용하여 EgoDex를 수집했습니다: 현재까지 가장 크고 다양한 정교한 인간 조작 데이터셋입니다. EgoDex는 829시간의 자기중심적 비디오와 녹화 시점에 수집된 3D 손 및 손가락 추적 데이터를 포함하며, 여러 보정된 카메라와 기기 내 SLAM을 사용하여 각 손의 모든 관절 자세를 정밀하게 추적할 수 있습니다. 이 데이터셋은 신발 끈 묶기부터 빨래 개기까지 194가지 다양한 탁상 작업에서 일상적인 가정용 물체를 사용한 다양한 조작 행동을 포괄합니다. 또한, 우리는 데이터셋에서 손 궤적 예측을 위한 모방 학습 정책을 훈련하고 체계적으로 평가하며, 이 점점 더 중요해지는 분야의 진전을 측정하기 위한 지표와 벤치마크를 도입합니다. 이 대규모 데이터셋을 공개함으로써 로봇 공학, 컴퓨터 비전 및 기초 모델의 경계를 넓히기를 희망합니다. EgoDex는 https://github.com/apple/ml-egodex에서 공개적으로 다운로드 가능합니다.
