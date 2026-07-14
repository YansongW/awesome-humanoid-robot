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
  en: This 2017 arXiv paper presents an automated robotic charging station that uses a stereo-camera 3D vision system, shape-based
    matching, and a UR10 arm to locate and plug into EV/PHEV charging ports without vehicle modification.
  zh: 这篇2017年arXiv论文提出了一种自动化机器人充电站，利用立体相机三维视觉系统、基于形状的匹配和UR10机械臂，在不改装车辆的情况下定位并插入电动/插电式混合动力汽车的充电口。
  ko: 이 2017년 arXiv 논문은 스테레오 카메라 3D 비전 시스템, 형상 기반 매칭 및 UR10 로봇 암을 사용하여 차량을 개조하지 않고도 EV/PHEV 충전 포트를 찾아 연결하는 자동 로봇 충전 스테이션을
    제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1703.05381v1.
sources:
- id: src_001
  type: paper
  title: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  url: https://arxiv.org/abs/1703.05381
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Electric vehicles (EVs) and plug-in hybrid vehicles (PHEVs) are rapidly gaining popularity on our roads. Besides a comparatively high purchasing price, the main two problems limiting their use are the short driving range and inconvenient charging process. In this paper we address the following by presenting an automatic robot-based charging station with 3D vision guidance for plugging and unplugging the charger. First of all, the whole system concept consisting of a 3D vision system, an UR10 robot and a charging station is presented. Then we show the shape-based matching methods used to successfully identify and get the exact pose of the charging port. The same approach is used to calibrate the camera-robot system by using just known structure of the connector plug and no additional markers. Finally, a three-step robot motion planning procedure for plug-in is presented and functionality is demonstrated in a series of successful experiments.

## 核心内容
Electric vehicles (EVs) and plug-in hybrid vehicles (PHEVs) are rapidly gaining popularity on our roads. Besides a comparatively high purchasing price, the main two problems limiting their use are the short driving range and inconvenient charging process. In this paper we address the following by presenting an automatic robot-based charging station with 3D vision guidance for plugging and unplugging the charger. First of all, the whole system concept consisting of a 3D vision system, an UR10 robot and a charging station is presented. Then we show the shape-based matching methods used to successfully identify and get the exact pose of the charging port. The same approach is used to calibrate the camera-robot system by using just known structure of the connector plug and no additional markers. Finally, a three-step robot motion planning procedure for plug-in is presented and functionality is demonstrated in a series of successful experiments.

## 参考
- http://arxiv.org/abs/1703.05381v1

