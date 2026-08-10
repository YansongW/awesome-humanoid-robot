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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.07788v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (998 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2407.07788v2

## Overview
BiGym is a simulation benchmark and learning environment designed specifically for mobile dual-arm robots, aimed at advancing research in demonstration-driven manipulation tasks. The environment includes 40 diverse household scenario tasks, ranging from simple object grasping to complex kitchen cleaning, covering multiple modalities present in real-world robot trajectories. To accurately reflect real-world performance, BiGym provides human-collected demonstration data for each task and supports multiple observation inputs, including proprioceptive data as well as RGB and depth visual information from three camera viewpoints. The research team validated BiGym's practicality by comprehensively testing state-of-the-art imitation learning algorithms and demonstration-driven reinforcement learning algorithms within this environment, and discussed future research directions.

## Content
### Method
The core design of BiGym revolves around demonstration-driven mobile dual-arm manipulation tasks. The environment is built on a simulation platform, emphasizing learning from human demonstrations to simulate the diversity of real-world robot trajectories. Each task is accompanied by demonstration data collected by human operators, which covers multiple modalities and provides rich training samples for algorithms.

### Architecture and Observations
BiGym supports multiple observation types to match the complexity of real robot systems:
- **Proprioceptive data**: Includes internal state information such as robot joint angles and end-effector positions.
- **Visual input**: Provides RGB images and depth images from three camera viewpoints, enabling algorithms to perceive the three-dimensional spatial environment.

### Experimental Setup
- **Task set**: Includes 40 household environment tasks, with difficulty ranging from simple target reaching to complex kitchen cleaning.
- **Benchmark testing**: The research team systematically evaluated state-of-the-art imitation learning algorithms (e.g., Behavior Cloning) and demonstration-driven reinforcement learning algorithms (e.g., Demo-Driven RL) in the BiGym environment. All code and datasets have been open-sourced.

### Key Numbers and Conclusions
- Number of tasks: 40, covering a variety of household manipulation scenarios.
- Demonstration data: Each task provides human-collected demonstrations, ensuring the data accurately reflects human manipulation patterns.
- Observation dimensions: Supports RGB and depth information from 3 camera viewpoints, as well as proprioceptive data.
- Benchmark results: Experiments show that existing algorithms perform well on simple tasks, but there remains significant room for improvement on complex tasks (e.g., kitchen cleaning), revealing key directions for future research.

### Conclusion
BiGym provides a standardized and reproducible evaluation platform for mobile dual-arm robot manipulation, and its demonstration-driven characteristics help bridge the gap between simulation and the real world. The research team notes that future work could focus on improving algorithm generalization in complex tasks and exploring multimodal fusion strategies.

## 개요
BiGym은 이동형 이중 팔 로봇을 위해 설계된 시뮬레이션 벤치마크 및 학습 환경으로, 시연 기반 조작 작업 연구를 촉진하는 것을 목표로 합니다. 이 환경은 간단한 목표물 집기부터 복잡한 주방 청소까지 40가지 다양한 가정 환경 작업을 포함하며, 실제 세계 로봇 궤적의 다양한 모달리티를 포괄합니다. 실제 성능을 정확히 반영하기 위해 BiGym은 각 작업에 대해 인간이 수집한 시연 데이터를 제공하며, 고유수용감각 데이터와 세 개의 카메라 시점에서 얻은 RGB 및 깊이 시각 정보를 포함한 다양한 관측 입력을 지원합니다. 연구팀은 이 환경에서 최신 모방 학습 알고리즘과 시연 기반 강화 학습 알고리즘을 포괄적으로 테스트하여 BiGym의 실용성을 검증하고 향후 연구 방향을 논의했습니다.

## 핵심 내용
### 방법
BiGym의 핵심 설계는 시연 기반(demo-driven) 이동형 이중 팔 조작 작업을 중심으로 이루어집니다. 환경은 시뮬레이션 플랫폼을 기반으로 구축되었으며, 인간 시연에서 학습하여 실제 세계 로봇 궤적의 다양성을 모방하는 데 중점을 둡니다. 각 작업에는 인간 운영자가 수집한 시연 데이터가 포함되며, 이 데이터는 다양한 모달리티를 포괄하여 알고리즘에 풍부한 훈련 샘플을 제공합니다.

### 아키텍처 및 관측
BiGym은 실제 로봇 시스템의 복잡성을 반영하기 위해 여러 관측 유형을 지원합니다:
- **고유수용감각 데이터**: 로봇 관절 각도, 말단 실행기 위치 등 내부 상태 정보를 포함합니다.
- **시각 입력**: 세 개의 카메라 시점에서 얻은 RGB 이미지와 깊이 이미지를 제공하여 알고리즘이 3차원 공간 환경을 인식할 수 있게 합니다.

### 실험 설정
- **작업 세트**: 목표 도달(target reaching)부터 복잡한 주방 청소(kitchen cleaning)까지 다양한 난이도의 40가지 가정 환경 작업을 포함합니다.
- **벤치마크 테스트**: 연구팀은 BiGym 환경에서 현재 최신 모방 학습 알고리즘(예: Behavior Cloning)과 시연 기반 강화 학습 알고리즘(예: Demo-Driven RL)을 체계적으로 평가했습니다. 모든 코드와 데이터 세트는 오픈소스로 공개되었습니다.

### 주요 수치 및 결론
- 작업 수: 40가지로, 다양한 가정 조작 시나리오를 포괄합니다.
- 시연 데이터: 각 작업에 인간이 수집한 시연을 제공하여 데이터가 인간 조작 패턴을 실제로 반영하도록 보장합니다.
- 관측 차원: 세 개의 카메라 시점에서 얻은 RGB 및 깊이 정보와 고유수용감각 데이터를 지원합니다.
- 벤치마크 결과: 실험에 따르면 기존 알고리즘은 간단한 작업에서 우수한 성능을 보이지만, 복잡한 작업(예: 주방 청소)에서는 여전히 상당한 개선 여지가 있어 향후 연구의 핵심 방향을 제시합니다.

### 결론
BiGym은 이동형 이중 팔 로봇 조작을 위한 표준화되고 재현 가능한 평가 플랫폼을 제공하며, 시연 기반 특성은 시뮬레이션과 실제 세계 간의 격차를 줄이는 데 기여합니다. 연구팀은 향후 작업이 복잡한 작업에서 알고리즘의 일반화 능력을 향상시키고 다중 모달리티 융합 전략을 탐구하는 데 초점을 맞출 수 있다고 지적합니다.
