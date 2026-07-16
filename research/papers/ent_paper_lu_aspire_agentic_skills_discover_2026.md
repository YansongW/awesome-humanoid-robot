---
$id: ent_paper_lu_aspire_agentic_skills_discover_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASPIRE: Agentic Skills Discovery for Robotics'
  zh: ASPIRE：面向机器人的自主技能发现
  ko: 'ASPIRE: Agentic Skills Discovery for Robotics'
summary:
  en: ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy
    robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained
    multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that
    explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon
    household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real
    transfer across embodiments.
  zh: ASPIRE 是一个面向机器人的自改进持续学习系统，能够根据执行反馈自动编写并迭代优化 code-as-policy 机器人控制程序。它由三部分组成：暴露细粒度多模态追踪的闭环机器人执行引擎、不断积累可复用修复策略的技能库，以及超越单轨迹优化的进化搜索过程。在操作、双手交接和长程家庭任务基准上，ASPIRE
    显著优于现有 VLA 和 coding-agent 基线，并展现了跨本体的初步 sim-to-real 迁移能力。
  ko: ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy
    robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained
    multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that
    explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon
    household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real
    transfer across embodiments.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- robotics
- agentic
- skill_discovery
- code_as_policy
- continual_learning
- sim_to_real
- nvidia
- gear
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00272v1.
sources:
- id: src_001
  type: website
  title: 'ASPIRE: Agentic Skills Discovery for Robotics (NVIDIA GEAR)'
  url: https://research.nvidia.com/labs/gear/aspire/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## 核心内容
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## 参考
- http://arxiv.org/abs/2607.00272v1

## Overview
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## Content
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## 개요
전통적인 로봇 프로그래밍은 다중 모달 인식을 조율하고, 물리적 접촉 역학을 관리하며, 다양한 구성과 실행 실패를 처리해야 하기 때문에 어렵습니다. 우리는 ASPIRE(Agentic Skill Programming through Iterative Robot Exploration)를 소개합니다. 이는 코드-정책 패러다임에서 로봇 제어 프로그램을 자율적으로 작성하고 개선하며, 경험을 재사용 가능한 스킬 라이브러리로 축적하는 지속적 학습 시스템입니다. ASPIRE는 작업, 시뮬레이션 및 실제 환경, 그리고 로봇 플랫폼에 걸쳐 지속되는 스킬을 발견합니다. 이는 세 가지 구성 요소로 이루어진 개방형 루프에서 작동합니다: (1) 세분화된 다중 모달 추적을 노출하여 자율적인 실패 진단, 수리 합성 및 검증을 가능하게 하는 폐쇄 루프 로봇 실행 엔진, (2) 검증된 수정 사항을 재사용 가능하고 전이 가능한 지식으로 정제하는 지속적으로 확장되는 스킬 라이브러리, (3) 단일 궤적 개선을 넘어 탐색하기 위해 다양한 작업 시퀀스와 제어 프로그램을 생성하는 진화적 탐색입니다. ASPIRE는 LIBERO-Pro 조작(교란 하에서)에서 최대 77%, Robosuite 양손 핸드오버에서 72%, BEHAVIOR-1K 장기 가사 작업에서 32%까지 이전 방법을 능가합니다. 축적된 라이브러리는 또한 보지 못한 장기 작업에 대한 제로샷 일반화를 가능하게 합니다: LIBERO-Pro Long에서 ASPIRE는 31%의 성공률을 달성한 반면, 이전 방법은 테스트 시간 추론 및 재시도를 사용함에도 불구하고 4%에 그쳤습니다. 마지막으로, 시뮬레이션에서 발견된 스킬은 시뮬레이션-실제 전이의 초기 증거를 제공하며, 다양한 로봇 플랫폼과 로봇 API에서 실제 로봇 프로그래밍 노력을 크게 줄입니다.

## 핵심 내용
전통적인 로봇 프로그래밍은 다중 모달 인식을 조율하고, 물리적 접촉 역학을 관리하며, 다양한 구성과 실행 실패를 처리해야 하기 때문에 어렵습니다. 우리는 ASPIRE(Agentic Skill Programming through Iterative Robot Exploration)를 소개합니다. 이는 코드-정책 패러다임에서 로봇 제어 프로그램을 자율적으로 작성하고 개선하며, 경험을 재사용 가능한 스킬 라이브러리로 축적하는 지속적 학습 시스템입니다. ASPIRE는 작업, 시뮬레이션 및 실제 환경, 그리고 로봇 플랫폼에 걸쳐 지속되는 스킬을 발견합니다. 이는 세 가지 구성 요소로 이루어진 개방형 루프에서 작동합니다: (1) 세분화된 다중 모달 추적을 노출하여 자율적인 실패 진단, 수리 합성 및 검증을 가능하게 하는 폐쇄 루프 로봇 실행 엔진, (2) 검증된 수정 사항을 재사용 가능하고 전이 가능한 지식으로 정제하는 지속적으로 확장되는 스킬 라이브러리, (3) 단일 궤적 개선을 넘어 탐색하기 위해 다양한 작업 시퀀스와 제어 프로그램을 생성하는 진화적 탐색입니다. ASPIRE는 LIBERO-Pro 조작(교란 하에서)에서 최대 77%, Robosuite 양손 핸드오버에서 72%, BEHAVIOR-1K 장기 가사 작업에서 32%까지 이전 방법을 능가합니다. 축적된 라이브러리는 또한 보지 못한 장기 작업에 대한 제로샷 일반화를 가능하게 합니다: LIBERO-Pro Long에서 ASPIRE는 31%의 성공률을 달성한 반면, 이전 방법은 테스트 시간 추론 및 재시도를 사용함에도 불구하고 4%에 그쳤습니다. 마지막으로, 시뮬레이션에서 발견된 스킬은 시뮬레이션-실제 전이의 초기 증거를 제공하며, 다양한 로봇 플랫폼과 로봇 API에서 실제 로봇 프로그래밍 노력을 크게 줄입니다.
