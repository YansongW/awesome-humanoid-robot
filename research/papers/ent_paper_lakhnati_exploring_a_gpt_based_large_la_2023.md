---
$id: ent_paper_lakhnati_exploring_a_gpt_based_large_la_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based Human-Robot Teaming Simulation
  zh: 探索基于GPT的大语言模型在虚拟现实人机团队协作仿真中的可变自主性
  ko: VR 기반 인간-로봇 팀워크 시뮬레이션에서의 가변 자율성을 위한 GPT 기반 대형 언어 모델 탐구
summary:
  en: This paper presents a Unity-based VR simulation framework in which users converse via natural language with multiple
    simulated robots, each powered by an individual GPT-4 instance, and uses OpenAI's function-calling API to translate unstructured
    speech into structured robot actions. A 12-participant user study examines conversational strategies and provides lessons
    learned for LLM-driven human-robot teaming.
  zh: 本文提出了一个基于Unity的虚拟现实仿真框架，用户可通过自然语言与由独立GPT-4实例驱动的多个仿真机器人对话，并利用OpenAI的函数调用API将非结构化语音转换为结构化机器人动作。一项包含12名参与者的用户研究考察了对话策略，并为基于大语言模型的人机团队协作提供了经验教训。
  ko: 본 논문은 사용자가 개별 GPT-4 인스턴스로 구동되는 여러 시뮬레이션 로봇과 자연어로 대화하고, OpenAI의 함수 호출 API를 사용하여 비구조화된 음성을 구조화된 로봇 동작으로 변환하는 Unity 기반
    VR 시뮬레이션 프레임워크를 제시한다. 12명의 참가자를 대상으로 한 사용자 연구는 대화 전략을 조사하고 LLM 기반 인간-로봇 팀워크에 대한 교훈을 제공했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.07214v3.
sources:
- id: src_001
  type: paper
  title: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based Human-Robot Teaming Simulation
  url: https://arxiv.org/abs/2312.07214
  date: '2023'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
In a rapidly evolving digital landscape autonomous tools and robots are becoming commonplace. Recognizing the significance of this development, this paper explores the integration of Large Language Models (LLMs) like Generative pre-trained transformer (GPT) into human-robot teaming environments to facilitate variable autonomy through the means of verbal human-robot communication. In this paper, we introduce a novel framework for such a GPT-powered multi-robot testbed environment, based on a Unity Virtual Reality (VR) setting. This system allows users to interact with robot agents through natural language, each powered by individual GPT cores. By means of OpenAI's function calling, we bridge the gap between unstructured natural language input and structure robot actions. A user study with 12 participants explores the effectiveness of GPT-4 and, more importantly, user strategies when being given the opportunity to converse in natural language within a multi-robot environment. Our findings suggest that users may have preconceived expectations on how to converse with robots and seldom try to explore the actual language and cognitive capabilities of their robot collaborators. Still, those users who did explore where able to benefit from a much more natural flow of communication and human-like back-and-forth. We provide a set of lessons learned for future research and technical implementations of similar systems.

## 核心内容
In a rapidly evolving digital landscape autonomous tools and robots are becoming commonplace. Recognizing the significance of this development, this paper explores the integration of Large Language Models (LLMs) like Generative pre-trained transformer (GPT) into human-robot teaming environments to facilitate variable autonomy through the means of verbal human-robot communication. In this paper, we introduce a novel framework for such a GPT-powered multi-robot testbed environment, based on a Unity Virtual Reality (VR) setting. This system allows users to interact with robot agents through natural language, each powered by individual GPT cores. By means of OpenAI's function calling, we bridge the gap between unstructured natural language input and structure robot actions. A user study with 12 participants explores the effectiveness of GPT-4 and, more importantly, user strategies when being given the opportunity to converse in natural language within a multi-robot environment. Our findings suggest that users may have preconceived expectations on how to converse with robots and seldom try to explore the actual language and cognitive capabilities of their robot collaborators. Still, those users who did explore where able to benefit from a much more natural flow of communication and human-like back-and-forth. We provide a set of lessons learned for future research and technical implementations of similar systems.

## 参考
- http://arxiv.org/abs/2312.07214v3

