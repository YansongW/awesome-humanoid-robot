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

