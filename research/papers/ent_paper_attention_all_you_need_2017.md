---
$id: ent_paper_attention_all_you_need_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Attention Is All You Need
  zh: Attention Is All You Need
  ko: Attention Is All You Need
summary:
  en: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder
    configuration. The best performing models also connect the encoder and decoder through an attention mechanism. Institutions
    per source list: Google Brain、Google Research.'
  zh: 本文由Google团队提出Transformer架构，完全基于注意力机制，摒弃了循环与卷积网络。在WMT 2014英德翻译任务上达到28.4 BLEU，英法翻译任务以41.8 BLEU创下新纪录，训练时间仅需3.5天（8 GPU）。该模型还成功泛化到英文成分句法分析任务。
  ko: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder
    configuration. The best performing models also connect the encoder and decoder through an attention mechanism. Institutions
    per source list: Google Brain、Google Research.'
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
- attention
- all
- you
- need
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 311 (.staging/ingest_yuanxq). Tier C->full. arXiv id 1706.03762 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (1706.03762v7); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:1706.03762 Attention Is All You Need
  url: https://arxiv.org/abs/1706.03762
  accessed_at: '2026-07-31'
  date: '2017-06-12'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

传统序列转导模型依赖编码器-解码器结构中的复杂循环或卷积网络，而最佳模型通常通过注意力机制连接编码器与解码器。本文提出的Transformer架构彻底摒弃了循环与卷积，仅依靠注意力机制构建网络。在机器翻译任务中，该模型不仅翻译质量更优，且具有更高的并行化能力与更短的训练时间。实验表明，Transformer在WMT 2014英德翻译任务上以28.4 BLEU超越此前最佳集成模型2 BLEU以上；在英法翻译任务上，仅用8块GPU训练3.5天便以41.8 BLEU刷新单模型最优记录。此外，该架构在英文成分句法分析任务中同样表现优异。

## 核心内容
### 核心架构创新
- **完全摒弃循环与卷积**：Transformer仅依赖自注意力（Self-Attention）和前馈神经网络，通过多头注意力（Multi-Head Attention）机制并行处理序列中所有位置的关系。
- **编码器-解码器结构**：编码器由6层相同子层组成，每层包含多头自注意力和位置全连接前馈网络；解码器同样为6层，额外引入掩码多头注意力防止未来信息泄露。
- **位置编码**：由于无循环结构，模型通过正弦/余弦函数生成位置编码，为每个位置注入相对或绝对位置信息。

### 关键实验设置
- **训练配置**：使用Adam优化器（β₁=0.9, β₂=0.98, ε=10⁻⁹），学习率采用预热策略（warmup_steps=4000）。正则化包含残差连接后的Dropout（rate=0.1）与标签平滑（ε=0.1）。
- **硬件与时间**：在8块NVIDIA P100 GPU上训练，英德任务耗时3.5天（100,000步），英法任务耗时3.5天（300,000步）。

### 核心结果
- **WMT 2014英德翻译**：单模型BLEU=28.4，超越此前最佳集成模型（27.3 BLEU）2.1分。
- **WMT 2014英法翻译**：单模型BLEU=41.8，训练成本仅为文献最佳模型的极小部分（此前最佳单模型需训练数周）。
- **成分句法分析**：在WSJ数据集上，Transformer在有限训练数据（仅WSJ训练集）和大规模数据（WSJ+半监督数据）下均达到与专用模型竞争的性能。

### 结论
Transformer证明了纯注意力机制在序列建模中的有效性，其并行化特性大幅降低训练时间，且无需领域特定架构即可迁移至其他NLP任务。该工作为后续BERT、GPT等预训练模型奠定了架构基础。

