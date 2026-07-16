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

## Overview
This paper presents a shear-based control scheme for grasping and manipulating delicate objects with a Pisa/IIT anthropomorphic SoftHand equipped with soft biomimetic tactile sensors on all five fingertips. These `microTac' tactile sensors are miniature versions of the TacTip vision-based tactile sensor, and can extract precise contact geometry and force information at each fingertip for use as feedback into a controller to modulate the grasp while a held object is manipulated. Using a parallel processing pipeline, we asynchronously capture tactile images and predict contact pose and force from multiple tactile sensors. Consistent pose and force models across all sensors are developed using supervised deep learning with transfer learning techniques. We then develop a grasp control framework that uses contact force feedback from all fingertip sensors simultaneously, allowing the hand to safely handle delicate objects even under external disturbances. This control framework is applied to several grasp-manipulation experiments: first, retaining a flexible cup in a grasp without crushing it under changes in object weight; second, a pouring task where the center of mass of the cup changes dynamically; and third, a tactile-driven leader-follower task where a human guides a held object. These manipulation tasks demonstrate more human-like dexterity with underactuated robotic hands by using fast reflexive control from tactile sensing.

## Content
This paper presents a shear-based control scheme for grasping and manipulating delicate objects with a Pisa/IIT anthropomorphic SoftHand equipped with soft biomimetic tactile sensors on all five fingertips. These `microTac' tactile sensors are miniature versions of the TacTip vision-based tactile sensor, and can extract precise contact geometry and force information at each fingertip for use as feedback into a controller to modulate the grasp while a held object is manipulated. Using a parallel processing pipeline, we asynchronously capture tactile images and predict contact pose and force from multiple tactile sensors. Consistent pose and force models across all sensors are developed using supervised deep learning with transfer learning techniques. We then develop a grasp control framework that uses contact force feedback from all fingertip sensors simultaneously, allowing the hand to safely handle delicate objects even under external disturbances. This control framework is applied to several grasp-manipulation experiments: first, retaining a flexible cup in a grasp without crushing it under changes in object weight; second, a pouring task where the center of mass of the cup changes dynamically; and third, a tactile-driven leader-follower task where a human guides a held object. These manipulation tasks demonstrate more human-like dexterity with underactuated robotic hands by using fast reflexive control from tactile sensing.

## 개요
본 논문은 다섯 개의 손가락 끝에 생체 모방 촉각 센서를 장착한 Pisa/IIT 인체공학적 SoftHand를 사용하여 섬세한 물체를 파지하고 조작하기 위한 전단 기반 제어 방식을 제시합니다. 이 `microTac` 촉각 센서는 TacTip 시각 기반 촉각 센서의 소형 버전으로, 각 손가락 끝에서 정밀한 접촉 형상과 힘 정보를 추출하여 물체를 조작하는 동안 파지를 조절하는 제어기의 피드백으로 사용할 수 있습니다. 병렬 처리 파이프라인을 사용하여 비동기적으로 촉각 이미지를 캡처하고 여러 촉각 센서로부터 접촉 자세와 힘을 예측합니다. 전이 학습 기법을 활용한 지도 딥러닝을 통해 모든 센서에서 일관된 자세 및 힘 모델을 개발합니다. 그런 다음 모든 손가락 끝 센서의 접촉 힘 피드백을 동시에 사용하는 파지 제어 프레임워크를 개발하여, 외부 교란에도 손이 섬세한 물체를 안전하게 다룰 수 있도록 합니다. 이 제어 프레임워크는 여러 파지-조작 실험에 적용됩니다: 첫째, 물체 무게 변화에도 유연한 컵을 으스러뜨리지 않고 파지 유지; 둘째, 컵의 질량 중심이 동적으로 변하는 따르기 작업; 셋째, 사람이 잡은 물체를 안내하는 촉각 기반 리더-팔로워 작업. 이러한 조작 작업은 촉각 감지의 빠른 반사 제어를 통해 저구동 로봇 손으로 더 인간다운 손재주를 보여줍니다.

## 핵심 내용
본 논문은 다섯 개의 손가락 끝에 생체 모방 촉각 센서를 장착한 Pisa/IIT 인체공학적 SoftHand를 사용하여 섬세한 물체를 파지하고 조작하기 위한 전단 기반 제어 방식을 제시합니다. 이 `microTac` 촉각 센서는 TacTip 시각 기반 촉각 센서의 소형 버전으로, 각 손가락 끝에서 정밀한 접촉 형상과 힘 정보를 추출하여 물체를 조작하는 동안 파지를 조절하는 제어기의 피드백으로 사용할 수 있습니다. 병렬 처리 파이프라인을 사용하여 비동기적으로 촉각 이미지를 캡처하고 여러 촉각 센서로부터 접촉 자세와 힘을 예측합니다. 전이 학습 기법을 활용한 지도 딥러닝을 통해 모든 센서에서 일관된 자세 및 힘 모델을 개발합니다. 그런 다음 모든 손가락 끝 센서의 접촉 힘 피드백을 동시에 사용하는 파지 제어 프레임워크를 개발하여, 외부 교란에도 손이 섬세한 물체를 안전하게 다룰 수 있도록 합니다. 이 제어 프레임워크는 여러 파지-조작 실험에 적용됩니다: 첫째, 물체 무게 변화에도 유연한 컵을 으스러뜨리지 않고 파지 유지; 둘째, 컵의 질량 중심이 동적으로 변하는 따르기 작업; 셋째, 사람이 잡은 물체를 안내하는 촉각 기반 리더-팔로워 작업. 이러한 조작 작업은 촉각 감지의 빠른 반사 제어를 통해 저구동 로봇 손으로 더 인간다운 손재주를 보여줍니다.
