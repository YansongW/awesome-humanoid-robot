---
$id: ent_paper_liu_humanoid_whole_body_badminton_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning
  zh: 基于多阶段强化学习的人形全身羽毛球运动
  ko: 다단계 강화학습을 통한 휴머노이드 전신 배드민턴
summary:
  en: A unified whole-body reinforcement-learning controller enables a 21-DoF humanoid
    to play badminton in simulation and on hardware, achieving 21-hit rallies in simulation
    and outgoing shuttle speeds up to 19.1 m/s in real-world tests.
  zh: 统一的全身强化学习控制器使21自由度人形机器人能够在仿真和硬件中打羽毛球，仿真中实现21次连续击球回合，真实测试中羽毛球出球速度高达19.1米/秒。
  ko: 통합된 전신 강화학습 제어기를 통해 21자유도 휴머노이드가 시뮬레이션 및 실제 환경에서 배드민턴을 칠 수 있으며, 시뮬레이션에서는 21회
    연속 랠리를, 실제 테스트에서는 초당 최대 19.1m의 셔틀콕 속도를 달성했다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- whole_body_control
- sim_to_real
- humanoid_locomotion
- badminton
- ppo
- isaacgym
- extended_kalman_filter
- prediction_free
- dynamic_object_interaction
- curriculum_learning
- phybot_c1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; exact section-level source
    citations require human review against the full paper.
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning
  url: https://arxiv.org/abs/2511.11218
  date: '2026'
  accessed_at: '2026-06-26'
---


## Overview

This paper presents a reinforcement-learning pipeline for humanoid badminton that trains a unified whole-body controller without relying on motion priors or expert demonstrations. The training curriculum is divided into three stages: footwork acquisition, precision-guided swing generation, and task-focused refinement. Through this staged approach, the robot learns to coordinate leg movements and arm swings toward the common objective of hitting the shuttlecock. Deployment is performed with an Extended Kalman Filter (EKF) that estimates and predicts shuttlecock trajectories to determine when and where to strike, and a prediction-free variant is also developed that conditions the policy on a short history of shuttle positions.

The authors validate the framework through five sets of experiments in simulation and on hardware. In simulation, two robots sustain a rally of 21 consecutive hits. Real-world tests with machine-fed shuttles and human-robot rallies demonstrate outgoing shuttle speeds up to 19.1 m/s and a mean return landing distance of 4 m. The prediction-free variant achieves comparable performance to the EKF-based target-known policy, indicating that explicit trajectory prediction may not be strictly necessary for this task.

## Key Contributions

- First real-world humanoid badminton system using a single unified whole-body RL controller.
- Three-stage RL curriculum that fosters footwork-strike synergy without motion priors or expert demonstrations.
- Both EKF-based and prediction-free deployment variants, with the latter inferring hit timing and pose from short shuttle position history.
- Zero-shot sim-to-real transfer on a 21-DoF 1.28 m humanoid achieving 19.1 m/s outgoing shuttle speeds and human-robot rallies.

## Relevance to Humanoid Robotics

The work is relevant to humanoid robotics because it demonstrates zero-shot sim-to-real deployment of a learned unified whole-body controller on a real humanoid for a dynamic, fast-moving object interaction task. The learned controller jointly manages locomotion and manipulation, advancing the agility, coordination, and reactivity required for practical humanoid deployment in unstructured environments. Although the badminton task is a research demonstration, the underlying methods for whole-body RL, curriculum design, and sim-to-real transfer are directly applicable to broader dynamic manipulation and sports or service tasks for humanoids.
