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
  en: Proposes Manipulation Question Answering (MQA), where a robot actively pushes
    objects in a cluttered bin to change the scene until it can answer a natural-language
    counting question, using a VQA-based QA module and a DQN-based manipulation module.
  zh: 提出操作问答（MQA）任务：机器人通过在杂乱料箱中主动推动物体来改变场景，直到能够回答自然语言计数问题；框架包含基于视觉问答（VQA）的问答模块和基于深度Q网络（DQN）的操作模块。
  ko: 조작 질의응답(MQA)을 제안한다. 로봇은 복잡한 빈에서 물체를 밀어 장면을 바꾸고, VQA 기반 QA 모듈과 DQN 기반 조작 모듈을
    사용해 자연어 계수 질문에 답할 때까지 탐색한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; full-text review needed
    to confirm exact citations and method details.
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

## Overview

Manipulation Question Answering (MQA) is introduced as a task in which a robot must physically interact with a cluttered bin of objects to answer a natural-language question. Instead of relying on a single static view, the robot repeatedly pushes objects to reduce occlusion and reveal the information needed for answering. The proposed framework consists of two cooperating modules: a question-answering module adapted from Visual Question Answering (VQA), and a manipulation module based on a Deep Q-Network (DQN) that outputs pushing actions.

The QA module processes the current visual scene together with the textual question to predict an answer. The manipulation module receives the same visual-linguistic state and selects a push action that is expected to improve answerability, with rewards shaped toward task progress rather than generic scene clearing. Training and evaluation are performed in a simulated environment built in V-REP with the Bullet physics engine, using a UR5 manipulator, a gripper, and a Kinect-style camera.

The authors also release the MQA dataset, which contains multiple 3D object models, simulated bin scenarios, and paired question-answer annotations. Experiments focus on counting questions and show that the learned manipulation policy outperforms random pushing, demonstrating that purposeful manipulation can improve question answering in clutter.

## Key Contributions

- Formulation of the novel Manipulation Question Answering (MQA) task and a baseline solution framework.
- Design of a DQN-based manipulation policy with task-oriented reward shaping for active scene exploration.
- Construction and public release of the MQA dataset with 3D object models, simulated bin scenes, and question-answer pairs, plus an associated benchmark.
- Empirical validation that learned manipulation policies outperform random exploration on counting questions.

## Relevance to Humanoid Robotics

Humanoid service robots operating in homes, warehouses, or retail spaces must often answer verbal queries about their surroundings while objects are heavily occluded. MQA addresses exactly this need by combining natural-language understanding, active visual perception, and manipulation. The ability to decide which object to push, where to push, and when the scene is sufficiently resolved to answer a question is a key building block for interactive humanoid assistants that inspect inventory, retrieve items, or respond to user requests in unstructured environments.
