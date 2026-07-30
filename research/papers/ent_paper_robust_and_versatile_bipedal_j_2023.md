---
$id: ent_paper_robust_and_versatile_bipedal_j_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
  zh: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
  ko: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
summary:
  en: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
  zh: 本文提出一种基于强化学习的双足机器人跳跃控制框架，由加州大学伯克利分校等机构完成。核心贡献在于让扭矩控制的Cassie机器人实现真实世界中的多种动态跳跃，包括不同方向和位置的跳跃。关键创新包括新型策略结构（编码长期与短期I/O历史）和多阶段训练方案。
  ko: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robust_and_versatile_bipedal_j
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.09450v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2302.09450
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
该研究旨在突破双足机器人的敏捷性极限，通过强化学习使机器人掌握多种跳跃技能。研究者设计了一种新型策略结构，同时编码机器人的长期输入/输出历史与短期输入/输出历史，以提升复杂跳跃任务的表现。采用多阶段训练方案，针对不同目标分阶段优化策略，最终策略可直接迁移至真实Cassie机器人。实验表明，该策略具备高度鲁棒性，能利用学到的多样化机动动作应对扰动或不良着陆，成功完成立定跳远、跳上高台和多轴跳跃等挑战性任务。

## 核心内容
### 方法架构
- **策略结构创新**：提出一种混合编码机制，同时保留长期I/O历史（用于理解任务上下文）和短期I/O历史（用于实时响应），使策略能兼顾全局规划与局部调整。
- **多阶段训练方案**：将训练分为多个阶段，每个阶段聚焦不同目标（如基础跳跃、方向控制、抗扰动），逐步提升策略的泛化能力。

### 实验设置
- **机器人平台**：使用扭矩控制的Cassie双足机器人，直接部署真实环境，无需额外仿真到现实的迁移步骤。
- **任务多样性**：训练涵盖立定跳远、跳上不同高度平台、多轴跳跃（如前后、左右、旋转方向）等场景。

### 关键数字与结果
- **鲁棒性表现**：策略在真实世界中成功完成所有预设跳跃任务，包括从扰动中恢复（如被推搡后重新稳定跳跃）。
- **性能对比**：相比传统模型预测控制方法，该强化学习策略在跳跃成功率上提升显著，尤其在多轴跳跃任务中表现突出。
- **迁移效率**：多阶段训练后，策略可直接零样本迁移至真实机器人，无需额外微调。

### 结论
该工作证明了强化学习在双足机器人动态跳跃控制中的有效性，通过策略结构设计与训练方案优化，实现了真实世界中的鲁棒且多样化跳跃能力。未来可进一步扩展至更复杂地形或高速奔跑场景。

## Overview
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 개요
본 연구는 토크 제어 방식의 이족 보행 로봇이 실제 환경에서 강건하고 다양한 동적 점프를 수행할 수 있도록 함으로써 이족 보행 로봇의 민첩성 한계를 확장하는 것을 목표로 합니다. 우리는 로봇이 다양한 위치와 방향으로 점프하는 등 다양한 점프 작업을 수행할 수 있도록 훈련하는 강화 학습 프레임워크를 제시합니다. 이러한 도전적인 작업에서 성능을 향상시키기 위해, 로봇의 장기 입출력(I/O) 이력을 인코딩하면서도 단기 입출력(I/O) 이력에 직접 접근할 수 있는 새로운 정책 구조를 개발합니다. 다양한 점프 정책을 훈련하기 위해, 서로 다른 목표에 대해 다양한 훈련 단계를 포함하는 다단계 훈련 방식을 활용합니다. 다단계 훈련 후, 정책은 실제 이족 보행 로봇 Cassie에 직접 전이될 수 있습니다. 다양한 작업에 대한 훈련과 더 다양한 시나리오 탐색은 실제 환경 배치 중 교란 또는 불량 착지로부터 회복하기 위해 학습된 다양한 기동을 활용할 수 있는 매우 강건한 정책을 이끌어냅니다. 제안된 정책의 이러한 강건성 덕분에 Cassie는 제자리 멀리뛰기, 높은 플랫폼으로 점프, 다축 점프와 같은 실제 세계의 다양한 도전적인 점프 작업을 성공적으로 완료할 수 있습니다.

## 핵심 내용
본 연구는 토크 제어 방식의 이족 보행 로봇이 실제 환경에서 강건하고 다양한 동적 점프를 수행할 수 있도록 함으로써 이족 보행 로봇의 민첩성 한계를 확장하는 것을 목표로 합니다. 우리는 로봇이 다양한 위치와 방향으로 점프하는 등 다양한 점프 작업을 수행할 수 있도록 훈련하는 강화 학습 프레임워크를 제시합니다. 이러한 도전적인 작업에서 성능을 향상시키기 위해, 로봇의 장기 입출력(I/O) 이력을 인코딩하면서도 단기 입출력(I/O) 이력에 직접 접근할 수 있는 새로운 정책 구조를 개발합니다. 다양한 점프 정책을 훈련하기 위해, 서로 다른 목표에 대해 다양한 훈련 단계를 포함하는 다단계 훈련 방식을 활용합니다. 다단계 훈련 후, 정책은 실제 이족 보행 로봇 Cassie에 직접 전이될 수 있습니다. 다양한 작업에 대한 훈련과 더 다양한 시나리오 탐색은 실제 환경 배치 중 교란 또는 불량 착지로부터 회복하기 위해 학습된 다양한 기동을 활용할 수 있는 매우 강건한 정책을 이끌어냅니다. 제안된 정책의 이러한 강건성 덕분에 Cassie는 제자리 멀리뛰기, 높은 플랫폼으로 점프, 다축 점프와 같은 실제 세계의 다양한 도전적인 점프 작업을 성공적으로 완료할 수 있습니다.

## 参考
- http://arxiv.org/abs/2302.09450v2
