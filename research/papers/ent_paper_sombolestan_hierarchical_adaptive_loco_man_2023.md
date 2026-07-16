---
$id: ent_paper_sombolestan_hierarchical_adaptive_loco_man_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  zh: 面向四足机器人的分层自适应移动操作控制
  ko: 사족 로봇을 위한 계층적 적응형 이동-조작 제어
summary:
  en: Proposes a hierarchical adaptive control framework that enables quadruped robots to perform loco-manipulation without
    assuming object mass, terrain friction, or slope, and experimentally validates it on a Unitree A1 robot manipulating unknown
    time-varying loads up to 7 kg.
  zh: 提出一种分层自适应控制框架，使四足机器人无需已知物体质量、地形摩擦或坡度即可完成移动操作任务，并在Unitree A1机器人上通过操纵未知时变负载达7 kg进行了实验验证。
  ko: 사족 로봇이 물체 질량, 지형 마찰 또는 경사를 사전에 알 필요 없이 이동-조작 작업을 수행할 수 있게 하는 계층적 적응형 제어 프레임워크를 제안하고, Unitree A1 로봇에서 최대 7 kg의 미지 시변
    하중을 조작하여 실험적으로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- loco_manipulation
- adaptive_control
- model_predictive_control
- quadruped_robot
- unitree_a1
- force_control
- whole_body_control
- unknown_object_manipulation
- terrain_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.13145v2.
sources:
- id: src_001
  type: paper
  title: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  url: https://arxiv.org/abs/2209.13145
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Legged robots have shown remarkable advantages in navigating uneven terrain. However, realizing effective locomotion and manipulation tasks on quadruped robots is still challenging. In addition, object and terrain parameters are generally unknown to the robot in these problems. Therefore, this paper proposes a hierarchical adaptive control framework that enables legged robots to perform loco-manipulation tasks without any given assumption on the object's mass, the friction coefficient, or the slope of the terrain. In our approach, we first present an adaptive manipulation control to regulate the contact force to manipulate an unknown object on unknown terrain. We then introduce a unified model predictive control (MPC) for loco-manipulation that takes into account the manipulation force in our robot dynamics. The proposed MPC framework thus can effectively regulate the interaction force between the robot and the object while keeping the robot balance. Experimental validation of our proposed approach is successfully conducted on a Unitree A1 robot, allowing it to manipulate an unknown time-varying load up to $7$ $kg$ ($60\%$ of the robot's weight). Moreover, our framework enables fast adaptation to unknown slopes (up to $20^\circ$) or different surfaces with different friction coefficients.

## 核心内容
Legged robots have shown remarkable advantages in navigating uneven terrain. However, realizing effective locomotion and manipulation tasks on quadruped robots is still challenging. In addition, object and terrain parameters are generally unknown to the robot in these problems. Therefore, this paper proposes a hierarchical adaptive control framework that enables legged robots to perform loco-manipulation tasks without any given assumption on the object's mass, the friction coefficient, or the slope of the terrain. In our approach, we first present an adaptive manipulation control to regulate the contact force to manipulate an unknown object on unknown terrain. We then introduce a unified model predictive control (MPC) for loco-manipulation that takes into account the manipulation force in our robot dynamics. The proposed MPC framework thus can effectively regulate the interaction force between the robot and the object while keeping the robot balance. Experimental validation of our proposed approach is successfully conducted on a Unitree A1 robot, allowing it to manipulate an unknown time-varying load up to $7$ $kg$ ($60\%$ of the robot's weight). Moreover, our framework enables fast adaptation to unknown slopes (up to $20^\circ$) or different surfaces with different friction coefficients.

## 参考
- http://arxiv.org/abs/2209.13145v2

## Overview
Legged robots have shown remarkable advantages in navigating uneven terrain. However, realizing effective locomotion and manipulation tasks on quadruped robots is still challenging. In addition, object and terrain parameters are generally unknown to the robot in these problems. Therefore, this paper proposes a hierarchical adaptive control framework that enables legged robots to perform loco-manipulation tasks without any given assumption on the object's mass, the friction coefficient, or the slope of the terrain. In our approach, we first present an adaptive manipulation control to regulate the contact force to manipulate an unknown object on unknown terrain. We then introduce a unified model predictive control (MPC) for loco-manipulation that takes into account the manipulation force in our robot dynamics. The proposed MPC framework thus can effectively regulate the interaction force between the robot and the object while keeping the robot balance. Experimental validation of our proposed approach is successfully conducted on a Unitree A1 robot, allowing it to manipulate an unknown time-varying load up to $7$ $kg$ ($60\%$ of the robot's weight). Moreover, our framework enables fast adaptation to unknown slopes (up to $20^\circ$) or different surfaces with different friction coefficients.

