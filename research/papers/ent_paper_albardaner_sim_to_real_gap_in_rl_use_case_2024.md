---
$id: ent_paper_albardaner_sim_to_real_gap_in_rl_use_case_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  zh: 强化学习中的仿真到现实差距：基于 TIAGo 与 Isaac Sim/Gym 的实例研究
  ko: 'RL의 시뮬레이션-현실 간격: TIAGo 및 Isaac Sim/Gym 활용 사례'
summary:
  en: This 2024 arXiv paper trains reinforcement-learning policies for the TIAGo mobile
    manipulator in Nvidia Isaac Gym and Isaac Sim, then quantifies joint-response
    differences and accumulated errors against the real robot to demonstrate sim-to-real
    transfer.
  zh: 这篇 2024 年 arXiv 论文在 Nvidia Isaac Gym 和 Isaac Sim 中为 TIAGo 移动操作机器人训练强化学习策略，并通过与真实机器人的关节响应差异和累积误差对比，展示仿真到现实的迁移效果。
  ko: 이 2024년 arXiv 논문은 Nvidia Isaac Gym과 Isaac Sim에서 TIAGo 이동 조작 로봇용 강화학습 정책을 학습한
    후, 실제 로봇과의 관절 응답 차이 및 누적 오차를 정량화하여 시뮬레이션-현실 전이를 입증한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- reinforcement_learning
- isaac_gym
- isaac_sim
- tiago
- mobile_manipulation
- physics_simulation
- control_architecture
- collision_avoidance
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full paper not independently retrieved
    for verification.
sources:
- id: src_001
  type: paper
  title: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  url: https://arxiv.org/abs/2403.07091
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This study addresses the sim-to-real gap for reinforcement-learning policies in robotic manipulation. The authors train RL policies for PAL Robotics' TIAGo mobile manipulator inside two Nvidia simulators, Isaac Gym and Isaac Sim, and then execute the trained policies on the physical TIAGo robot. They compare the control pipelines, joint responses, and accumulated errors of each simulator against the real hardware. A central concern throughout the work is achieving collision-free motion both in simulation and on the real robot. The quantitative comparison highlights that the two simulators exhibit different joint responses and velocity constraints, which must be understood and compensated for during transfer.

The paper focuses on a home-to-zero arm movement task as the use case. Policies are trained with reinforcement learning and deployed through ROS-based controllers on the real platform, including JointGroupPosition, PD, and PID controllers. The authors report that, despite the identified discrepancies, the RL-trained model produces similar movements in simulation and reality, indicating that successful sim-to-real transfer is feasible for this manipulation task when the control architecture is carefully aligned.

## Key Contributions

- Comparative analysis of Isaac Gym and Isaac Sim for the TIAGo mobile manipulator.
- Identification of control-pipeline differences between the two simulators and the real robot.
- Demonstration of successful sim-to-real transfer with qualitatively similar simulated and real movements.
- Quantitative analysis of joint-response differences and accumulated errors between the simulators and real hardware.

## Relevance to Humanoid Robotics

Although the experiments are conducted on TIAGo, a mobile manipulator rather than a humanoid, the methodology is directly relevant to humanoid robotics. Sim-to-real transfer is a foundational challenge for humanoid policy deployment at scale, and the paper's comparison of Isaac Gym versus Isaac Sim, its treatment of control architectures, and its collision-avoidance insights provide transferable lessons. Humanoid platforms typically face even higher dimensionalities and contact-rich dynamics, making the careful alignment of simulator physics, controller interfaces, and real-robot execution emphasized here equally critical for humanoids.
