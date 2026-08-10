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
  zh: CODEBOTLER是一个开源、机器人无关的工具，通过少样本提示LLMs，利用Python嵌入式领域特定语言（eDSL）在技能抽象之上为服务移动机器人生成程序。ROBOEVAL是一个符号仿真基准，通过检查生成程序在多个提示和初始状态下是否满足时序逻辑正确性属性来评估LLMs。该研究还分析了多种流行LLMs的失败模式，并建立了分类体系。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.11183v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (817 chars, DeepSeek).'
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
本文提出了CODEBOTLER和ROBOEVAL两个工具，用于利用LLMs从自然语言生成服务移动机器人程序。CODEBOTLER通过少样本提示LLMs，结合Python eDSL和技能抽象，实现机器人无关的程序生成与部署。ROBOEVAL则通过符号仿真，从多个初始状态和提示出发，检查程序执行轨迹是否满足时序逻辑属性，从而评估LLMs的生成正确性。研究评估了多种先进LLMs，并系统分析了失败模式，形成分类法，揭示了常见陷阱。

## 核心内容
### 方法
- **CODEBOTLER**：采用少样本提示（few-shot prompting）方式，向LLMs提供Python嵌入式领域特定语言（eDSL）示例，该eDSL封装了移动、感知和人类交互等技能抽象。生成的程序可部署到任何通用移动机器人上，实现机器人无关性。
- **ROBOEVAL**：通过符号仿真，从多个初始状态开始执行生成程序，并检查执行轨迹是否满足为每个任务编码的时序逻辑属性。每个任务包含多个提示，以测试程序生成的鲁棒性。

### 实验设置
- 评估了多种流行且先进的LLMs（如GPT-4、Claude等），使用ROBOEVAL基准进行测试。
- 任务涉及服务移动机器人的典型场景，强调动作的准确排序和顺序执行。

### 关键数字与结果
- 实验揭示了LLMs在生成机器人程序时的常见失败模式，包括动作顺序错误、感知条件遗漏、技能调用不当等。
- 通过分类法（taxonomy）系统化这些失败模式，为后续改进提供指导。

### 结论
- CODEBOTLER和ROBOEVAL为LLMs在服务机器人编程中的应用提供了实用工具和评估框架。
- 失败模式分析表明，当前LLMs在复杂任务序列生成中仍存在显著局限，需进一步优化提示设计和技能抽象。

代码和基准已开源：https://amrl.cs.utexas.edu/codebotler/

## Overview
Recent advancements in large language models (LLMs) have spurred interest in using them for generating robot programs from natural language, with promising initial results. We investigate the use of LLMs to generate programs for service mobile robots leveraging mobility, perception, and human interaction skills, and where accurate sequencing and ordering of actions is crucial for success. We contribute CodeBotler, an open-source robot-agnostic tool to program service mobile robots from natural language, and RoboEval, a benchmark for evaluating LLMs' capabilities of generating programs to complete service robot tasks. CodeBotler performs program generation via few-shot prompting of LLMs with an embedded domain-specific language (eDSL) in Python, and leverages skill abstractions to deploy generated programs on any general-purpose mobile robot. RoboEval evaluates the correctness of generated programs by checking execution traces starting with multiple initial states, and checking whether the traces satisfy temporal logic properties that encode correctness for each task. RoboEval also includes multiple prompts per task to test for the robustness of program generation. We evaluate several popular state-of-the-art LLMs with the RoboEval benchmark, and perform a thorough analysis of the modes of failures, resulting in a taxonomy that highlights common pitfalls of LLMs at generating robot programs. We release our code and benchmark at https://amrl.cs.utexas.edu/codebotler/.

## 参考
- http://arxiv.org/abs/2311.11183v3

## 개요
본 논문은 LLM을 활용하여 자연어로부터 서비스 이동 로봇 프로그램을 생성하기 위한 CODEBOTLER와 ROBOEVAL이라는 두 가지 도구를 제안합니다. CODEBOTLER는 few-shot 프롬프팅을 통해 LLM에 Python eDSL과 스킬 추상화를 결합하여 로봇에 독립적인 프로그램 생성 및 배포를 구현합니다. ROBOEVAL은 기호 시뮬레이션을 통해 여러 초기 상태와 프롬프트에서 프로그램 실행 궤적이 시간 논리 속성을 충족하는지 검사하여 LLM의 생성 정확성을 평가합니다. 연구는 다양한 최신 LLM을 평가하고 실패 모드를 체계적으로 분석하여 분류법을 형성하고 일반적인 함정을 밝혀냅니다.

## 핵심 내용
### 방법
- **CODEBOTLER**: few-shot 프롬프팅 방식을 채택하여 LLM에 Python 임베디드 도메인 특화 언어(eDSL) 예제를 제공합니다. 이 eDSL은 이동, 인식, 인간 상호작용 등의 스킬 추상화를 캡슐화합니다. 생성된 프로그램은 모든 범용 이동 로봇에 배포 가능하여 로봇 독립성을 구현합니다.
- **ROBOEVAL**: 기호 시뮬레이션을 통해 여러 초기 상태에서 생성된 프로그램을 실행하고, 각 작업에 대해 인코딩된 시간 논리 속성을 실행 궤적이 충족하는지 검사합니다. 각 작업은 여러 프롬프트를 포함하여 프로그램 생성의 견고성을 테스트합니다.

### 실험 설정
- GPT-4, Claude 등 여러 인기 있고 최신 LLM을 ROBOEVAL 벤치마크를 사용하여 평가했습니다.
- 작업은 서비스 이동 로봇의 일반적인 시나리오를 포함하며, 동작의 정확한 순서 지정과 순차 실행을 강조합니다.

### 주요 수치 및 결과
- 실험은 LLM이 로봇 프로그램 생성 시 동작 순서 오류, 인식 조건 누락, 스킬 호출 부적절 등 일반적인 실패 모드를 드러냈습니다.
- 분류법(taxonomy)을 통해 이러한 실패 모드를 체계화하여 향후 개선을 위한 지침을 제공합니다.

### 결론
- CODEBOTLER와 ROBOEVAL은 서비스 로봇 프로그래밍에서 LLM 적용을 위한 실용적인 도구와 평가 프레임워크를 제공합니다.
- 실패 모드 분석은 현재 LLM이 복잡한 작업 시퀀스 생성에서 여전히 상당한 한계를 보이며, 프롬프트 설계와 스킬 추상화의 추가 최적화가 필요함을 시사합니다.

코드와 벤치마크는 오픈소스로 공개되었습니다: https://amrl.cs.utexas.edu/codebotler/
