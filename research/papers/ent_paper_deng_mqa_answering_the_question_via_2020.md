---
$id: ent_paper_deng_mqa_answering_the_question_via_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MQA: Answering the Question via Robotic Manipulation'
  zh: MQA：通过机器人操作回答问题
  ko: 'MQA: 로봇 매니퓰레이션을 통한 질문 답변'
summary:
  en: Proposes Manipulation Question Answering (MQA), where a robot actively pushes objects in a cluttered bin to change the
    scene until it can answer a natural-language counting question, using a VQA-based QA module and a DQN-based manipulation
    module.
  zh: 提出操作问答（MQA）任务：机器人通过在杂乱料箱中主动推动物体来改变场景，直到能够回答自然语言计数问题；框架包含基于视觉问答（VQA）的问答模块和基于深度Q网络（DQN）的操作模块。
  ko: 조작 질의응답(MQA)을 제안한다. 로봇은 복잡한 빈에서 물체를 밀어 장면을 바꾸고, VQA 기반 QA 모듈과 DQN 기반 조작 모듈을 사용해 자연어 계수 질문에 답할 때까지 탐색한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- manipulation_question_answering
- visual_question_answering
- deep_q_network
- active_perception
- bin_pushing
- cluttered_scene
- robotic_qa
- simulation
- counting_questions
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.04641v4.
sources:
- id: src_001
  type: paper
  title: 'MQA: Answering the Question via Robotic Manipulation'
  url: https://arxiv.org/abs/2003.04641
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this paper, we propose a novel task, Manipulation Question Answering (MQA), where the robot performs manipulation actions to change the environment in order to answer a given question. To solve this problem, a framework consisting of a QA module and a manipulation module is proposed. For the QA module, we adopt the method for the Visual Question Answering (VQA) task. For the manipulation module, a Deep Q Network (DQN) model is designed to generate manipulation actions for the robot to interact with the environment. We consider the situation where the robot continuously manipulating objects inside a bin until the answer to the question is found. Besides, a novel dataset that contains a variety of object models, scenarios and corresponding question-answer pairs is established in a simulation environment. Extensive experiments have been conducted to validate the effectiveness of the proposed framework.

## 核心内容
In this paper, we propose a novel task, Manipulation Question Answering (MQA), where the robot performs manipulation actions to change the environment in order to answer a given question. To solve this problem, a framework consisting of a QA module and a manipulation module is proposed. For the QA module, we adopt the method for the Visual Question Answering (VQA) task. For the manipulation module, a Deep Q Network (DQN) model is designed to generate manipulation actions for the robot to interact with the environment. We consider the situation where the robot continuously manipulating objects inside a bin until the answer to the question is found. Besides, a novel dataset that contains a variety of object models, scenarios and corresponding question-answer pairs is established in a simulation environment. Extensive experiments have been conducted to validate the effectiveness of the proposed framework.

## 参考
- http://arxiv.org/abs/2003.04641v4

