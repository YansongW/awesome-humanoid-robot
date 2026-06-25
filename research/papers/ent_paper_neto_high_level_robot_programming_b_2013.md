---
$id: ent_paper_neto_high_level_robot_programming_b_2013
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'High-level robot programming based on CAD: dealing with unpredictable environments'
  zh: 基于CAD的高级机器人编程：应对不可预测环境
  ko: 'CAD 기반 고수준 로봇 프로그래밍: 예측 불가능한 환경 대응'
summary:
  en: This paper presents a CAD-based human-robot interface that lets non-expert users
    program industrial robots by drawing paths in Autodesk Inventor, and compensates
    for environmental uncertainty using online feedback from a laser camera and a
    force/torque sensor.
  zh: 本文提出一种基于CAD的人机交互界面，允许非专业用户在Autodesk Inventor中绘制路径来编程工业机器人，并通过激光相机和力/力矩传感器的在线反馈补偿环境不确定性。
  ko: 본 논문은 Autodesk Inventor에서 경로를 그려 비전문 사용자가 산업용 로봇을 프로그래밍할 수 있는 CAD 기반 인간-로봇 인터페이스를
    제안하며, 레이저 카메라와 힘/토크 센서의 온라인 피드백을 통해 환경 불확실성을 보상한다.
domains:
- 08_software_middleware
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cad_based_programming
- robot_programming
- teach_by_demonstration
- sensory_feedback
- online_path_correction
- seam_tracking
- force_controlled_profile_following
- industrial_robot
- autodesk_inventor
- laser_camera
- force_torque_sensor
- human_robot_interface
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full arXiv text before final verification.
sources:
- id: src_001
  type: paper
  title: 'High-level robot programming based on CAD: dealing with unpredictable environments'
  url: https://arxiv.org/abs/1309.2086
  date: '2013'
  accessed_at: '2026-06-26'
---


## Overview

This paper introduces a CAD-based human-robot interface that enables non-expert users to generate industrial robot programs by drawing paths directly in a 3D CAD model. Instead of relying on commercial computer-aided robotics (CAR) software, the system extracts three-dimensional positions and orientations from Autodesk Inventor through its API and converts them into robot programs off-line. The goal is to make robot programming as intuitive as showing a human coworker what motion to perform, thereby reducing setup time and the need for specialized robot-programming expertise.

A second focus of the work is handling uncertainty in real-world, unpredictable environments. Calibration errors, discrepancies between CAD models and physical parts, and dynamic changes can make pre-programmed paths inaccurate. To address this, the authors close the control loop with sensory feedback: a laser camera is used for seam tracking, and a force/torque sensor is used for profile following. The sensory data adjusts the robot trajectory on-line so that the executed motion matches the actual workpiece rather than the nominal CAD geometry.

The experimental validation covers two representative industrial tasks. In the first, an ABB IRB 2400 robot with a laser camera performs seam tracking. In the second, a Motoman HP6 robot equipped with a JR3 force/torque sensor follows an unknown profile. The results are reported to demonstrate reduced setup time, lower sensitivity to calibration, and the ability of untrained operators to generate programs within minutes.

## Key Contributions

- A robot programming system that generates executable programs directly from Autodesk Inventor via its API, avoiding dependence on dedicated CAR/CAM packages.
- An intuitive, low-cost interface that allows non-expert users to program robots by drawing paths in a familiar 3D CAD environment.
- Automatic extraction and coordinate transformation of CAD geometry into robot target poses, with smooth interpolation of both position and orientation.
- Integration of on-line sensory feedback from a laser camera and a force/torque sensor to compensate uncertainty in dynamic environments.
- Experimental demonstration of seam tracking and force-controlled profile following on industrial manipulators.

## Relevance to Humanoid Robotics

Although the paper demonstrates the approach on industrial manipulators rather than humanoid robots, the underlying principles are directly transferable to humanoid deployment in unstructured environments. Intuitive, CAD-based teaching can reduce the programming effort required to specify whole-body or manipulation tasks for humanoids, while on-line sensory feedback can compensate for model errors, calibration drift, and unexpected obstacles that are common in human-centered settings. For humanoid robots operating in homes, healthcare facilities, or construction sites, combining high-level task specification from a familiar digital model with low-level sensor-based correction is a promising route to robust, adaptive behavior.
