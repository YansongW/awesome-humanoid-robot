---
$id: ent_paper_darvish_whole_body_geometric_retargeti_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Geometric Retargeting for Humanoid Robots
  zh: 面向人形机器人的全身几何重定向
  ko: 휴머노이드 로봇을 위한 전신 기하학적 리타기팅
summary:
  en: A framework for scalable whole-body teleoperation of humanoid robots that maps
    measured human link orientations and angular velocities to corresponding robot
    links via constant relative rotations, then solves inverse kinematics directly
    on the robot URDF model using a dynamical optimization QP formulation.
  zh: 一种可扩展的人形机器人全身遥操作框架，通过恒定相对旋转将测量的人体连杆朝向和角速度映射到对应机器人连杆，并利用动态优化二次规划在机器人URDF模型上直接求解逆运动学。
  ko: 측정된 인간 링크 방향과 각속도를 일정한 상대 회전을 통해 대응 로봇 링크에 매핑하고, 동적 최적화 QP 공식을 사용해 로봇 URDF 모델에서
    직접 역기구학을 풀어 휴머노이드 로봇의 확장 가능한 전신 텔레오퍼레이션을 위한 프레임워크.
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
- teleoperation
- motion_retargeting
- whole_body_control
- inverse_kinematics
- humanoid_robot
- geometric_retargeting
- urdf
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; the full arXiv text
    was not independently consulted. Requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Whole-Body Geometric Retargeting for Humanoid Robots
  url: https://arxiv.org/abs/1909.10080
  date: '2019'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

This paper presents a geometric whole-body retargeting framework for teleoperating humanoid robots. The approach maps measured human link orientations and angular velocities to corresponding robot links through constant relative rotations, and then solves inverse kinematics directly on the robot's URDF model using a dynamical optimization quadratic-programming formulation. By operating on the robot model rather than on a custom human model, the method is intended to generalize across different human body dimensions and different robot kinematics with minimal system changes.

The retargeting pipeline is combined with two state-of-the-art whole-body controllers: a momentum-based balancing controller and a divergent-component-of-motion (DCM)-based walking controller. Experiments are reported using multiple robot models (iCub, NAO, Atlas, Baxter) and multiple human subjects. The hardware interface includes an Xsens MVN full-body motion-capture suit, a Cyberith Virtualizer VR treadmill, an Oculus headset, and joypads.

## Key Contributions

- Scalable retargeting using only the robot URDF model and human link orientation/velocity measurements, avoiding per-user human models.
- Real-time anthropomorphic retargeting that works across different robot kinematics and human body dimensions.
- Validation on multiple robot models (iCub, NAO, Atlas, Baxter) and multiple human subjects.
- Integration and experimental validation with two whole-body controllers: a momentum-based balancing controller and a DCM-based walking controller.

## Relevance to Humanoid Robotics

The work directly addresses a core enabling technology for humanoid robots: intuitive, scalable whole-body teleoperation and motion retargeting. By allowing a single operator interface to drive diverse humanoid platforms without re-building a custom human model, it lowers the barrier to deploying humanoids in real-world demonstration and manipulation scenarios. The combination with balancing and walking controllers also links perception-level retargeting to whole-body control, which is central to practical humanoid operation.