## Overview
The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## 参考
- https://arxiv.org/abs/1706.03762
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 시퀀스 변환 모델은 인코더-디코더 구조에서 복잡한 순환 또는 합성곱 네트워크에 의존했으며, 최적의 모델은 일반적으로 어텐션 메커니즘을 통해 인코더와 디코더를 연결했습니다. 본 논문에서 제안하는 Transformer 아키텍처는 순환과 합성곱을 완전히 배제하고 오직 어텐션 메커니즘만으로 네트워크를 구축합니다. 기계 번역 작업에서 이 모델은 번역 품질이 더 우수할 뿐만 아니라 병렬화 능력이 뛰어나고 훈련 시간이 더 짧습니다. 실험 결과, Transformer는 WMT 2014 영어-독일어 번역 작업에서 28.4 BLEU를 기록하며 이전 최고의 앙상블 모델을 2 BLEU 이상 능가했습니다. 영어-프랑스어 번역 작업에서는 8개의 GPU로 3.5일 동안 훈련하여 41.8 BLEU로 단일 모델 최고 기록을 갱신했습니다. 또한, 이 아키텍처는 영어 구성 성분 구문 분석 작업에서도 뛰어난 성능을 보였습니다.

## 핵심 내용
### 핵심 아키텍처 혁신
- **순환 및 합성곱 완전 배제**: Transformer는 오직 자기 어텐션(Self-Attention)과 피드포워드 신경망에 의존하며, 멀티헤드 어텐션(Multi-Head Attention) 메커니즘을 통해 시퀀스 내 모든 위치의 관계를 병렬로 처리합니다.
- **인코더-디코더 구조**: 인코더는 6개의 동일한 하위 레이어로 구성되며, 각 레이어는 멀티헤드 자기 어텐션과 위치별 완전 연결 피드포워드 네트워크를 포함합니다. 디코더도 6개의 레이어로 구성되며, 미래 정보 유출을 방지하기 위해 마스크된 멀티헤드 어텐션이 추가로 도입됩니다.
- **위치 인코딩**: 순환 구조가 없기 때문에 모델은 사인/코사인 함수를 통해 위치 인코딩을 생성하여 각 위치에 상대적 또는 절대적 위치 정보를 주입합니다.

### 주요 실험 설정
- **훈련 구성**: Adam 옵티마이저(β₁=0.9, β₂=0.98, ε=10⁻⁹)를 사용하고, 학습률은 웜업 전략(warmup_steps=4000)을 적용합니다. 정규화는 잔차 연결 후 드롭아웃(rate=0.1)과 레이블 스무딩(ε=0.1)을 포함합니다.
- **하드웨어 및 시간**: 8개의 NVIDIA P100 GPU에서 훈련하며, 영어-독일어 작업은 3.5일(100,000 스텝), 영어-프랑스어 작업은 3.5일(300,000 스텝)이 소요됩니다.

### 핵심 결과
- **WMT 2014 영어-독일어 번역**: 단일 모델 BLEU=28.4로, 이전 최고의 앙상블 모델(27.3 BLEU)을 2.1점 능가합니다.
- **WMT 2014 영어-프랑스어 번역**: 단일 모델 BLEU=41.8로, 훈련 비용은 기존 문헌의 최고 모델에 비해 극히 일부에 불과합니다(이전 최고 단일 모델은 수 주간 훈련 필요).
- **구성 성분 구문 분석**: WSJ 데이터셋에서 Transformer는 제한된 훈련 데이터(WSJ 훈련 세트만 사용)와 대규모 데이터(WSJ+반지도 데이터) 모두에서 전용 모델과 경쟁할 만한 성능을 달성합니다.

### 결론
Transformer는 순수 어텐션 메커니즘이 시퀀스 모델링에서 효과적임을 입증했으며, 병렬화 특성으로 훈련 시간을 크게 단축하고 도메인 특화 아키텍처 없이도 다른 NLP 작업으로 전이할 수 있습니다. 이 연구는 이후 BERT, GPT 등 사전 훈련 모델의 아키텍처 기반을 마련했습니다.
