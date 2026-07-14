---
$id: ent_paper_chen_enhanced_visual_feedback_with_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid Robot Teleoperation using SLAM
  zh: 基于SLAM的沉浸式人形机器人遥操作中解耦视角控制的增强视觉反馈
  ko: SLAM을 이용한 몰입형 휴머노이드 로봇 원격조작에서 분리된 시점 제어를 통한 향상된 시각 피드백
summary:
  en: This paper presents a decoupled viewpoint control system for immersive teleoperation of the HRP-4CR humanoid, fusing
    real-time point-cloud streaming from a ZED Mini camera with a SLAM-reconstructed mesh to mitigate visual feedback latency,
    camera field-of-view limits, and restricted robot neck motion.
  zh: 本文提出了一种用于HRP-4CR人形机器人沉浸式遥操作的解耦视角控制系统，将ZED Mini相机的实时点云流与SLAM重建网格融合，以缓解视觉反馈延迟、相机视场角限制以及机器人颈部运动范围受限的问题。
  ko: 본 논문은 HRP-4CR 휴머노이드 로봇의 몰입형 원격조작을 위한 분리된 시점 제어 시스템을 제안하며, ZED Mini 카메라의 실시간 포인트 클라우드 스트리밍과 SLAM 재구성 메시를 융합하여 시각 피드백
    지연, 카메라 시야각 제한, 그리고 로봇 목 운동 범위 제한을 완화한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.01749v1.
sources:
- id: src_001
  type: paper
  title: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid Robot Teleoperation using SLAM
  url: https://arxiv.org/abs/2211.01749
  date: '2022'
  accessed_at: '2026-06-26'
---
## 概述
In immersive humanoid robot teleoperation, there are three main shortcomings that can alter the transparency of the visual feedback: the lag between the motion of the operator's and robot's head due to network communication delays or slow robot joint motion. This latency could cause a noticeable delay in the visual feedback, which jeopardizes the embodiment quality, can cause dizziness, and affects the interactivity resulting in operator frequent motion pauses for the visual feedback to settle; (ii) the mismatch between the camera's and the headset's field-of-views (FOV), the former having generally a lower FOV; and (iii) a mismatch between human's and robot's range of motions of the neck, the latter being also generally lower. In order to leverage these drawbacks, we developed a decoupled viewpoint control solution for a humanoid platform which allows visual feedback with low-latency and artificially increases the camera's FOV range to match that of the operator's headset. Our novel solution uses SLAM technology to enhance the visual feedback from a reconstructed mesh, complementing the areas that are not covered by the visual feedback from the robot. The visual feedback is presented as a point cloud in real-time to the operator. As a result, the operator is fed with real-time vision from the robot's head orientation by observing the pose of the point cloud. Balancing this kind of awareness and immersion is important in virtual reality based teleoperation, considering the safety and robustness of the control system. An experiment shows the effectiveness of our solution.

## 核心内容
In immersive humanoid robot teleoperation, there are three main shortcomings that can alter the transparency of the visual feedback: the lag between the motion of the operator's and robot's head due to network communication delays or slow robot joint motion. This latency could cause a noticeable delay in the visual feedback, which jeopardizes the embodiment quality, can cause dizziness, and affects the interactivity resulting in operator frequent motion pauses for the visual feedback to settle; (ii) the mismatch between the camera's and the headset's field-of-views (FOV), the former having generally a lower FOV; and (iii) a mismatch between human's and robot's range of motions of the neck, the latter being also generally lower. In order to leverage these drawbacks, we developed a decoupled viewpoint control solution for a humanoid platform which allows visual feedback with low-latency and artificially increases the camera's FOV range to match that of the operator's headset. Our novel solution uses SLAM technology to enhance the visual feedback from a reconstructed mesh, complementing the areas that are not covered by the visual feedback from the robot. The visual feedback is presented as a point cloud in real-time to the operator. As a result, the operator is fed with real-time vision from the robot's head orientation by observing the pose of the point cloud. Balancing this kind of awareness and immersion is important in virtual reality based teleoperation, considering the safety and robustness of the control system. An experiment shows the effectiveness of our solution.

## 参考
- http://arxiv.org/abs/2211.01749v1

