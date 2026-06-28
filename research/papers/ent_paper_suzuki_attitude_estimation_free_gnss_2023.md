---
$id: ent_paper_suzuki_attitude_estimation_free_gnss_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Attitude-Estimation-Free GNSS and IMU Integration
  zh: 无需姿态估计的GNSS/IMU融合定位
  ko: 자세 추정 없는 GNSS/IMU 통합 위치 추정
summary:
  en: Proposes an optimization-based GNSS/IMU integration method that avoids attitude
    estimation by using acceleration-magnitude and velocity-vector angular-change
    constraints, reducing calibration sensitivity and improving robustness to multipath
    and GNSS outages.
  zh: 提出了一种基于优化的GNSS/IMU融合定位方法，仅利用加速度计幅值与速度矢量角度变化约束来避免姿态估计，从而降低对IMU安装标定的敏感性，并提升多路径与GNSS中断时的鲁棒性。
  ko: 가속도계 크기와 속도 벡터 각도 변화 제약만을 사용하여 자세 추정 없이 GNSS/IMU를 융합하는 최적화 기반 위치 추정 방법을 제안하여
    IMU 장착 오차에 둔감하고 다중경로·GNSS 단절에 강건함을 보였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- gnss_imu_fusion
- outdoor_localization
- sensor_fusion
- attitude_free_estimation
- factor_graph
- multipath_robustness
- localization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Attitude-Estimation-Free GNSS and IMU Integration
  url: https://arxiv.org/abs/2304.10142
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Global navigation satellite systems (GNSS) provide 3D position and velocity in an earth-fixed frame and are widely used for outdoor localization of robots and vehicles. Existing GNSS/inertial measurement unit (IMU) integration techniques generally augment the estimated state with a 3D attitude in order to fuse IMU measurements, which increases calibration demands and can degrade accuracy when the IMU mounting angle or position is imperfect.

This paper proposes an optimization-based positioning method that combines GNSS and IMU without estimating attitude. The approach introduces two attitude-independent constraints in a factor-graph framework: an acceleration-magnitude factor derived from 3D accelerometer readings, and an angular-velocity factor that constrains the angle between successive velocity vectors. By removing attitude from the state vector, the method reduces state dimension and computation time while becoming insensitive to IMU mounting-angle errors.

Evaluation on MATLAB-generated simulation trajectories based on the Google Smartphone Decimeter Challenge shows that the proposed method preserves positioning accuracy as IMU mounting-position error grows and improves accuracy when GNSS observations contain multipath errors or short outages. Real-world experiments using smartphone GNSS/IMU data collected in driving environments further demonstrate that the reduced-state approach achieves comparable accuracy to conventional 6-DOF pose estimation while running faster and requiring less calibration.

## Key Contributions

- Introduced an IMU constraint that avoids attitude estimation, making GNSS/IMU integration independent of IMU mounting angle and position.
- Developed a factor-graph formulation with acceleration magnitude and angular-velocity factors, reducing state dimension and computation time.
- Demonstrated robustness to IMU mounting-position errors through simulation experiments.
- Showed improved position accuracy under multipath and short GNSS outages in both simulation and real-world smartphone driving tests.
- Validated that the reduced-state method achieves comparable accuracy to conventional 6-DOF pose estimation while being faster and less sensitive to calibration errors.

## Relevance to Humanoid Robotics

Humanoid robots deployed outdoors for logistics, inspection, or service require reliable localization in challenging environments where GNSS signals may be reflected or temporarily obstructed. This method reduces the sensor calibration overhead associated with precise IMU mounting-angle and position estimation, supporting scalable deployment where IMUs may be placed in varying positions and orientations on the robot body.

By fusing GNSS with IMU without attitude estimation, the approach offers a lightweight and robust localization option for outdoor humanoid platforms, particularly in scenarios with multipath, short GNSS outages, or hardware configurations where tight IMU-to-body calibration is impractical.
