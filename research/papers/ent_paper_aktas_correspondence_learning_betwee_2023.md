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
  en: Proposes a correspondence-learning framework that trains separate Conditional Neural Movement Primitives for each robot
    and blends their latent codes through a learned convex combination, enabling zero-shot trajectory generation across morphologically
    different robots from a single task demonstration.
  zh: 提出一种对应关系学习框架，为每个机器人训练独立的条件神经运动基元，并通过学习的凸组合融合其潜在编码，从而从单次任务演示中实现跨形态不同机器人的零样本轨迹生成。
  ko: 각 로봇에 대해 개별적인 조건적 신경 운동 기본형을 학습하고 학습된 볼록 조합을 통해 잠재 코드를 혼합하여, 단일 작업 시연으로 형태학적으로 다른 로봇 간 제로샷 궤적 생성을 가능하게 하는 대응 관계 학습 프레임워크를
    제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.13458v3.
sources:
- id: src_001
  type: paper
  title: Correspondence learning between morphologically different robots via task demonstrations
  url: https://arxiv.org/abs/2310.13458
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
We observe a large variety of robots in terms of their bodies, sensors, and actuators. Given the commonalities in the skill sets, teaching each skill to each different robot independently is inefficient and not scalable when the large variety in the robotic landscape is considered. If we can learn the correspondences between the sensorimotor spaces of different robots, we can expect a skill that is learned in one robot can be more directly and easily transferred to other robots. In this paper, we propose a method to learn correspondences among two or more robots that may have different morphologies. To be specific, besides robots with similar morphologies with different degrees of freedom, we show that a fixed-based manipulator robot with joint control and a differential drive mobile robot can be addressed within the proposed framework. To set up the correspondence among the robots considered, an initial base task is demonstrated to the robots to achieve the same goal. Then, a common latent representation is learned along with the individual robot policies for achieving the goal. After the initial learning stage, the observation of a new task execution by one robot becomes sufficient to generate a latent space representation pertaining to the other robots to achieve the same task. We verified our system in a set of experiments where the correspondence between robots is learned (1) when the robots need to follow the same paths to achieve the same task, (2) when the robots need to follow different trajectories to achieve the same task, and (3) when complexities of the required sensorimotor trajectories are different for the robots. We also provide a proof-of-the-concept realization of correspondence learning between a real manipulator robot and a simulated mobile robot.

## 核心内容
We observe a large variety of robots in terms of their bodies, sensors, and actuators. Given the commonalities in the skill sets, teaching each skill to each different robot independently is inefficient and not scalable when the large variety in the robotic landscape is considered. If we can learn the correspondences between the sensorimotor spaces of different robots, we can expect a skill that is learned in one robot can be more directly and easily transferred to other robots. In this paper, we propose a method to learn correspondences among two or more robots that may have different morphologies. To be specific, besides robots with similar morphologies with different degrees of freedom, we show that a fixed-based manipulator robot with joint control and a differential drive mobile robot can be addressed within the proposed framework. To set up the correspondence among the robots considered, an initial base task is demonstrated to the robots to achieve the same goal. Then, a common latent representation is learned along with the individual robot policies for achieving the goal. After the initial learning stage, the observation of a new task execution by one robot becomes sufficient to generate a latent space representation pertaining to the other robots to achieve the same task. We verified our system in a set of experiments where the correspondence between robots is learned (1) when the robots need to follow the same paths to achieve the same task, (2) when the robots need to follow different trajectories to achieve the same task, and (3) when complexities of the required sensorimotor trajectories are different for the robots. We also provide a proof-of-the-concept realization of correspondence learning between a real manipulator robot and a simulated mobile robot.

## 参考
- http://arxiv.org/abs/2310.13458v3

