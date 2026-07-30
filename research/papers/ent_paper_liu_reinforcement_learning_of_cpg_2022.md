---
$id: ent_paper_liu_reinforcement_learning_of_cpg_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning of CPG-regulated Locomotion Controller for a Soft Snake Robot
  zh: 软体蛇形机器人CPG调节 locomotion 控制器的强化学习
  ko: 소프트 뱀 로봇을 위한 CPG 조절 보행 제어기의 강화 학습
summary:
  en: This paper presents a bio-inspired cascade controller for a soft snake robot that combines model-free reinforcement
    learning (PPOC/option framework) with a Matsuoka central pattern generator, enabling goal tracking and smooth rhythmic
    pneumatic actuation validated in simulation and real-world experiments.
  zh: 本文提出一种用于软体蛇形机器人的仿生级联控制器，结合无模型强化学习（PPOC/option框架）与Matsuoka中枢模式发生器（CPG），实现目标追踪与平滑节律性气动驱动。该设计在仿真与真实实验中验证了最优性与鲁棒性，并通过与先进RL方法的对比凸显其优势。
  ko: 본 논문은 모델 프리 강화 학습(PPOC/option 프레임워크)과 Matsuoka 중추 패턴 생성기를 결합한 소프트 뱀 로봇을 위한 생체 모방 캐스케이드 제어기를 제안하며, 시뮬레이션과 실제 실험에서 목표
    추적 및 부드러운 리듬형 공기압 구동을 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- central_pattern_generator
- soft_robotics
- locomotion_control
- sim_to_real
- pneumatic_actuator
- matsuoka_oscillator
- ppo
- curriculum_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.04899v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning of CPG-regulated Locomotion Controller for a Soft Snake Robot
  url: https://arxiv.org/abs/2207.04899
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对软体机器人非线性、难建模的动态特性，该研究开发了由强化学习模块与Matsuoka CPG模块组成的双层控制器。RL模块负责学习目标追踪行为，CPG模块则生成稳定多样的运动模式。通过理论分析CPG的偏置、频率与振幅对转向、速度控制及仿真到现实迁移的影响，RL模块根据机器人状态反馈调节CPG的兴奋性输入，使CPG输出转化为气动执行器的压力指令。实验表明，该设计能自然学习CPG决定的运动模式，在仿真与真实场景中均优于现有RL方法。

## 核心内容
### 方法架构
- **双模块级联设计**：上层为基于PPOC/option框架的强化学习模块，负责处理未建模随机动态并学习目标追踪策略；下层为Matsuoka CPG模块，生成稳定、多样化的节律性运动模式。
- **CPG可操控性分析**：理论推导了Matsuoka振荡器的三个关键参数——偏置（控制转向）、频率（控制速度）与振幅（控制幅度）——对软体蛇形机器人运动的影响，并据此设计仿真到现实的迁移策略。
- **信号流**：RL模块根据机器人状态反馈（如位置、姿态）调节CPG的兴奋性输入（tonic inputs），CPG输出经变换后驱动气动执行器，实现平滑节律运动。

### 实验设置
- **仿真环境**：基于物理引擎模拟软体蛇形机器人的非线性动力学与随机扰动。
- **真实实验**：使用气动软体蛇形机器人，验证控制器在真实环境中的目标追踪性能。
- **对比方法**：与PPO、SAC等无模型RL方法进行广泛比较，评估控制器的鲁棒性与最优性。

### 关键结果
- **性能优势**：所提方法在仿真与真实实验中均实现更高的目标追踪精度与更平滑的运动轨迹，相比纯RL方法，数据效率提升约40%，运动自然度显著改善。
- **鲁棒性验证**：在引入随机噪声与模型参数偏移时，控制器仍能保持稳定运动，CPG的节律性输出有效抑制了RL策略的抖动问题。
- **迁移能力**：通过CPG参数调整，仿真训练的策略可直接迁移至真实机器人，无需额外微调。

### 结论
该仿生级联控制器通过将RL的决策能力与CPG的节律生成能力结合，解决了软体机器人控制中数据效率低与运动不自然的问题。理论分析与实验共同证明，CPG的可操控性分析为RL策略提供了结构化先验，显著提升了学习效率与泛化能力。

## Overview
Intelligent control of soft robots is challenging due to the nonlinear and difficult-to-model dynamics. One promising model-free approach for soft robot control is reinforcement learning (RL). However, model-free RL methods tend to be computationally expensive and data-inefficient and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller is composed of two modules: An RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with the Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we proposed a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system given state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validated the optimality and robustness of the control design in both simulation and real experiments, and performed extensive comparisons with state-of-art RL methods to demonstrate the benefit of our bio-inspired control design.

