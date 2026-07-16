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
  zh: 本文提出了一种面向软体蛇形机器人的生物启发级联控制器，将无模型强化学习（PPOC/option框架）与Matsuoka中枢模式发生器相结合，实现了目标跟踪与平滑节律气动驱动，并在仿真与真实实验中进行了验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.04899v2.
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
Intelligent control of soft robots is challenging due to the nonlinear and difficult-to-model dynamics. One promising model-free approach for soft robot control is reinforcement learning (RL). However, model-free RL methods tend to be computationally expensive and data-inefficient and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller is composed of two modules: An RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with the Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we proposed a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system given state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validated the optimality and robustness of the control design in both simulation and real experiments, and performed extensive comparisons with state-of-art RL methods to demonstrate the benefit of our bio-inspired control design.

## 核心内容
Intelligent control of soft robots is challenging due to the nonlinear and difficult-to-model dynamics. One promising model-free approach for soft robot control is reinforcement learning (RL). However, model-free RL methods tend to be computationally expensive and data-inefficient and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller is composed of two modules: An RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with the Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we proposed a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system given state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validated the optimality and robustness of the control design in both simulation and real experiments, and performed extensive comparisons with state-of-art RL methods to demonstrate the benefit of our bio-inspired control design.

## 参考
- http://arxiv.org/abs/2207.04899v2

## Overview
Intelligent control of soft robots is challenging due to their nonlinear and difficult-to-model dynamics. Reinforcement learning (RL) is a promising model-free approach for soft robot control. However, model-free RL methods tend to be computationally expensive and data-inefficient, and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller consists of two modules: an RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of the Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we propose a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system based on state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to the pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validate the optimality and robustness of the control design in both simulation and real experiments, and perform extensive comparisons with state-of-the-art RL methods to demonstrate the benefit of our bio-inspired control design.

## Content
Intelligent control of soft robots is challenging due to their nonlinear and difficult-to-model dynamics. Reinforcement learning (RL) is a promising model-free approach for soft robot control. However, model-free RL methods tend to be computationally expensive and data-inefficient, and may not yield natural and smooth locomotion patterns for soft robots. In this work, we develop a bio-inspired design of a learning-based goal-tracking controller for a soft snake robot. The controller consists of two modules: an RL module for learning goal-tracking behaviors given the unmodeled and stochastic dynamics of the robot, and a central pattern generator (CPG) with Matsuoka oscillators for generating stable and diverse locomotion patterns. We theoretically investigate the maneuverability of the Matsuoka CPG's oscillation bias, frequency, and amplitude for steering control, velocity control, and sim-to-real adaptation of the soft snake robot. Based on this analysis, we propose a composition of RL and CPG modules such that the RL module regulates the tonic inputs to the CPG system based on state feedback from the robot, and the output of the CPG module is then transformed into pressure inputs to the pneumatic actuators of the soft snake robot. This design allows the RL agent to naturally learn to entrain the desired locomotion patterns determined by the CPG maneuverability. We validate the optimality and robustness of the control design in both simulation and real experiments, and perform extensive comparisons with state-of-the-art RL methods to demonstrate the benefit of our bio-inspired control design.

## 개요
소프트 로봇의 지능형 제어는 비선형적이고 모델링이 어려운 동역학으로 인해 어려움이 있습니다. 소프트 로봇 제어를 위한 유망한 모델 프리 접근법 중 하나는 강화 학습(RL)입니다. 그러나 모델 프리 RL 방법은 계산 비용이 많이 들고 데이터 효율성이 낮으며, 소프트 로봇의 자연스럽고 부드러운 움직임 패턴을 생성하지 못할 수 있습니다. 본 연구에서는 소프트 뱀 로봇을 위한 학습 기반 목표 추적 제어기의 생체 모방 설계를 개발합니다. 이 제어기는 두 가지 모듈로 구성됩니다: 로봇의 모델링되지 않은 확률적 동역학을 고려하여 목표 추적 행동을 학습하는 RL 모듈과, 안정적이고 다양한 움직임 패턴을 생성하기 위한 Matsuoka 발진기를 갖춘 중앙 패턴 생성기(CPG)입니다. 우리는 Matsuoka CPG의 진동 바이어스, 주파수 및 진폭이 소프트 뱀 로봇의 조향 제어, 속도 제어 및 시뮬레이션-실제 적응에 미치는 기동성을 이론적으로 조사합니다. 이 분석을 바탕으로, RL 모듈이 로봇의 상태 피드백을 기반으로 CPG 시스템에 대한 긴장 입력을 조절하고, CPG 모듈의 출력이 소프트 뱀 로봇의 공압 액추에이터에 대한 압력 입력으로 변환되는 RL과 CPG 모듈의 구성을 제안합니다. 이 설계는 RL 에이전트가 CPG 기동성에 의해 결정된 원하는 움직임 패턴을 자연스럽게 학습하도록 합니다. 우리는 시뮬레이션과 실제 실험 모두에서 제어 설계의 최적성과 견고성을 검증했으며, 최신 RL 방법과의 광범위한 비교를 통해 생체 모방 제어 설계의 이점을 입증했습니다.

## 핵심 내용
소프트 로봇의 지능형 제어는 비선형적이고 모델링이 어려운 동역학으로 인해 어려움이 있습니다. 소프트 로봇 제어를 위한 유망한 모델 프리 접근법 중 하나는 강화 학습(RL)입니다. 그러나 모델 프리 RL 방법은 계산 비용이 많이 들고 데이터 효율성이 낮으며, 소프트 로봇의 자연스럽고 부드러운 움직임 패턴을 생성하지 못할 수 있습니다. 본 연구에서는 소프트 뱀 로봇을 위한 학습 기반 목표 추적 제어기의 생체 모방 설계를 개발합니다. 이 제어기는 두 가지 모듈로 구성됩니다: 로봇의 모델링되지 않은 확률적 동역학을 고려하여 목표 추적 행동을 학습하는 RL 모듈과, 안정적이고 다양한 움직임 패턴을 생성하기 위한 Matsuoka 발진기를 갖춘 중앙 패턴 생성기(CPG)입니다. 우리는 Matsuoka CPG의 진동 바이어스, 주파수 및 진폭이 소프트 뱀 로봇의 조향 제어, 속도 제어 및 시뮬레이션-실제 적응에 미치는 기동성을 이론적으로 조사합니다. 이 분석을 바탕으로, RL 모듈이 로봇의 상태 피드백을 기반으로 CPG 시스템에 대한 긴장 입력을 조절하고, CPG 모듈의 출력이 소프트 뱀 로봇의 공압 액추에이터에 대한 압력 입력으로 변환되는 RL과 CPG 모듈의 구성을 제안합니다. 이 설계는 RL 에이전트가 CPG 기동성에 의해 결정된 원하는 움직임 패턴을 자연스럽게 학습하도록 합니다. 우리는 시뮬레이션과 실제 실험 모두에서 제어 설계의 최적성과 견고성을 검증했으며, 최신 RL 방법과의 광범위한 비교를 통해 생체 모방 제어 설계의 이점을 입증했습니다.
