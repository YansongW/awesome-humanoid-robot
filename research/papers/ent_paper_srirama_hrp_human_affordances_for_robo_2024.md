---
$id: ent_paper_srirama_hrp_human_affordances_for_robo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HRP: Human Affordances for Robotic Pre-Training'
  zh: HRP：面向机器人预训练的人类可供性学习
  ko: 'HRP: 로봇 사전 훈련을 위한 인간 어포던스'
summary:
  en: HRP extracts contact points, future hand poses, and active object bounding boxes from internet-scale human videos, then
    distills these affordances into pre-trained visual encoders via L2 regression with LayerNorm-only fine-tuning, improving
    robotic manipulation across diverse camera views and robot morphologies.
  zh: HRP 提出从互联网规模的人类视频中自动提取接触点、未来手部姿态和主动物体边界框等“可供性”标签，并通过仅微调 LayerNorm 的 L2 回归将这些标签蒸馏到预训练的视觉编码器中。该方法无需额外机器人数据，即可显著提升机器人操作任务在多种相机视角和机器人形态下的泛化能力。
  ko: HRP는 인터넷 규모의 인간 비디오에서 접촉점, 미래 손 자세, 활성 객체 경계 상자를 추출한 후 LayerNorm만 미세 조정하는 L2 회귀를 통해 이러한 어포던스를 사전 훈련된 시각 인코더에 증류하여 다양한
    카메라 시점과 로봇 형태에서 조작 성능을 향상시킨다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- affordance_pre_training
