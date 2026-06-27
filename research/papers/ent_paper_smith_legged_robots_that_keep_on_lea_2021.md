---
$id: ent_paper_smith_legged_robots_that_keep_on_lea_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the
    Real World'
  zh: 持续学习的腿式机器人：在现实世界中微调运动策略
  ko: '지속적으로 학습하는 보행 로봇: 실세계에서의 보행 정책 미세 조정'
summary:
  en: Proposes a practical real-world reinforcement learning system that pre-trains
    locomotion policies via motion imitation in simulation and fine-tunes them on
    a real Unitree A1 quadruped using the sample-efficient off-policy REDQ algorithm,
    onboard state estimation, and a learned reset policy for autonomous recovery.
  zh: 提出了一种实用的现实世界强化学习系统：在仿真中通过动作模仿预训练运动策略，然后在真实的宇树A1四足机器人上使用样本高效的离策略REDQ算法、机载状态估计和学习得到的复位策略进行微调，以实现自主恢复。
  ko: 시뮬레이션에서 동작 모방을 통해 보행 정책을 사전 훈련시키고, 실제 Unitree A1 사족 로봇에서 샘플 효율적인 오프폴리시 REDQ
    알고리즘, 온보드 상태 추정, 그리고 학습된 리셋 정책을 사용하여 자율적으로 복구하면서 미세 조정하는 실용적인 실세계 강화학습 시스템을 제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- real_world_rl
- sim_to_real_transfer
- locomotion_policy
- reinforcement_learning
- motion_imitation
- quadruped_robot
- autonomous_reset
- onboard_state_estimation
- redq
- legged_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in
    the Real World'
  url: https://arxiv.org/abs/2110.05457
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper presents a practical system for real-world reinforcement learning fine-tuning of legged locomotion policies. Rather than attempting to train controllers in simulation that are robust to every possible deployment condition, the authors enable a robot to continue learning after deployment. Policies are first pre-trained in simulation via motion imitation from reference trajectories, then fine-tuned on the physical robot using the sample-efficient off-policy REDQ algorithm. The system incorporates onboard state estimation from an IMU and foot contact sensors, together with a learned reset policy that allows the robot to autonomously recover from falls and continue training without human intervention.

The authors demonstrate the approach on a Unitree A1 quadruped in both outdoor (grass lawn) and indoor environments with varied terrains. The experiments show that a relatively modest amount of real-world training can substantially improve locomotion performance over the simulation-pretrained policy alone. Multiple agile skills, including pacing and side-stepping, are autonomously fine-tuned on the real robot. The work addresses core challenges of real-world RL—sample efficiency, safety, and autonomy—by combining sim-to-real pre-training, an efficient off-policy learner, and an autonomous reset mechanism.

## Key Contributions

- A complete system for real-world autonomous fine-tuning of agile quadrupedal locomotion skills.
- First demonstration of real-world RL fine-tuning with automated resets and onboard state estimation for multiple agile behaviors on an underactuated robot.
- Integration of motion imitation pre-training, the REDQ off-policy RL algorithm, and a learned recovery/reset controller.
- Empirical validation on a Unitree A1 robot across an outdoor lawn and multiple indoor terrains, showing substantial improvement after modest real-world training.

## Relevance to Humanoid Robotics

Although the experiments are conducted on a quadruped, the underlying capabilities developed in this work are directly relevant to humanoid robotics. Real-world RL fine-tuning, autonomous fall recovery without external motion capture, and robust onboard state estimation are foundational requirements for deploying humanoid robots in unstructured human environments. The paper's emphasis on continual learning after deployment, rather than one-shot sim-to-real transfer, aligns with the long-term need for humanoids that can adapt to novel indoor, outdoor, and industrial settings. The integration of an efficient off-policy learner with a learned reset policy also provides a template for autonomous training pipelines that could reduce dependence on instrumented labs and accelerate the industrialization of humanoid platforms.
