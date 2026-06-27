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
  en: This paper presents a runtime knowledge-base expansion pipeline for artificial
    conversational agents that extracts concepts from user utterances using Dialogflow
    and Google Cloud Natural Language, then inserts them into an OWL2 ontology via
    four user-guided insertion strategies. The approach was integrated into the CARESSES
    culture-aware conversational system for social humanoid robots and evaluated using
    Amazon Mechanical Turk data.
  zh: 本文提出了一种面向人工对话代理的运行时知识库扩展流程，该流程利用 Dialogflow 和 Google Cloud Natural Language
    从用户话语中提取概念，并通过四种用户引导的插入策略将其写入 OWL2 本体；该方法已集成到面向社交人形机器人的 CARESSES 文化感知对话系统中，并使用
    Amazon Mechanical Turk 数据进行了评估。
  ko: 본 논문은 Dialogflow와 Google Cloud Natural Language를 사용해 사용자 발화에서 개념을 추출하고, 네 가지
    사용자 안내 삽입 전략을 통해 OWL2 온톨로지에 삽입하는 인공 대화 에이전트를 위한 실행 시 지식 기반 확장 파이프라인을 제시한다. 이 접근법은
    사회적 휴머노이드 로봇을 위한 CARESSES 문화 인식 대화 시스템에 통합되었으며 Amazon Mechanical Turk 데이터를 사용해
    평가되었다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full arXiv text before verification.
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

## Overview

This paper addresses the limitation that social robots and chatbots cannot sustain long-term engagement because their hand-crafted knowledge bases restrict available conversation topics. The authors propose a runtime knowledge-base expansion approach for an Artificial Conversational Agent (ACA). During human-robot verbal interaction, the system extracts candidate concepts from user utterances and inserts newly acquired concepts into an OWL2 ontology, thereby broadening the range of topics the robot can discuss.

The extraction pipeline combines Dialogflow for intent recognition and entity extraction with Google Cloud Natural Language for additional entity analysis. Once a candidate concept is identified, the system applies one of four user-guided insertion methods to place it into the ontology: depth-first search, entity-type based insertion, definition/synonym based insertion, and content classification. These methods are designed to run automatically during conversation while preserving ontology consistency.

The work is integrated into the CARESSES culture-aware conversational system, which has been tested with the SoftBank Pepper robot in care homes. Two experiments evaluate the knowledge extraction technique and the efficiency of the insertion methods. The first experiment uses Amazon Mechanical Turk vocal questionnaire responses for training and testing; the second experiment uses a professional translator to evaluate how effectively each method inserts multiple concepts into the ontology. Statistical comparisons are performed using Wilcoxon signed-rank tests.

## Key Contributions

- Automatic recognition of meaningful concepts from user utterances as candidates for knowledge-base expansion.
- A portfolio of four run-time insertion methods for adding recognized concepts into an OWL2 ontology.
- Integration of the extraction and insertion pipeline into the CARESSES culture-aware conversational system for socially assistive robots.
- Experimental evaluation using Amazon Mechanical Turk workers for training/testing and a professional translator for evaluating insertion efficiency.
- Statistical comparison of insertion methods using Wilcoxon signed-rank tests.

## Relevance to Humanoid Robotics

The system is explicitly designed for social humanoid robots, particularly the SoftBank Pepper robot, assisting older adults in care homes. Run-time expansion of the conversational knowledge base is a prerequisite for scalable long-term deployment of humanoid robots in social-assistance roles, because it reduces reliance on exhaustive hand-engineering of conversation topics and enables the robot to adapt to individual users' interests.
