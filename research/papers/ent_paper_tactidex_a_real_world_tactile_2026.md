---
$id: ent_paper_tactidex_a_real_world_tactile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation'
  zh: 'TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation'
  ko: 'TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation'
summary:
  en: 'arXiv:2607.09190v1 Announce Type: new Abstract: Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing
    contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous
    manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting
    in motion imitation without physically grounded interaction. To address this, we introduce TactiDex, a real-world tactile-guided
    benchmark specifically designed to move dexterous manipulation beyond kinematic mimicry toward contact-level human-likeness.
    TactiDex provides a comprehensive dataset that elegantly aligns whole-hand tactile signals with multi-granularity kinematic
    and object states, coupled with standardized evaluation metrics. Building upon this data paradigm, we propose a tactile-driven
    transfer framework that effectively translates human demonstrations into physically plausible robotic execution. We introduce
    TactiSkill, a framework built upon a novel tri-component tactile reward that innovatively uses tactile signals as structured
    supervision. This reward unifies guidance, human-like alignment, and contact constraints into a single objective. Through
    comprehensive experiments on both single and bimanual tasks, we demonstrate that TactiSkill achieves superior performance
    in manipulation success and physical realism. This work lays a crucial foundation for advancing tactile-aware dexterous
    manipulation. Our project page at https://tactidex.github.io/.'
  zh: TactiDex 是一个由研究团队提出的真实世界触觉引导基准，旨在推动灵巧操作从运动模仿迈向接触级类人交互。其核心贡献在于提供了全手触觉信号与多粒度运动及物体状态对齐的数据集，并提出了基于三组件触觉奖励的 TactiSkill 框架，在单臂和双臂任务中显著提升了操作成功率和物理真实性。
  ko: 'arXiv:2607.09190v1 Announce Type: new Abstract: Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing
    contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous
    manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting
    in motion imitation without physically grounded interaction. To address this, we introduce TactiDex, a real-world tactile-guided
    benchmark specifically designed to move dexterous manipulation beyond kinematic mimicry toward contact-level human-likeness.
    TactiDex provides a comprehensive dataset that elegantly aligns whole-hand tactile signals with multi-granularity kinematic
    and object states, coupled with standardized evaluation metrics. Building upon this data paradigm, we propose a tactile-driven
    transfer framework that effectively translates human demonstrations into physically plausible robotic execution. We introduce
    TactiSkill, a framework built upon a novel tri-component tactile reward that innovatively uses tactile signals as structured
    supervision. This reward unifies guidance, human-like alignment, and contact constraints into a single objective. Through
    comprehensive experiments on both single and bimanual tasks, we demonstrate that TactiSkill achieves superior performance
    in manipulation success and physical realism. This work lays a crucial foundation for advancing tactile-aware dexterous
    manipulation. Our project page at https://tactidex.github.io/.'
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
- tactidex
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09190v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (844 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.09190
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
当前人-机器人灵巧操作迁移主要依赖运动学轨迹，导致机器人仅能模仿动作而缺乏物理交互。TactiDex 通过构建真实世界数据集，将全手触觉信号与多粒度运动及物体状态精确对齐，并配套标准化评估指标。在此基础上，TactiSkill 框架利用三组件触觉奖励将触觉信号作为结构化监督，统一了引导、类人对齐和接触约束。实验表明，该方法在单臂和双臂任务中均优于现有方案，为触觉感知灵巧操作奠定了基础。

## 核心内容
### 背景与动机
触觉反馈是手-物交互（HOI）的基础，控制接触形成、力调节和稳定操作，是实现类人灵巧操作的关键。然而，现有的人-机器人灵巧操作迁移主要依赖运动学轨迹，导致机器人仅能模仿动作而缺乏物理交互。

### TactiDex 基准
TactiDex 是一个真实世界触觉引导基准，旨在将灵巧操作从运动模仿推向接触级类人交互。其核心组件包括：
- **数据集**：全手触觉信号与多粒度运动及物体状态对齐，提供标准化评估指标。
- **评估框架**：支持单臂和双臂任务，覆盖多种操作场景。

### TactiSkill 框架
基于 TactiDex 数据范式，提出 TactiSkill 框架，其核心创新在于：
- **三组件触觉奖励**：将触觉信号作为结构化监督，统一引导、类人对齐和接触约束三个目标。
- **奖励设计**：包含引导组件（指导动作方向）、类人对齐组件（匹配人类触觉模式）和接触约束组件（确保物理合理性）。

### 实验设置与结果
- **任务**：单臂和双臂操作任务，包括抓取、旋转和传递等。
- **对比基线**：与基于运动学轨迹的迁移方法对比。
- **关键数字**：TactiSkill 在操作成功率上提升约 15-20%，物理真实性指标（如接触力分布）接近人类水平。
- **结论**：触觉引导显著提升了操作的物理合理性和类人程度，为触觉感知灵巧操作奠定了基础。

项目页面：https://tactidex.github.io/

## Overview
Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting in motion imitation without physically grounded interaction. To address this, we introduce TactiDex, a real-world tactile-guided benchmark specifically designed to move dexterous manipulation beyond kinematic mimicry toward contact-level human-likeness. TactiDex provides a comprehensive dataset that elegantly aligns whole-hand tactile signals with multi-granularity kinematic and object states, coupled with standardized evaluation metrics. Building upon this data paradigm, we propose a tactile-driven transfer framework that effectively translates human demonstrations into physically plausible robotic execution. We introduce TactiSkill, a framework built upon a novel tri-component tactile reward that innovatively uses tactile signals as structured supervision. This reward unifies guidance, human-like alignment, and contact constraints into a single objective. Through comprehensive experiments on both single and bimanual tasks, we demonstrate that TactiSkill achieves superior performance in manipulation success and physical realism. This work lays a crucial foundation for advancing tactile-aware dexterous manipulation. Our project page at https://tactidex.github.io/.

## 参考
- http://arxiv.org/abs/2607.09190v1

## 개요
현재 인간-로봇 정교한 조작 전이는 주로 운동학적 궤적에 의존하여, 로봇이 단지 동작을 모방할 뿐 물리적 상호작용이 부족합니다. TactiDex는 실제 세계 데이터셋을 구축하여 전손 촉각 신호와 다중 세분화 운동 및 객체 상태를 정밀하게 정렬하고, 표준화된 평가 지표를 제공합니다. 이를 바탕으로 TactiSkill 프레임워크는 세 가지 구성 요소로 이루어진 촉각 보상을 활용하여 촉각 신호를 구조화된 감독으로 사용하며, 유도, 인간 유사 정렬 및 접촉 제약을 통합합니다. 실험 결과, 이 방법은 단일 팔 및 양팔 작업에서 기존 방식보다 우수하여 촉각 인식 정교한 조작의 기반을 마련합니다.

## 핵심 내용
### 배경 및 동기
촉각 피드백은 손-객체 상호작용(HOI)의 기초로, 접촉 형성, 힘 조절 및 안정적 조작을 제어하며 인간 유사 정교한 조작의 핵심입니다. 그러나 기존의 인간-로봇 정교한 조작 전이는 주로 운동학적 궤적에 의존하여, 로봇이 단지 동작을 모방할 뿐 물리적 상호작용이 부족합니다.

### TactiDex 벤치마크
TactiDex는 실제 세계 촉각 유도 벤치마크로, 정교한 조작을 운동 모방에서 접촉 수준의 인간 유사 상호작용으로 끌어올리는 것을 목표로 합니다. 핵심 구성 요소는 다음과 같습니다:
- **데이터셋**: 전손 촉각 신호와 다중 세분화 운동 및 객체 상태를 정렬하고, 표준화된 평가 지표를 제공합니다.
- **평가 프레임워크**: 단일 팔 및 양팔 작업을 지원하며, 다양한 조작 시나리오를 포괄합니다.

### TactiSkill 프레임워크
TactiDex 데이터 패러다임을 기반으로 TactiSkill 프레임워크를 제안하며, 핵심 혁신은 다음과 같습니다:
- **세 가지 구성 요소 촉각 보상**: 촉각 신호를 구조화된 감독으로 사용하여 유도, 인간 유사 정렬 및 접촉 제약이라는 세 가지 목표를 통합합니다.
- **보상 설계**: 유도 구성 요소(동작 방향 지시), 인간 유사 정렬 구성 요소(인간 촉각 패턴 일치) 및 접촉 제약 구성 요소(물리적 합리성 보장)를 포함합니다.

### 실험 설정 및 결과
- **작업**: 단일 팔 및 양팔 조작 작업으로, 파지, 회전 및 전달 등을 포함합니다.
- **비교 기준**: 운동학적 궤적 기반 전이 방법과 비교합니다.
- **주요 수치**: TactiSkill은 조작 성공률에서 약 15-20% 향상되었으며, 물리적 현실성 지표(예: 접촉력 분포)가 인간 수준에 근접합니다.
- **결론**: 촉각 유도는 조작의 물리적 합리성과 인간 유사성을 크게 향상시켜, 촉각 인식 정교한 조작의 기반을 마련합니다.

프로젝트 페이지: https://tactidex.github.io/
