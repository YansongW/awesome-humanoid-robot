---
$id: ent_paper_inoue_dialogue_system_with_humanoid_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dialogue system with humanoid robot
  zh: 人形机器人对话系统
  ko: 휴머노이드 로봇 대화 시스템
summary:
  en: Develops a multimodal dialogue system for a humanoid robot that controls speech
    content, facial expressions, and gaze to enable natural face-to-face customer-service
    interaction, and reports its participation in the Dialogue Robot Competition 2022.
  zh: 开发了一种用于人形机器人的多模态对话系统，该系统同时控制语音内容、面部表情和视线，以实现自然面对面的客户服务交互，并报告了该系统参加2022年对话机器人竞赛的情况。
  ko: 음성 내용뿐만 아니라 로봇의 표정과 시선을 함께 제어하여 자연스러운 대면 고객 서비스 상호작용을 가능하게 하는 휴머노이드 로봇용 다중 모달
    대화 시스템을 개발하고 2022 대화 로봇 경진대회 참가 결과를 보고한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- system
- knowledge
tags:
- humanoid_robot
- dialogue_system
- multimodal_interaction
- spoken_dialogue
- facial_expression_control
- gaze_control
- customer_service
- japanese_nlp
- word_rotators_distance
- dialogue_robot_competition
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv text before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Dialogue system with humanoid robot
  url: https://arxiv.org/abs/2210.10151
  date: '2022'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

This paper describes the development of a multimodal dialogue system for a humanoid robot, created for participation in the Japanese Dialogue Robot Competition 2022. The authors argue that conventional spoken dialogue systems, as exemplified by smart speakers, focus only on speech content and ignore paralinguistic and non-verbal channels such as prosody, eye contact, and facial expressions. To move toward more natural face-to-face interaction, they build a system that simultaneously generates appropriate verbal responses and controls the robot's facial expressions and gaze.

The dialogue pipeline processes visitor utterances through speech recognition, morphological analysis with MeCab and mecab-ipadic-NEologd, and semantic matching against predefined question categories. A Japanese Wikipedia-based word-embedding model created with gensim supports this matching. The system integrates external information sources including Rurubu DATA for tourist information and the Google Maps API for restaurant recommendations, and uses Amazon Polly for speech output. Non-verbal behavior is driven by valence, arousal, dominance, and realIntention parameters that modulate facial expression and gaze.

The authors report that the system finished 10th of 13 teams in the preliminary round and did not advance to the finals. Post-hoc analysis identifies failure modes including misunderstanding of ambiguous Japanese utterances, mechanical-sounding responses, limited question categories, and insufficient information provision. The paper also discusses potential deployment of the system in customer-service roles such as travel-agent concierge.

## Key Contributions

- Developed a dialogue system that controls both speech content and non-verbal robot behaviors (facial expressions and gaze).
- Used a Japanese Wikipedia-based language model built with gensim, MeCab, and mecab-ipadic-NEologd for visitor utterance understanding.
- Classified user utterances with Word Rotator's Distance, falling back to cosine similarity when similarity scores were low.
- Integrated Rurubu DATA tourist information and Google Maps API restaurant data into the dialogue.
- Participated in the Dialogue Robot Competition 2022 and analyzed the system's failure modes.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it addresses deployment of a humanoid robot as an interactive travel-agent concierge. Rather than treating the robot as a voice-only terminal, the authors exploit the physical humanoid platform to render facial expressions and gaze alongside speech, targeting natural face-to-face customer-service dialogue. This situates the paper at the intersection of AI dialogue methods, robot software integration, and service applications, and provides a concrete competition-based evaluation of how well such multimodal behaviors support human-robot interaction.
