---
$id: ent_paper_hu_deploying_and_evaluating_llms_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deploying and Evaluating LLMs to Program Service Mobile Robots
  zh: 部署与评估用于服务移动机器人编程的大语言模型
  ko: 서비스 모바일 로봇 프로그래밍을 위한 LLM 배포 및 평가
summary:
  en: Introduces CODEBOTLER, an open-source, robot-agnostic tool that few-shot prompts
    LLMs to generate programs for service mobile robots using a Python eDSL over skill
    abstractions, and ROBOEVAL, a symbolic-simulation benchmark that checks generated
    programs against temporal-logic correctness properties across multiple prompts
    and initial states.
  zh: 提出 CODEBOTLER，一个开源且与机器人无关的工具，通过少样本提示大语言模型，使用基于技能抽象的 Python 嵌入式领域特定语言为服务移动机器人生成程序；并提出
    ROBOEVAL，一个符号仿真基准，通过多提示与多初始状态检验生成程序是否满足时序逻辑正确性属性。
  ko: 로봇에 무관한 오픈소스 도구 CODEBOTLER를 제안하며, Python eDSL을 기반으로 한 기술 추상화를 통해 서비스 모바일 로봇용
    프로그램을 생성하도록 LLM을 퓨샷 프롬프팅하고, ROBOEVAL이라는 기호 시뮬레이션 벤치마크로 다양한 프롬프트와 초기 상태에서 생성된 프로그램의
    시간 논리적 정답 속성을 검증한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
- tool_equipment
tags:
- llm
- program_synthesis
- robot_programming
- service_robot
- mobile_robot
- skill_abstraction
- edsl
- temporal_logic
- benchmark
- simulation
- natural_language_programming
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review before
    full verification.
sources:
- id: src_001
  type: paper
  title: Deploying and Evaluating LLMs to Program Service Mobile Robots
  url: https://arxiv.org/abs/2311.11183
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper investigates the use of large language models (LLMs) to generate executable programs for service mobile robots from natural-language instructions. The authors identify that accurate sequencing and ordering of actions—leveraging mobility, perception, and human interaction skills—is crucial for reliable task completion in home and office service scenarios. To address this, they present CODEBOTLER, an open-source, robot-agnostic tool that few-shot prompts an LLM to synthesize programs in a Python-embedded domain-specific language (eDSL). The eDSL abstracts robot capabilities as skills such as go_to, pick, place, ask, say, and perception helpers like get_current_location and is_in_room, enabling deployment on any general-purpose mobile robot that exposes compatible skill interfaces.

The paper also introduces ROBOEVAL, a benchmark for evaluating LLM-generated robot programs. ROBOEVAL uses a symbolic simulator to execute generated programs from multiple initial world states and checks the resulting traces against temporal logic properties that encode task-specific correctness. Each task includes multiple paraphrased prompts to test robustness of program generation across linguistic variation. The authors evaluate several state-of-the-art LLMs and analyze failure modes, resulting in a taxonomy of common pitfalls such as incorrect action ordering, missing actions, hallucinated objects or locations, and condition-handling errors. A rejection-sampling mechanism uses simulation to filter out programs that would produce Python or robot execution errors before deployment.

## Key Contributions

- CODEBOTLER: an open-source, robot-agnostic natural-language programming tool for service mobile robots.
- ROBOEVAL: a benchmark evaluating LLM-generated robot programs via symbolic simulation, multiple initial states, and temporal-logic correctness checks.
- A comprehensive taxonomy and empirical analysis of failure modes for LLM-generated robot programs.
- A rejection-sampling mechanism that uses simulation to reduce Python runtime and robot execution errors before deployment.

## Relevance to Humanoid Robotics

Although the experiments focus on service mobile robots rather than bipedal humanoids, the toolchain is explicitly designed to be robot-agnostic. The skill-abstraction layer, the LLM program-generation pipeline, and the simulation-based verification workflow are all directly transferable to humanoid robots operating in home service and automation contexts. Humanoid platforms must likewise sequence mobility, manipulation, perception, and human-interaction skills from natural-language instructions, and they face similar failure modes around ordering, hallucination, and environmental assumptions. The ROBOEVAL framework could therefore be adapted to evaluate LLM-generated behavior for humanoid robots by defining appropriate skill abstractions and temporal-logic task specifications.
