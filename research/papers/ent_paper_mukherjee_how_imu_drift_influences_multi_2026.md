---
$id: ent_paper_mukherjee_how_imu_drift_influences_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in
    Subterranean Terrains
  zh: IMU漂移如何影响地下地形地面机器人的多雷达惯性里程计
  ko: 지하 지형에서 지상 로봇을 위한 다중 레이더 관성 주행거리측정에 IMU 드리프트가 미치는 영향
summary:
  en: This paper proposes a two-stage Multi-Radar Inertial Odometry (MRIO) framework
    that estimates radar ego-velocity via least squares, uses an EKF for online IMU
    bias correction, and fuses corrected IMU accelerations with measurements from
    multiple TI IWR6843AOP EVM FMCW radars to achieve robust localization and mapping
    in GPS-denied subterranean environments.
  zh: 本文提出了一个两阶段多雷达惯性里程计（MRIO）框架，通过最小二乘法估计雷达自车速度，利用扩展卡尔曼滤波器（EKF）在线校正IMU偏差，并将校正后的IMU加速度与多个TI
    IWR6843AOP EVM FMCW雷达的测量数据融合，以在GPS拒止的地下环境中实现稳健定位与建图。
  ko: 본 논문은 최소자승법을 통해 레이더 자차 속도를 추정하고, EKF를 사용해 IMU 바이어스를 온라인으로 보정하며, 보정된 IMU 가속도를
    여러 개의 TI IWR6843AOP EVM FMCW 레이더 측정값과 융합하여 GPS가 차단된 지하 환경에서 강건한 위치 추정 및 맵핑을 달성하는
    두 단계 다중 레이더 관성 주행거리측정(MRIO) 프레임워크를 제안한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; full-text review is required
    before marking verified.
sources:
- id: src_001
  type: paper
  title: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots
    in Subterranean Terrains
  url: https://arxiv.org/abs/2602.24192
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Reliable radar inertial odometry (RIO) in GPS-denied subterranean environments is challenged by IMU bias drift, sparse and noisy radar returns, and visually degraded conditions where LiDAR can fail. This paper proposes a two-stage Multi-Radar Inertial Odometry (MRIO) framework that couples radar-based ego-velocity estimation with online IMU bias correction and multi-radar fusion. In the first stage, radar ego-velocity is formulated as a least-squares problem and fed into an Extended Kalman Filter (EKF) to correct IMU biases. In the second stage, the corrected IMU accelerations are fused with heterogeneous measurements from multiple FMCW radars and the IMU to refine global odometry and support radar-only mapping using estimated translational and rotational displacements.

The authors focus on cost-effective hardware, specifically the TI IWR6843AOP EVM mmWave radar paired with either a low-cost Pixhawk 2.1 Cube Orange IMU or a higher-grade VectorNav VN-100 IMU/AHRS. A key component of the approach is a sensing-radius outlier rejection method designed to handle sparse, noisy, and flickering radar point clouds without relying on RANSAC. The framework is evaluated in real subterranean tunnel trials, demonstrating robust localization and mapping performance that outperforms EKF-RIO and remains competitive with or superior to LiDAR-inertial odometry in dust- and smoke-filled conditions.

The paper also discusses important limitations. Because orientation is sourced solely from the IMU, gyro bias can induce drift and degrade map consistency. Additionally, the evaluation is limited to a wheeled ground robot, and FMCW radars require sufficient relative motion to generate returns, which can impair performance during static or very slow operation.

## Key Contributions

- First radar inertial odometry and mapping framework using multiple cost-effective TI IWR6843AOP EVM mmWave radars.
- Sensing-radius outlier rejection method for sparse, noisy, and flickering radar point clouds, reported to outperform RANSAC.
- Complementary online IMU bias estimator that enables robust operation with both low-cost Pixhawk and high-grade VectorNav IMUs.
- Extensive subterranean tunnel validation showing large accuracy improvements over EKF-RIO and LiDAR-inertial odometry.
- Open-source release of the implementation at https://github.com/LTU-RAI/MRIO.

## Relevance to Humanoid Robotics

The core contribution—robust radar-IMU fusion with online IMU bias compensation—is directly transferable to humanoid robots. Humanoids operating in industrial facilities, search-and-rescue scenarios, or subterranean environments must localize in GPS-denied, visually degraded conditions where LiDAR and vision systems can fail due to dust, smoke, or aerosols. FMCW radars are compact, lightweight, and cost-effective, making them attractive for humanoid payloads where size, weight, and power are constrained. The demonstrated ability to maintain accurate odometry using both low-cost and high-grade IMUs provides a practical path for affordable humanoid state estimation in challenging real-world deployments.
