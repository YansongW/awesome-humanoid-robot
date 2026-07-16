---
$id: ent_paper_brohan_rt_1_robotics_transformer_for_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-1: Robotics Transformer for Real-World Control at Scale'
  zh: RT-1
  ko: 'RT-1: Robotics Transformer for Real-World Control at Scale'
summary:
  en: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
  zh: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
  ko: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rt_1
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.06817v2.
sources:
- id: src_001
  type: website
  title: RT-1 source
  url: https://doi.org/10.15607/RSS.2023.XIX.025
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## 核心内容
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## 参考
- http://arxiv.org/abs/2212.06817v2

## Overview
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## Content
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## 개요
대규모의 다양하고 작업에 구애받지 않는 데이터셋에서 지식을 전이함으로써, 현대 머신러닝 모델은 특정 하위 작업을 제로샷(zero-shot) 또는 소규모 작업별 데이터셋만으로도 높은 성능 수준으로 해결할 수 있습니다. 이러한 능력은 컴퓨터 비전, 자연어 처리 또는 음성 인식과 같은 다른 분야에서는 입증되었지만, 실제 로봇 데이터 수집의 어려움으로 인해 모델의 일반화 능력이 특히 중요한 로보틱스 분야에서는 아직 입증되지 않았습니다. 우리는 이러한 일반 로봇 모델의 성공 열쇠 중 하나가 개방형 작업에 구애받지 않는 훈련과 모든 다양한 로봇 데이터를 흡수할 수 있는 고용량 아키텍처의 결합에 있다고 주장합니다. 본 논문에서는 유망한 확장 가능한 모델 속성을 보여주는 Robotics Transformer라는 모델 클래스를 제시합니다. 우리는 실제 로봇이 실제 작업을 수행하는 대규모 데이터 수집을 기반으로, 데이터 크기, 모델 크기 및 데이터 다양성의 함수로서 일반화 능력을 연구한 다양한 모델 클래스 연구를 통해 결론을 검증합니다. 프로젝트 웹사이트와 비디오는 robotics-transformer1.github.io에서 확인할 수 있습니다.

## 핵심 내용
대규모의 다양하고 작업에 구애받지 않는 데이터셋에서 지식을 전이함으로써, 현대 머신러닝 모델은 특정 하위 작업을 제로샷(zero-shot) 또는 소규모 작업별 데이터셋만으로도 높은 성능 수준으로 해결할 수 있습니다. 이러한 능력은 컴퓨터 비전, 자연어 처리 또는 음성 인식과 같은 다른 분야에서는 입증되었지만, 실제 로봇 데이터 수집의 어려움으로 인해 모델의 일반화 능력이 특히 중요한 로보틱스 분야에서는 아직 입증되지 않았습니다. 우리는 이러한 일반 로봇 모델의 성공 열쇠 중 하나가 개방형 작업에 구애받지 않는 훈련과 모든 다양한 로봇 데이터를 흡수할 수 있는 고용량 아키텍처의 결합에 있다고 주장합니다. 본 논문에서는 유망한 확장 가능한 모델 속성을 보여주는 Robotics Transformer라는 모델 클래스를 제시합니다. 우리는 실제 로봇이 실제 작업을 수행하는 대규모 데이터 수집을 기반으로, 데이터 크기, 모델 크기 및 데이터 다양성의 함수로서 일반화 능력을 연구한 다양한 모델 클래스 연구를 통해 결론을 검증합니다. 프로젝트 웹사이트와 비디오는 robotics-transformer1.github.io에서 확인할 수 있습니다.
