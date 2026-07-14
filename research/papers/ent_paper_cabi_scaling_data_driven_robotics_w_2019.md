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
  en: Introduces reward sketching to learn task-specific reward functions from human preferences, retrospectively labels stored
    robot experience, and trains visuomotor policies offline via batch reinforcement learning to scale real-world manipulation
    learning.
  zh: 提出奖励草图以从人类偏好中学习任务奖励，对存储的机器人经验进行回顾性标注，并通过批量强化学习离线训练视觉运动策略，以扩展真实世界操作学习。
  ko: 인간의 선호도에서 작업 보상을 학습하는 보상 스케칭을 도입하고, 저장된 로봇 경험을 소급 라벨링한 뒤 배치 강화학습으로 오프라인에서 시각운동 정책을 훈련하여 실제 조작 학습을 확장한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.12200v3.
sources:
- id: src_001
  type: paper
  title: Scaling data-driven robotics with reward sketching and batch reinforcement learning
  url: https://arxiv.org/abs/1909.12200
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
We present a framework for data-driven robotics that makes use of a large dataset of recorded robot experience and scales to several tasks using learned reward functions. We show how to apply this framework to accomplish three different object manipulation tasks on a real robot platform. Given demonstrations of a task together with task-agnostic recorded experience, we use a special form of human annotation as supervision to learn a reward function, which enables us to deal with real-world tasks where the reward signal cannot be acquired directly. Learned rewards are used in combination with a large dataset of experience from different tasks to learn a robot policy offline using batch RL. We show that using our approach it is possible to train agents to perform a variety of challenging manipulation tasks including stacking rigid objects and handling cloth.

## 核心内容
We present a framework for data-driven robotics that makes use of a large dataset of recorded robot experience and scales to several tasks using learned reward functions. We show how to apply this framework to accomplish three different object manipulation tasks on a real robot platform. Given demonstrations of a task together with task-agnostic recorded experience, we use a special form of human annotation as supervision to learn a reward function, which enables us to deal with real-world tasks where the reward signal cannot be acquired directly. Learned rewards are used in combination with a large dataset of experience from different tasks to learn a robot policy offline using batch RL. We show that using our approach it is possible to train agents to perform a variety of challenging manipulation tasks including stacking rigid objects and handling cloth.

## 参考
- http://arxiv.org/abs/1909.12200v3

