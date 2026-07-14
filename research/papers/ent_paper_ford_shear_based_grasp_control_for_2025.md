---
$id: ent_paper_ford_shear_based_grasp_control_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shear-based Grasp Control for Multi-fingered Underactuated Tactile Robotic Hands
  zh: 基于剪切力的多指欠驱动触觉机器人手抓取控制
  ko: 다지점 저작동 촉각 로봇 손을 위한 전단력 기반 파지 제어
summary:
  en: Proposes a shear-based grasp controller for the Pisa/IIT SoftHand using five fingertip microTac optical tactile sensors;
    contact pose and shear/normal force are predicted via supervised deep learning with transfer learning, enabling real-time
    multi-finger grasp adjustments during delicate-object manipulation.
  zh: 提出一种用于Pisa/IIT SoftHand的基于剪切力的抓取控制器，该手五指配备microTac光学触觉传感器；通过监督式深度学习和迁移学习预测接触位姿及剪切/法向力，从而在易碎物体操作中实现实时多指抓取调整。
  ko: Pisa/IIT SoftHand의 다섯 손끝에 장착된 microTac 광학 촉각 센서를 이용한 전단력 기반 파지 제어기를 제안하며, 지도 학습과 전이 학습으로 접촉 자세 및 전단/법선력을 예측하여 섬세한 물체
    조작 중 실시간 다지점 파지 조정을 가능하게 한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- tactile_sensing
- grasp_control
- underactuated_hand
- soft_robotics
- optical_tactile_sensor
- shear_force
- deep_learning
- transfer_learning
- multi_fingered_hand
- pisa_iit_softhand
- microtac
- dexterous_manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.17501v1.
sources:
- id: src_001
  type: paper
  title: Shear-based Grasp Control for Multi-fingered Underactuated Tactile Robotic Hands
  url: https://arxiv.org/abs/2503.17501
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
This paper presents a shear-based control scheme for grasping and manipulating delicate objects with a Pisa/IIT anthropomorphic SoftHand equipped with soft biomimetic tactile sensors on all five fingertips. These `microTac' tactile sensors are miniature versions of the TacTip vision-based tactile sensor, and can extract precise contact geometry and force information at each fingertip for use as feedback into a controller to modulate the grasp while a held object is manipulated. Using a parallel processing pipeline, we asynchronously capture tactile images and predict contact pose and force from multiple tactile sensors. Consistent pose and force models across all sensors are developed using supervised deep learning with transfer learning techniques. We then develop a grasp control framework that uses contact force feedback from all fingertip sensors simultaneously, allowing the hand to safely handle delicate objects even under external disturbances. This control framework is applied to several grasp-manipulation experiments: first, retaining a flexible cup in a grasp without crushing it under changes in object weight; second, a pouring task where the center of mass of the cup changes dynamically; and third, a tactile-driven leader-follower task where a human guides a held object. These manipulation tasks demonstrate more human-like dexterity with underactuated robotic hands by using fast reflexive control from tactile sensing.

## 核心内容
This paper presents a shear-based control scheme for grasping and manipulating delicate objects with a Pisa/IIT anthropomorphic SoftHand equipped with soft biomimetic tactile sensors on all five fingertips. These `microTac' tactile sensors are miniature versions of the TacTip vision-based tactile sensor, and can extract precise contact geometry and force information at each fingertip for use as feedback into a controller to modulate the grasp while a held object is manipulated. Using a parallel processing pipeline, we asynchronously capture tactile images and predict contact pose and force from multiple tactile sensors. Consistent pose and force models across all sensors are developed using supervised deep learning with transfer learning techniques. We then develop a grasp control framework that uses contact force feedback from all fingertip sensors simultaneously, allowing the hand to safely handle delicate objects even under external disturbances. This control framework is applied to several grasp-manipulation experiments: first, retaining a flexible cup in a grasp without crushing it under changes in object weight; second, a pouring task where the center of mass of the cup changes dynamically; and third, a tactile-driven leader-follower task where a human guides a held object. These manipulation tasks demonstrate more human-like dexterity with underactuated robotic hands by using fast reflexive control from tactile sensing.

## 参考
- http://arxiv.org/abs/2503.17501v1

