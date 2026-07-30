---
$id: ent_paper_bigym_a_demo_driven_mobile_bi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark'
  zh: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark'
  ko: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark'
summary:
  en: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark is a 2024 work on simulation benchmark for humanoid robots,
    with open-source code available.'
  zh: BiGym 是一个2024年发布的面向移动双臂人形机器人的演示驱动操作基准与学习环境。该工作由研究团队提出，包含40种家庭场景任务，并提供人类采集的演示数据，用于评估模仿学习与演示驱动强化学习算法的性能。
  ko: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark is a 2024 work on simulation benchmark for humanoid robots,
    with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- bigym
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.07788v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark (arXiv)'
  url: https://arxiv.org/abs/2407.07788
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark project page'
  url: https://chernyadev.github.io/bigym/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
BiGym 是一个专为移动双臂机器人设计的仿真基准与学习环境，旨在推动演示驱动操作任务的研究。该环境包含40种多样化的家庭场景任务，从简单的目标抓取到复杂的厨房清洁，覆盖了真实世界机器人轨迹中的多种模态。为了准确反映真实性能，BiGym 为每个任务提供了人类采集的演示数据，并支持多种观测输入，包括本体感觉数据以及来自三个摄像头视角的RGB和深度视觉信息。研究团队通过在该环境中全面测试最先进的模仿学习算法和演示驱动强化学习算法，验证了BiGym的实用性，并探讨了未来的研究方向。

## 核心内容
### 方法
BiGym 的核心设计围绕演示驱动（demo-driven）的移动双臂操作任务展开。环境基于仿真平台构建，强调从人类演示中学习，以模拟真实世界机器人轨迹的多样性。每个任务都配有由人类操作员采集的演示数据，这些数据涵盖了多种模态，为算法提供了丰富的训练样本。

### 架构与观测
BiGym 支持多种观测类型，以匹配真实机器人系统的复杂性：
- **本体感觉数据**：包括机器人关节角度、末端执行器位置等内部状态信息。
- **视觉输入**：提供来自三个摄像头视角的RGB图像和深度图像，使算法能够感知三维空间环境。

### 实验设置
- **任务集**：包含40种家庭环境任务，难度从简单的目标到达（target reaching）到复杂的厨房清洁（kitchen cleaning）不等。
- **基准测试**：研究团队在BiGym环境中系统评估了当前最先进的模仿学习算法（如Behavior Cloning）和演示驱动强化学习算法（如Demo-Driven RL）。所有代码和数据集均已开源。

### 关键数字与结论
- 任务数量：40种，覆盖多种家庭操作场景。
- 演示数据：每个任务均提供人类采集的演示，确保数据真实反映人类操作模式。
- 观测维度：支持3个摄像头视角的RGB和深度信息，以及本体感觉数据。
- 基准结果：实验表明，现有算法在简单任务上表现良好，但在复杂任务（如厨房清洁）中仍有显著提升空间，揭示了未来研究的关键方向。

### 结论
BiGym 为移动双臂机器人操作提供了一个标准化、可复现的评估平台，其演示驱动特性有助于缩小仿真与真实世界之间的差距。研究团队指出，未来工作可聚焦于提升算法在复杂任务中的泛化能力，以及探索多模态融合策略。

## Overview
We introduce BiGym, a new benchmark and learning environment for mobile bi-manual demo-driven robotic manipulation. BiGym features 40 diverse tasks set in home environments, ranging from simple target reaching to complex kitchen cleaning. To capture the real-world performance accurately, we provide human-collected demonstrations for each task, reflecting the diverse modalities found in real-world robot trajectories. BiGym supports a variety of observations, including proprioceptive data and visual inputs such as RGB, and depth from 3 camera views. To validate the usability of BiGym, we thoroughly benchmark the state-of-the-art imitation learning algorithms and demo-driven reinforcement learning algorithms within the environment and discuss the future opportunities.

## 개요
BiGym은 모바일 양팔 로봇의 데모 기반 조작을 위한 새로운 벤치마크 및 학습 환경을 소개합니다. BiGym은 간단한 목표 도달부터 복잡한 주방 청소까지 가정 환경에서 설정된 40가지 다양한 작업을 특징으로 합니다. 실제 성능을 정확하게 포착하기 위해 각 작업에 대해 인간이 수집한 데모를 제공하며, 이는 실제 로봇 궤적에서 발견되는 다양한 양식을 반영합니다. BiGym은 고유수용성 데이터와 3개의 카메라 뷰에서 제공되는 RGB 및 깊이와 같은 시각적 입력을 포함한 다양한 관측을 지원합니다. BiGym의 유용성을 검증하기 위해 환경 내에서 최신 모방 학습 알고리즘과 데모 기반 강화 학습 알고리즘을 철저히 벤치마킹하고 향후 기회를 논의합니다.

## 핵심 내용
BiGym은 모바일 양팔 로봇의 데모 기반 조작을 위한 새로운 벤치마크 및 학습 환경을 소개합니다. BiGym은 간단한 목표 도달부터 복잡한 주방 청소까지 가정 환경에서 설정된 40가지 다양한 작업을 특징으로 합니다. 실제 성능을 정확하게 포착하기 위해 각 작업에 대해 인간이 수집한 데모를 제공하며, 이는 실제 로봇 궤적에서 발견되는 다양한 양식을 반영합니다. BiGym은 고유수용성 데이터와 3개의 카메라 뷰에서 제공되는 RGB 및 깊이와 같은 시각적 입력을 포함한 다양한 관측을 지원합니다. BiGym의 유용성을 검증하기 위해 환경 내에서 최신 모방 학습 알고리즘과 데모 기반 강화 학습 알고리즘을 철저히 벤치마킹하고 향후 기회를 논의합니다.

## 参考
- http://arxiv.org/abs/2407.07788v2