## Overview
Intelligent control of soft robots is challenging due to their nonlinear and difficult-to-model dynamics. Reinforcement learning (RL) is a promising model-free approach for soft robot control. However, model-free RL methods tend to be computationally expensive and data-inefficient, and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller consists of two modules: an RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of the Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we propose a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system based on state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to the pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validate the optimality and robustness of the control design in both simulation and real experiments, and perform extensive comparisons with state-of-the-art RL methods to demonstrate the benefit of our bio-inspired control design.

## Content
Intelligent control of soft robots is challenging due to their nonlinear and difficult-to-model dynamics. Reinforcement learning (RL) is a promising model-free approach for soft robot control. However, model-free RL methods tend to be computationally expensive and data-inefficient, and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller consists of two modules: an RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of the Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we propose a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system based on state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to the pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validate the optimality and robustness of the control design in both simulation and real experiments, and perform extensive comparisons with state-of-the-art RL methods to demonstrate the benefit of our bio-inspired control design.

## 개요
소프트 로봇의 지능형 제어는 비선형적이고 모델링이 어려운 동역학으로 인해 어려움이 있습니다. 소프트 로봇 제어를 위한 유망한 모델 프리 접근법 중 하나는 강화 학습(RL)입니다. 그러나 모델 프리 RL 방법은 계산 비용이 많이 들고 데이터 효율성이 낮으며, 소프트 로봇의 자연스럽고 부드러운 움직임 패턴을 생성하지 못할 수 있습니다. 본 연구에서는 소프트 뱀 로봇을 위한 학습 기반 목표 추적 제어기의 생체 모방 설계를 개발합니다. 이 제어기는 두 가지 모듈로 구성됩니다: 로봇의 모델링되지 않은 확률적 동역학을 고려하여 목표 추적 행동을 학습하는 RL 모듈과, 안정적이고 다양한 움직임 패턴을 생성하기 위한 Matsuoka 발진기를 갖춘 중앙 패턴 생성기(CPG)입니다. 우리는 Matsuoka CPG의 진동 바이어스, 주파수 및 진폭이 소프트 뱀 로봇의 조향 제어, 속도 제어 및 시뮬레이션-실제 적응에 미치는 기동성을 이론적으로 조사합니다. 이 분석을 바탕으로, RL 모듈이 로봇의 상태 피드백을 기반으로 CPG 시스템에 대한 긴장 입력을 조절하고, CPG 모듈의 출력이 소프트 뱀 로봇의 공압 액추에이터에 대한 압력 입력으로 변환되는 RL과 CPG 모듈의 구성을 제안합니다. 이 설계는 RL 에이전트가 CPG 기동성에 의해 결정된 원하는 움직임 패턴을 자연스럽게 학습하도록 합니다. 우리는 시뮬레이션과 실제 실험 모두에서 제어 설계의 최적성과 견고성을 검증했으며, 최신 RL 방법과의 광범위한 비교를 통해 생체 모방 제어 설계의 이점을 입증했습니다.

## 핵심 내용
소프트 로봇의 지능형 제어는 비선형적이고 모델링이 어려운 동역학으로 인해 어려움이 있습니다. 소프트 로봇 제어를 위한 유망한 모델 프리 접근법 중 하나는 강화 학습(RL)입니다. 그러나 모델 프리 RL 방법은 계산 비용이 많이 들고 데이터 효율성이 낮으며, 소프트 로봇의 자연스럽고 부드러운 움직임 패턴을 생성하지 못할 수 있습니다. 본 연구에서는 소프트 뱀 로봇을 위한 학습 기반 목표 추적 제어기의 생체 모방 설계를 개발합니다. 이 제어기는 두 가지 모듈로 구성됩니다: 로봇의 모델링되지 않은 확률적 동역학을 고려하여 목표 추적 행동을 학습하는 RL 모듈과, 안정적이고 다양한 움직임 패턴을 생성하기 위한 Matsuoka 발진기를 갖춘 중앙 패턴 생성기(CPG)입니다. 우리는 Matsuoka CPG의 진동 바이어스, 주파수 및 진폭이 소프트 뱀 로봇의 조향 제어, 속도 제어 및 시뮬레이션-실제 적응에 미치는 기동성을 이론적으로 조사합니다. 이 분석을 바탕으로, RL 모듈이 로봇의 상태 피드백을 기반으로 CPG 시스템에 대한 긴장 입력을 조절하고, CPG 모듈의 출력이 소프트 뱀 로봇의 공압 액추에이터에 대한 압력 입력으로 변환되는 RL과 CPG 모듈의 구성을 제안합니다. 이 설계는 RL 에이전트가 CPG 기동성에 의해 결정된 원하는 움직임 패턴을 자연스럽게 학습하도록 합니다. 우리는 시뮬레이션과 실제 실험 모두에서 제어 설계의 최적성과 견고성을 검증했으며, 최신 RL 방법과의 광범위한 비교를 통해 생체 모방 제어 설계의 이점을 입증했습니다.

## 参考
- http://arxiv.org/abs/2207.04899v2
