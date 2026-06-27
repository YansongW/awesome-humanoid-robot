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
  en: Proposes a shear-based grasp controller for the Pisa/IIT SoftHand using five
    fingertip microTac optical tactile sensors; contact pose and shear/normal force
    are predicted via supervised deep learning with transfer learning, enabling real-time
    multi-finger grasp adjustments during delicate-object manipulation.
  zh: 提出一种用于Pisa/IIT SoftHand的基于剪切力的抓取控制器，该手五指配备microTac光学触觉传感器；通过监督式深度学习和迁移学习预测接触位姿及剪切/法向力，从而在易碎物体操作中实现实时多指抓取调整。
  ko: Pisa/IIT SoftHand의 다섯 손끝에 장착된 microTac 광학 촉각 센서를 이용한 전단력 기반 파지 제어기를 제안하며, 지도
    학습과 전이 학습으로 접촉 자세 및 전단/법선력을 예측하여 섬세한 물체 조작 중 실시간 다지점 파지 조정을 가능하게 한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the paper metadata and abstract; hardware details and exact
    section citations require human review against the full arXiv text.
sources:
- id: src_001
  type: paper
  title: Shear-based Grasp Control for Multi-fingered Underactuated Tactile Robotic
    Hands
  url: https://arxiv.org/abs/2503.17501
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## Overview

This paper addresses force-sensitive grasping and manipulation with highly underactuated robotic hands, which typically lack accurate proprioception and shear information. The authors equip a single-actuated Pisa/IIT anthropomorphic SoftHand with soft biomimetic tactile sensors—miniaturized TacTip variants called microTac—on all five fingertips. These sensors capture tactile images that are processed to estimate 3D contact pose together with shear and normal contact forces.

A parallel processing pipeline asynchronously captures images from the five fingertips and predicts contact pose and force using supervised deep-learning models. Transfer learning is used to develop consistent pose and force models across all sensors. The resulting grasp-control framework modulates grasp force based on feedback from all fingertip sensors simultaneously, allowing the hand to maintain a pre-slip state and to react safely under external disturbances.

The approach is evaluated on three grasp-manipulation tasks: holding a flexible cup without crushing it while its weight changes, pouring rice so that the cup’s center of mass shifts dynamically, and a tactile-driven leader-follower task in which a human guides the held object. The experiments demonstrate more human-like dexterity for an underactuated hand by exploiting fast, reflexive tactile feedback.

## Key Contributions

- Novel shear-based grasp controller that maintains a pre-slip state by balancing normal and shear contact forces on a single-actuated SoftHand.
- Custom fingertip-sized microTac optical tactile sensors integrated on all five fingers of an anthropomorphic hand.
- Parallel Jetson Nano computing architecture for real-time multi-sensor tactile image capture and inference.
- Multi-tactile-sensor deep-learning models for pose and shear/normal force, improved via transfer learning across sensors.

## Relevance to Humanoid Robotics

Underactuated anthropomorphic hands are attractive for mass-produced humanoids because they reduce cost and mechanical complexity, but safe, dexterous manipulation requires reliable tactile feedback. This work shows how vision-based fingertip tactile sensing and shear-aware control can compensate for the lack of joint-level proprioception, enabling robust grasp regulation in unstructured or disturbance-prone settings. The low-complexity, tactile-driven control approach is directly relevant to humanoid robots that must handle delicate objects and interact safely with humans in industrial and service environments.
