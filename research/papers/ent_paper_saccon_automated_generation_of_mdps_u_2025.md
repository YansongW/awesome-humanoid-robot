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
  en: This paper presents a framework that combines few-shot-prompted large language
    models with Prolog-based knowledge extraction, reachability analysis, and the
    Storm model checker to automatically generate Markov Decision Processes and executable
    policies from natural-language robotic scenario descriptions.
  zh: 本研究提出一个框架，结合少样本提示的大语言模型、基于Prolog的知识抽取、可达性分析与Storm模型检测器，从自然语言描述的机器人场景中自动生成马尔可夫决策过程及可执行策略。
  ko: 본 논문은 소수 샘플 프롬프트된 대형 언어 모델, Prolog 기반 지식 추출, 도달 가능성 분석 및 Storm 모델 검사기를 결합하여
    자연어로 기술된 로봇 시나리오에서 마르코프 결정 과정과 실행 가능한 정책을 자동 생성하는 프레임워크를 제시한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    and human review are needed before promotion to verified.; approved by autonomous
    review workflow.
sources:
- id: src_001
  type: paper
  title: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic
    Applications
  url: https://arxiv.org/abs/2511.23143
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper introduces an integrated framework that closes the gap between informal natural-language descriptions of robotic tasks and the formal models required by probabilistic planners. It first prompts a large language model with few-shot examples to translate natural-language scenario descriptions into a structured Prolog knowledge base. Then, through reachability analysis and probability refinement, it constructs a Markov Decision Process (MDP) that captures the states, actions, transitions, and rewards of the scenario. Finally, it uses the Storm model checker to synthesize an optimal policy and exports the policy as an executable state-action table.

## Key Contributions

- LLM-driven extraction of Prolog knowledge bases from informal natural-language scenario descriptions.
- Automatic MDP construction from a Prolog knowledge base through reachability analysis and probability refinement.
- Policy synthesis using the Storm model checker with export to executable state-action tables.
- Distinction between necessary and sufficient reward conditions to separate hard constraints from soft preferences.
- Experimental validation on three domains: collaborative structure building, industrial AGV traffic management, and UR5e gripper manipulation.

## Relevance to Humanoid Robotics

Although the validation scenarios involve industrial manipulators and mobile robots rather than bipedal humanoids, the framework is directly relevant to humanoid robotics. It enables domain experts to specify uncertain, interactive human-robot behaviors in plain language and automatically obtain formally verifiable, executable policies. This can accelerate behavior-authoring pipelines for humanoid robots operating in collaborative industrial or assistive settings.
