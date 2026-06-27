---
$id: ent_paper_johns_coarse_to_fine_imitation_learn_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  zh: 从粗到精的模仿学习：单演示下的机器人操作
  ko: 'Coarse-to-Fine 모방 학습: 단일 시연으로부터의 로봇 조작'
summary:
  en: Johns (2021) proposes a visual imitation-learning method that learns a novel
    manipulation task from a single human demonstration by estimating the end-effector's
    bottleneck pose and replaying the demonstration's end-effector velocities from
    that pose.
  zh: Johns（2021）提出了一种视觉模仿学习方法，通过估计末端执行器的瓶颈位姿并从此位姿开始回放演示的末端执行器速度，从单条人类演示中学习新的操作任务。
  ko: Johns(2021)은 엔드이펙터의 병목 자세를 추정하고 해당 자세부터 시연의 엔드이펙터 속도를 재생함으로써 단일 인간 시연으로부터 새로운
    조작 작업을 학습하는 시각적 모방 학습 방법을 제안한다.
domains:
- 07_ai_models_algorithms
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- imitation_learning
- single_demonstration_learning
- visual_imitation
- bottleneck_pose_estimation
- end_effector_velocity_replay
- self_supervised_learning
- manipulation
- sawyer_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full paper before full verification.
sources:
- id: src_001
  type: paper
  title: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  url: https://arxiv.org/abs/2105.06411
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper introduces a method for visual imitation learning that enables a robot to learn a new manipulation task from a single human demonstration without prior object knowledge. The core idea is to treat imitation learning as a state estimation problem, where the estimated state is the end-effector's pose at the moment object interaction begins. The method decomposes a manipulation task into a coarse approach trajectory and a fine interaction trajectory, enabling self-supervised training of a bottleneck pose estimator by moving the end-effector camera around the object. At test time, the robot first moves linearly to the estimated bottleneck pose and then replays the end-effector velocities from the original demonstration, avoiding the need to explicitly learn a control policy.

## Key Contributions

- Formulates imitation learning as state estimation for the bottleneck pose at the start of object interaction.
- Decomposes manipulation into a coarse approach trajectory and a fine interaction trajectory.
- Trains the bottleneck pose estimator self-supervisedly by automatically moving the end-effector camera around the object.
- Avoids explicit policy learning by replaying the demonstration's end-effector velocities from the bottleneck pose.
- Demonstrates real-world single-demonstration learning on eight everyday manipulation tasks using a Sawyer robot.

## Relevance to Humanoid Robotics

The coarse-to-fine imitation-learning framework is relevant to humanoid robotics because it offers a lightweight mechanism for acquiring complex manipulation trajectories from minimal human demonstration. For humanoid assembly, service, or mass-production tasks, the ability to transfer a skill from a single operator demonstration—without object-specific prior knowledge—could reduce programming overhead and accelerate deployment. The self-supervised bottleneck estimation and velocity replay approach also yield an interpretable controller, which is valuable for debugging and safety validation in humanoid systems.
