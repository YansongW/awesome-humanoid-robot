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
  zh: 本文提出了一种面向人工对话代理的运行时知识库扩展流程，该流程利用 Dialogflow 和 Google Cloud Natural Language 从用户话语中提取概念，并通过四种用户引导的插入策略将其写入 OWL2 本体；该方法已集成到面向社交人形机器人的
    CARESSES 文化感知对话系统中，并使用 Amazon Mechanical Turk 数据进行了评估。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.11170v1.
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
This article describes a novel approach to expand in run-time the knowledge base of an Artificial Conversational Agent. A technique for automatic knowledge extraction from the user's sentence and four methods to insert the new acquired concepts in the knowledge base have been developed and integrated into a system that has already been tested for knowledge-based conversation between a social humanoid robot and residents of care homes. The run-time addition of new knowledge allows overcoming some limitations that affect most robots and chatbots: the incapability of engaging the user for a long time due to the restricted number of conversation topics. The insertion in the knowledge base of new concepts recognized in the user's sentence is expected to result in a wider range of topics that can be covered during an interaction, making the conversation less repetitive. Two experiments are presented to assess the performance of the knowledge extraction technique, and the efficiency of the developed insertion methods when adding several concepts in the Ontology.

## 核心内容
This article describes a novel approach to expand in run-time the knowledge base of an Artificial Conversational Agent. A technique for automatic knowledge extraction from the user's sentence and four methods to insert the new acquired concepts in the knowledge base have been developed and integrated into a system that has already been tested for knowledge-based conversation between a social humanoid robot and residents of care homes. The run-time addition of new knowledge allows overcoming some limitations that affect most robots and chatbots: the incapability of engaging the user for a long time due to the restricted number of conversation topics. The insertion in the knowledge base of new concepts recognized in the user's sentence is expected to result in a wider range of topics that can be covered during an interaction, making the conversation less repetitive. Two experiments are presented to assess the performance of the knowledge extraction technique, and the efficiency of the developed insertion methods when adding several concepts in the Ontology.

## 参考
- http://arxiv.org/abs/2104.11170v1

## Overview
This article describes a novel approach to expand in run-time the knowledge base of an Artificial Conversational Agent. A technique for automatic knowledge extraction from the user's sentence and four methods to insert the new acquired concepts in the knowledge base have been developed and integrated into a system that has already been tested for knowledge-based conversation between a social humanoid robot and residents of care homes. The run-time addition of new knowledge allows overcoming some limitations that affect most robots and chatbots: the incapability of engaging the user for a long time due to the restricted number of conversation topics. The insertion in the knowledge base of new concepts recognized in the user's sentence is expected to result in a wider range of topics that can be covered during an interaction, making the conversation less repetitive. Two experiments are presented to assess the performance of the knowledge extraction technique, and the efficiency of the developed insertion methods when adding several concepts in the Ontology.

## Content
This article describes a novel approach to expand in run-time the knowledge base of an Artificial Conversational Agent. A technique for automatic knowledge extraction from the user's sentence and four methods to insert the new acquired concepts in the knowledge base have been developed and integrated into a system that has already been tested for knowledge-based conversation between a social humanoid robot and residents of care homes. The run-time addition of new knowledge allows overcoming some limitations that affect most robots and chatbots: the incapability of engaging the user for a long time due to the restricted number of conversation topics. The insertion in the knowledge base of new concepts recognized in the user's sentence is expected to result in a wider range of topics that can be covered during an interaction, making the conversation less repetitive. Two experiments are presented to assess the performance of the knowledge extraction technique, and the efficiency of the developed insertion methods when adding several concepts in the Ontology.

## 개요
본 논문은 인공 대화 에이전트의 지식 베이스를 런타임에 확장하는 새로운 접근 방식을 설명합니다. 사용자 문장에서 자동으로 지식을 추출하는 기술과 새로 획득한 개념을 지식 베이스에 삽입하는 네 가지 방법이 개발되어, 이미 요양원 거주자와 사회적 휴머노이드 로봇 간의 지식 기반 대화를 위해 테스트된 시스템에 통합되었습니다. 런타임에 새로운 지식을 추가함으로써 대부분의 로봇과 챗봇이 겪는 한계, 즉 제한된 대화 주제로 인해 사용자를 오랫동안 참여시키지 못하는 문제를 극복할 수 있습니다. 사용자 문장에서 인식된 새로운 개념을 지식 베이스에 삽입하면 상호작용 중 다룰 수 있는 주제의 범위가 넓어져 대화가 덜 반복적이 될 것으로 기대됩니다. 지식 추출 기술의 성능과 개발된 삽입 방법이 온톨로지에 여러 개념을 추가할 때의 효율성을 평가하기 위해 두 가지 실험이 제시됩니다.

## 핵심 내용
본 논문은 인공 대화 에이전트의 지식 베이스를 런타임에 확장하는 새로운 접근 방식을 설명합니다. 사용자 문장에서 자동으로 지식을 추출하는 기술과 새로 획득한 개념을 지식 베이스에 삽입하는 네 가지 방법이 개발되어, 이미 요양원 거주자와 사회적 휴머노이드 로봇 간의 지식 기반 대화를 위해 테스트된 시스템에 통합되었습니다. 런타임에 새로운 지식을 추가함으로써 대부분의 로봇과 챗봇이 겪는 한계, 즉 제한된 대화 주제로 인해 사용자를 오랫동안 참여시키지 못하는 문제를 극복할 수 있습니다. 사용자 문장에서 인식된 새로운 개념을 지식 베이스에 삽입하면 상호작용 중 다룰 수 있는 주제의 범위가 넓어져 대화가 덜 반복적이 될 것으로 기대됩니다. 지식 추출 기술의 성능과 개발된 삽입 방법이 온톨로지에 여러 개념을 추가할 때의 효율성을 평가하기 위해 두 가지 실험이 제시됩니다.
