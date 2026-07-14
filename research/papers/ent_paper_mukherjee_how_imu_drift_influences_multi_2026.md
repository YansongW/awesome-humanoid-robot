---
$id: ent_paper_mukherjee_how_imu_drift_influences_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
  zh: IMU漂移如何影响地下地形地面机器人的多雷达惯性里程计
  ko: 지하 지형에서 지상 로봇을 위한 다중 레이더 관성 주행거리측정에 IMU 드리프트가 미치는 영향
summary:
  en: This paper proposes a two-stage Multi-Radar Inertial Odometry (MRIO) framework that estimates radar ego-velocity via
    least squares, uses an EKF for online IMU bias correction, and fuses corrected IMU accelerations with measurements from
    multiple TI IWR6843AOP EVM FMCW radars to achieve robust localization and mapping in GPS-denied subterranean environments.
  zh: 本文提出了一个两阶段多雷达惯性里程计（MRIO）框架，通过最小二乘法估计雷达自车速度，利用扩展卡尔曼滤波器（EKF）在线校正IMU偏差，并将校正后的IMU加速度与多个TI IWR6843AOP EVM FMCW雷达的测量数据融合，以在GPS拒止的地下环境中实现稳健定位与建图。
  ko: 본 논문은 최소자승법을 통해 레이더 자차 속도를 추정하고, EKF를 사용해 IMU 바이어스를 온라인으로 보정하며, 보정된 IMU 가속도를 여러 개의 TI IWR6843AOP EVM FMCW 레이더 측정값과 융합하여
    GPS가 차단된 지하 환경에서 강건한 위치 추정 및 맵핑을 달성하는 두 단계 다중 레이더 관성 주행거리측정(MRIO) 프레임워크를 제안한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- radar_inertial_odometry
- multi_radar_fusion
- imu_bias_estimation
- fmcw_radar
- gps_denied_localization
- subterranean_navigation
- ekf_fusion
- sensor_fusion
- ground_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.24192v1.
sources:
- id: src_001
  type: paper
  title: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
  url: https://arxiv.org/abs/2602.24192
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO

## 核心内容
Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO

## 参考
- http://arxiv.org/abs/2602.24192v1

