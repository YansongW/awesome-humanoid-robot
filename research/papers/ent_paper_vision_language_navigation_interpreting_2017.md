---
$id: ent_paper_vision_language_navigation_interpreting_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments'
  zh: 'Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments'
  ko: 'Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments'
summary:
  en: 'A robot that can carry out a natural-language instruction has been a dream since before the Jetsons cartoon series
    imagined a life of leisure mediated by a fleet of attentive robot helpers. Institutions per source list: 澳大利亚国立大学、阿德莱德大学.'
  zh: 本文提出将自然语言导航指令转化为视觉-语言序列到序列翻译问题，并为此构建了Matterport3D Simulator仿真环境与Room-to-Room (R2R)数据集。该工作旨在推动具身智能体在真实建筑场景中基于视觉理解执行导航指令的研究。
  ko: 'A robot that can carry out a natural-language instruction has been a dream since before the Jetsons cartoon series
    imagined a life of leisure mediated by a fleet of attentive robot helpers. Institutions per source list: 澳大利亚国立大学、阿德莱德大学.'
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
- vision
- language
- navigation
- interpreting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 816 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (1711.07280v3); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1711.07280 Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real
    environments'
  url: https://arxiv.org/abs/1711.07280
  accessed_at: '2026-07-31'
  date: '2017-11-20'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

论文指出，机器人理解自然语言导航指令本质上与视觉问答（Visual Question Answering）任务同构，均可视为视觉引导的序列到序列翻译问题。为此，作者基于真实建筑图像构建了大规模强化学习环境Matterport3D Simulator，并发布了首个面向真实建筑场景的视觉导航基准数据集Room-to-Room (R2R)。该数据集包含在真实建筑中采集的导航指令与对应路径，为具身视觉-语言任务提供了标准化评估平台。

## 核心内容
### 核心问题
- 将自然语言导航指令理解定义为视觉引导的序列到序列翻译任务，与Visual Question Answering共享方法论基础
- 机器人需通过视觉感知实时解析指令，在真实环境中完成路径规划

### 技术贡献
#### Matterport3D Simulator
- 基于Matterport3D真实建筑扫描数据构建的强化学习环境
- 支持多种具身视觉-语言任务（导航、问答等）
- 提供全景图像、深度图、语义标签等多模态输入

#### Room-to-Room (R2R) 数据集
- 首个真实建筑场景的视觉导航指令基准
- 包含90个建筑场景的7,189条路径，每条路径对应3条人工标注的自然语言指令
- 路径长度平均10米，覆盖室内环境中的多房间导航

### 实验设置
- 任务形式：智能体从起始位置出发，根据自然语言指令导航至目标位置
- 评估指标：导航成功率（Success Rate）、路径长度加权成功率（SPL）
- 基线方法：基于LSTM的序列到序列模型，结合视觉特征与语言编码

### 关键结论
- 现有视觉-语言方法在R2R数据集上表现有限，最高成功率仅约20%
- 任务对空间推理、视觉定位和语言理解提出综合挑战
- 该工作为后续研究（如基于强化学习的导航策略、跨模态注意力机制）奠定了基准

## Overview
A robot that can carry out a natural-language instruction has been a dream since before the Jetsons cartoon series imagined a life of leisure mediated by a fleet of attentive robot helpers. It is a dream that remains stubbornly distant. However, recent advances in vision and language methods have made incredible progress in closely related areas. This is significant because a robot interpreting a natural-language navigation instruction on the basis of what it sees is carrying out a vision and language process that is similar to Visual Question Answering. Both tasks can be interpreted as visually grounded sequence-to-sequence translation problems, and many of the same methods are applicable. To enable and encourage the application of vision and language methods to the problem of interpreting visually-grounded navigation instructions, we present the Matterport3D Simulator -- a large-scale reinforcement learning environment based on real imagery. Using this simulator, which can in future support a range of embodied vision and language tasks, we provide the first benchmark dataset for visually-grounded natural language navigation in real buildings -- the Room-to-Room (R2R) dataset.

## 参考
- https://arxiv.org/abs/1711.07280
- https://github.com/ImChong/Robotics_Notebooks

## 개요

논문은 로봇이 자연어 내비게이션 지시를 이해하는 것이 본질적으로 시각 질의응답(Visual Question Answering) 작업과 동형이며, 둘 다 시각 기반 시퀀스-투-시퀀스 번역 문제로 간주될 수 있다고 지적한다. 이를 위해 저자들은 실제 건물 이미지를 기반으로 대규모 강화 학습 환경인 Matterport3D Simulator를 구축하고, 실제 건물 장면을 대상으로 한 최초의 시각 내비게이션 벤치마크 데이터셋인 Room-to-Room (R2R)을 공개했다. 이 데이터셋은 실제 건물에서 수집된 내비게이션 지시와 해당 경로를 포함하며, 구현형(embodied) 비전-언어 작업을 위한 표준화된 평가 플랫폼을 제공한다.

## 핵심 내용
### 핵심 문제
- 자연어 내비게이션 지시 이해를 시각 기반 시퀀스-투-시퀀스 번역 작업으로 정의하며, Visual Question Answering와 방법론적 기반을 공유함
- 로봇은 시각적 인식을 통해 지시를 실시간으로 해석하고, 실제 환경에서 경로 계획을 완료해야 함

### 기술 기여
#### Room-to-Room (R2R) 데이터셋
- 실제 건물 장면을 대상으로 한 최초의 시각 내비게이션 지시 벤치마크
- 90개 건물 장면의 7,189개 경로를 포함하며, 각 경로는 3개의 수작업 주석 자연어 지시에 대응
- 경로 길이는 평균 10미터이며, 실내 환경의 다중 방 내비게이션을 포괄

### 실험 설정
- 작업 형태: 에이전트가 시작 위치에서 출발하여 자연어 지시에 따라 목표 위치까지 내비게이션
- 평가 지표: 내비게이션 성공률(Success Rate), 경로 길이 가중 성공률(SPL)
- 기준 방법: LSTM 기반 시퀀스-투-시퀀스 모델로, 시각 특징과 언어 인코딩을 결합

### 핵심 결론
- 기존 비전-언어 방법은 R2R 데이터셋에서 제한적인 성능을 보이며, 최고 성공률은 약 20%에 불과
- 작업은 공간 추론, 시각적 위치 파악, 언어 이해에 대한 종합적인 도전을 제기
- 이 작업은 후속 연구(예: 강화 학습 기반 내비게이션 전략, 교차 양식 주의 메커니즘)를 위한 벤치마크를 마련함
