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
  en: Introduces CODEBOTLER, an open-source, robot-agnostic tool that few-shot prompts LLMs to generate programs for service
    mobile robots using a Python eDSL over skill abstractions, and ROBOEVAL, a symbolic-simulation benchmark that checks generated
    programs against temporal-logic correctness properties across multiple prompts and initial states.
  zh: 提出 CODEBOTLER，一个开源且与机器人无关的工具，通过少样本提示大语言模型，使用基于技能抽象的 Python 嵌入式领域特定语言为服务移动机器人生成程序；并提出 ROBOEVAL，一个符号仿真基准，通过多提示与多初始状态检验生成程序是否满足时序逻辑正确性属性。
  ko: 로봇에 무관한 오픈소스 도구 CODEBOTLER를 제안하며, Python eDSL을 기반으로 한 기술 추상화를 통해 서비스 모바일 로봇용 프로그램을 생성하도록 LLM을 퓨샷 프롬프팅하고, ROBOEVAL이라는
    기호 시뮬레이션 벤치마크로 다양한 프롬프트와 초기 상태에서 생성된 프로그램의 시간 논리적 정답 속성을 검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.11183v3.
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
## 概述
Recent advancements in large language models (LLMs) have spurred interest in using them for generating robot programs from natural language, with promising initial results. We investigate the use of LLMs to generate programs for service mobile robots leveraging mobility, perception, and human interaction skills, and where accurate sequencing and ordering of actions is crucial for success. We contribute CodeBotler, an open-source robot-agnostic tool to program service mobile robots from natural language, and RoboEval, a benchmark for evaluating LLMs' capabilities of generating programs to complete service robot tasks. CodeBotler performs program generation via few-shot prompting of LLMs with an embedded domain-specific language (eDSL) in Python, and leverages skill abstractions to deploy generated programs on any general-purpose mobile robot. RoboEval evaluates the correctness of generated programs by checking execution traces starting with multiple initial states, and checking whether the traces satisfy temporal logic properties that encode correctness for each task. RoboEval also includes multiple prompts per task to test for the robustness of program generation. We evaluate several popular state-of-the-art LLMs with the RoboEval benchmark, and perform a thorough analysis of the modes of failures, resulting in a taxonomy that highlights common pitfalls of LLMs at generating robot programs. We release our code and benchmark at https://amrl.cs.utexas.edu/codebotler/.

## 核心内容
Recent advancements in large language models (LLMs) have spurred interest in using them for generating robot programs from natural language, with promising initial results. We investigate the use of LLMs to generate programs for service mobile robots leveraging mobility, perception, and human interaction skills, and where accurate sequencing and ordering of actions is crucial for success. We contribute CodeBotler, an open-source robot-agnostic tool to program service mobile robots from natural language, and RoboEval, a benchmark for evaluating LLMs' capabilities of generating programs to complete service robot tasks. CodeBotler performs program generation via few-shot prompting of LLMs with an embedded domain-specific language (eDSL) in Python, and leverages skill abstractions to deploy generated programs on any general-purpose mobile robot. RoboEval evaluates the correctness of generated programs by checking execution traces starting with multiple initial states, and checking whether the traces satisfy temporal logic properties that encode correctness for each task. RoboEval also includes multiple prompts per task to test for the robustness of program generation. We evaluate several popular state-of-the-art LLMs with the RoboEval benchmark, and perform a thorough analysis of the modes of failures, resulting in a taxonomy that highlights common pitfalls of LLMs at generating robot programs. We release our code and benchmark at https://amrl.cs.utexas.edu/codebotler/.

## 参考
- http://arxiv.org/abs/2311.11183v3

## Overview
Recent advancements in large language models (LLMs) have spurred interest in using them for generating robot programs from natural language, with promising initial results. We investigate the use of LLMs to generate programs for service mobile robots leveraging mobility, perception, and human interaction skills, and where accurate sequencing and ordering of actions is crucial for success. We contribute CodeBotler, an open-source robot-agnostic tool to program service mobile robots from natural language, and RoboEval, a benchmark for evaluating LLMs' capabilities of generating programs to complete service robot tasks. CodeBotler performs program generation via few-shot prompting of LLMs with an embedded domain-specific language (eDSL) in Python, and leverages skill abstractions to deploy generated programs on any general-purpose mobile robot. RoboEval evaluates the correctness of generated programs by checking execution traces starting with multiple initial states, and checking whether the traces satisfy temporal logic properties that encode correctness for each task. RoboEval also includes multiple prompts per task to test for the robustness of program generation. We evaluate several popular state-of-the-art LLMs with the RoboEval benchmark, and perform a thorough analysis of the modes of failures, resulting in a taxonomy that highlights common pitfalls of LLMs at generating robot programs. We release our code and benchmark at https://amrl.cs.utexas.edu/codebotler/.

