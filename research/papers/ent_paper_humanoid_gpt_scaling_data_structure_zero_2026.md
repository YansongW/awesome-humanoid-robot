---
$id: ent_paper_humanoid_gpt_scaling_data_structure_zero_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking'
  zh: 亿帧数据驱动的人形零样本动作跟踪
  ko: 'Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking'
summary:
  en: 'We introduce Humanoid-GPT, a GPT-style Transformer with causal attention trained on a billion-scale motion corpus for
    whole-body control. Unlike prior shallow MLP trackers constrained by scarce data and an agility-generalization trade-off,
    Humanoid-GPT is pre-trained on a 2B-frame retargeted corpus that unifies all major mocap datasets with large-scale in-house
    recordings. Institutions per source list: 清华大学、银河通用、上海交大、北京大学、上海期智研究院.'
  zh: Humanoid-GPT 是一个基于因果注意力的 GPT 风格 Transformer 模型，由研究团队在十亿级运动语料上预训练，用于全身控制。其核心贡献在于通过扩展数据（20亿帧重定向语料）和模型容量，实现了对高度动态行为的零样本运动跟踪，并展现出前所未有的泛化能力。
  ko: 'We introduce Humanoid-GPT, a GPT-style Transformer with causal attention trained on a billion-scale motion corpus for
    whole-body control. Unlike prior shallow MLP trackers constrained by scarce data and an agility-generalization trade-off,
    Humanoid-GPT is pre-trained on a 2B-frame retargeted corpus that unifies all major mocap datasets with large-scale in-house
    recordings. Institutions per source list: 清华大学、银河通用、上海交大、北京大学、上海期智研究院.'
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
- humanoid
- gpt
- scaling
- data
- structure
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 29 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.03985 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.03985v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.03985 Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking'
  url: https://arxiv.org/abs/2606.03985
  accessed_at: '2026-07-31'
  date: '2026-06-02'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/GalaxyGeneralRobotics/Humanoid-GPT/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/GalaxyGeneralRobotics/Humanoid-GPT/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

Humanoid-GPT 旨在解决传统浅层 MLP 跟踪器因数据稀缺和敏捷性-泛化权衡而受限的问题。该模型在统一了所有主要动作捕捉数据集和大规模内部录制的 20 亿帧重定向语料上进行预训练。通过同时扩展数据和模型规模，Humanoid-GPT 作为一个单一的生成式 Transformer，能够跟踪高度动态的行为，并在未见过的运动和任务上实现零样本泛化。广泛的实验和缩放分析表明，该模型建立了新的性能前沿。

## 核心内容
### 方法
- **模型架构**：Humanoid-GPT 采用 GPT 风格的 Transformer 架构，使用因果注意力机制，专为序列生成任务设计。
- **预训练数据**：构建了一个包含 20 亿帧的重定向运动语料库，该语料库统一了所有主要动作捕捉数据集（如 CMU、AMASS 等）并加入了大规模内部录制数据，解决了数据稀缺问题。
- **训练策略**：采用自回归方式预训练模型，使其学习运动序列的生成分布，从而具备零样本跟踪能力。

### 实验设置
- **任务**：零样本运动跟踪，即模型在训练时未见过的运动序列和任务上进行测试。
- **对比基线**：与传统的浅层 MLP 跟踪器进行对比，这些跟踪器通常受限于数据量和敏捷性-泛化权衡。
- **评估指标**：使用跟踪精度、运动自然度等标准指标，并进行了缩放分析以验证数据量和模型容量对性能的影响。

### 关键结果
- **性能前沿**：Humanoid-GPT 在零样本泛化到未见任务的同时，能够跟踪高度动态和复杂的运动，建立了新的性能标准。
- **缩放分析**：实验表明，同时增加数据量和模型容量能持续提升性能，验证了扩展策略的有效性。
- **泛化能力**：模型在未见过的运动类型和控制任务上表现出鲁棒的零样本泛化能力，超越了先前方法。

### 结论
Humanoid-GPT 通过大规模预训练和模型扩展，成功解决了运动跟踪中的敏捷性-泛化权衡问题，为全身控制任务提供了一种高效的零样本解决方案。

