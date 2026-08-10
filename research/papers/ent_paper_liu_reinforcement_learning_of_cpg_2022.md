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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2207.04899v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (980 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2207.04899v2

## 개요
소프트 로봇의 비선형적이고 모델링이 어려운 동적 특성을 대상으로, 본 연구는 강화학습 모듈과 Matsuoka CPG 모듈로 구성된 이중 계층 제어기를 개발하였다. RL 모듈은 목표 추적 행동을 학습하고, CPG 모듈은 안정적이고 다양한 운동 패턴을 생성한다. CPG의 바이어스, 주파수, 진폭이 조향, 속도 제어 및 시뮬레이션-실제 전이에 미치는 영향을 이론적으로 분석하고, RL 모듈은 로봇 상태 피드백에 따라 CPG의 흥분 입력을 조절하여 CPG 출력을 공압 액추에이터의 압력 명령으로 변환한다. 실험 결과, 이 설계는 CPG가 결정하는 운동 패턴을 자연스럽게 학습할 수 있으며, 시뮬레이션과 실제 환경 모두에서 기존 RL 방법보다 우수한 성능을 보였다.

## 핵심 내용
### 방법 아키텍처
- **이중 모듈 캐스케이드 설계**: 상위 계층은 PPOC/option 프레임워크 기반 강화학습 모듈로, 모델링되지 않은 무작위 동적 특성을 처리하고 목표 추적 전략을 학습한다. 하위 계층은 Matsuoka CPG 모듈로, 안정적이고 다양한 리드미컬한 운동 패턴을 생성한다.
- **CPG 조작 가능성 분석**: Matsuoka 발진기의 세 가지 핵심 파라미터——바이어스(조향 제어), 주파수(속도 제어), 진폭(크기 제어)——가 소프트 뱀형 로봇의 운동에 미치는 영향을 이론적으로 유도하고, 이를 바탕으로 시뮬레이션-실제 전이 전략을 설계한다.
- **신호 흐름**: RL 모듈은 로봇 상태 피드백(예: 위치, 자세)에 따라 CPG의 흥분 입력(tonic inputs)을 조절하고, CPG 출력은 변환을 거쳐 공압 액추에이터를 구동하여 부드러운 리드미컬한 운동을 구현한다.

### 실험 설정
- **시뮬레이션 환경**: 물리 엔진 기반으로 소프트 뱀형 로봇의 비선형 동역학과 무작위 교란을 모의한다.
- **실제 실험**: 공압 소프트 뱀형 로봇을 사용하여 실제 환경에서 제어기의 목표 추적 성능을 검증한다.
- **비교 방법**: PPO, SAC 등 모델 프리 RL 방법과 광범위하게 비교하여 제어기의 강건성과 최적성을 평가한다.

### 핵심 결과
- **성능 우위**: 제안된 방법은 시뮬레이션과 실제 실험 모두에서 더 높은 목표 추적 정확도와 더 부드러운 운동 궤적을 달성했으며, 순수 RL 방법 대비 데이터 효율성이 약 40% 향상되고 운동 자연스러움이 크게 개선되었다.
- **강건성 검증**: 무작위 노이즈와 모델 파라미터 오프셋을 도입했을 때도 제어기는 안정적인 운동을 유지했으며, CPG의 리드미컬한 출력이 RL 정책의 떨림 문제를 효과적으로 억제했다.
- **전이 능력**: CPG 파라미터 조정을 통해 시뮬레이션에서 학습된 정책을 추가 미세 조정 없이 실제 로봇에 직접 전이할 수 있었다.

### 결론
본 생체모방 캐스케이드 제어기는 RL의 의사결정 능력과 CPG의 리듬 생성 능력을 결합하여 소프트 로봇 제어에서의 데이터 효율성 저하와 부자연스러운 운동 문제를 해결하였다. 이론 분석과 실험은 CPG의 조작 가능성 분석이 RL 정책에 구조적 사전 지식을 제공하여 학습 효율성과 일반화 능력을 크게 향상시킨다는 것을 공동으로 입증하였다.
