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
  en: This paper proposes rPRAE, a seq2seq model that retrofits pre-trained Word2Vec
    embeddings into robot sensory-motor grounded representations, enabling a NAO humanoid
    to bidirectionally translate between manipulation actions and linguistic descriptions
    including unseen words.
  zh: 本文提出rPRAE模型，通过将预训练Word2Vec词嵌入改造为基于机器人感知运动经验的表征，使NAO人形机器人能够在操作动作与包含未见词汇的语言描述之间进行双向转换。
  ko: 본 논문은 사전 학습된 Word2Vec 임베딩을 로봇의 감각운동 경험에 기반한 표현으로 변환하는 rPRAE 모델을 제안하여, NAO 휴머노이드
    로봇이 조작 행동과 보지 못한 단어를 포함한 언어 설명 간 양방향 변환을 수행할 수 있게 한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review of full text
    before verification.
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

## Overview

This paper addresses the grounding problem in robot language understanding: pre-trained word embeddings derived from text corpora under the distributional hypothesis do not capture robot sensory-motor experience, which can cause inappropriate action generation for unseen linguistic commands. The authors propose rPRAE (retrofitted Paired Recurrent AutoEncoder), a neural seq2seq architecture that bidirectionally translates between robot action sequences and their linguistic descriptions. The model retrofits pre-trained Word2Vec embeddings through a multi-layer nonlinear transformation layer, training the retrofit layer and the bidirectional translation model alternately to prevent overfitting and adapt the embeddings to the paired action-description dataset.

The rPRAE model is built upon a Paired Recurrent Autoencoder (PRAE) that uses bidirectional LSTM recurrent autoencoders to encode action sequences and linguistic descriptions into a shared latent space. Visual state features are extracted using a convolutional autoencoder (CAE) from camera observations of a NAO robot interacting with colored cubes. The retrofit layer consists of three fully connected tanh layers that map distributional word embeddings into embodied representations reflecting the robot's actions and environments.

Experimental validation was performed on a real NAO humanoid robot for two tasks: description generation from observed actions and action generation from linguistic descriptions containing unseen words. The results show that the retrofitted embeddings cluster synonyms and separate antonyms according to part of speech and the robot's action-environment experience, improving the robot's ability to respond to unseen words.

## Key Contributions

- Proposed rPRAE, a seq2seq-based model that bidirectionally translates robot actions and linguistic descriptions containing unseen words by retrofitting pre-trained embeddings.
- Introduced a retrofit layer that transforms distributional word embeddings into representations grounded in robot sensory-motor experience.
- Developed an alternating training procedure for the retrofit layer and the PRAE to constrain expressivity and prevent overfitting.
- Demonstrated that retrofitted embeddings cluster synonyms and separate antonyms according to part of speech and action-environment experience.
- Validated the model on a real NAO humanoid robot for both description generation from actions and action generation from unseen-word descriptions.

## Relevance to Humanoid Robotics

The work was implemented and evaluated on a real NAO humanoid robot, making it directly relevant to humanoid robotics. It enables linguistic human-robot interaction in which the robot generates physical arm manipulation actions from natural-language instructions, a core capability for deploying humanoid robots in interactive industrial or service settings. The focus on grounding language in physical experience is particularly important for humanoids that must operate alongside humans in unstructured environments.
