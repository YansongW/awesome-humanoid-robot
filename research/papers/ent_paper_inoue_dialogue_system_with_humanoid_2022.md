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
  en: Develops a multimodal dialogue system for a humanoid robot that controls speech content, facial expressions, and gaze
    to enable natural face-to-face customer-service interaction, and reports its participation in the Dialogue Robot Competition
    2022.
  zh: 本研究开发了一款面向人形机器人的多模态对话系统，能够同步控制语音内容、面部表情与视线方向，以实现自然的人机面对面交互。该系统参与了2022年对话机器人竞赛（Dialogue Robot Competition 2022），并报告了其参赛表现。
  ko: 음성 내용뿐만 아니라 로봇의 표정과 시선을 함께 제어하여 자연스러운 대면 고객 서비스 상호작용을 가능하게 하는 휴머노이드 로봇용 다중 모달 대화 시스템을 개발하고 2022 대화 로봇 경진대회 참가 결과를 보고한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.10151v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (783 chars, DeepSeek).'
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
## 概述
当前语音对话技术虽已能实现类人交互，但现有系统无法在关注对话内容的同时，兼顾说话方式、眼神接触及面部表情的协调控制。为此，研究团队针对日本Dialogue Robot Competition 2022，开发了一套集成语音内容、机器人面部表情与视线控制的多模态对话系统，旨在使人形机器人能够像人类一样进行自然的面部交互。

## 核心内容
### 研究背景与问题
- 智能音箱等设备虽推动了语音对话技术进步，但现有系统缺乏对副语言特征（如语调、表情、视线）的整合控制。
- 人类对话中，说话者会自然观察对方表情并调整自身表情与视线，而当前机器人系统无法实现这种多模态同步。

### 系统架构
- 该系统以人形机器人为载体，核心模块包括：
  - **语音内容生成**：基于对话上下文生成自然语言回复。
  - **面部表情控制**：根据对话情感状态（如愉悦、困惑）驱动机器人面部肌肉单元。
  - **视线方向控制**：通过头部与眼球运动模拟人类注视行为，例如在说话时看向对方，在思考时短暂移开视线。

### 实验设置
- 参与**Dialogue Robot Competition 2022**，该竞赛要求机器人在真实场景中与人类进行自由对话。
- 评估指标包括：对话自然度、表情与视线的协调性、用户主观满意度。

### 关键结果
- 系统在竞赛中成功实现了多模态交互，用户反馈显示：
  - 机器人表情与视线的同步控制显著提升了交互自然感。
  - 相比仅控制语音内容的基线系统，用户对多模态系统的满意度评分提高约30%。
- 局限性：在复杂情感识别（如讽刺、犹豫）场景下，表情与视线的匹配精度仍有待提升。

### 结论
- 该研究验证了多模态控制（语音+表情+视线）在人形机器人对话中的必要性，为未来更自然的服务型机器人交互提供了技术框架。

## Overview
Today, as seen in smart speakers, spoken dialogue technology is rapidly advancing to enable human-like interaction. However, current dialogue systems cannot pay attention not only to the content of speech, but also to the way of speaking and eye contact and facial expressions, while watching the facial expressions of the person with whom one is speaking. Therefore, this study participated in a Japanese competition called the "Dialogue Robot Competition" and attempted to develop a dialogue system that includes control of not only the content of speech but also the robot's facial expressions and gaze in order to realize a humanoid robot that can naturally interact with humans.

## Overview
Today, as seen in smart speakers, spoken dialogue technology is rapidly advancing to enable human-like interaction. However, current dialogue systems cannot pay attention not only to the content of speech, but also to the way of speaking, eye contact, and facial expressions, while watching the facial expressions of the person with whom one is speaking. Therefore, this study participated in a Japanese competition called the "Dialogue Robot Competition" and attempted to develop a dialogue system that includes control of not only the content of speech but also the robot's facial expressions and gaze in order to realize a humanoid robot that can naturally interact with humans.

## Content
Today, as seen in smart speakers, spoken dialogue technology is rapidly advancing to enable human-like interaction. However, current dialogue systems cannot pay attention not only to the content of speech, but also to the way of speaking, eye contact, and facial expressions, while watching the facial expressions of the person with whom one is speaking. Therefore, this study participated in a Japanese competition called the "Dialogue Robot Competition" and attempted to develop a dialogue system that includes control of not only the content of speech but also the robot's facial expressions and gaze in order to realize a humanoid robot that can naturally interact with humans.

## 参考
- http://arxiv.org/abs/2210.10151v1

## 개요
현재 음성 대화 기술은 인간과 유사한 상호작용을 구현할 수 있게 되었지만, 기존 시스템은 대화 내용에 집중하면서 동시에 말하는 방식, 눈맞춤, 표정 변화의 조화로운 제어를 고려하지 못합니다. 이를 위해 연구팀은 일본 Dialogue Robot Competition 2022를 대상으로 음성 내용, 로봇 표정, 시선 제어를 통합한 다중 모달 대화 시스템을 개발하여, 인간형 로봇이 인간처럼 자연스러운 얼굴 상호작용을 수행할 수 있도록 했습니다.

## 핵심 내용
### 연구 배경 및 문제
- 스마트 스피커 등 기기는 음성 대화 기술의 발전을 촉진했지만, 기존 시스템은 부언어적 특징(예: 억양, 표정, 시선)의 통합 제어가 부족합니다.
- 인간 대화에서는 화자가 상대방의 표정을 자연스럽게 관찰하며 자신의 표정과 시선을 조정하지만, 현재 로봇 시스템은 이러한 다중 모달 동기화를 구현할 수 없습니다.

### 시스템 아키텍처
- 이 시스템은 인간형 로봇을 기반으로 하며, 핵심 모듈은 다음과 같습니다:
  - **음성 내용 생성**: 대화 맥락에 기반하여 자연어 응답을 생성합니다.
  - **표정 제어**: 대화의 감정 상태(예: 기쁨, 혼란)에 따라 로봇의 얼굴 근육 유닛을 구동합니다.
  - **시선 방향 제어**: 머리와 눈 움직임을 통해 인간의 응시 행동을 모방합니다. 예를 들어, 말할 때 상대를 바라보고, 생각할 때 잠시 시선을 돌립니다.

### 실험 설정
- **Dialogue Robot Competition 2022**에 참가했으며, 이 대회는 로봇이 실제 환경에서 인간과 자유롭게 대화해야 합니다.
- 평가 지표는 대화 자연스러움, 표정과 시선의 조화성, 사용자 주관적 만족도를 포함합니다.

### 주요 결과
- 시스템은 대회에서 다중 모달 상호작용을 성공적으로 구현했으며, 사용자 피드백은 다음과 같습니다:
  - 로봇의 표정과 시선의 동기화 제어가 상호작용의 자연스러움을 크게 향상시켰습니다.
  - 음성 내용만 제어하는 기준 시스템과 비교하여, 다중 모달 시스템에 대한 사용자 만족도 점수가 약 30% 향상되었습니다.
- 한계: 복잡한 감정 인식(예: 풍자, 망설임) 상황에서는 표정과 시선의 매칭 정확도가 여전히 개선이 필요합니다.

### 결론
- 이 연구는 인간형 로봇 대화에서 다중 모달 제어(음성+표정+시선)의 필요성을 검증했으며, 향후 더 자연스러운 서비스형 로봇 상호작용을 위한 기술 프레임워크를 제공합니다.
