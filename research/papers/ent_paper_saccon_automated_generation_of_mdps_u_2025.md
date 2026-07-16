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

## Overview
We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

## Content
We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

## 개요
본 논문에서는 대규모 언어 모델(LLM)과 자동 계획 및 형식 검증을 통합하여 마르코프 결정 과정(MDP)의 생성과 사용을 간소화하는 새로운 프레임워크를 제시합니다. 우리 시스템은 LLM을 활용하여 자연어(NL) 설명으로부터 Prolog 지식 베이스 형태의 구조화된 지식을 추출합니다. 그런 다음 도달 가능성 분석을 통해 자동으로 MDP를 구축하고, Storm 모델 검사기를 사용하여 최적 정책을 합성합니다. 결과 정책은 실행을 위해 상태-행동 테이블로 내보내집니다. 우리는 세 가지 인간-로봇 상호작용 시나리오에서 프레임워크를 검증하여 최소한의 수동 노력으로 실행 가능한 정책을 생성할 수 있음을 입증합니다. 이 연구는 언어 모델과 형식 방법을 결합하여 로봇 공학에서 보다 접근 가능하고 확장 가능한 확률적 계획을 가능하게 하는 잠재력을 강조합니다.

## 핵심 내용
본 논문에서는 대규모 언어 모델(LLM)과 자동 계획 및 형식 검증을 통합하여 마르코프 결정 과정(MDP)의 생성과 사용을 간소화하는 새로운 프레임워크를 제시합니다. 우리 시스템은 LLM을 활용하여 자연어(NL) 설명으로부터 Prolog 지식 베이스 형태의 구조화된 지식을 추출합니다. 그런 다음 도달 가능성 분석을 통해 자동으로 MDP를 구축하고, Storm 모델 검사기를 사용하여 최적 정책을 합성합니다. 결과 정책은 실행을 위해 상태-행동 테이블로 내보내집니다. 우리는 세 가지 인간-로봇 상호작용 시나리오에서 프레임워크를 검증하여 최소한의 수동 노력으로 실행 가능한 정책을 생성할 수 있음을 입증합니다. 이 연구는 언어 모델과 형식 방법을 결합하여 로봇 공학에서 보다 접근 가능하고 확장 가능한 확률적 계획을 가능하게 하는 잠재력을 강조합니다.
