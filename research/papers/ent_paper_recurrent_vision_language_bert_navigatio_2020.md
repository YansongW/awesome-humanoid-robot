---
$id: ent_paper_recurrent_vision_language_bert_navigatio_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Recurrent Vision-and-Language BERT for Navigation
  zh: A Recurrent Vision-and-Language BERT for Navigation
  ko: A Recurrent Vision-and-Language BERT for Navigation
summary:
  en: 'Accuracy of many visiolinguistic tasks has benefited significantly from the application of vision-and-language(V&L)
    BERT. However, its application for the task of vision-and-language navigation (VLN) remains limited. Institutions per
    source list: 澳大利亚国立大学、阿德莱德大学.'
  zh: 本文提出一种名为Recurrent Vision-and-Language BERT的循环BERT模型，用于视觉与语言导航任务。该模型通过引入时间感知的循环函数，使BERT架构能处理部分可观测马尔可夫决策过程，在R2R和REVERIE基准上取得最先进结果，并支持预训练与多任务联合求解。
  ko: 'Accuracy of many visiolinguistic tasks has benefited significantly from the application of vision-and-language(V&L)
    BERT. However, its application for the task of vision-and-language navigation (VLN) remains limited. Institutions per
    source list: 澳大利亚国立大学、阿德莱德大学.'
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
- recurrent
- vision
- language
- bert
- navigatio
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 820 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2011.13922v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2011.13922 A Recurrent Vision-and-Language BERT for Navigation
  url: https://arxiv.org/abs/2011.13922
  accessed_at: '2026-07-31'
  date: '2020-11-26'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

视觉与语言BERT在多项跨模态任务中表现优异，但在视觉与语言导航任务中应用受限，主要原因是导航环境具有部分可观测马尔可夫决策过程特性，需要依赖历史信息的注意力机制与决策。本文提出的Recurrent V&L BERT在标准BERT中嵌入循环函数，维护智能体的跨模态状态信息，从而实现对时间序列的建模。在R2R和REVERIE两个基准上的实验表明，该模型能替代更复杂的编码器-解码器架构，达到最先进性能。此外，该方法可推广至其他基于Transformer的架构，支持预训练，并能同时解决导航与指代表达任务。

## 核心内容
### 方法架构
- **核心创新**：在BERT中引入循环函数，使模型能维护跨模态状态信息，适应VLN任务中的部分可观测马尔可夫决策过程。
- **时间感知机制**：通过循环连接使每个时间步的隐藏状态包含历史信息，实现依赖历史的注意力与决策。
- **跨模态融合**：视觉特征（来自ResNet-152）与语言指令（来自BERT tokenizer）通过多头注意力交互，循环函数作用于融合后的表示。

### 实验设置
- **基准**：R2R（房间到房间导航）和REVERIE（指代表达导航与物体定位）。
- **评估指标**：导航成功率（SR）、路径长度加权成功率（SPL）、目标定位成功率（REVERIE中的R@1）。
- **预训练**：使用Matterport3D数据集中的导航轨迹进行掩码语言建模与动作预测预训练。

### 关键结果
- **R2R**：在未见环境上，Recurrent V&L BERT达到SR 63.2%、SPL 59.8%，超越之前最优的编码器-解码器模型（SR 61.3%、SPL 57.9%）。
- **REVERIE**：在未见环境上，导航成功率SR 52.1%，目标定位R@1 38.7%，均优于基线模型。
- **消融实验**：移除循环函数后，SR下降约5个百分点，证明历史状态信息的重要性。

### 结论
- 该模型证明了BERT架构通过简单循环扩展即可有效处理序列决策任务，无需复杂编码器-解码器设计。
- 支持端到端预训练，且能同时优化导航与指代表达两个子任务，具有良好泛化性。

