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
  zh: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.09450v2.
sources:
- id: src_001
  type: paper
  title: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2302.09450
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 核心内容
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 参考
- http://arxiv.org/abs/2302.09450v2

## Overview
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## Content
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 개요
본 연구는 토크 제어 방식의 이족 보행 로봇이 실제 환경에서 강건하고 다양한 동적 점프를 수행할 수 있도록 함으로써 이족 보행 로봇의 민첩성 한계를 확장하는 것을 목표로 합니다. 우리는 로봇이 다양한 위치와 방향으로 점프하는 등 다양한 점프 작업을 수행할 수 있도록 훈련하는 강화 학습 프레임워크를 제시합니다. 이러한 도전적인 작업에서 성능을 향상시키기 위해, 로봇의 장기 입출력(I/O) 이력을 인코딩하면서도 단기 입출력(I/O) 이력에 직접 접근할 수 있는 새로운 정책 구조를 개발합니다. 다양한 점프 정책을 훈련하기 위해, 서로 다른 목표에 대해 다양한 훈련 단계를 포함하는 다단계 훈련 방식을 활용합니다. 다단계 훈련 후, 정책은 실제 이족 보행 로봇 Cassie에 직접 전이될 수 있습니다. 다양한 작업에 대한 훈련과 더 다양한 시나리오 탐색은 실제 환경 배치 중 교란 또는 불량 착지로부터 회복하기 위해 학습된 다양한 기동을 활용할 수 있는 매우 강건한 정책을 이끌어냅니다. 제안된 정책의 이러한 강건성 덕분에 Cassie는 제자리 멀리뛰기, 높은 플랫폼으로 점프, 다축 점프와 같은 실제 세계의 다양한 도전적인 점프 작업을 성공적으로 완료할 수 있습니다.

## 핵심 내용
본 연구는 토크 제어 방식의 이족 보행 로봇이 실제 환경에서 강건하고 다양한 동적 점프를 수행할 수 있도록 함으로써 이족 보행 로봇의 민첩성 한계를 확장하는 것을 목표로 합니다. 우리는 로봇이 다양한 위치와 방향으로 점프하는 등 다양한 점프 작업을 수행할 수 있도록 훈련하는 강화 학습 프레임워크를 제시합니다. 이러한 도전적인 작업에서 성능을 향상시키기 위해, 로봇의 장기 입출력(I/O) 이력을 인코딩하면서도 단기 입출력(I/O) 이력에 직접 접근할 수 있는 새로운 정책 구조를 개발합니다. 다양한 점프 정책을 훈련하기 위해, 서로 다른 목표에 대해 다양한 훈련 단계를 포함하는 다단계 훈련 방식을 활용합니다. 다단계 훈련 후, 정책은 실제 이족 보행 로봇 Cassie에 직접 전이될 수 있습니다. 다양한 작업에 대한 훈련과 더 다양한 시나리오 탐색은 실제 환경 배치 중 교란 또는 불량 착지로부터 회복하기 위해 학습된 다양한 기동을 활용할 수 있는 매우 강건한 정책을 이끌어냅니다. 제안된 정책의 이러한 강건성 덕분에 Cassie는 제자리 멀리뛰기, 높은 플랫폼으로 점프, 다축 점프와 같은 실제 세계의 다양한 도전적인 점프 작업을 성공적으로 완료할 수 있습니다.