## Content
Legged robots have shown remarkable advantages in navigating uneven terrain. However, realizing effective locomotion and manipulation tasks on quadruped robots is still challenging. In addition, object and terrain parameters are generally unknown to the robot in these problems. Therefore, this paper proposes a hierarchical adaptive control framework that enables legged robots to perform loco-manipulation tasks without any given assumption on the object's mass, the friction coefficient, or the slope of the terrain. In our approach, we first present an adaptive manipulation control to regulate the contact force to manipulate an unknown object on unknown terrain. We then introduce a unified model predictive control (MPC) for loco-manipulation that takes into account the manipulation force in our robot dynamics. The proposed MPC framework thus can effectively regulate the interaction force between the robot and the object while keeping the robot balance. Experimental validation of our proposed approach is successfully conducted on a Unitree A1 robot, allowing it to manipulate an unknown time-varying load up to $7$ $kg$ ($60\%$ of the robot's weight). Moreover, our framework enables fast adaptation to unknown slopes (up to $20^\circ$) or different surfaces with different friction coefficients.

## 개요
보행 로봇은 불균일한 지형을 탐색하는 데 뛰어난 장점을 보여주었습니다. 그러나 사족 보행 로봇에서 효과적인 이동 및 조작 작업을 실현하는 것은 여전히 어려운 과제입니다. 또한, 이러한 문제에서 물체와 지형의 매개변수는 일반적으로 로봇에 알려져 있지 않습니다. 따라서 본 논문은 물체의 질량, 마찰 계수 또는 지형의 경사에 대한 어떠한 가정도 없이 보행 로봇이 이동-조작 작업을 수행할 수 있도록 하는 계층적 적응 제어 프레임워크를 제안합니다. 우리의 접근 방식에서는 먼저 알려지지 않은 지형에서 알려지지 않은 물체를 조작하기 위해 접촉력을 조절하는 적응형 조작 제어를 제시합니다. 그런 다음 로봇 동역학에서 조작력을 고려한 이동-조작을 위한 통합 모델 예측 제어(MPC)를 도입합니다. 제안된 MPC 프레임워크는 로봇의 균형을 유지하면서 로봇과 물체 간의 상호 작용력을 효과적으로 조절할 수 있습니다. 제안된 접근 방식의 실험적 검증은 Unitree A1 로봇에서 성공적으로 수행되었으며, 로봇이 최대 $7$ $kg$(로봇 무게의 $60\%$)의 알려지지 않은 시변 하중을 조작할 수 있음을 보여주었습니다. 또한, 우리의 프레임워크는 알려지지 않은 경사(최대 $20^\circ$) 또는 서로 다른 마찰 계수를 가진 다양한 표면에 빠르게 적응할 수 있게 합니다.

## 핵심 내용
보행 로봇은 불균일한 지형을 탐색하는 데 뛰어난 장점을 보여주었습니다. 그러나 사족 보행 로봇에서 효과적인 이동 및 조작 작업을 실현하는 것은 여전히 어려운 과제입니다. 또한, 이러한 문제에서 물체와 지형의 매개변수는 일반적으로 로봇에 알려져 있지 않습니다. 따라서 본 논문은 물체의 질량, 마찰 계수 또는 지형의 경사에 대한 어떠한 가정도 없이 보행 로봇이 이동-조작 작업을 수행할 수 있도록 하는 계층적 적응 제어 프레임워크를 제안합니다. 우리의 접근 방식에서는 먼저 알려지지 않은 지형에서 알려지지 않은 물체를 조작하기 위해 접촉력을 조절하는 적응형 조작 제어를 제시합니다. 그런 다음 로봇 동역학에서 조작력을 고려한 이동-조작을 위한 통합 모델 예측 제어(MPC)를 도입합니다. 제안된 MPC 프레임워크는 로봇의 균형을 유지하면서 로봇과 물체 간의 상호 작용력을 효과적으로 조절할 수 있습니다. 제안된 접근 방식의 실험적 검증은 Unitree A1 로봇에서 성공적으로 수행되었으며, 로봇이 최대 $7$ $kg$(로봇 무게의 $60\%$)의 알려지지 않은 시변 하중을 조작할 수 있음을 보여주었습니다. 또한, 우리의 프레임워크는 알려지지 않은 경사(최대 $20^\circ$) 또는 서로 다른 마찰 계수를 가진 다양한 표면에 빠르게 적응할 수 있게 합니다.
