---
$id: ent_paper_du_learning_universal_policies_vi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Universal Policies via Text-Guided Video Generation
  zh: UniPi
  ko: Learning Universal Policies via Text-Guided Video Generation
summary:
  en: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
  zh: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
  ko: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
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
- unipi
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.00111v3.
sources:
- id: src_001
  type: website
  title: UniPi source
  url: http://papers.nips.cc/paper_files/paper/2023/hash/1d5b9233ad716a43be5c0d3023cb82d0-Abstract-Conference.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 核心内容
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 参考
- http://arxiv.org/abs/2302.00111v3

## Overview
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## Content
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 개요
인공지능의 목표 중 하나는 다양한 작업을 해결할 수 있는 에이전트를 구축하는 것입니다. 최근 텍스트 기반 이미지 합성의 발전으로 인해 모델은 복잡한 새로운 이미지를 생성하는 놀라운 능력을 보여주며, 도메인 간 조합적 일반화를 나타냈습니다. 이러한 성공에 동기를 얻어, 우리는 이러한 도구가 더 범용적인 에이전트를 구축하는 데 사용될 수 있는지 조사합니다. 구체적으로, 순차적 의사 결정 문제를 텍스트 조건부 비디오 생성 문제로 변환합니다. 여기서 원하는 목표의 텍스트 인코딩된 사양이 주어지면, 플래너는 미래의 계획된 행동을 묘사하는 일련의 미래 프레임을 합성하고, 이후 생성된 비디오에서 제어 동작을 추출합니다. 텍스트를 기본 목표 사양으로 활용함으로써, 우리는 자연스럽고 조합적으로 새로운 목표로 일반화할 수 있습니다. 제안된 정책-비디오(policy-as-video) 공식은 다양한 상태 및 행동 공간을 가진 환경을 이미지의 통합 공간에서 표현할 수 있으며, 예를 들어 다양한 로봇 조작 작업에서 학습 및 일반화를 가능하게 합니다. 마지막으로, 사전 훈련된 언어 임베딩과 인터넷에서 널리 사용 가능한 비디오를 활용함으로써, 이 접근 방식은 실제 로봇을 위한 매우 현실적인 비디오 계획을 예측하여 지식 전이를 가능하게 합니다.

## 핵심 내용
인공지능의 목표 중 하나는 다양한 작업을 해결할 수 있는 에이전트를 구축하는 것입니다. 최근 텍스트 기반 이미지 합성의 발전으로 인해 모델은 복잡한 새로운 이미지를 생성하는 놀라운 능력을 보여주며, 도메인 간 조합적 일반화를 나타냈습니다. 이러한 성공에 동기를 얻어, 우리는 이러한 도구가 더 범용적인 에이전트를 구축하는 데 사용될 수 있는지 조사합니다. 구체적으로, 순차적 의사 결정 문제를 텍스트 조건부 비디오 생성 문제로 변환합니다. 여기서 원하는 목표의 텍스트 인코딩된 사양이 주어지면, 플래너는 미래의 계획된 행동을 묘사하는 일련의 미래 프레임을 합성하고, 이후 생성된 비디오에서 제어 동작을 추출합니다. 텍스트를 기본 목표 사양으로 활용함으로써, 우리는 자연스럽고 조합적으로 새로운 목표로 일반화할 수 있습니다. 제안된 정책-비디오(policy-as-video) 공식은 다양한 상태 및 행동 공간을 가진 환경을 이미지의 통합 공간에서 표현할 수 있으며, 예를 들어 다양한 로봇 조작 작업에서 학습 및 일반화를 가능하게 합니다. 마지막으로, 사전 훈련된 언어 임베딩과 인터넷에서 널리 사용 가능한 비디오를 활용함으로써, 이 접근 방식은 실제 로봇을 위한 매우 현실적인 비디오 계획을 예측하여 지식 전이를 가능하게 합니다.
