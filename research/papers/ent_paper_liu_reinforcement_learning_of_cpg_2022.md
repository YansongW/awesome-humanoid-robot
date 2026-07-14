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

