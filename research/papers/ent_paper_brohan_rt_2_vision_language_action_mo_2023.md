---
$id: ent_paper_brohan_rt_2_vision_language_action_mo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control'
  zh: RT-2
  ko: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control'
summary:
  en: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (RT-2), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  zh: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (RT-2), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  ko: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (RT-2), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rt_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.15818v1.
sources:
- id: src_001
  type: paper
  title: RT-2 source
  url: https://proceedings.mlr.press/v229/zitkovich23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## 核心内容
We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## 参考
- http://arxiv.org/abs/2307.15818v1

## Overview
We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## Content
We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## 개요
우리는 인터넷 규모 데이터로 학습된 시각-언어 모델을 엔드투엔드 로봇 제어에 직접 통합하여 일반화를 향상시키고 창발적 의미 추론을 가능하게 하는 방법을 연구합니다. 우리의 목표는 단일 엔드투엔드 학습 모델이 로봇 관찰을 행동으로 매핑하는 방법을 학습함과 동시에 웹의 언어 및 시각-언어 데이터에 대한 대규모 사전 학습의 이점을 누릴 수 있도록 하는 것입니다. 이를 위해, 우리는 로봇 궤적 데이터와 시각적 질문 응답과 같은 인터넷 규모의 시각-언어 작업 모두에 대해 최첨단 시각-언어 모델을 공동 미세 조정할 것을 제안합니다. 다른 접근 방식과 달리, 우리는 이 목표를 달성하기 위한 간단하고 일반적인 방법을 제안합니다. 자연어 응답과 로봇 행동을 동일한 형식에 맞추기 위해, 행동을 텍스트 토큰으로 표현하고 이를 자연어 토큰과 동일한 방식으로 모델의 학습 세트에 직접 통합합니다. 이러한 모델 범주를 시각-언어-행동 모델(VLA)이라고 부르며, RT-2라는 예시 모델을 구현합니다. 우리의 광범위한 평가(6,000회 평가 시험)는 우리의 접근 방식이 성능 좋은 로봇 정책을 이끌어내고 RT-2가 인터넷 규모 학습에서 다양한 창발적 능력을 얻을 수 있게 함을 보여줍니다. 여기에는 새로운 객체에 대한 현저히 향상된 일반화, 로봇 학습 데이터에 없는 명령 해석 능력(예: 객체를 특정 숫자나 아이콘 위에 놓기), 사용자 명령에 대한 기초적 추론 능력(예: 가장 작거나 큰 객체, 또는 다른 객체에 가장 가까운 객체 집기)이 포함됩니다. 또한, 사고 사슬 추론을 통합함으로써 RT-2가 다단계 의미 추론을 수행할 수 있음을 보여줍니다. 예를 들어, 즉석 망치로 사용할 객체(돌)를 찾거나, 피곤한 사람에게 가장 적합한 음료 유형(에너지 드링크)을 파악하는 것입니다.

## 핵심 내용
우리는 인터넷 규모 데이터로 학습된 시각-언어 모델을 엔드투엔드 로봇 제어에 직접 통합하여 일반화를 향상시키고 창발적 의미 추론을 가능하게 하는 방법을 연구합니다. 우리의 목표는 단일 엔드투엔드 학습 모델이 로봇 관찰을 행동으로 매핑하는 방법을 학습함과 동시에 웹의 언어 및 시각-언어 데이터에 대한 대규모 사전 학습의 이점을 누릴 수 있도록 하는 것입니다. 이를 위해, 우리는 로봇 궤적 데이터와 시각적 질문 응답과 같은 인터넷 규모의 시각-언어 작업 모두에 대해 최첨단 시각-언어 모델을 공동 미세 조정할 것을 제안합니다. 다른 접근 방식과 달리, 우리는 이 목표를 달성하기 위한 간단하고 일반적인 방법을 제안합니다. 자연어 응답과 로봇 행동을 동일한 형식에 맞추기 위해, 행동을 텍스트 토큰으로 표현하고 이를 자연어 토큰과 동일한 방식으로 모델의 학습 세트에 직접 통합합니다. 이러한 모델 범주를 시각-언어-행동 모델(VLA)이라고 부르며, RT-2라는 예시 모델을 구현합니다. 우리의 광범위한 평가(6,000회 평가 시험)는 우리의 접근 방식이 성능 좋은 로봇 정책을 이끌어내고 RT-2가 인터넷 규모 학습에서 다양한 창발적 능력을 얻을 수 있게 함을 보여줍니다. 여기에는 새로운 객체에 대한 현저히 향상된 일반화, 로봇 학습 데이터에 없는 명령 해석 능력(예: 객체를 특정 숫자나 아이콘 위에 놓기), 사용자 명령에 대한 기초적 추론 능력(예: 가장 작거나 큰 객체, 또는 다른 객체에 가장 가까운 객체 집기)이 포함됩니다. 또한, 사고 사슬 추론을 통합함으로써 RT-2가 다단계 의미 추론을 수행할 수 있음을 보여줍니다. 예를 들어, 즉석 망치로 사용할 객체(돌)를 찾거나, 피곤한 사람에게 가장 적합한 음료 유형(에너지 드링크)을 파악하는 것입니다.
