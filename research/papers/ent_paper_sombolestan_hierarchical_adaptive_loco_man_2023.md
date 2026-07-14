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

