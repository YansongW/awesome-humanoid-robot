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
  zh: 'arXiv:2510.17801v2 Announce Type: replace Abstract: Building robots that can perceive, reason, and act in dynamic,
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17801v2.
sources:
- id: src_001
  type: paper
  title: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain (arXiv)'
  url: https://arxiv.org/abs/2510.17801
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain, the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust robotic intelligence.

## 核心内容
Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain, the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust robotic intelligence.

## 参考
- http://arxiv.org/abs/2510.17801v2

## Overview
Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain, the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust robotic intelligence.

## Content
Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain, the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust robotic intelligence.

## 개요
동적이고 비구조화된 환경에서 인지, 추론, 행동할 수 있는 로봇을 구축하는 것은 여전히 핵심 과제로 남아 있습니다. 최근의 구현형 시스템은 종종 이중 시스템 패러다임을 따르는데, System 2는 고수준 추론을 수행하고 System 1은 저수준 제어를 담당합니다. 우리는 System 2를 구현형 두뇌, 즉 조작 과정에서 의사 결정을 위한 인지적 핵심이라고 부릅니다. 이러한 구현형 두뇌를 평가하는 것은 중요하지만, 기존 벤치마크는 주로 실행 성공 여부를 측정하거나 고수준 인지 및 작업 현실성의 제한된 측면만을 다룹니다. 우리는 구현형 두뇌로서의 다중 모달 대규모 언어 모델(MLLM)을 평가하기 위한 벤치마크인 RoboBench를 소개합니다. RoboBench는 지시 이해, 지각 추론, 일반화 계획, 행동 가능성 예측, 실패 분석의 다섯 가지 차원을 다룹니다. 14가지 능력, 25가지 작업, 6,092개의 QA 쌍으로 구성됩니다. 현실성을 높이기 위해, 다양한 구현체, 속성이 풍부한 객체, 다중 시점 장면, 메모리 기반 내비게이션에 걸친 대규모 실제 로봇 데이터와 자체 수집 데이터를 활용합니다. 계획 측면에서 RoboBench는 MLLM-세계-시뮬레이터 프레임워크를 도입하여, 예측된 계획이 물리적 및 시각적 제약 하에서 중요한 객체 상태 변화를 달성할 수 있는지 평가함으로써, 기호적 매칭보다 장기 추론의 더 신뢰성 있는 평가를 가능하게 합니다. 18개의 최첨단 MLLM에 대한 실험은 암시적 지시 이해, 시공간 추론, 교차 시나리오 계획, 세분화된 행동 가능성 이해, 실패 진단에서 지속적인 한계를 드러냅니다. 우리는 또한 구현형 인지 능력이 하위 로봇 제어와 어떻게 관련되는지 분석합니다. RoboBench는 고수준 인지를 정량화하고 차세대 MLLM을 보다 강력한 로봇 지능으로 안내하기 위한 포괄적인 프레임워크를 제공합니다.

## 핵심 내용
동적이고 비구조화된 환경에서 인지, 추론, 행동할 수 있는 로봇을 구축하는 것은 여전히 핵심 과제로 남아 있습니다. 최근의 구현형 시스템은 종종 이중 시스템 패러다임을 따르는데, System 2는 고수준 추론을 수행하고 System 1은 저수준 제어를 담당합니다. 우리는 System 2를 구현형 두뇌, 즉 조작 과정에서 의사 결정을 위한 인지적 핵심이라고 부릅니다. 이러한 구현형 두뇌를 평가하는 것은 중요하지만, 기존 벤치마크는 주로 실행 성공 여부를 측정하거나 고수준 인지 및 작업 현실성의 제한된 측면만을 다룹니다. 우리는 구현형 두뇌로서의 다중 모달 대규모 언어 모델(MLLM)을 평가하기 위한 벤치마크인 RoboBench를 소개합니다. RoboBench는 지시 이해, 지각 추론, 일반화 계획, 행동 가능성 예측, 실패 분석의 다섯 가지 차원을 다룹니다. 14가지 능력, 25가지 작업, 6,092개의 QA 쌍으로 구성됩니다. 현실성을 높이기 위해, 다양한 구현체, 속성이 풍부한 객체, 다중 시점 장면, 메모리 기반 내비게이션에 걸친 대규모 실제 로봇 데이터와 자체 수집 데이터를 활용합니다. 계획 측면에서 RoboBench는 MLLM-세계-시뮬레이터 프레임워크를 도입하여, 예측된 계획이 물리적 및 시각적 제약 하에서 중요한 객체 상태 변화를 달성할 수 있는지 평가함으로써, 기호적 매칭보다 장기 추론의 더 신뢰성 있는 평가를 가능하게 합니다. 18개의 최첨단 MLLM에 대한 실험은 암시적 지시 이해, 시공간 추론, 교차 시나리오 계획, 세분화된 행동 가능성 이해, 실패 진단에서 지속적인 한계를 드러냅니다. 우리는 또한 구현형 인지 능력이 하위 로봇 제어와 어떻게 관련되는지 분석합니다. RoboBench는 고수준 인지를 정량화하고 차세대 MLLM을 보다 강력한 로봇 지능으로 안내하기 위한 포괄적인 프레임워크를 제공합니다.
