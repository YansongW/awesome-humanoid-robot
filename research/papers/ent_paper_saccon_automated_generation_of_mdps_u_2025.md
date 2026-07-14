---
$id: ent_paper_saccon_automated_generation_of_mdps_u_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications
  zh: 利用逻辑编程与大语言模型自动生成机器人应用中的马尔可夫决策过程
  ko: 논리 프로그래밍과 대형 언어 모델을 활용한 로봇 응용을 위한 MDP 자동 생성
summary:
  en: This paper presents a framework that combines few-shot-prompted large language models with Prolog-based knowledge extraction,
    reachability analysis, and the Storm model checker to automatically generate Markov Decision Processes and executable
    policies from natural-language robotic scenario descriptions.
  zh: 本研究提出一个框架，结合少样本提示的大语言模型、基于Prolog的知识抽取、可达性分析与Storm模型检测器，从自然语言描述的机器人场景中自动生成马尔可夫决策过程及可执行策略。
  ko: 본 논문은 소수 샘플 프롬프트된 대형 언어 모델, Prolog 기반 지식 추출, 도달 가능성 분석 및 Storm 모델 검사기를 결합하여 자연어로 기술된 로봇 시나리오에서 마르코프 결정 과정과 실행 가능한 정책을
    자동 생성하는 프레임워크를 제시한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- mdp_generation
- probabilistic_planning
- policy_synthesis
- llm_knowledge_extraction
- prolog
- storm_model_checker
- formal_verification
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23143v1.
sources:
- id: src_001
  type: paper
  title: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications
  url: https://arxiv.org/abs/2511.23143
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

## 核心内容
We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

## 参考
- http://arxiv.org/abs/2511.23143v1

