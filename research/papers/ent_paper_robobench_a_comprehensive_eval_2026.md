---
$id: ent_paper_robobench_a_comprehensive_eval_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
  zh: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
  ko: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
summary:
  en: 'arXiv:2510.17801v2 Announce Type: replace Abstract: Building robots that can perceive, reason, and act in dynamic,
    unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where
    System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain,
    the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks
    mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce
    RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five
    dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure
    Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic
    data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven
    navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans
    can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of
    long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations
    in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding,
    and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench
    offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust
    robotic intelligence.'
  zh: RoboBench 是一个用于评估多模态大语言模型作为具身大脑的综合基准，由研究团队提出。它覆盖指令理解、感知推理、广义规划、功能预测和故障分析五个维度，包含 14 种能力、25 个任务和 6,092 个问答对。该基准通过引入 MLLM-as-world-simulator
    框架，在物理和视觉约束下评估长期规划，揭示了现有 MLLM 在隐式指令理解、时空推理等方面的持续局限。
  ko: 'arXiv:2510.17801v2 Announce Type: replace Abstract: Building robots that can perceive, reason, and act in dynamic,
    unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where
    System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain,
    the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks
    mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce
    RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five
    dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure
    Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic
    data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven
    navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans
    can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of
    long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations
    in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding,
    and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench
    offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust
    robotic intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- robobench
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17801v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (980 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain (arXiv)'
  url: https://arxiv.org/abs/2510.17801
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
RoboBench 旨在解决现有基准仅测量执行成功率或覆盖有限高级认知和任务真实性的问题。它从大规模真实机器人数据和内部收集的多形态、属性丰富物体、多视角场景及记忆驱动导航数据中提取内容，以提升现实性。在规划评估上，RoboBench 采用 MLLM-as-world-simulator 框架，检查预测计划能否在物理和视觉约束下实现关键物体状态变化，从而比符号匹配更忠实地评估长期推理。对 18 个最先进 MLLM 的实验显示，它们在隐式指令理解、时空推理、跨场景规划、细粒度功能理解和故障诊断方面存在持续不足。该基准还分析了具身认知能力与下游机器人控制的关系，为量化高级认知和指导下一代 MLLM 提供全面框架。

## 核心内容
### 背景与动机
构建能在动态非结构化环境中感知、推理和行动的机器人仍是核心挑战。当前具身系统常采用双系统范式：System 2 负责高级推理，System 1 处理低级控制。本文称 System 2 为具身大脑，即操作决策的认知核心。现有基准主要测量执行成功率，或仅覆盖高级认知和任务真实性的有限方面。

### RoboBench 基准设计
- **评估维度**：覆盖五个维度——指令理解、感知推理、广义规划、功能预测和故障分析。
- **规模**：包含 14 种能力、25 个任务和 6,092 个问答对。
- **数据来源**：为提升真实性，数据来自大规模真实机器人数据和内部收集，涵盖多种形态、属性丰富的物体、多视角场景和记忆驱动导航。

### 规划评估创新：MLLM-as-world-simulator
- 传统方法依赖符号匹配评估规划，但 RoboBench 引入 MLLM-as-world-simulator 框架。
- 该框架检查预测计划能否在物理和视觉约束下实现关键物体状态变化，从而更忠实地评估长期推理。

### 实验与发现
- 对 18 个最先进 MLLM 进行实验，揭示以下持续局限：
  - 隐式指令理解不足
  - 时空推理能力弱
  - 跨场景规划困难
  - 细粒度功能理解有限
  - 故障诊断能力差
- 进一步分析具身认知能力与下游机器人控制的关系。

### 结论
RoboBench 为量化高级认知提供全面框架，指导下一代 MLLM 向更鲁棒的机器人智能发展。

## Overview
Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain, the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust robotic intelligence.

## 参考
- http://arxiv.org/abs/2510.17801v2

## 개요
RoboBench는 기존 벤치마크가 실행 성공률만 측정하거나 제한된 고급 인지 및 작업 현실성만 다루는 문제를 해결하기 위해 설계되었습니다. 대규모 실제 로봇 데이터와 내부 수집을 통해 얻은 다형태(multi-modal), 속성 풍부 객체, 다중 시점 장면, 메모리 기반 내비게이션 데이터에서 콘텐츠를 추출하여 현실성을 높입니다. 계획 평가에서 RoboBench는 MLLM-as-world-simulator 프레임워크를 채택하여 예측된 계획이 물리적 및 시각적 제약 하에서 핵심 객체 상태 변화를 달성할 수 있는지 검사함으로써, 기호 매칭보다 장기 추론을 더 충실하게 평가합니다. 18개의 최첨단 MLLM에 대한 실험은 암시적 명령 이해, 시공간 추론, 교차 장면 계획, 세분화된 기능 이해, 오류 진단에서 지속적인 부족을 드러냅니다. 이 벤치마크는 또한 구현 인지 능력과 하위 로봇 제어 간의 관계를 분석하여 고급 인지 정량화와 차세대 MLLM 지침을 위한 포괄적인 프레임워크를 제공합니다.

## 핵심 내용
### 배경 및 동기
동적 비구조화 환경에서 인지, 추론, 행동할 수 있는 로봇 구축은 여전히 핵심 과제입니다. 현재 구현 시스템은 종종 이중 시스템 패러다임을 채택합니다: System 2는 고급 추론을 담당하고 System 1은 저수준 제어를 처리합니다. 본 논문은 System 2를 구현 뇌(embodied brain), 즉 조작 결정의 인지 핵심으로 부릅니다. 기존 벤치마크는 주로 실행 성공률을 측정하거나 고급 인지 및 작업 현실성의 제한된 측면만 다룹니다.

### RoboBench 벤치마크 설계
- **평가 차원**: 명령 이해, 지각 추론, 일반화 계획, 기능 예측, 오류 분석의 다섯 가지 차원을 다룹니다.
- **규모**: 14가지 능력, 25개 작업, 6,092개의 질문-답변 쌍을 포함합니다.
- **데이터 출처**: 현실성을 높이기 위해 대규모 실제 로봇 데이터와 내부 수집 데이터를 사용하며, 다양한 형태, 속성 풍부 객체, 다중 시점 장면, 메모리 기반 내비게이션을 포함합니다.

### 계획 평가 혁신: MLLM-as-world-simulator
- 전통적인 방법은 기호 매칭으로 계획을 평가하지만, RoboBench는 MLLM-as-world-simulator 프레임워크를 도입합니다.
- 이 프레임워크는 예측된 계획이 물리적 및 시각적 제약 하에서 핵심 객체 상태 변화를 달성할 수 있는지 검사하여 장기 추론을 더 충실하게 평가합니다.

### 실험 및 발견
- 18개의 최첨단 MLLM에 대한 실험은 다음과 같은 지속적인 한계를 드러냅니다:
  - 암시적 명령 이해 부족
  - 시공간 추론 능력 약화
  - 교차 장면 계획의 어려움
  - 세분화된 기능 이해 제한
  - 오류 진단 능력 부족
- 구현 인지 능력과 하위 로봇 제어 간의 관계를 추가로 분석합니다.

### 결론
RoboBench는 고급 인지 정량화를 위한 포괄적인 프레임워크를 제공하여 차세대 MLLM이 더 견고한 로봇 지능으로 발전하도록 안내합니다.
