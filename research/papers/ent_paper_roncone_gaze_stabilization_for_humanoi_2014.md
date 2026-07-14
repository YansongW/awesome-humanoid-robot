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
  en: This paper proposes a gaze stabilization framework for humanoid robots that combines a kinematic feedforward term derived
    from joint velocity commands with an inertial feedback term from a head-mounted gyroscope to compensate for camera disturbances
    caused by self-generated motion and external perturbations, validated on the iCub robot using residual optical flow.
  zh: 本文提出了一种人形机器人凝视稳定框架，该框架将关节速度指令得到的运动学前馈项与头部陀螺仪的惯性反馈项相结合，以补偿自运动和外部扰动引起的相机扰动，并在 iCub 机器人上通过残余光流进行了验证。
  ko: 본 논문은 관절 속도 명령에서 도출된 운동학적 피드포워드 항과 머리에 장착된 자이로스코프의 관성 피드백 항을 결합하여 자기 발생 움직임과 외부 섭동으로 인한 카메라 섭동을 보상하는 휴머노이드 로봇 시선 안정화
    프레임워크를 제안하고, iCub 로봇에서 잔여 광학 흐름으로 검증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1411.3525v1.
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
## 概述
Gaze stabilization is an important requisite for humanoid robots. Previous work on this topic has focused on the integration of inertial and visual information. Little attention has been given to a third component, which is the knowledge that the robot has about its own movement. In this work we propose a comprehensive framework for gaze stabilization in a humanoid robot. We focus on the problem of compensating for disturbances induced in the cameras due to self-generated movements of the robot. In this work we employ two separate signals for stabilization: (1) an anticipatory term obtained from the velocity commands sent to the joints while the robot moves autonomously; (2) a feedback term from the on board gyroscope, which compensates unpredicted external disturbances. We first provide the mathematical formulation to derive the forward and the differential kinematics of the fixation point of the stereo system. We finally test our method on the iCub robot. We show that the stabilization consistently reduces the residual optical flow during the movement of the robot and in presence of external disturbances. We also demonstrate that proper integration of the neck DoF is crucial to achieve correct stabilization.

## 核心内容
Gaze stabilization is an important requisite for humanoid robots. Previous work on this topic has focused on the integration of inertial and visual information. Little attention has been given to a third component, which is the knowledge that the robot has about its own movement. In this work we propose a comprehensive framework for gaze stabilization in a humanoid robot. We focus on the problem of compensating for disturbances induced in the cameras due to self-generated movements of the robot. In this work we employ two separate signals for stabilization: (1) an anticipatory term obtained from the velocity commands sent to the joints while the robot moves autonomously; (2) a feedback term from the on board gyroscope, which compensates unpredicted external disturbances. We first provide the mathematical formulation to derive the forward and the differential kinematics of the fixation point of the stereo system. We finally test our method on the iCub robot. We show that the stabilization consistently reduces the residual optical flow during the movement of the robot and in presence of external disturbances. We also demonstrate that proper integration of the neck DoF is crucial to achieve correct stabilization.

## 参考
- http://arxiv.org/abs/1411.3525v1

