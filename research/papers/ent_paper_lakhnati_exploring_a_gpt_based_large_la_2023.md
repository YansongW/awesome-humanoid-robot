---
$id: ent_paper_lakhnati_exploring_a_gpt_based_large_la_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based
    Human-Robot Teaming Simulation
  zh: 探索基于GPT的大语言模型在虚拟现实人机团队协作仿真中的可变自主性
  ko: VR 기반 인간-로봇 팀워크 시뮬레이션에서의 가변 자율성을 위한 GPT 기반 대형 언어 모델 탐구
summary:
  en: This paper presents a Unity-based VR simulation framework in which users converse
    via natural language with multiple simulated robots, each powered by an individual
    GPT-4 instance, and uses OpenAI's function-calling API to translate unstructured
    speech into structured robot actions. A 12-participant user study examines conversational
    strategies and provides lessons learned for LLM-driven human-robot teaming.
  zh: 本文提出了一个基于Unity的虚拟现实仿真框架，用户可通过自然语言与由独立GPT-4实例驱动的多个仿真机器人对话，并利用OpenAI的函数调用API将非结构化语音转换为结构化机器人动作。一项包含12名参与者的用户研究考察了对话策略，并为基于大语言模型的人机团队协作提供了经验教训。
  ko: 본 논문은 사용자가 개별 GPT-4 인스턴스로 구동되는 여러 시뮬레이션 로봇과 자연어로 대화하고, OpenAI의 함수 호출 API를 사용하여
    비구조화된 음성을 구조화된 로봇 동작으로 변환하는 Unity 기반 VR 시뮬레이션 프레임워크를 제시한다. 12명의 참가자를 대상으로 한 사용자
    연구는 대화 전략을 조사하고 LLM 기반 인간-로봇 팀워크에 대한 교훈을 제공했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
- 06_design_engineering
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- large_language_model
- gpt_4
- variable_autonomy
- shared_control
- human_robot_teaming
- natural_language_interface
- function_calling
- multi_robot_coordination
- vr_simulation
- speech_interface
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based
    Human-Robot Teaming Simulation
  url: https://arxiv.org/abs/2312.07214
  date: '2023'
  accessed_at: '2026-06-26'
---


## Overview

This work investigates how large language models, specifically OpenAI's GPT-4, can be integrated into human-robot teaming to enable variable autonomy through verbal communication. The authors introduce a Unity-based virtual-reality simulation framework in which a single user interacts by voice with three heterogeneous simulated robot agents—Jupiter, Pluto, and Neptune—each controlled by its own GPT-4 instance. A central GPT controller interprets the user's speech, distributes utterances to the relevant agents, and maintains conversational context; the agents then decide which structured actions to execute via OpenAI's function-calling API. Speech input is transcribed by OpenAI Whisper v2, and agent responses are synthesized into audio using Amazon Polly, creating a closed-loop spoken-dialog system.

The framework was evaluated in an exploratory within-subjects user study with 12 participants (after excluding the first two due to system changes). Participants wore a Meta Quest 2 HMD and used a Quest 2 controller while seated, completing seven progressively complex tasks—such as moving agents, retrieving keys, and jointly flipping a bed—by giving spoken instructions to the simulated robots. The authors analyzed interview transcripts thematically and administered a German version of the SASSI questionnaire to assess perceptions of the speech interface.

The results indicate that users often brought preconceived expectations about how to command robots and rarely explored the broader language capabilities of the GPT-based agents. Participants who did engage in more open, exploratory dialogue, however, experienced a more natural, human-like back-and-forth. Based on these observations, the authors derive lessons learned for the design and technical implementation of LLM-driven human-robot teaming systems.

## Key Contributions

• A Unity-based VR framework architecture for voice-controlled multi-agent teaming with GPT-powered simulated robots.
• Empirical findings from a 12-participant user study on how people converse with LLM-based simulated robot agents.
• Use of OpenAI's function-calling API to map unstructured natural-language speech input to structured robot actions in a multi-robot setting.
• A set of lessons learned on feasibility, user expectations, and design improvements for LLM-driven human-robot teaming.

## Relevance to Humanoid Robotics

Although the study uses simulated, non-humanoid robot agents, its exploration of scalable natural-language command interfaces, variable autonomy, and multi-agent coordination is directly relevant to the design of interaction and control systems for deployable humanoid robots in factory, household, or service settings. The function-calling paradigm for grounding unstructured speech into executable actions can be adapted to humanoid action planners and shared-control modules.

The paper also highlights practical challenges—such as response latency, LLM opacity, and the gap between simulated and physical embodiment—that would need to be addressed when migrating this approach to real humanoid platforms. Its qualitative findings on user expectations and conversational strategies can inform the design of more intuitive voice-control interfaces for humanoid robot teams.
