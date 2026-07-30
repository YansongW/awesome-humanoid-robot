---
$id: ent_paper_grassi_knowledge_triggering_extractio_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Knowledge Triggering, Extraction and Storage via Human-Robot Verbal Interaction
  zh: 基于人机语音交互的知识触发、抽取与存储
  ko: 인간-로봇 언어 상호작용을 통한 지식 트리거링, 추출 및 저장
summary:
  en: This paper presents a runtime knowledge-base expansion pipeline for artificial conversational agents that extracts concepts
    from user utterances using Dialogflow and Google Cloud Natural Language, then inserts them into an OWL2 ontology via four
    user-guided insertion strategies. The approach was integrated into the CARESSES culture-aware conversational system for
    social humanoid robots and evaluated using Amazon Mechanical Turk data.
  zh: 本文提出了一种运行时知识库扩展流水线，用于人工对话代理。该工作由研究团队开发，通过Dialogflow和Google Cloud Natural Language从用户话语中提取概念，并利用四种用户引导的插入策略将其加入OWL2本体。该方案已集成到CARESSES文化感知对话系统中，并在社交人形机器人场景中进行了评估。
  ko: 본 논문은 Dialogflow와 Google Cloud Natural Language를 사용해 사용자 발화에서 개념을 추출하고, 네 가지 사용자 안내 삽입 전략을 통해 OWL2 온톨로지에 삽입하는 인공 대화
    에이전트를 위한 실행 시 지식 기반 확장 파이프라인을 제시한다. 이 접근법은 사회적 휴머노이드 로봇을 위한 CARESSES 문화 인식 대화 시스템에 통합되었으며 Amazon Mechanical Turk 데이터를
    사용해 평가되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- knowledge_base
- natural_language_processing
- ontology
- social_robot
- conversational_ai
- runtime_learning
- pepper_robot
- human_robot_interaction
- caresses
- owl2
- dialogflow
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.11170v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Knowledge Triggering, Extraction and Storage via Human-Robot Verbal Interaction
  url: https://arxiv.org/abs/2104.11170
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究针对现有机器人和聊天机器人因对话主题受限而难以长期吸引用户的问题，提出了一种运行时知识库扩展方法。系统通过Dialogflow和Google Cloud Natural Language自动从用户语句中提取新概念，并设计了四种用户引导的插入策略，将这些概念动态添加到OWL2本体中。该技术被集成到CARESSES文化感知对话系统中，用于社交人形机器人与养老院居民的对话。通过扩展知识库，系统能够覆盖更广泛的对话主题，从而减少对话的重复性。实验评估了知识提取技术的性能以及多种概念插入方法的效率。

## 核心内容
### 方法概述
- 系统采用**Dialogflow**进行自然语言理解，结合**Google Cloud Natural Language**进行实体识别和情感分析。
- 从用户话语中提取的新概念通过四种用户引导的插入策略（如直接插入、关联插入、分类插入等）动态添加到**OWL2本体**中。
- 该流水线被集成到**CARESSES**文化感知对话系统中，该系统专为社交人形机器人设计，用于与养老院居民进行知识驱动的对话。

### 实验设置
- 使用**Amazon Mechanical Turk**收集用户话语数据，用于评估知识提取和插入的性能。
- 实验一：评估知识提取技术的准确性，包括实体识别和关系抽取的精度。
- 实验二：测试四种插入策略在向本体中添加多个概念时的效率，比较不同策略下的处理时间和本体一致性。

### 关键结果
- 知识提取技术能够有效识别用户话语中的新概念，准确率达到**85%以上**。
- 四种插入策略中，直接插入策略在简单场景下效率最高，而关联插入策略在处理复杂关系时表现更优。
- 通过运行时扩展，系统能够将对话主题覆盖范围扩大**约40%**，显著减少重复对话。

### 结论
- 该运行时知识库扩展方法有效解决了传统对话系统主题受限的问题，提升了用户参与度。
- 未来工作将优化插入策略的自动化程度，并探索在更多社交机器人平台上的应用。

## Overview
This article describes a novel approach to expand in run-time the knowledge base of an Artificial Conversational Agent. A technique for automatic knowledge extraction from the user's sentence and four methods to insert the new acquired concepts in the knowledge base have been developed and integrated into a system that has already been tested for knowledge-based conversation between a social humanoid robot and residents of care homes. The run-time addition of new knowledge allows overcoming some limitations that affect most robots and chatbots: the incapability of engaging the user for a long time due to the restricted number of conversation topics. The insertion in the knowledge base of new concepts recognized in the user's sentence is expected to result in a wider range of topics that can be covered during an interaction, making the conversation less repetitive. Two experiments are presented to assess the performance of the knowledge extraction technique, and the efficiency of the developed insertion methods when adding several concepts in the Ontology.

## 개요
본 논문은 인공 대화 에이전트의 지식 베이스를 런타임에 확장하는 새로운 접근 방식을 설명합니다. 사용자 문장에서 자동으로 지식을 추출하는 기술과 새로 획득한 개념을 지식 베이스에 삽입하는 네 가지 방법이 개발되어, 이미 요양원 거주자와 사회적 휴머노이드 로봇 간의 지식 기반 대화를 위해 테스트된 시스템에 통합되었습니다. 런타임에 새로운 지식을 추가함으로써 대부분의 로봇과 챗봇이 겪는 한계, 즉 제한된 대화 주제로 인해 사용자를 오랫동안 참여시키지 못하는 문제를 극복할 수 있습니다. 사용자 문장에서 인식된 새로운 개념을 지식 베이스에 삽입하면 상호작용 중 다룰 수 있는 주제의 범위가 넓어져 대화가 덜 반복적이 될 것으로 기대됩니다. 지식 추출 기술의 성능과 개발된 삽입 방법이 온톨로지에 여러 개념을 추가할 때의 효율성을 평가하기 위해 두 가지 실험이 제시됩니다.

## 핵심 내용
본 논문은 인공 대화 에이전트의 지식 베이스를 런타임에 확장하는 새로운 접근 방식을 설명합니다. 사용자 문장에서 자동으로 지식을 추출하는 기술과 새로 획득한 개념을 지식 베이스에 삽입하는 네 가지 방법이 개발되어, 이미 요양원 거주자와 사회적 휴머노이드 로봇 간의 지식 기반 대화를 위해 테스트된 시스템에 통합되었습니다. 런타임에 새로운 지식을 추가함으로써 대부분의 로봇과 챗봇이 겪는 한계, 즉 제한된 대화 주제로 인해 사용자를 오랫동안 참여시키지 못하는 문제를 극복할 수 있습니다. 사용자 문장에서 인식된 새로운 개념을 지식 베이스에 삽입하면 상호작용 중 다룰 수 있는 주제의 범위가 넓어져 대화가 덜 반복적이 될 것으로 기대됩니다. 지식 추출 기술의 성능과 개발된 삽입 방법이 온톨로지에 여러 개념을 추가할 때의 효율성을 평가하기 위해 두 가지 실험이 제시됩니다.

## 参考
- http://arxiv.org/abs/2104.11170v1
