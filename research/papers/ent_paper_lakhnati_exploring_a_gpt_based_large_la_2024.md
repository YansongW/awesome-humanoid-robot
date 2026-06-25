---
$id: ent_paper_lakhnati_exploring_a_gpt_based_large_la_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based
    Human-Robot Teaming Simulation
  zh: 在基于VR的人机协作模拟中探索基于GPT的大型语言模型实现可变自主性
  ko: VR 기반 인간-로봇 협업 시뮬레이션에서 GPT 기반 대형 언어 모델을 활용한 가변 자율성 탐구
summary:
  en: This 2024 arXiv paper presents a Unity VR simulation in which multiple simulated
    robot agents, each driven by a GPT-4 core via OpenAI function calling, receive
    natural-language voice commands from users. An exploratory within-subjects study
    with 12 participants yields observations on user conversational strategies and
    lessons learned for natural-language-driven variable autonomy in human-robot teaming.
  zh: 这篇2024年arXiv论文介绍了一个Unity VR仿真环境，其中多个由GPT-4核心通过OpenAI函数调用驱动的模拟机器人代理接收用户的自然语言语音指令。一项包含12名参与者的探索性被试内研究提供了用户对话策略的观察结果，并总结了面向自然语言驱动的人机协作可变自主性的经验教训。
  ko: 이 2024년 arXiv 논문은 OpenAI 함수 호출을 통해 GPT-4 코어로 구동되는 여러 시뮬레이션 로봇 에이전트가 사용자의 자연어
    음성 명령을 받는 Unity VR 시뮬레이션을 제시한다. 12명의 참가자를 대상으로 한 탐색적 피험자 내 연구는 사용자의 대화 전략에 대한
    관찰과 자연어 기반 인간-로봇 협업의 가변 자율성을 위한 교훈을 제공한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and provided metadata; full-text review
    by a human is needed before full verification.
sources:
- id: src_001
  type: paper
  title: Exploring a GPT-based Large Language Model for Variable Autonomy in a VR-based
    Human-Robot Teaming Simulation
  url: https://arxiv.org/abs/2312.07214
  date: '2024'
  accessed_at: '2026-06-26'
---


## Overview

This paper investigates how GPT-based large language models can support variable autonomy in human-robot teaming through natural-language interaction. The authors built a Unity VR simulation framework in which users collaborate with multiple simulated robot agents. Each agent is controlled by an individual GPT-4 core, and OpenAI's function-calling mechanism translates free-form spoken commands into structured robot actions. The user interface combines a Meta Quest 2 headset, OpenAI Whisper v2 for speech recognition, and Amazon Polly for synthetic speech output.

An exploratory within-subjects user study with 12 participants was conducted in the simulated environment. Participants completed seven collaborative tasks using natural-language speech. The analysis focuses on how users converse with the agents, the strategies they adopt, and the perceived naturalness and feasibility of the interaction. The authors report that many participants brought preconceived expectations about robot-directed speech and rarely explored the full linguistic capabilities of the agents, while those who did adopt more natural dialogue experienced smoother collaboration.

The paper also frames language-based communication as a mechanism for shared control and variable autonomy, spanning cooperational, strategic, tactical, and operational layers. It closes with a set of lessons learned intended to guide future research and technical implementations of LLM-powered human-robot teaming systems.

## Key Contributions

- Design and architecture of a Unity-based VR voice-controlled multi-agent simulation framework for LLM-based human-robot teaming.
- Empirical understanding of user strategies and behaviors when conversing with LLM-powered simulated multi-robot agents.
- Lessons learned on feasibility, naturalness, and adaptability of GPT-based natural-language interaction with simulated robot agents.
- Conceptualization of language-based communication as a mechanism for shared control and variable autonomy across cooperational, strategic, tactical, and operational layers.

## Relevance to Humanoid Robotics

Although the study uses abstract simulated robot agents rather than physical humanoids, its focus on natural-language command, dynamic task allocation, and user-calibrated autonomy is directly relevant to scalable humanoid deployment. Intuitive verbal instruction can reduce programming and setup overhead on factory or service floors, where operators may need to redirect humanoid robots quickly without specialized interfaces. The findings on user expectations and conversational strategies therefore provide useful design guidance for future humanoid systems that rely on LLM-based voice interaction.
