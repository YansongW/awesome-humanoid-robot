---
$id: ent_paper_farazi_nimbro_robots_winning_robocup_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: NimbRo Robots Winning RoboCup 2018 Humanoid AdultSize Soccer Competitions
  zh: NimbRo机器人赢得2018年RoboCup人形成人组足球比赛
  ko: NimbRo 로봇, 2018 RoboCup 휴머노이드 AdultSize 축구 대회 우승
summary:
  en: This paper presents the open-source hardware and software designs that enabled
    Team NimbRo to win all AdultSize competitions and the Best Humanoid Award at RoboCup
    2018, including a deep-learning visual perception system, a modular hierarchical
    state machine for soccer behaviors, Bayesian gait optimization, and the fully
    3D-printed NimbRo-OP2X robot.
  zh: 本文介绍了使NimbRo队在2018年RoboCup人形成人组比赛中赢得所有奖项（包括最佳人形机器人奖）的开源软硬件设计，包括基于深度学习的视觉感知系统、模块化的分层状态机足球行为、贝叶斯步态优化以及全3D打印的NimbRo-OP2X机器人。
  ko: 본 논문은 2018 RoboCup 휴머노이드 AdultSize 대회에서 모든 부문과 최고 휴머노이드상을 수상한 NimbRo 팀의 오픈소스
    하드웨어 및 소프트웨어 설계를 제시하며, 딥러닝 기반 시각 인식 시스템, 모듈화된 계층적 상태 기반 축구 행위, 베이지안 보행 최적화, 그리고
    완전 3D 프린팅된 NimbRo-OP2X 로봇을 포함한다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- robocup
- humanoid_soccer
- adult_size
- nimbro_op2x
- deep_learning_perception
- gait_optimization
- bayesian_optimization
- hierarchical_state_machine
- ros
- 3d_printed_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the arXiv source; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: NimbRo Robots Winning RoboCup 2018 Humanoid AdultSize Soccer Competitions
  url: https://arxiv.org/abs/1909.02385
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## Overview

Team NimbRo's 2018 AdultSize entry combined three robot platforms—Copedo, NimbRo-OP2, and the newly redesigned fully 3D-printed NimbRo-OP2X—with an open-source ROS-based software stack. The paper describes a deep-learning visual perception pipeline that detects the ball, goal posts, and opponent robots using an encoder-decoder convolutional network with a ResNet-18 encoder and sub-pixel centroid post-processing. Behaviors are organized as a modular, multi-layer hierarchical state machine that maps high-level game strategy to low-level walking, kicking, and dribbling skills, while obstacle avoidance and ball handling are implemented generically across skills. Bipedal walking is stabilized by fused-angle feedback controllers whose parameters are tuned with a Bayesian optimization approach that fuses inexpensive simulation evaluations with a limited number of real-world experiments.

At RoboCup 2018 in Montreal, these integrated designs enabled NimbRo to win every AdultSize award: the main soccer tournament, the drop-in games, the technical challenges (Push Recovery, High Jump, High Kick, and Goal Kick from Moving Ball), and the overall Best Humanoid Award. The team officially played 220 minutes with a goal difference of 66:5. The authors also release the NimbRo-OP2 generation hardware and the ROS software stack as open source.

## Key Contributions

- A deep-learning visual perception system for detecting the ball, goal posts, and robots in real time under variable lighting and lens distortions.
- NimbRo-OP2X, a fully 3D-printed adult-sized humanoid robot using Robotis Dynamixel XM-540 actuators, SLS printing, and low-backlash double helical gears.
- A modular, multi-layer hierarchical state machine architecture for soccer behaviors, packaged as a ROS module.
- Bayesian gait optimization that combines many simulated evaluations with a small number of real-world evaluations to tune fused-angle feedback controllers.
- Winning all AdultSize competitions—soccer tournament, drop-in games, technical challenges—and the Best Humanoid Award at RoboCup 2018.

## Relevance to Humanoid Robotics

The work demonstrates a complete, open-source adult-sized humanoid system integrating perception, locomotion, and behavior in a dynamic, competitive environment. Its 3D-printed hardware, standardized actuators, and modular software provide practical design and manufacturing principles relevant to affordable, reproducible humanoid robots, while the perception and gait optimization methods are directly applicable to robust humanoid locomotion and scene understanding.
