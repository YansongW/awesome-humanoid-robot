---
$id: ent_paper_chen_enhanced_visual_feedback_with_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid
    Robot Teleoperation using SLAM
  zh: 基于SLAM的沉浸式人形机器人遥操作中解耦视角控制的增强视觉反馈
  ko: SLAM을 이용한 몰입형 휴머노이드 로봇 원격조작에서 분리된 시점 제어를 통한 향상된 시각 피드백
summary:
  en: This paper presents a decoupled viewpoint control system for immersive teleoperation
    of the HRP-4CR humanoid, fusing real-time point-cloud streaming from a ZED Mini
    camera with a SLAM-reconstructed mesh to mitigate visual feedback latency, camera
    field-of-view limits, and restricted robot neck motion.
  zh: 本文提出了一种用于HRP-4CR人形机器人沉浸式遥操作的解耦视角控制系统，将ZED Mini相机的实时点云流与SLAM重建网格融合，以缓解视觉反馈延迟、相机视场角限制以及机器人颈部运动范围受限的问题。
  ko: 본 논문은 HRP-4CR 휴머노이드 로봇의 몰입형 원격조작을 위한 분리된 시점 제어 시스템을 제안하며, ZED Mini 카메라의 실시간
    포인트 클라우드 스트리밍과 SLAM 재구성 메시를 융합하여 시각 피드백 지연, 카메라 시야각 제한, 그리고 로봇 목 운동 범위 제한을 완화한다.
domains:
- 08_software_middleware
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- immersive_teleoperation
- humanoid_teleoperation
- hrp4cr
- slam
- visual_feedback
- point_cloud
- decoupled_viewpoint_control
- virtual_reality
- visual_inertial_odometry
- human_robot_interface
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text verification
    is needed before confirming all component and method details.
sources:
- id: src_001
  type: paper
  title: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid
    Robot Teleoperation using SLAM
  url: https://arxiv.org/abs/2211.01749
  date: '2022'
  accessed_at: '2026-06-26'
---

## Overview

Immersive teleoperation of humanoid robots depends on fast, consistent visual feedback that aligns the operator's head motion with the robot's head camera view. The authors identify three transparency problems: latency between operator and robot head motion due to network delays or slow robot joints; a mismatch between the camera's narrower field-of-view and the headset's wider field-of-view; and the robot neck's smaller range of motion compared to a human neck. These issues can degrade embodiment, cause dizziness, force the operator to pause, and reduce overall interactivity.

To address these problems, the paper proposes a decoupled viewpoint control approach for a humanoid platform. The operator can freely control their viewpoint in an augmented-reality environment while receiving low-latency visual feedback. The system streams a real-time point cloud from the robot's camera and augments it with a SLAM-reconstructed mesh that covers blank areas caused by the three mismatches. An online calibration method aligns the virtual head-mounted display frame with the virtual robot camera frame, and visual-inertial odometry aligns the mesh with the live point cloud. Mesh coloring is used to balance immersion and the operator's awareness of the robot's actual head orientation.

The approach was implemented on the HRP-4CR adult-size humanoid using a ZED Mini stereo camera, an HTC Vive Pro Eye HMD, Valve Index controllers, an Intel NUC, an Nvidia Jetson Nano, and Valve Lighthouse tracking. A qualitative experiment demonstrated the effectiveness of the solution, though the authors note that a full user study remains future work.

## Key Contributions

- Decoupled viewpoint solution for a humanoid platform enabling low-latency visual feedback while operators freely control their viewpoint in an augmented reality environment.
- Use of a SLAM-reconstructed mesh to complement blank areas caused by FOV mismatch, neck range-of-motion mismatch, or operator-robot head motion lag.
- Online calibration method to align the virtual HMD and virtual robot camera frame for improved point cloud visualization quality.
- Integration of visual-inertial odometry to align mesh and point cloud, with mesh coloring used to balance immersion and operator awareness.

## Relevance to Humanoid Robotics

The work is highly relevant to humanoid robotics because it directly targets immersive teleoperation of the adult-size HRP-4CR humanoid, addressing the visual feedback latency and field-of-view constraints that are critical for safe, intuitive remote operation. By decoupling the operator's viewpoint from the robot's head orientation, the system improves embodiment and reduces operator fatigue, which are key barriers in real-world deployment and avatar-competition scenarios.

The integration of SLAM, real-time point-cloud streaming, and online calibration also contributes to the software-middleware layer of humanoid systems, providing a concrete example of how perception, human-robot interfaces, and control can be combined for practical telepresence applications.
