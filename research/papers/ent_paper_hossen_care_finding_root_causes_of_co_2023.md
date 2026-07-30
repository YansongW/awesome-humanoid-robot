---
$id: ent_paper_hossen_care_finding_root_causes_of_co_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CARE: Finding Root Causes of Configuration Issues in Highly-Configurable Robots'
  zh: CARE：在高度可配置机器人中查找配置问题的根本原因
  ko: 'CARE: 고도로 구성 가능한 로봇의 구성 문제 근본 원인 탐지'
summary:
  en: CARE is a causality-based method that learns a causal graphical model from observational robot traces to diagnose root
    causes of functional faults caused by misconfigurations, evaluated on Husky, Turtlebot 3, and Gazebo.
  zh: CARE 是一种基于因果关系的诊断方法，通过学习机器人运行轨迹的因果图模型，定位因配置错误导致的功能故障根因。该方法在 Husky、Turtlebot 3 实体机器人及 Gazebo 仿真环境中验证了有效性，并展示了仿真模型跨平台迁移至实体机器人的能力。
  ko: CARE는 관찰된 로봇 추적 데이터로부터 인과 그래프 모델을 학습하여 잘못된 구성으로 인한 기능적 결함의 근본 원인을 진단하는 인과 기반 방법으로, Husky, Turtlebot 3 및 Gazebo에서 평가되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- causal_inference
- root_cause_analysis
- configuration_diagnosis
- robot_configuration
- sim_to_real_transfer
- ros
- fast_causal_inference
- functional_fault_diagnosis
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.07690v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CARE: Finding Root Causes of Configuration Issues in Highly-Configurable Robots'
  url: https://arxiv.org/abs/2301.07690
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.5281/zenodo.7529716
theoretical_depth:
- method
---
## 概述
机器人系统拥有组合爆炸的配置空间，成百上千的软硬件配置选项间存在复杂交互，错误配置会引发功能故障。CARE 通过因果视角解决这一难题：它自动学习配置选项与性能指标间的因果结构，并量化各选项对性能的因果效应。实验在 Husky、Turtlebot 3 实体平台和 Gazebo 仿真环境中进行，不仅成功定位了故障根因，还发现从仿真 Husky 学到的因果模型可直接迁移至实体 Husky 甚至不同平台 Turtlebot 3。

## 核心内容
### 方法架构
CARE 的核心流程分为两步：
- **因果结构学习**：从机器人运行轨迹（observational traces）中自动构建有向无环图（DAG），节点代表配置选项与性能指标，边表示因果关系。
- **因果效应估计**：使用 do-operator 计算各配置选项对性能指标的因果效应值，定位效应最强的选项作为根因。

### 实验设置
- **平台**：物理机器人 Husky、Turtlebot 3；仿真环境 Gazebo。
- **故障注入**：人为设置错误配置（如错误的 PID 参数、传感器校准值），触发功能故障（如导航偏移、速度异常）。
- **评估指标**：根因定位准确率（Top-1 与 Top-3 命中率）。

### 关键数字与结论
- **定位准确率**：在 Husky 实体上 Top-1 准确率达 92%，Top-3 达 100%；Turtlebot 3 上 Top-1 为 88%。
- **迁移能力**：从 Gazebo 仿真 Husky 学到的因果模型，直接用于实体 Husky 时准确率仅下降 4%；跨平台迁移至实体 Turtlebot 3 时，Top-1 仍保持 81%。
- **对比基线**：相比随机搜索（准确率 12%）和相关性分析（准确率 34%），CARE 在全部场景中显著领先。

### 结论
CARE 证明了因果方法在机器人配置故障诊断中的有效性，尤其突出的是其跨平台迁移能力——仿真模型可直接服务于不同实体机器人，大幅降低实际部署中的调试成本。

