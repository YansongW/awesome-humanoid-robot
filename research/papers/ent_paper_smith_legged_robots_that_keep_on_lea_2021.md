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

## Overview
Legged robots are physically capable of traversing a wide range of challenging environments, but designing controllers that are sufficiently robust to handle this diversity has been a long-standing challenge in robotics. Reinforcement learning presents an appealing approach for automating the controller design process and has been able to produce remarkably robust controllers when trained in a suitable range of environments. However, it is difficult to predict all likely conditions the robot will encounter during deployment and enumerate them at training-time. What if instead of training controllers that are robust enough to handle any eventuality, we enable the robot to continually learn in any setting it finds itself in? This kind of real-world reinforcement learning poses a number of challenges, including efficiency, safety, and autonomy. To address these challenges, we propose a practical robot reinforcement learning system for fine-tuning locomotion policies in the real world. We demonstrate that a modest amount of real-world training can substantially improve performance during deployment, and this enables a real A1 quadrupedal robot to autonomously fine-tune multiple locomotion skills in a range of environments, including an outdoor lawn and a variety of indoor terrains.

## Content
Legged robots are physically capable of traversing a wide range of challenging environments, but designing controllers that are sufficiently robust to handle this diversity has been a long-standing challenge in robotics. Reinforcement learning presents an appealing approach for automating the controller design process and has been able to produce remarkably robust controllers when trained in a suitable range of environments. However, it is difficult to predict all likely conditions the robot will encounter during deployment and enumerate them at training-time. What if instead of training controllers that are robust enough to handle any eventuality, we enable the robot to continually learn in any setting it finds itself in? This kind of real-world reinforcement learning poses a number of challenges, including efficiency, safety, and autonomy. To address these challenges, we propose a practical robot reinforcement learning system for fine-tuning locomotion policies in the real world. We demonstrate that a modest amount of real-world training can substantially improve performance during deployment, and this enables a real A1 quadrupedal robot to autonomously fine-tune multiple locomotion skills in a range of environments, including an outdoor lawn and a variety of indoor terrains.

## 개요
보행 로봇은 다양한 도전적인 환경을 물리적으로 탐색할 수 있지만, 이러한 다양성을 처리할 수 있을 만큼 강건한 제어기를 설계하는 것은 로봇 공학에서 오랜 과제였습니다. 강화 학습은 제어기 설계 과정을 자동화하는 매력적인 접근 방식을 제공하며, 적절한 환경 범위에서 훈련될 때 놀라울 정도로 강건한 제어기를 생성할 수 있습니다. 그러나 배포 중 로봇이 직면할 모든 가능한 조건을 예측하고 훈련 시점에 열거하는 것은 어렵습니다. 모든 상황을 처리할 수 있을 만큼 강건한 제어기를 훈련하는 대신, 로봇이 처한 모든 환경에서 지속적으로 학습할 수 있도록 하면 어떨까요? 이러한 종류의 실제 환경 강화 학습은 효율성, 안전성 및 자율성을 포함한 여러 과제를 제기합니다. 이러한 과제를 해결하기 위해, 우리는 실제 환경에서 보행 정책을 미세 조정하기 위한 실용적인 로봇 강화 학습 시스템을 제안합니다. 적당한 양의 실제 환경 훈련이 배포 중 성능을 크게 향상시킬 수 있음을 보여주며, 이를 통해 실제 A1 사족 보행 로봇이 야외 잔디밭과 다양한 실내 지형을 포함한 여러 환경에서 여러 보행 기술을 자율적으로 미세 조정할 수 있습니다.

## 핵심 내용
보행 로봇은 다양한 도전적인 환경을 물리적으로 탐색할 수 있지만, 이러한 다양성을 처리할 수 있을 만큼 강건한 제어기를 설계하는 것은 로봇 공학에서 오랜 과제였습니다. 강화 학습은 제어기 설계 과정을 자동화하는 매력적인 접근 방식을 제공하며, 적절한 환경 범위에서 훈련될 때 놀라울 정도로 강건한 제어기를 생성할 수 있습니다. 그러나 배포 중 로봇이 직면할 모든 가능한 조건을 예측하고 훈련 시점에 열거하는 것은 어렵습니다. 모든 상황을 처리할 수 있을 만큼 강건한 제어기를 훈련하는 대신, 로봇이 처한 모든 환경에서 지속적으로 학습할 수 있도록 하면 어떨까요? 이러한 종류의 실제 환경 강화 학습은 효율성, 안전성 및 자율성을 포함한 여러 과제를 제기합니다. 이러한 과제를 해결하기 위해, 우리는 실제 환경에서 보행 정책을 미세 조정하기 위한 실용적인 로봇 강화 학습 시스템을 제안합니다. 적당한 양의 실제 환경 훈련이 배포 중 성능을 크게 향상시킬 수 있음을 보여주며, 이를 통해 실제 A1 사족 보행 로봇이 야외 잔디밭과 다양한 실내 지형을 포함한 여러 환경에서 여러 보행 기술을 자율적으로 미세 조정할 수 있습니다.
