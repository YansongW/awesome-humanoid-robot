---
$id: ent_paper_lakhnati_exploring_a_gpt_based_large_la_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based Human-Robot Teaming Simulation
  zh: 在基于VR的人机协作模拟中探索基于GPT的大型语言模型实现可变自主性
  ko: VR 기반 인간-로봇 협업 시뮬레이션에서 GPT 기반 대형 언어 모델을 활용한 가변 자율성 탐구
summary:
  en: This 2024 arXiv paper presents a Unity VR simulation in which multiple simulated robot agents, each driven by a GPT-4
    core via OpenAI function calling, receive natural-language voice commands from users. An exploratory within-subjects study
    with 12 participants yields observations on user conversational strategies and lessons learned for natural-language-driven
    variable autonomy in human-robot teaming.
  zh: 这篇2024年arXiv论文介绍了一个Unity VR仿真环境，其中多个由GPT-4核心通过OpenAI函数调用驱动的模拟机器人代理接收用户的自然语言语音指令。一项包含12名参与者的探索性被试内研究提供了用户对话策略的观察结果，并总结了面向自然语言驱动的人机协作可变自主性的经验教训。
  ko: 이 2024년 arXiv 논문은 OpenAI 함수 호출을 통해 GPT-4 코어로 구동되는 여러 시뮬레이션 로봇 에이전트가 사용자의 자연어 음성 명령을 받는 Unity VR 시뮬레이션을 제시한다. 12명의 참가자를
    대상으로 한 탐색적 피험자 내 연구는 사용자의 대화 전략에 대한 관찰과 자연어 기반 인간-로봇 협업의 가변 자율성을 위한 교훈을 제공한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- large_language_model
- gpt_4
- variable_autonomy
- natural_language_command
- human_robot_teaming
- vr_simulation
- multi_robot_system
- openai_function_calling
- speech_interface
- unity
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
  date: '2024'
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
급변하는 디지털 환경에서 자율 도구와 로봇이 보편화되고 있습니다. 본 논문은 이러한 발전의 중요성을 인식하여, 생성형 사전 학습 트랜스포머(GPT)와 같은 대규모 언어 모델(LLM)을 인간-로봇 협업 환경에 통합하여 음성 기반 인간-로봇 의사소통을 통해 가변 자율성을 구현하는 방안을 탐구합니다. 본 논문에서는 Unity 가상 현실(VR) 환경을 기반으로 한 GPT 기반 다중 로봇 테스트베드 환경을 위한 새로운 프레임워크를 소개합니다. 이 시스템은 사용자가 각각 개별 GPT 코어로 구동되는 로봇 에이전트와 자연어로 상호작용할 수 있도록 합니다. OpenAI의 함수 호출을 통해 비정형 자연어 입력과 구조화된 로봇 동작 간의 격차를 해소합니다. 12명의 참가자를 대상으로 한 사용자 연구는 GPT-4의 효과성과, 더 중요하게는 다중 로봇 환경에서 자연어로 대화할 기회가 주어졌을 때 사용자 전략을 탐구합니다. 연구 결과에 따르면 사용자는 로봇과 대화하는 방법에 대해 선입견을 가지고 있으며, 로봇 협력자의 실제 언어 및 인지 능력을 탐구하려는 시도를 거의 하지 않는 것으로 나타났습니다. 그럼에도 불구하고 탐구를 시도한 사용자들은 훨씬 더 자연스러운 의사소통 흐름과 인간적인 상호작용의 이점을 누릴 수 있었습니다. 본 논문은 유사 시스템의 향후 연구 및 기술 구현을 위한 일련의 교훈을 제공합니다.

## 핵심 내용
급변하는 디지털 환경에서 자율 도구와 로봇이 보편화되고 있습니다. 본 논문은 이러한 발전의 중요성을 인식하여, 생성형 사전 학습 트랜스포머(GPT)와 같은 대규모 언어 모델(LLM)을 인간-로봇 협업 환경에 통합하여 음성 기반 인간-로봇 의사소통을 통해 가변 자율성을 구현하는 방안을 탐구합니다. 본 논문에서는 Unity 가상 현실(VR) 환경을 기반으로 한 GPT 기반 다중 로봇 테스트베드 환경을 위한 새로운 프레임워크를 소개합니다. 이 시스템은 사용자가 각각 개별 GPT 코어로 구동되는 로봇 에이전트와 자연어로 상호작용할 수 있도록 합니다. OpenAI의 함수 호출을 통해 비정형 자연어 입력과 구조화된 로봇 동작 간의 격차를 해소합니다. 12명의 참가자를 대상으로 한 사용자 연구는 GPT-4의 효과성과, 더 중요하게는 다중 로봇 환경에서 자연어로 대화할 기회가 주어졌을 때 사용자 전략을 탐구합니다. 연구 결과에 따르면 사용자는 로봇과 대화하는 방법에 대해 선입견을 가지고 있으며, 로봇 협력자의 실제 언어 및 인지 능력을 탐구하려는 시도를 거의 하지 않는 것으로 나타났습니다. 그럼에도 불구하고 탐구를 시도한 사용자들은 훨씬 더 자연스러운 의사소통 흐름과 인간적인 상호작용의 이점을 누릴 수 있었습니다. 본 논문은 유사 시스템의 향후 연구 및 기술 구현을 위한 일련의 교훈을 제공합니다.