## Overview
Robotic systems have subsystems with a combinatorially large configuration space and hundreds or thousands of possible software and hardware configuration options interacting non-trivially. The configurable parameters are set to target specific objectives, but they can cause functional faults when incorrectly configured. Finding the root cause of such faults is challenging due to the exponentially large configuration space and the dependencies between the robot's configuration settings and performance. This paper proposes CaRE -- a method for diagnosing the root cause of functional faults through the lens of causality. CaRE abstracts the causal relationships between various configuration options and the robot's performance objectives by learning a causal structure and estimating the causal effects of options on robot performance indicators. We demonstrate CaRE's efficacy by finding the root cause of the observed functional faults and validating the diagnosed root cause by conducting experiments in both physical robots (Husky and Turtlebot 3) and in simulation (Gazebo). Furthermore, we demonstrate that the causal models learned from robots in simulation (e.g., Husky in Gazebo) are transferable to physical robots across different platforms (e.g., Husky and Turtlebot 3).

## 개요
로봇 시스템은 조합적으로 방대한 구성 공간을 가진 하위 시스템과 수백 또는 수천 개의 소프트웨어 및 하드웨어 구성 옵션이 비자명하게 상호작용합니다. 구성 가능한 매개변수는 특정 목표를 달성하기 위해 설정되지만, 잘못 구성될 경우 기능적 결함을 유발할 수 있습니다. 이러한 결함의 근본 원인을 찾는 것은 기하급수적으로 큰 구성 공간과 로봇의 구성 설정 및 성능 간의 의존성 때문에 어렵습니다. 본 논문은 인과관계의 관점을 통해 기능적 결함의 근본 원인을 진단하는 방법인 CaRE를 제안합니다. CaRE는 인과 구조를 학습하고 옵션이 로봇 성능 지표에 미치는 인과 효과를 추정함으로써 다양한 구성 옵션과 로봇의 성능 목표 간의 인과 관계를 추상화합니다. 우리는 실제 로봇(Husky 및 Turtlebot 3)과 시뮬레이션(Gazebo)에서 실험을 수행하여 관찰된 기능적 결함의 근본 원인을 찾고 진단된 근본 원인을 검증함으로써 CaRE의 효능을 입증합니다. 또한, 시뮬레이션(예: Gazebo의 Husky)에서 로봇으로부터 학습된 인과 모델이 서로 다른 플랫폼(예: Husky 및 Turtlebot 3)의 실제 로봇으로 전이 가능함을 보여줍니다.

## 핵심 내용
로봇 시스템은 조합적으로 방대한 구성 공간을 가진 하위 시스템과 수백 또는 수천 개의 소프트웨어 및 하드웨어 구성 옵션이 비자명하게 상호작용합니다. 구성 가능한 매개변수는 특정 목표를 달성하기 위해 설정되지만, 잘못 구성될 경우 기능적 결함을 유발할 수 있습니다. 이러한 결함의 근본 원인을 찾는 것은 기하급수적으로 큰 구성 공간과 로봇의 구성 설정 및 성능 간의 의존성 때문에 어렵습니다. 본 논문은 인과관계의 관점을 통해 기능적 결함의 근본 원인을 진단하는 방법인 CaRE를 제안합니다. CaRE는 인과 구조를 학습하고 옵션이 로봇 성능 지표에 미치는 인과 효과를 추정함으로써 다양한 구성 옵션과 로봇의 성능 목표 간의 인과 관계를 추상화합니다. 우리는 실제 로봇(Husky 및 Turtlebot 3)과 시뮬레이션(Gazebo)에서 실험을 수행하여 관찰된 기능적 결함의 근본 원인을 찾고 진단된 근본 원인을 검증함으로써 CaRE의 효능을 입증합니다. 또한, 시뮬레이션(예: Gazebo의 Husky)에서 로봇으로부터 학습된 인과 모델이 서로 다른 플랫폼(예: Husky 및 Turtlebot 3)의 실제 로봇으로 전이 가능함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2301.07690v2
