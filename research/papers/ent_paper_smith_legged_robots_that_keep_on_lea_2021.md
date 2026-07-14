---
$id: ent_paper_smith_legged_robots_that_keep_on_lea_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World'
  zh: 持续学习的腿式机器人：在现实世界中微调运动策略
  ko: '지속적으로 학습하는 보행 로봇: 실세계에서의 보행 정책 미세 조정'
summary:
  en: Proposes a practical real-world reinforcement learning system that pre-trains locomotion policies via motion imitation
    in simulation and fine-tunes them on a real Unitree A1 quadruped using the sample-efficient off-policy REDQ algorithm,
    onboard state estimation, and a learned reset policy for autonomous recovery.
  zh: 提出了一种实用的现实世界强化学习系统：在仿真中通过动作模仿预训练运动策略，然后在真实的宇树A1四足机器人上使用样本高效的离策略REDQ算法、机载状态估计和学习得到的复位策略进行微调，以实现自主恢复。
  ko: 시뮬레이션에서 동작 모방을 통해 보행 정책을 사전 훈련시키고, 실제 Unitree A1 사족 로봇에서 샘플 효율적인 오프폴리시 REDQ 알고리즘, 온보드 상태 추정, 그리고 학습된 리셋 정책을 사용하여 자율적으로
    복구하면서 미세 조정하는 실용적인 실세계 강화학습 시스템을 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2110.05457v1.
sources:
- id: src_001
  type: paper
  title: 'Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World'
  url: https://arxiv.org/abs/2110.05457
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Legged robots are physically capable of traversing a wide range of challenging environments, but designing controllers that are sufficiently robust to handle this diversity has been a long-standing challenge in robotics. Reinforcement learning presents an appealing approach for automating the controller design process and has been able to produce remarkably robust controllers when trained in a suitable range of environments. However, it is difficult to predict all likely conditions the robot will encounter during deployment and enumerate them at training-time. What if instead of training controllers that are robust enough to handle any eventuality, we enable the robot to continually learn in any setting it finds itself in? This kind of real-world reinforcement learning poses a number of challenges, including efficiency, safety, and autonomy. To address these challenges, we propose a practical robot reinforcement learning system for fine-tuning locomotion policies in the real world. We demonstrate that a modest amount of real-world training can substantially improve performance during deployment, and this enables a real A1 quadrupedal robot to autonomously fine-tune multiple locomotion skills in a range of environments, including an outdoor lawn and a variety of indoor terrains.

## 核心内容
Legged robots are physically capable of traversing a wide range of challenging environments, but designing controllers that are sufficiently robust to handle this diversity has been a long-standing challenge in robotics. Reinforcement learning presents an appealing approach for automating the controller design process and has been able to produce remarkably robust controllers when trained in a suitable range of environments. However, it is difficult to predict all likely conditions the robot will encounter during deployment and enumerate them at training-time. What if instead of training controllers that are robust enough to handle any eventuality, we enable the robot to continually learn in any setting it finds itself in? This kind of real-world reinforcement learning poses a number of challenges, including efficiency, safety, and autonomy. To address these challenges, we propose a practical robot reinforcement learning system for fine-tuning locomotion policies in the real world. We demonstrate that a modest amount of real-world training can substantially improve performance during deployment, and this enables a real A1 quadrupedal robot to autonomously fine-tune multiple locomotion skills in a range of environments, including an outdoor lawn and a variety of indoor terrains.

## 参考
- http://arxiv.org/abs/2110.05457v1

