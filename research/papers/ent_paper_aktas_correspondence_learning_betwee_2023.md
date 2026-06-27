---
$id: ent_paper_aktas_correspondence_learning_betwee_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Correspondence learning between morphologically different robots via task demonstrations
  zh: 基于任务演示的形态不同机器人之间的对应关系学习
  ko: 작업 시연을 통한 형태학적으로 다른 로봇 간 대응 관계 학습
summary:
  en: Proposes a correspondence-learning framework that trains separate Conditional
    Neural Movement Primitives for each robot and blends their latent codes through
    a learned convex combination, enabling zero-shot trajectory generation across
    morphologically different robots from a single task demonstration.
  zh: 提出一种对应关系学习框架，为每个机器人训练独立的条件神经运动基元，并通过学习的凸组合融合其潜在编码，从而从单次任务演示中实现跨形态不同机器人的零样本轨迹生成。
  ko: 각 로봇에 대해 개별적인 조건적 신경 운동 기본형을 학습하고 학습된 볼록 조합을 통해 잠재 코드를 혼합하여, 단일 작업 시연으로 형태학적으로
    다른 로봇 간 제로샷 궤적 생성을 가능하게 하는 대응 관계 학습 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- skill_transfer
- correspondence_learning
- conditional_neural_movement_primitives
- zero_shot_learning
- morphological_differences
- latent_representation
- imitation_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided abstract and metadata; requires human review against
    the full PDF before verification.
sources:
- id: src_001
  type: paper
  title: Correspondence learning between morphologically different robots via task
    demonstrations
  url: https://arxiv.org/abs/2310.13458
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Aktas et al. address the scalability problem of teaching every skill to every robot independently by learning correspondences between the sensorimotor spaces of morphologically different robots. The authors first demonstrate an initial base task to each robot so that all robots share the same goal. They then train a separate Conditional Neural Movement Primitive (CNMP) for each robot and learn a common latent representation by convexly blending the individual latent codes. After this initial learning stage, observing a new task execution by one robot is sufficient to generate the corresponding latent representation and trajectory for the other robots.

The framework is designed to handle two or more robots without requiring per-pair hyperparameter tuning. The authors show experiments in three settings: robots following the same paths, robots following different trajectories to reach the same goal, and tasks where the required sensorimotor trajectories differ in complexity. They also present a proof-of-concept realization combining a real UR-10 manipulator and a simulated mobile robot.

The proposed architecture avoids the factorial growth of pairwise alignment losses that burden earlier methods, making the approach more scalable as the number of robots increases. The method does not rely on object geometric or visual features; it builds correspondences purely from demonstrated sensorimotor trajectories.

## Key Contributions

- A correspondence-learning framework applicable to two or more morphologically different robots without per-pair hyperparameter tuning.
- A common latent representation formed by convexly blending individual CNMP latent codes.
- Zero-shot skill transfer demonstrated between fixed-base manipulators and a differential-drive mobile robot.
- A scalable architecture that avoids the factorial growth of pairwise alignment losses required by prior methods.
- A real-world proof-of-concept combining a real UR-10 manipulator and a simulated mobile robot.

## Relevance to Humanoid Robotics

The paper is highly relevant to humanoid robotics because it provides a principled way to transfer skills across heterogeneous platforms that differ in bodies, sensors, and actuators. Humanoid robots exhibit large morphological variety across manufacturers and research platforms, so a method that can align sensorimotor correspondences without re-teaching every skill to each robot directly supports scalable humanoid deployment. The framework's reliance on task demonstrations rather than hand-crafted mappings also matches the practical need to teach humanoid robots through imitation or teleoperation.
