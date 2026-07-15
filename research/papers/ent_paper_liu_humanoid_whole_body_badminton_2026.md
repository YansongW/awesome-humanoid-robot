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
  en: A unified whole-body reinforcement-learning controller enables a 21-DoF humanoid to play badminton in simulation and
    on hardware, achieving 21-hit rallies in simulation and outgoing shuttle speeds up to 19.1 m/s in real-world tests.
  zh: 'Humanoid robots have demonstrated strong capabilities for interacting with static scenes across locomotion and manipulation,
    yet dynamic real-world interactions remain challenging. As a step toward fast-moving object interactions, we present a
    reinforcement-learning training pipeline that yields a unified whole-body controller for humanoid badminton, coordinating
    footwork and striking without motion priors or expert demonstrations. Training follows a three-stage curriculum (footwork
    acquisition, precision-guided swing generation, and task-focused refinement) so legs and arms jointly serve the '
  ko: 통합된 전신 강화학습 제어기를 통해 21자유도 휴머노이드가 시뮬레이션 및 실제 환경에서 배드민턴을 칠 수 있으며, 시뮬레이션에서는 21회 연속 랠리를, 실제 테스트에서는 초당 최대 19.1m의 셔틀콕 속도를
    달성했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.11218v3.
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning
  url: https://arxiv.org/abs/2511.11218
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
Humanoid robots have demonstrated strong capabilities for interacting with static scenes across locomotion and manipulation, yet dynamic real-world interactions remain challenging. As a step toward fast-moving object interactions, we present a reinforcement-learning training pipeline that yields a unified whole-body controller for humanoid badminton, coordinating footwork and striking without motion priors or expert demonstrations. Training follows a three-stage curriculum (footwork acquisition, precision-guided swing generation, and task-focused refinement) so legs and arms jointly serve the hitting objective. For deployment, we use an Extended Kalman Filter (EKF) to estimate and predict shuttlecock trajectories for target striking, and also develop a prediction-free variant that removes the EKF and explicit prediction. We validate the framework with five sets of experiments in simulation and on hardware. In simulation, two robots sustain a rally of 21 consecutive hits. In real-world tests with both machine-fed shuttles and human-robot rallies, the robot achieves outgoing shuttle speeds up to 19.1~m/s with a mean return landing distance of 4~m. Moreover, the prediction-free variant attains comparable performance to the EKF-based target-known policy. Overall, our approach enables dynamic yet precise goal striking in humanoid badminton and suggests a path toward more dynamics-critical whole-body interaction tasks.

## 核心内容
Humanoid robots have demonstrated strong capabilities for interacting with static scenes across locomotion and manipulation, yet dynamic real-world interactions remain challenging. As a step toward fast-moving object interactions, we present a reinforcement-learning training pipeline that yields a unified whole-body controller for humanoid badminton, coordinating footwork and striking without motion priors or expert demonstrations. Training follows a three-stage curriculum (footwork acquisition, precision-guided swing generation, and task-focused refinement) so legs and arms jointly serve the hitting objective. For deployment, we use an Extended Kalman Filter (EKF) to estimate and predict shuttlecock trajectories for target striking, and also develop a prediction-free variant that removes the EKF and explicit prediction. We validate the framework with five sets of experiments in simulation and on hardware. In simulation, two robots sustain a rally of 21 consecutive hits. In real-world tests with both machine-fed shuttles and human-robot rallies, the robot achieves outgoing shuttle speeds up to 19.1~m/s with a mean return landing distance of 4~m. Moreover, the prediction-free variant attains comparable performance to the EKF-based target-known policy. Overall, our approach enables dynamic yet precise goal striking in humanoid badminton and suggests a path toward more dynamics-critical whole-body interaction tasks.

## 参考
- http://arxiv.org/abs/2511.11218v3


