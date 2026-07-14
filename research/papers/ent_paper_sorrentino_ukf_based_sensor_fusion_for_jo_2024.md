---
$id: ent_paper_sorrentino_ukf_based_sensor_fusion_for_jo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: UKF-Based Sensor Fusion for Joint-Torque Sensorless Humanoid Robots
  zh: 基于无迹卡尔曼滤波的仿人机器人无关节力矩传感器力矩估计
  ko: UKF 기반 관절 토크 센서가 없는 휴머노이드 로봇을 위한 센서 융합
summary:
  en: Proposes an Unscented Kalman Filter-based sensor fusion method for online joint-torque estimation in humanoid robots
    that lack joint-torque sensors, and validates the approach experimentally on the ergoCub humanoid within a two-level torque-control
    architecture.
  zh: 提出一种基于无迹卡尔曼滤波的多传感器融合方法，用于无关节力矩传感器的仿人机器人在线关节力矩估计，并在ergoCub仿人机器人的双层力矩控制架构中进行了实验验证。
  ko: 관절 토크 센서가 없는 휴머노이드 로봇의 온라인 관절 토크 추정을 위한 무향 칼만 필터 기반 센서 융합법을 제안하고, ergoCub 휴머노이드의 이중 토크 제어 아키텍처에서 실험적으로 검증한다.
domains:
- 08_software_middleware
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sensor_fusion
- unscented_kalman_filter
- joint_torque_estimation
- torque_control
- sensorless_humanoid
- floating_base_dynamics
- ergocub
- force_torque_sensors
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.18380v1.
sources:
- id: src_001
  type: paper
  title: UKF-Based Sensor Fusion for Joint-Torque Sensorless Humanoid Robots
  url: https://arxiv.org/abs/2402.18380
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
This paper proposes a novel sensor fusion based on Unscented Kalman Filtering for the online estimation of joint-torques of humanoid robots without joint-torque sensors. At the feature level, the proposed approach considers multimodal measurements (e.g. currents, accelerations, etc.) and non-directly measurable effects, such as external contacts, thus leading to joint torques readily usable in control architectures for human-robot interaction. The proposed sensor fusion can also integrate distributed, non-collocated force/torque sensors, thus being a flexible framework with respect to the underlying robot sensor suit. To validate the approach, we show how the proposed sensor fusion can be integrated into a twolevel torque control architecture aiming at task-space torquecontrol. The performances of the proposed approach are shown through extensive tests on the new humanoid robot ergoCub, currently being developed at Istituto Italiano di Tecnologia. We also compare our strategy with the existing state-of-theart approach based on the recursive Newton-Euler algorithm. Results demonstrate that our method achieves low root mean square errors in torque tracking, ranging from 0.05 Nm to 2.5 Nm, even in the presence of external contacts.

## 核心内容
This paper proposes a novel sensor fusion based on Unscented Kalman Filtering for the online estimation of joint-torques of humanoid robots without joint-torque sensors. At the feature level, the proposed approach considers multimodal measurements (e.g. currents, accelerations, etc.) and non-directly measurable effects, such as external contacts, thus leading to joint torques readily usable in control architectures for human-robot interaction. The proposed sensor fusion can also integrate distributed, non-collocated force/torque sensors, thus being a flexible framework with respect to the underlying robot sensor suit. To validate the approach, we show how the proposed sensor fusion can be integrated into a twolevel torque control architecture aiming at task-space torquecontrol. The performances of the proposed approach are shown through extensive tests on the new humanoid robot ergoCub, currently being developed at Istituto Italiano di Tecnologia. We also compare our strategy with the existing state-of-theart approach based on the recursive Newton-Euler algorithm. Results demonstrate that our method achieves low root mean square errors in torque tracking, ranging from 0.05 Nm to 2.5 Nm, even in the presence of external contacts.

## 参考
- http://arxiv.org/abs/2402.18380v1

