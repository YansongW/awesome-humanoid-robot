---
$id: ent_paper_toyoda_embodying_pre_trained_word_emb_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodying pre-trained word embeddings through robot actions
  zh: 通过机器人动作实现预训练词嵌入的身体化
  ko: 로봇 행동을 통한 사전 학습 단어 임베딩의 구현
summary:
  en: This paper proposes rPRAE, a seq2seq model that retrofits pre-trained Word2Vec embeddings into robot sensory-motor grounded
    representations, enabling a NAO humanoid to bidirectionally translate between manipulation actions and linguistic descriptions
    including unseen words.
  zh: 本文提出 rPRAE，一个 seq2seq 模型，将预训练的 Word2Vec 嵌入改造为机器人感觉运动接地表示，使 NAO 人形机器人能够在操作动作与语言描述（包括未见过的词汇）之间进行双向翻译。核心贡献在于通过交替训练改造层与双向翻译模型，将分布假设下纯文本训练的嵌入转化为基于机器人自身感觉运动经验的接地表示。
  ko: 본 논문은 사전 학습된 Word2Vec 임베딩을 로봇의 감각운동 경험에 기반한 표현으로 변환하는 rPRAE 모델을 제안하여, NAO 휴머노이드 로봇이 조작 행동과 보지 못한 단어를 포함한 언어 설명 간 양방향
    변환을 수행할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vision_language_action
- word_embedding_retrofitting
- nao_robot
- human_robot_interaction
- seq2seq
- bidirectional_translation
- grounded_language_learning
- manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.08521v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Embodying pre-trained word embeddings through robot actions
  url: https://arxiv.org/abs/2104.08521
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对机器人需处理多义词等复杂语言表达的需求，现有方法虽能利用预训练词嵌入处理未配对词汇，但分布假设下的嵌入缺乏接地性。本文提出的 rPRAE 模型通过引入非线性层改造预训练词嵌入，并采用交替训练策略，使嵌入适应动作-描述配对数据集。实验表明，改造后的嵌入能根据机器人实际动作与环境经验形成同义词语义聚类，使机器人能对未见过的词汇生成恰当动作。

## 核心内容
### 方法架构
- **核心模型**：rPRAE 基于 seq2seq 架构，扩展了动作与描述的双向翻译模型。
- **嵌入改造**：在模型中插入非线性层（retrofit layer），将预训练的 Word2Vec 嵌入映射为接地表示。
- **训练策略**：交替训练改造层与双向翻译模型，使嵌入逐步适应动作-描述配对数据集。

### 实验设置
- **机器人平台**：NAO 人形机器人
- **数据集**：包含操作动作与对应语言描述的配对数据
- **预训练嵌入**：使用 Word2Vec 在文本语料上预训练的嵌入

### 关键结果
- **语义聚类**：改造后的嵌入中，同义词根据机器人实际动作与环境经验形成语义聚类。
- **泛化能力**：机器人能对数据集中未与动作配对的未见词汇生成恰当动作。
- **多义词处理**：模型能正确响应包含多义词的多种语言表达。

### 结论
rPRAE 通过将预训练词嵌入与机器人感觉运动经验结合，成功实现了语言与动作的接地双向翻译，为机器人语言交互中的词汇泛化问题提供了有效解决方案。

## Overview
We propose a promising neural network model with which to acquire a grounded representation of robot actions and the linguistic descriptions thereof. Properly responding to various linguistic expressions, including polysemous words, is an important ability for robots that interact with people via linguistic dialogue. Previous studies have shown that robots can use words that are not included in the action-description paired datasets by using pre-trained word embeddings. However, the word embeddings trained under the distributional hypothesis are not grounded, as they are derived purely from a text corpus. In this letter, we transform the pre-trained word embeddings to embodied ones by using the robot's sensory-motor experiences. We extend a bidirectional translation model for actions and descriptions by incorporating non-linear layers that retrofit the word embeddings. By training the retrofit layer and the bidirectional translation model alternately, our proposed model is able to transform the pre-trained word embeddings to adapt to a paired action-description dataset. Our results demonstrate that the embeddings of synonyms form a semantic cluster by reflecting the experiences (actions and environments) of a robot. These embeddings allow the robot to properly generate actions from unseen words that are not paired with actions in a dataset.

## 개요
우리는 로봇 동작과 이에 대한 언어적 설명의 기반 표현을 획득하기 위한 유망한 신경망 모델을 제안합니다. 다의어를 포함한 다양한 언어 표현에 적절히 대응하는 것은 언어적 대화를 통해 사람과 상호작용하는 로봇에게 중요한 능력입니다. 이전 연구들은 사전 훈련된 단어 임베딩을 사용함으로써 로봇이 동작-설명 쌍 데이터셋에 포함되지 않은 단어도 사용할 수 있음을 보여주었습니다. 그러나 분포 가설 하에 훈련된 단어 임베딩은 순수하게 텍스트 코퍼스에서 도출되었기 때문에 기반을 갖추지 못했습니다. 본 논문에서는 로봇의 감각-운동 경험을 활용하여 사전 훈련된 단어 임베딩을 체화된 임베딩으로 변환합니다. 우리는 단어 임베딩을 개조하는 비선형 레이어를 통합하여 동작과 설명을 위한 양방향 번역 모델을 확장합니다. 개조 레이어와 양방향 번역 모델을 번갈아 훈련함으로써, 제안된 모델은 사전 훈련된 단어 임베딩을 변환하여 동작-설명 쌍 데이터셋에 적응시킬 수 있습니다. 실험 결과는 동의어의 임베딩이 로봇의 경험(동작 및 환경)을 반영하여 의미적 군집을 형성함을 보여줍니다. 이러한 임베딩을 통해 로봇은 데이터셋에서 동작과 쌍을 이루지 않은 미지의 단어로부터도 적절히 동작을 생성할 수 있습니다.

## 핵심 내용
우리는 로봇 동작과 이에 대한 언어적 설명의 기반 표현을 획득하기 위한 유망한 신경망 모델을 제안합니다. 다의어를 포함한 다양한 언어 표현에 적절히 대응하는 것은 언어적 대화를 통해 사람과 상호작용하는 로봇에게 중요한 능력입니다. 이전 연구들은 사전 훈련된 단어 임베딩을 사용함으로써 로봇이 동작-설명 쌍 데이터셋에 포함되지 않은 단어도 사용할 수 있음을 보여주었습니다. 그러나 분포 가설 하에 훈련된 단어 임베딩은 순수하게 텍스트 코퍼스에서 도출되었기 때문에 기반을 갖추지 못했습니다. 본 논문에서는 로봇의 감각-운동 경험을 활용하여 사전 훈련된 단어 임베딩을 체화된 임베딩으로 변환합니다. 우리는 단어 임베딩을 개조하는 비선형 레이어를 통합하여 동작과 설명을 위한 양방향 번역 모델을 확장합니다. 개조 레이어와 양방향 번역 모델을 번갈아 훈련함으로써, 제안된 모델은 사전 훈련된 단어 임베딩을 변환하여 동작-설명 쌍 데이터셋에 적응시킬 수 있습니다. 실험 결과는 동의어의 임베딩이 로봇의 경험(동작 및 환경)을 반영하여 의미적 군집을 형성함을 보여줍니다. 이러한 임베딩을 통해 로봇은 데이터셋에서 동작과 쌍을 이루지 않은 미지의 단어로부터도 적절히 동작을 생성할 수 있습니다.

## 参考
- http://arxiv.org/abs/2104.08521v1
