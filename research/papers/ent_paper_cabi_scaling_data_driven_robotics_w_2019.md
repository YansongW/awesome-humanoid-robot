---
$id: ent_paper_cabi_scaling_data_driven_robotics_w_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling data-driven robotics with reward sketching and batch reinforcement learning
  zh: 通过奖励草图和批量强化学习扩展数据驱动的机器人技术
  ko: 보상 스케칭과 배치 강화학습을 통한 데이터 기반 로보틱스 확장
summary:
  en: Introduces reward sketching to learn task-specific reward functions from human
    preferences, retrospectively labels stored robot experience, and trains visuomotor
    policies offline via batch reinforcement learning to scale real-world manipulation
    learning.
  zh: 提出奖励草图以从人类偏好中学习任务奖励，对存储的机器人经验进行回顾性标注，并通过批量强化学习离线训练视觉运动策略，以扩展真实世界操作学习。
  ko: 인간의 선호도에서 작업 보상을 학습하는 보상 스케칭을 도입하고, 저장된 로봇 경험을 소급 라벨링한 뒤 배치 강화학습으로 오프라인에서 시각운동
    정책을 훈련하여 실제 조작 학습을 확장한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- reward_sketching
- batch_reinforcement_learning
- offline_rl
- distributional_rl
- human_in_the_loop
- visuomotor_policy
- robot_learning
- manipulation
- neverending_storage
- data_driven_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and full PDF; hardware details and dataset
    names verified against the paper text, but some claims require human review.
sources:
- id: src_001
  type: paper
  title: Scaling data-driven robotics with reward sketching and batch reinforcement
    learning
  url: https://arxiv.org/abs/1909.12200
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Real-world robot learning is typically bottlenecked by the need to design hand-crafted rewards and collect fresh on-robot experience for every new task. This paper presents a cyclical framework that harnesses a growing dataset of recorded robot experience to learn visuomotor policies for diverse manipulation tasks. At its center are three ideas: efficiently eliciting human preferences to learn a reward function, automatically annotating all historical data with that reward function, and training policies purely from stored data via offline batch reinforcement learning. The authors introduce reward sketching, an interface in which a human annotator draws a per-timestep reward curve over an episode, providing supervision to learn a task-specific reward model. This model is applied retrospectively to all trajectories in NeverEnding Storage (NES), a relational metadata system that records multi-camera and sensor experience across tasks. The annotated dataset is then used to train recurrent visuomotor policies with a D4PG-like batch RL algorithm using distributional value functions, without further real-robot interaction. The approach is evaluated on a Sawyer robot with a Robotiq 2F-85 gripper, wrist cameras, and a wrist force-torque sensor, on tasks such as lifting and stacking rigid objects, lifting cloth, and USB insertion. The learned agents exhibit robustness and generalization, sometimes outperforming human teleoperators. Limitations include the need for human-in-the-loop annotation, sensitivity to large setup perturbations, and unsuitability for tasks requiring variable speed or cyclic motion.

## Key Contributions

- Reward sketching: a human-in-the-loop interface for eliciting per-timestep reward annotations to learn task reward functions.
- Retrospective reward assignment that repurposes all historical robot experience stored in NES for new tasks.
- Offline batch reinforcement learning with distributional value functions to train visuomotor policies purely from stored visual robot data.
- NeverEnding Storage (NES), a scalable relational metadata system for robot experience.
- Real-robot demonstrations on rigid/deformable object stacking, lifting, and USB insertion, with agents sometimes outperforming human teleoperators.

## Relevance to Humanoid Robotics

The paper's pipeline—learning reward functions from human feedback and training policies offline from large stored datasets—directly addresses the data-scaling challenge that humanoid robots face when acquiring diverse manipulation skills. By reusing historical experience and reducing the need for per-task online rollouts, the approach can accelerate skill acquisition and generalization for complex, contact-rich tasks in industrial or service settings. However, the experiments were conducted on a single-arm Sawyer manipulator rather than a full humanoid, so transfer to high-DoF, whole-body, or bipedal humanoid systems requires further validation.