## Content
Recent advancements in large language models (LLMs) have spurred interest in using them for generating robot programs from natural language, with promising initial results. We investigate the use of LLMs to generate programs for service mobile robots leveraging mobility, perception, and human interaction skills, and where accurate sequencing and ordering of actions is crucial for success. We contribute CodeBotler, an open-source robot-agnostic tool to program service mobile robots from natural language, and RoboEval, a benchmark for evaluating LLMs' capabilities of generating programs to complete service robot tasks. CodeBotler performs program generation via few-shot prompting of LLMs with an embedded domain-specific language (eDSL) in Python, and leverages skill abstractions to deploy generated programs on any general-purpose mobile robot. RoboEval evaluates the correctness of generated programs by checking execution traces starting with multiple initial states, and checking whether the traces satisfy temporal logic properties that encode correctness for each task. RoboEval also includes multiple prompts per task to test for the robustness of program generation. We evaluate several popular state-of-the-art LLMs with the RoboEval benchmark, and perform a thorough analysis of the modes of failures, resulting in a taxonomy that highlights common pitfalls of LLMs at generating robot programs. We release our code and benchmark at https://amrl.cs.utexas.edu/codebotler/.

## 개요
최근 대규모 언어 모델(LLM)의 발전으로 자연어로부터 로봇 프로그램을 생성하는 데 이를 활용하려는 관심이 높아지고 있으며, 초기 결과도 유망합니다. 본 연구에서는 이동성, 인식 및 인간 상호작용 기술을 활용하는 서비스 모바일 로봇을 위한 프로그램을 생성하는 데 LLM을 사용하는 방법을 조사하며, 특히 정확한 동작 순서와 배열이 성공에 중요한 요소입니다. 우리는 자연어로 서비스 모바일 로봇을 프로그래밍할 수 있는 오픈소스 로봇 독립 도구인 CodeBotler와, 서비스 로봇 작업을 완료하기 위한 프로그램 생성 능력을 평가하는 벤치마크인 RoboEval을 제공합니다. CodeBotler는 Python에 내장된 도메인 특화 언어(eDSL)를 사용한 퓨샷 프롬프팅을 통해 프로그램을 생성하며, 스킬 추상화를 활용하여 생성된 프로그램을 모든 범용 모바일 로봇에 배포합니다. RoboEval은 여러 초기 상태에서 시작하는 실행 추적을 확인하고, 각 작업의 정확성을 인코딩하는 시간 논리 속성을 추적이 충족하는지 검사하여 생성된 프로그램의 정확성을 평가합니다. 또한 RoboEval은 작업당 여러 프롬프트를 포함하여 프로그램 생성의 견고성을 테스트합니다. 우리는 RoboEval 벤치마크를 사용하여 여러 인기 있는 최신 LLM을 평가하고, 실패 모드에 대한 철저한 분석을 수행하여 LLM이 로봇 프로그램 생성 시 자주 범하는 함정을 강조하는 분류 체계를 도출했습니다. 코드와 벤치마크는 https://amrl.cs.utexas.edu/codebotler/에서 공개합니다.

## 핵심 내용
최근 대규모 언어 모델(LLM)의 발전으로 자연어로부터 로봇 프로그램을 생성하는 데 이를 활용하려는 관심이 높아지고 있으며, 초기 결과도 유망합니다. 본 연구에서는 이동성, 인식 및 인간 상호작용 기술을 활용하는 서비스 모바일 로봇을 위한 프로그램을 생성하는 데 LLM을 사용하는 방법을 조사하며, 특히 정확한 동작 순서와 배열이 성공에 중요한 요소입니다. 우리는 자연어로 서비스 모바일 로봇을 프로그래밍할 수 있는 오픈소스 로봇 독립 도구인 CodeBotler와, 서비스 로봇 작업을 완료하기 위한 프로그램 생성 능력을 평가하는 벤치마크인 RoboEval을 제공합니다. CodeBotler는 Python에 내장된 도메인 특화 언어(eDSL)를 사용한 퓨샷 프롬프팅을 통해 프로그램을 생성하며, 스킬 추상화를 활용하여 생성된 프로그램을 모든 범용 모바일 로봇에 배포합니다. RoboEval은 여러 초기 상태에서 시작하는 실행 추적을 확인하고, 각 작업의 정확성을 인코딩하는 시간 논리 속성을 추적이 충족하는지 검사하여 생성된 프로그램의 정확성을 평가합니다. 또한 RoboEval은 작업당 여러 프롬프트를 포함하여 프로그램 생성의 견고성을 테스트합니다. 우리는 RoboEval 벤치마크를 사용하여 여러 인기 있는 최신 LLM을 평가하고, 실패 모드에 대한 철저한 분석을 수행하여 LLM이 로봇 프로그램 생성 시 자주 범하는 함정을 강조하는 분류 체계를 도출했습니다. 코드와 벤치마크는 https://amrl.cs.utexas.edu/codebotler/에서 공개합니다.
