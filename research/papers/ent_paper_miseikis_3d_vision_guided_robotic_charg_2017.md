---
$id: ent_paper_miseikis_3d_vision_guided_robotic_charg_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  zh: 面向电动和插电式混合动力汽车的3D视觉引导机器人充电站
  ko: 전기 및 플러그인 하이브리드 차량을 위한 3D 비전 기반 로봇 충전 스테이션
summary:
  en: This 2017 arXiv paper presents an automated robotic charging station that uses
    a stereo-camera 3D vision system, shape-based matching, and a UR10 arm to locate
    and plug into EV/PHEV charging ports without vehicle modification.
  zh: 这篇2017年arXiv论文提出了一种自动化机器人充电站，利用立体相机三维视觉系统、基于形状的匹配和UR10机械臂，在不改装车辆的情况下定位并插入电动/插电式混合动力汽车的充电口。
  ko: 이 2017년 arXiv 논문은 스테레오 카메라 3D 비전 시스템, 형상 기반 매칭 및 UR10 로봇 암을 사용하여 차량을 개조하지 않고도
    EV/PHEV 충전 포트를 찾아 연결하는 자동 로봇 충전 스테이션을 제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- robotic_charging
- ev_charging
- 3d_vision
- stereo_vision
- shape_based_matching
- visual_servoing
- hand_eye_calibration
- markerless_calibration
- force_monitored_insertion
- plug_insertion
- ur10
- contact_rich_manipulation
- manipulation_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full text not independently reviewed;
    method details and source citations require human verification.
sources:
- id: src_001
  type: paper
  title: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid
    Vehicles
  url: https://arxiv.org/abs/1703.05381
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper proposes an automated robotic charging station designed to plug and unplug electric vehicle (EV) and plug-in hybrid vehicle (PHEV) chargers without modifying the vehicle. The system integrates a stereo-camera 3D vision system, a UR10 industrial robot arm, and a charging station fixture. The vision pipeline uses shape-based template matching to identify the charging port type and estimate its six-degree-of-freedom pose. A marker-less eye-to-hand calibration method is introduced that exploits the known geometry of the connector plug instead of requiring additional calibration markers.

For plug-in, the authors present a three-step Cartesian motion planning procedure: approach the port, align the connector, and insert with force/torque monitoring to prevent damage. The system was experimentally evaluated on Type 1 and Type 2 charging ports under varying angles and lighting conditions. Results demonstrated successful plug-in, although small angular misalignments (2°–5°) were observed, particularly at 30° port angles.

## Key Contributions

- Integration of a 3D stereo vision system, UR10 robot arm, and charging station into a unified robotic charging concept.
- Shape-based template matching for identifying the charging port type and estimating its precise 3D position and orientation.
- Marker-less eye-to-hand calibration using the known structure of the connector plug, eliminating the need for additional calibration markers.
- Three-step plug-in motion planning (approach, align, insert) with force monitoring to prevent damage during contact.
- Experimental validation on Type 1 and Type 2 charging ports under varying angles and lighting conditions.

## Relevance to Humanoid Robotics

Although demonstrated on a fixed-base UR10 arm for EV charging, the work develops reusable capabilities that are directly applicable to humanoid robots. The marker-less hand-eye calibration, 6D pose estimation via shape-based matching, and force-monitored insertion strategies are foundational skills for contact-rich industrial and service manipulation. These same methods can transfer to humanoid platforms performing plug-in tasks, tool use, or constrained assembly in unstructured environments.
