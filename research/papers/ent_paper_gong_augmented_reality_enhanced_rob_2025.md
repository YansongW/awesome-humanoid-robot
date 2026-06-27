---
$id: ent_paper_gong_augmented_reality_enhanced_rob_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Augmented Reality-Enhanced Robot Teleoperation for Collecting User Demonstrations
  zh: 用于收集用户演示的增强现实增强型机器人遥操作系统
  ko: 사용자 시연 수집을 위한 증강 현실 기반 로봇 원격 조작
summary:
  en: Proposes an AR-based teleoperation system that lets operators control ABB industrial
    and collaborative robots remotely via an HMD and hand controllers, using real-time
    point-cloud rendering to collect Programming by Demonstration data without entering
    the workspace.
  zh: 提出一种基于增强现实的遥操作系统，操作者可通过头戴显示器和手柄远程控制ABB工业及协作机器人，并利用实时点云渲染在无需进入工作空间的情况下收集示教编程数据。
  ko: HMD와 컨트롤러를 이용해 ABB 산업용 및 협동 로봇을 원격으로 제어하고, 실시간 포인트 클라우드 렌더링을 통해 작업 공간에 들어가지
    않고도 시연 기반 프로그래밍 데이터를 수집하는 AR 기반 원격 조작 시스템을 제안한다.
domains:
- 08_software_middleware
- 09_data_datasets
- 03_manufacturing_processes
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- system
tags:
- augmented_reality
- teleoperation
- programming_by_demonstration
- industrial_robot
- collaborative_robot
- point_cloud
- human_robot_interface
- demonstration_collection
- machine_learning_data
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text review is
    needed to confirm section-level citations and exact quantitative results before
    marking fully verified.
sources:
- id: src_001
  type: paper
  title: Augmented Reality-Enhanced Robot Teleoperation for Collecting User Demonstrations
  url: https://arxiv.org/abs/2509.11783
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Traditional industrial robot programming is complex and time-consuming, often requiring weeks or months of expert effort. Programming by Demonstration (PbD) offers a more accessible alternative, but intuitive, contact-free interfaces for collecting demonstrations remain difficult, especially for robots that lack native lead-through capability. To address this gap, the authors propose an Augmented Reality (AR)-enhanced robot teleoperation system that combines AR-based control with real-time spatial point cloud rendering, allowing operators to control robots remotely without entering the workspace or using a teach pendant.

The system is modular and generally applicable; it is demonstrated on ABB robot platforms, specifically the IRB 1200 industrial robot and the GoFa 5 collaborative robot (CRB 15000). The operator wears a Meta Quest 3 HMD and uses Touch Plus controllers to manipulate a virtual robot, while the physical robot mirrors the motion via ABB Externally Guided Motion (EGM). Environmental perception is provided by an Intel RealSense D405 depth camera, and robot state monitoring is performed through ABB Robot Web Services (RWS). The paper also introduces a standardized robot model processing workflow to support consistent cross-platform AR visualization.

A user study evaluates the impact of real-time point cloud rendering on task completion accuracy, efficiency, and user confidence. The results show that enhanced environmental perception improves task performance by 28% and increases the System Usability Scale (SUS) score by 12%. The authors argue that the collected demonstrations can serve as valuable training data for machine learning applications, including future humanoid robot systems in manufacturing and assembly.

## Key Contributions

- AR teleoperation framework for industrial robots without lead-through capability, also compatible with collaborative robots.
- Integration of AR control with real-time spatial point cloud rendering for contact-free demonstration collection.
- Standardized robot model processing workflow for consistent cross-platform AR visualization.
- User study quantifying the impact of point cloud rendering on task performance and usability.

## Relevance to Humanoid Robotics

Although the validation focuses on ABB industrial and collaborative manipulators, the AR teleoperation and Programming by Demonstration pipeline is explicitly framed as applicable to humanoid robots deployed in manufacturing and assembly. By lowering the barrier for large-scale, contact-free demonstration collection, the work supports the data-generation needs of learning-based humanoid control. The modular software middleware architecture—combining AR rendering, point-cloud perception, and robot motion interfaces—is directly transferable to humanoid platforms that require intuitive task programming and safe remote operation.
