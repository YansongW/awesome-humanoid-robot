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
  zh: 本文提出rPRAE模型，通过将预训练Word2Vec词嵌入改造为基于机器人感知运动经验的表征，使NAO人形机器人能够在操作动作与包含未见词汇的语言描述之间进行双向转换。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.08521v1.
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
We propose a promising neural network model with which to acquire a grounded representation of robot actions and the linguistic descriptions thereof. Properly responding to various linguistic expressions, including polysemous words, is an important ability for robots that interact with people via linguistic dialogue. Previous studies have shown that robots can use words that are not included in the action-description paired datasets by using pre-trained word embeddings. However, the word embeddings trained under the distributional hypothesis are not grounded, as they are derived purely from a text corpus. In this letter, we transform the pre-trained word embeddings to embodied ones by using the robot's sensory-motor experiences. We extend a bidirectional translation model for actions and descriptions by incorporating non-linear layers that retrofit the word embeddings. By training the retrofit layer and the bidirectional translation model alternately, our proposed model is able to transform the pre-trained word embeddings to adapt to a paired action-description dataset. Our results demonstrate that the embeddings of synonyms form a semantic cluster by reflecting the experiences (actions and environments) of a robot. These embeddings allow the robot to properly generate actions from unseen words that are not paired with actions in a dataset.

## 核心内容
We propose a promising neural network model with which to acquire a grounded representation of robot actions and the linguistic descriptions thereof. Properly responding to various linguistic expressions, including polysemous words, is an important ability for robots that interact with people via linguistic dialogue. Previous studies have shown that robots can use words that are not included in the action-description paired datasets by using pre-trained word embeddings. However, the word embeddings trained under the distributional hypothesis are not grounded, as they are derived purely from a text corpus. In this letter, we transform the pre-trained word embeddings to embodied ones by using the robot's sensory-motor experiences. We extend a bidirectional translation model for actions and descriptions by incorporating non-linear layers that retrofit the word embeddings. By training the retrofit layer and the bidirectional translation model alternately, our proposed model is able to transform the pre-trained word embeddings to adapt to a paired action-description dataset. Our results demonstrate that the embeddings of synonyms form a semantic cluster by reflecting the experiences (actions and environments) of a robot. These embeddings allow the robot to properly generate actions from unseen words that are not paired with actions in a dataset.

## 参考
- http://arxiv.org/abs/2104.08521v1

## Overview
We propose a promising neural network model with which to acquire a grounded representation of robot actions and the linguistic descriptions thereof. Properly responding to various linguistic expressions, including polysemous words, is an important ability for robots that interact with people via linguistic dialogue. Previous studies have shown that robots can use words that are not included in the action-description paired datasets by using pre-trained word embeddings. However, the word embeddings trained under the distributional hypothesis are not grounded, as they are derived purely from a text corpus. In this letter, we transform the pre-trained word embeddings to embodied ones by using the robot's sensory-motor experiences. We extend a bidirectional translation model for actions and descriptions by incorporating non-linear layers that retrofit the word embeddings. By training the retrofit layer and the bidirectional translation model alternately, our proposed model is able to transform the pre-trained word embeddings to adapt to a paired action-description dataset. Our results demonstrate that the embeddings of synonyms form a semantic cluster by reflecting the experiences (actions and environments) of a robot. These embeddings allow the robot to properly generate actions from unseen words that are not paired with actions in a dataset.

## Content
We propose a promising neural network model with which to acquire a grounded representation of robot actions and the linguistic descriptions thereof. Properly responding to various linguistic expressions, including polysemous words, is an important ability for robots that interact with people via linguistic dialogue. Previous studies have shown that robots can use words that are not included in the action-description paired datasets by using pre-trained word embeddings. However, the word embeddings trained under the distributional hypothesis are not grounded, as they are derived purely from a text corpus. In this letter, we transform the pre-trained word embeddings to embodied ones by using the robot's sensory-motor experiences. We extend a bidirectional translation model for actions and descriptions by incorporating non-linear layers that retrofit the word embeddings. By training the retrofit layer and the bidirectional translation model alternately, our proposed model is able to transform the pre-trained word embeddings to adapt to a paired action-description dataset. Our results demonstrate that the embeddings of synonyms form a semantic cluster by reflecting the experiences (actions and environments) of a robot. These embeddings allow the robot to properly generate actions from unseen words that are not paired with actions in a dataset.

## 개요
우리는 로봇 동작과 이에 대한 언어적 설명의 기반 표현을 획득하기 위한 유망한 신경망 모델을 제안합니다. 다의어를 포함한 다양한 언어 표현에 적절히 대응하는 것은 언어적 대화를 통해 사람과 상호작용하는 로봇에게 중요한 능력입니다. 이전 연구들은 사전 훈련된 단어 임베딩을 사용함으로써 로봇이 동작-설명 쌍 데이터셋에 포함되지 않은 단어도 사용할 수 있음을 보여주었습니다. 그러나 분포 가설 하에 훈련된 단어 임베딩은 순수하게 텍스트 코퍼스에서 도출되었기 때문에 기반을 갖추지 못했습니다. 본 논문에서는 로봇의 감각-운동 경험을 활용하여 사전 훈련된 단어 임베딩을 체화된 임베딩으로 변환합니다. 우리는 단어 임베딩을 개조하는 비선형 레이어를 통합하여 동작과 설명을 위한 양방향 번역 모델을 확장합니다. 개조 레이어와 양방향 번역 모델을 번갈아 훈련함으로써, 제안된 모델은 사전 훈련된 단어 임베딩을 변환하여 동작-설명 쌍 데이터셋에 적응시킬 수 있습니다. 실험 결과는 동의어의 임베딩이 로봇의 경험(동작 및 환경)을 반영하여 의미적 군집을 형성함을 보여줍니다. 이러한 임베딩을 통해 로봇은 데이터셋에서 동작과 쌍을 이루지 않은 미지의 단어로부터도 적절히 동작을 생성할 수 있습니다.

## 핵심 내용
우리는 로봇 동작과 이에 대한 언어적 설명의 기반 표현을 획득하기 위한 유망한 신경망 모델을 제안합니다. 다의어를 포함한 다양한 언어 표현에 적절히 대응하는 것은 언어적 대화를 통해 사람과 상호작용하는 로봇에게 중요한 능력입니다. 이전 연구들은 사전 훈련된 단어 임베딩을 사용함으로써 로봇이 동작-설명 쌍 데이터셋에 포함되지 않은 단어도 사용할 수 있음을 보여주었습니다. 그러나 분포 가설 하에 훈련된 단어 임베딩은 순수하게 텍스트 코퍼스에서 도출되었기 때문에 기반을 갖추지 못했습니다. 본 논문에서는 로봇의 감각-운동 경험을 활용하여 사전 훈련된 단어 임베딩을 체화된 임베딩으로 변환합니다. 우리는 단어 임베딩을 개조하는 비선형 레이어를 통합하여 동작과 설명을 위한 양방향 번역 모델을 확장합니다. 개조 레이어와 양방향 번역 모델을 번갈아 훈련함으로써, 제안된 모델은 사전 훈련된 단어 임베딩을 변환하여 동작-설명 쌍 데이터셋에 적응시킬 수 있습니다. 실험 결과는 동의어의 임베딩이 로봇의 경험(동작 및 환경)을 반영하여 의미적 군집을 형성함을 보여줍니다. 이러한 임베딩을 통해 로봇은 데이터셋에서 동작과 쌍을 이루지 않은 미지의 단어로부터도 적절히 동작을 생성할 수 있습니다.
