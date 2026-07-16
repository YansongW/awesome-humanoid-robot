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

## Overview
In a rapidly evolving digital landscape, autonomous tools and robots are becoming commonplace. Recognizing the significance of this development, this paper explores the integration of Large Language Models (LLMs) like Generative Pre-trained Transformer (GPT) into human-robot teaming environments to facilitate variable autonomy through verbal human-robot communication. In this paper, we introduce a novel framework for such a GPT-powered multi-robot testbed environment, based on a Unity Virtual Reality (VR) setting. This system allows users to interact with robot agents through natural language, each powered by individual GPT cores. By means of OpenAI's function calling, we bridge the gap between unstructured natural language input and structured robot actions. A user study with 12 participants explores the effectiveness of GPT-4 and, more importantly, user strategies when given the opportunity to converse in natural language within a multi-robot environment. Our findings suggest that users may have preconceived expectations on how to converse with robots and seldom try to explore the actual language and cognitive capabilities of their robot collaborators. Still, those users who did explore were able to benefit from a much more natural flow of communication and human-like back-and-forth. We provide a set of lessons learned for future research and technical implementations of similar systems.

## Content
In a rapidly evolving digital landscape, autonomous tools and robots are becoming commonplace. Recognizing the significance of this development, this paper explores the integration of Large Language Models (LLMs) like Generative Pre-trained Transformer (GPT) into human-robot teaming environments to facilitate variable autonomy through verbal human-robot communication. In this paper, we introduce a novel framework for such a GPT-powered multi-robot testbed environment, based on a Unity Virtual Reality (VR) setting. This system allows users to interact with robot agents through natural language, each powered by individual GPT cores. By means of OpenAI's function calling, we bridge the gap between unstructured natural language input and structured robot actions. A user study with 12 participants explores the effectiveness of GPT-4 and, more importantly, user strategies when given the opportunity to converse in natural language within a multi-robot environment. Our findings suggest that users may have preconceived expectations on how to converse with robots and seldom try to explore the actual language and cognitive capabilities of their robot collaborators. Still, those users who did explore were able to benefit from a much more natural flow of communication and human-like back-and-forth. We provide a set of lessons learned for future research and technical implementations of similar systems.

## 개요
급변하는 디지털 환경에서 자율 도구와 로봇이 보편화되고 있습니다. 본 논문은 이러한 발전의 중요성을 인식하여, 인간-로봇 협업 환경에 Generative Pre-trained Transformer(GPT)와 같은 대규모 언어 모델(LLM)을 통합하여 언어적 인간-로봇 의사소통을 통해 가변 자율성을 촉진하는 방안을 탐구합니다. 본 논문에서는 Unity 가상 현실(VR) 환경을 기반으로 한 GPT 기반 다중 로봇 테스트베드 환경을 위한 새로운 프레임워크를 소개합니다. 이 시스템은 사용자가 각각 개별 GPT 코어로 구동되는 로봇 에이전트와 자연어로 상호작용할 수 있도록 합니다. OpenAI의 함수 호출을 통해 비정형 자연어 입력과 구조화된 로봇 동작 간의 격차를 해소합니다. 12명의 참가자를 대상으로 한 사용자 연구는 GPT-4의 효과성과, 더 중요하게는 다중 로봇 환경에서 자연어로 대화할 기회가 주어졌을 때 사용자 전략을 탐구합니다. 연구 결과에 따르면 사용자는 로봇과 대화하는 방법에 대해 선입견을 가지고 있으며, 실제 로봇 협력자의 언어 및 인지 능력을 거의 탐구하지 않는 경향이 있습니다. 그럼에도 불구하고 탐구를 시도한 사용자들은 훨씬 더 자연스러운 의사소통 흐름과 인간적인 상호작용의 이점을 누릴 수 있었습니다. 본 논문은 유사 시스템의 향후 연구 및 기술 구현을 위한 일련의 교훈을 제공합니다.

## 핵심 내용
급변하는 디지털 환경에서 자율 도구와 로봇이 보편화되고 있습니다. 본 논문은 이러한 발전의 중요성을 인식하여, 인간-로봇 협업 환경에 Generative Pre-trained Transformer(GPT)와 같은 대규모 언어 모델(LLM)을 통합하여 언어적 인간-로봇 의사소통을 통해 가변 자율성을 촉진하는 방안을 탐구합니다. 본 논문에서는 Unity 가상 현실(VR) 환경을 기반으로 한 GPT 기반 다중 로봇 테스트베드 환경을 위한 새로운 프레임워크를 소개합니다. 이 시스템은 사용자가 각각 개별 GPT 코어로 구동되는 로봇 에이전트와 자연어로 상호작용할 수 있도록 합니다. OpenAI의 함수 호출을 통해 비정형 자연어 입력과 구조화된 로봇 동작 간의 격차를 해소합니다. 12명의 참가자를 대상으로 한 사용자 연구는 GPT-4의 효과성과, 더 중요하게는 다중 로봇 환경에서 자연어로 대화할 기회가 주어졌을 때 사용자 전략을 탐구합니다. 연구 결과에 따르면 사용자는 로봇과 대화하는 방법에 대해 선입견을 가지고 있으며, 실제 로봇 협력자의 언어 및 인지 능력을 거의 탐구하지 않는 경향이 있습니다. 그럼에도 불구하고 탐구를 시도한 사용자들은 훨씬 더 자연스러운 의사소통 흐름과 인간적인 상호작용의 이점을 누릴 수 있었습니다. 본 논문은 유사 시스템의 향후 연구 및 기술 구현을 위한 일련의 교훈을 제공합니다.