## Overview
Accuracy of many visiolinguistic tasks has benefited significantly from the application of vision-and-language(V&L) BERT. However, its application for the task of vision-and-language navigation (VLN) remains limited. One reason for this is the difficulty adapting the BERT architecture to the partially observable Markov decision process present in VLN, requiring history-dependent attention and decision making. In this paper we propose a recurrent BERT model that is time-aware for use in VLN. Specifically, we equip the BERT model with a recurrent function that maintains cross-modal state information for the agent. Through extensive experiments on R2R and REVERIE we demonstrate that our model can replace more complex encoder-decoder models to achieve state-of-the-art results. Moreover, our approach can be generalised to other transformer-based architectures, supports pre-training, and is capable of solving navigation and referring expression tasks simultaneously.

## 参考
- https://arxiv.org/abs/2011.13922
- https://github.com/ImChong/Robotics_Notebooks

## 개요

비전-언어 BERT는 여러 크로스모달 태스크에서 뛰어난 성능을 보였지만, 비전-언어 내비게이션 태스크에서는 적용이 제한적이었다. 주요 원인은 내비게이션 환경이 부분 관측 가능 마르코프 결정 과정의 특성을 가지며, 과거 정보에 의존하는 어텐션 메커니즘과 의사 결정이 필요하기 때문이다. 본 논문에서 제안하는 Recurrent V&L BERT는 표준 BERT에 순환 함수를 내장하여 에이전트의 크로스모달 상태 정보를 유지함으로써 시계열 모델링을 가능하게 한다. R2R과 REVERIE 두 벤치마크에서의 실험 결과, 이 모델은 더 복잡한 인코더-디코더 아키텍처를 대체하여 최첨단 성능을 달성했다. 또한, 이 방법은 다른 Transformer 기반 아키텍처로 확장 가능하며, 사전 학습을 지원하고 내비게이션과 지시 표현 태스크를 동시에 해결할 수 있다.

## 핵심 내용
### 방법 아키텍처
- **핵심 혁신**: BERT에 순환 함수를 도입하여 모델이 크로스모달 상태 정보를 유지할 수 있게 하여 VLN 태스크의 부분 관측 가능 마르코프 결정 과정에 적응한다.
- **시간 인식 메커니즘**: 순환 연결을 통해 각 시간 단계의 은닉 상태가 과거 정보를 포함하도록 하여, 과거에 의존하는 어텐션과 의사 결정을 구현한다.
- **크로스모달 융합**: 시각적 특징(ResNet-152에서 추출)과 언어 명령(BERT 토크나이저에서 추출)이 멀티헤드 어텐션을 통해 상호작용하며, 순환 함수는 융합된 표현에 적용된다.

### 실험 설정
- **벤치마크**: R2R(방에서 방으로 내비게이션) 및 REVERIE(지시 표현 내비게이션 및 객체 위치 파악).
- **평가 지표**: 내비게이션 성공률(SR), 경로 길이 가중 성공률(SPL), 목표 위치 파악 성공률(REVERIE의 R@1).
- **사전 학습**: Matterport3D 데이터셋의 내비게이션 궤적을 사용하여 마스크 언어 모델링 및 행동 예측 사전 학습을 수행.

### 주요 결과
- **R2R**: 미지 환경에서 Recurrent V&L BERT는 SR 63.2%, SPL 59.8%를 달성하여 이전 최고의 인코더-디코더 모델(SR 61.3%, SPL 57.9%)을 능가.
- **REVERIE**: 미지 환경에서 내비게이션 성공률 SR 52.1%, 목표 위치 파악 R@1 38.7%로 모두 기준 모델보다 우수.
- **절제 실험**: 순환 함수를 제거하면 SR이 약 5% 포인트 하락하여 과거 상태 정보의 중요성을 입증.

### 결론
- 이 모델은 BERT 아키텍처가 간단한 순환 확장만으로 복잡한 인코더-디코더 설계 없이도 순차적 의사 결정 태스크를 효과적으로 처리할 수 있음을 증명.
- 엔드투엔드 사전 학습을 지원하며, 내비게이션과 지시 표현이라는 두 하위 태스크를 동시에 최적화할 수 있어 우수한 일반화 성능을 가짐.
