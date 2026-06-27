---
$id: ent_paper_roncone_gaze_stabilization_for_humanoi_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gaze Stabilization for Humanoid Robots: a Comprehensive Framework'
  zh: 人形机器人凝视稳定：一个综合框架
  ko: '휴머노이드 로봇을 위한 시선 안정화: 통합 프레임워크'
summary:
  en: This paper proposes a gaze stabilization framework for humanoid robots that
    combines a kinematic feedforward term derived from joint velocity commands with
    an inertial feedback term from a head-mounted gyroscope to compensate for camera
    disturbances caused by self-generated motion and external perturbations, validated
    on the iCub robot using residual optical flow.
  zh: 本文提出了一种人形机器人凝视稳定框架，该框架将关节速度指令得到的运动学前馈项与头部陀螺仪的惯性反馈项相结合，以补偿自运动和外部扰动引起的相机扰动，并在
    iCub 机器人上通过残余光流进行了验证。
  ko: 본 논문은 관절 속도 명령에서 도출된 운동학적 피드포워드 항과 머리에 장착된 자이로스코프의 관성 피드백 항을 결합하여 자기 발생 움직임과
    외부 섭동으로 인한 카메라 섭동을 보상하는 휴머노이드 로봇 시선 안정화 프레임워크를 제안하고, iCub 로봇에서 잔여 광학 흐름으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- gaze_stabilization
- visual_servoing
- oculomotor_control
- icub
- feedforward_control
- inertial_feedback
- stereo_vision
- neck_dof
- optical_flow
- humanoid_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the full arXiv text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Gaze Stabilization for Humanoid Robots: a Comprehensive Framework'
  url: https://arxiv.org/abs/1411.3525
  date: '2014'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Gaze stabilization is essential for humanoid robots because body motion during locomotion or whole-body tasks blurs the visual input and disrupts fixation. Most prior work combined inertial and visual cues; this paper argues that a third source—the robot's knowledge of its own commanded movement—has been largely overlooked. The authors therefore present a framework that fuses a kinematic feedforward (kFF) signal, computed from the velocity commands sent to the torso, neck, and eye joints, with an inertial feedback (iFB) signal from a head-mounted gyroscope.

The stabilization problem is formulated as keeping the 6-D velocity of the stereo fixation point equal to zero. The authors derive the forward and differential kinematics of the fixation point for the iCub head, map feedforward joint velocities and gyroscope angular rates into fixation-point motion, and use the pseudo-inverse of the neck-eye Jacobian to compute compensatory joint velocities. The controller deliberately decouples the task: the neck compensates rotational disturbances while the eyes compensate translational ones, exploiting their different dynamics and mechanical limits. Experiments on the iCub compare baseline (no compensation), kFF, and iFB conditions using dense optical flow as an independent performance measure.

## Key Contributions

- Integration of motor-command feedforward with inertial feedback for gaze stabilization in humanoid robots.
- Mathematical formulation of the forward and differential kinematics of the fixation point for a stereo camera system.
- Experimental demonstration that proper use of the neck degrees of freedom is crucial for effective stabilization.
- Validation on the iCub humanoid robot showing consistent reduction of residual optical flow during self-generated motion and external disturbances.

## Relevance to Humanoid Robotics

Gaze stabilization is a core perceptual-motor capability for deployed humanoid robots: it preserves image clarity during locomotion and whole-body motion, which is a prerequisite for reliable vision-based interaction, navigation, and manipulation. By exploiting the robot's own motor commands as an anticipatory feedforward term, the framework is directly aligned with the needs of autonomous humanoids that generate their own disturbances through walking and active body motion. The emphasis on integrating neck degrees of freedom also highlights the importance of head design and control in humanoid sensorimotor systems.
