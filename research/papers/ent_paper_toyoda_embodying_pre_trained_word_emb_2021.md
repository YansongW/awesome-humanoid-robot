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