## Overview
We introduce Humanoid-GPT, a GPT-style Transformer with causal attention trained on a billion-scale motion corpus for whole-body control. Unlike prior shallow MLP trackers constrained by scarce data and an agility-generalization trade-off, Humanoid-GPT is pre-trained on a 2B-frame retargeted corpus that unifies all major mocap datasets with large-scale in-house recordings. Scaling both data and model capacity yields a single generative Transformer that tracks highly dynamic behaviors while achieving unprecedented zero-shot generalization to unseen motions and control tasks. Extensive experiments and scaling analyses show that our model establishes a new performance frontier, demonstrating robust zero-shot generalization to unseen tasks while simultaneously tracking highly dynamic and complex motions.

## 参考
- https://arxiv.org/abs/2606.03985
- https://github.com/GalaxyGeneralRobotics/Humanoid-GPT/
- https://raw.githubusercontent.com/GalaxyGeneralRobotics/Humanoid-GPT/HEAD/README.md
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

Humanoid-GPT는 데이터 부족과 민첩성-일반화 간의 트레이드오프로 인해 제한되는 기존의 얕은 MLP 트래커의 문제를 해결하는 것을 목표로 합니다. 이 모델은 모든 주요 모션 캡처 데이터셋과 대규모 내부 녹화 데이터를 통합한 20억 프레임의 리타겟팅 코퍼스에서 사전 학습됩니다. 데이터와 모델 규모를 동시에 확장함으로써, Humanoid-GPT는 단일 생성형 Transformer로서 고도로 동적인 동작을 추적하고, 보지 못한 동작과 작업에 대해 제로샷 일반화를 달성합니다. 광범위한 실험과 스케일링 분석은 이 모델이 새로운 성능 최전선을 구축했음을 보여줍니다.

## 핵심 내용
### 방법
- **모델 아키텍처**: Humanoid-GPT는 GPT 스타일의 Transformer 아키텍처를 채택하며, 인과적 어텐션 메커니즘을 사용하여 시퀀스 생성 작업에 특화되어 설계되었습니다.
- **사전 학습 데이터**: CMU, AMASS 등 모든 주요 모션 캡처 데이터셋을 통합하고 대규모 내부 녹화 데이터를 추가한 20억 프레임의 리타겟팅 모션 코퍼스를 구축하여 데이터 부족 문제를 해결했습니다.
- **훈련 전략**: 모델을 자기회귀 방식으로 사전 학습하여 모션 시퀀스의 생성 분포를 학습하게 함으로써 제로샷 추적 능력을 갖추게 합니다.

### 실험 설정
- **작업**: 제로샷 모션 추적, 즉 모델이 훈련 중에 보지 못한 모션 시퀀스와 작업에서 테스트됩니다.
- **비교 기준**: 일반적으로 데이터 양과 민첩성-일반화 트레이드오프에 제한되는 기존의 얕은 MLP 트래커와 비교합니다.
- **평가 지표**: 추적 정밀도, 모션 자연스러움 등의 표준 지표를 사용하며, 데이터 양과 모델 용량이 성능에 미치는 영향을 검증하기 위해 스케일링 분석을 수행했습니다.

### 주요 결과
- **성능 최전선**: Humanoid-GPT는 보지 못한 작업에 대한 제로샷 일반화를 달성하면서도 고도로 동적이고 복잡한 동작을 추적하여 새로운 성능 기준을 세웠습니다.
- **스케일링 분석**: 실험 결과, 데이터 양과 모델 용량을 동시에 증가시키면 성능이 지속적으로 향상되어 확장 전략의 효과가 입증되었습니다.
- **일반화 능력**: 모델은 보지 못한 동작 유형과 제어 작업에서 강력한 제로샷 일반화 능력을 보여주며, 이전 방법을 능가했습니다.

### 결론
Humanoid-GPT는 대규모 사전 학습과 모델 확장을 통해 모션 추적에서의 민첩성-일반화 트레이드오프 문제를 성공적으로 해결하여, 전신 제어 작업에 효율적인 제로샷 솔루션을 제공합니다.