- visual_representation_learning
- imitation_learning
- human_video_learning
- diffusion_policy
- robotic_manipulation
- cross_view_generalization
- contact_point_prediction
- hand_pose_prediction
- active_object_detection
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.18911v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (884 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HRP: Human Affordances for Robotic Pre-Training'
  url: https://arxiv.org/abs/2407.18911
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
HRP 旨在解决机器人视觉表征学习所需海量多样化训练数据难以通过真实机器人采集的问题。该工作利用互联网上的人类视频，借助现成的计算机视觉模块自动提取环境与智能体层面的可供性标签，包括接触点、未来手部姿态和主动物体边界框。这些标签通过仅微调 LayerNorm 层的 L2 回归损失蒸馏到任意现有的预训练视觉编码器中。实验表明，在 3000 多次真实机器人试验中，该可供性预训练方案在 5 个真实世界任务上至少提升了 15% 的性能，且适用于包括灵巧手在内的三种不同机器人形态和三种不同相机视角。

## 核心内容
### 方法
- **可供性提取**：从互联网规模的人类视频中，利用现成的计算机视觉模块自动提取三类可供性标签：
  - **接触点**：手与物体交互时的接触位置。
  - **未来手部姿态**：交互过程中手部的未来姿态。
  - **主动物体边界框**：与手部交互的物体的边界框。
- **蒸馏过程**：将提取的可供性标签通过 L2 回归损失蒸馏到预训练的视觉编码器中，仅微调 LayerNorm 层，保持其他参数不变。该方法可应用于任意现有的视觉表征。

### 实验设置
- **机器人试验**：在 5 个真实世界任务上进行了 3000 多次机器人试验。
- **机器人形态**：包括三种不同的机器人形态，其中包含一个灵巧手。
- **相机视角**：测试了三种不同的相机视角。
- **基线对比**：与现有方法进行对比，评估在分布外场景下的泛化能力。

### 关键结果
- **性能提升**：可供性预训练方案在所有任务上至少提升了 15% 的性能。
- **泛化能力**：在分布外设置下，HRP 表现出更高的泛化水平。
- **跨视角与形态**：与先前工作不同，HRP 在三种不同相机视角和三种机器人形态下均能提升性能。

### 结论
HRP 通过从人类视频中提取可供性并蒸馏到视觉编码器中，提供了一种高效且通用的机器人预训练方法。该方法无需额外机器人数据，即可显著提升机器人操作任务在多种场景下的泛化能力。代码、权重和数据已开源。

## Overview
In order to *generalize* to various tasks in the wild, robotic agents will need a suitable representation (i.e., vision network) that enables the robot to predict optimal actions given high dimensional vision inputs. However, learning such a representation requires an extreme amount of diverse training data, which is prohibitively expensive to collect on a real robot. How can we overcome this problem? Instead of collecting more robot data, this paper proposes using internet-scale, human videos to extract "affordances," both at the environment and agent level, and distill them into a pre-trained representation. We present a simple framework for pre-training representations on hand, object, and contact "affordance labels" that highlight relevant objects in images and how to interact with them. These affordances are automatically extracted from human video data (with the help of off-the-shelf computer vision modules) and used to fine-tune existing representations. Our approach can efficiently fine-tune *any* existing representation, and results in models with stronger downstream robotic performance across the board. We experimentally demonstrate (using 3000+ robot trials) that this affordance pre-training scheme boosts performance by a minimum of 15% on 5 real-world tasks, which consider three diverse robot morphologies (including a dexterous hand). Unlike prior works in the space, these representations improve performance across 3 different camera views. Quantitatively, we find that our approach leads to higher levels of generalization in out-of-distribution settings. For code, weights, and data check: https://hrp-robot.github.io

## 参考
- http://arxiv.org/abs/2407.18911v1

## 개요
HRP는 로봇 시각 표현 학습에 필요한 대규모의 다양한 훈련 데이터를 실제 로봇으로 수집하기 어려운 문제를 해결하는 것을 목표로 한다. 이 연구는 인터넷상의 인간 비디오를 활용하여, 기성 컴퓨터 비전 모듈을 통해 환경 및 에이전트 수준의 어포던스(affordance) 라벨을 자동으로 추출한다. 여기에는 접촉점, 미래 손姿态, 능동 객체 경계 상자가 포함된다. 이러한 라벨은 LayerNorm 레이어만 미세 조정하는 L2 회귀 손실을 통해 기존의 사전 훈련된 비전 인코더에 증류된다. 실험 결과, 3000회 이상의 실제 로봇 실험에서 이 어포던스 사전 훈련 방식은 5개의 실제 세계 작업에서 최소 15%의 성능 향상을 보였으며, 손재주가 뛰어난 손을 포함한 세 가지 다른 로봇 형태와 세 가지 다른 카메라 시점에 적용 가능하다.

## 핵심 내용
### 방법
- **어포던스 추출**: 인터넷 규모의 인간 비디오에서 기성 컴퓨터 비전 모듈을 활용하여 세 가지 유형의 어포던스 라벨을 자동으로 추출한다:
  - **접촉점**: 손과 객체가 상호작용할 때의 접촉 위치.
  - **미래 손姿态**: 상호작용 과정에서 손의 미래 자세.
  - **능동 객체 경계 상자**: 손과 상호작용하는 객체의 경계 상자.
- **증류 과정**: 추출된 어포던스 라벨을 L2 회귀 손실을 통해 사전 훈련된 비전 인코더에 증류하며, LayerNorm 레이어만 미세 조정하고 다른 매개변수는 유지한다. 이 방법은 기존의 모든 시각 표현에 적용할 수 있다.

### 실험 설정
- **로봇 실험**: 5개의 실제 세계 작업에서 3000회 이상의 로봇 실험을 수행했다.
- **로봇 형태**: 손재주가 뛰어난 손을 포함한 세 가지 다른 로봇 형태가 포함된다.
- **카메라 시점**: 세 가지 다른 카메라 시점을 테스트했다.
- **기준선 비교**: 기존 방법과 비교하여 분포 외(out-of-distribution) 시나리오에서의 일반화 능력을 평가했다.

### 주요 결과
- **성능 향상**: 어포던스 사전 훈련 방식은 모든 작업에서 최소 15%의 성능 향상을 보였다.
- **일반화 능력**: 분포 외 설정에서 HRP는 더 높은 일반화 수준을 나타냈다.
- **교차 시점 및 형태**: 이전 연구와 달리 HRP는 세 가지 다른 카메라 시점과 세 가지 로봇 형태 모두에서 성능을 향상시켰다.

### 결론
HRP는 인간 비디오에서 어포던스를 추출하고 비전 인코더에 증류함으로써 효율적이고 범용적인 로봇 사전 훈련 방법을 제공한다. 이 방법은 추가 로봇 데이터 없이도 다양한 시나리오에서 로봇 조작 작업의 일반화 능력을 크게 향상시킨다. 코드, 가중치 및 데이터는 오픈소스로 공개되어 있다.
