---
$id: ent_paper_harmon_whole_body_motion_gener_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions'
  zh: Harmon｜从语言描述生成人形机器人的全身运动
  ko: 'HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions'
summary:
  en: Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments.
    Critical to their coexistence and cooperation with humans is the ability to understand natural language communications
    and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from
    language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions
    and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our
    approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through
    both simulated and real-world experiments. More videos can be found at https:/
  zh: Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- harmon
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: HARMON: Whole-Body Motion
    Generation of Humanoid Robots from Language Descriptions.'
sources:
- id: src_001
  type: website
  title: Harmon project page
  url: https://ut-austin-rpl.github.io/Harmon/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments. Critical to their coexistence and cooperation with humans is the ability to understand natural language communications and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through both simulated and real-world experiments. More videos can be found at https://ut-austin-rpl.github.io/Harmon/.

## 核心内容
Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments. Critical to their coexistence and cooperation with humans is the ability to understand natural language communications and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through both simulated and real-world experiments. More videos can be found at https://ut-austin-rpl.github.io/Harmon/.

## 参考
- Semantic Scholar search: HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions

## Overview
Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments. Critical to their coexistence and cooperation with humans is the ability to understand natural language communications and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through both simulated and real-world experiments. More videos can be found at https://ut-austin-rpl.github.io/Harmon/.

## Content
Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments. Critical to their coexistence and cooperation with humans is the ability to understand natural language communications and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through both simulated and real-world experiments. More videos can be found at https://ut-austin-rpl.github.io/Harmon/.

## 개요
휴머노이드 로봇은 인간과 유사한 형태를 갖추고 있어 인간 환경에 자연스럽게 통합될 가능성을 지니고 있습니다. 인간과의 공존 및 협력을 위해 중요한 것은 자연어 의사소통을 이해하고 인간과 유사한 행동을 보이는 능력입니다. 본 연구는 언어 설명으로부터 휴머노이드 로봇의 다양한 전신 동작을 생성하는 데 초점을 맞춥니다. 방대한 인간 동작 데이터셋의 인간 동작 사전 지식을 활용하여 휴머노이드 동작을 초기화하고, Vision Language Models(VLMs)의 상식 추론 능력을 사용하여 이러한 동작을 편집 및 개선합니다. 우리의 접근 방식은 시뮬레이션 및 실제 실험을 통해 자연스럽고 표현력이 풍부하며 텍스트와 일치하는 휴머노이드 동작을 생성할 수 있음을 입증합니다. 더 많은 비디오는 https://ut-austin-rpl.github.io/Harmon/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 인간과 유사한 형태를 갖추고 있어 인간 환경에 자연스럽게 통합될 가능성을 지니고 있습니다. 인간과의 공존 및 협력을 위해 중요한 것은 자연어 의사소통을 이해하고 인간과 유사한 행동을 보이는 능력입니다. 본 연구는 언어 설명으로부터 휴머노이드 로봇의 다양한 전신 동작을 생성하는 데 초점을 맞춥니다. 방대한 인간 동작 데이터셋의 인간 동작 사전 지식을 활용하여 휴머노이드 동작을 초기화하고, Vision Language Models(VLMs)의 상식 추론 능력을 사용하여 이러한 동작을 편집 및 개선합니다. 우리의 접근 방식은 시뮬레이션 및 실제 실험을 통해 자연스럽고 표현력이 풍부하며 텍스트와 일치하는 휴머노이드 동작을 생성할 수 있음을 입증합니다. 더 많은 비디오는 https://ut-austin-rpl.github.io/Harmon/에서 확인할 수 있습니다.
