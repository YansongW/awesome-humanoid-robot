---
$id: ent_paper_lu_contact_constrained_lower_limb_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots
  zh: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots
  ko: Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots
summary:
  en: Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration
    methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration
    framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact. The inter-foot
    transform from forward ...
  zh: 本文提出一种仅依赖关节编码器和骨盆IMU的自包含标定框架，用于人形机器人下肢关节偏移校准，无需外部动捕系统。该方法利用静态双足支撑接触约束，通过最小化前向运动学中足间变换的位姿相关离散度，求解12维偏移向量。在A3和A2机器人上，标定将足高RMS残差分别从4.26降至2.20
    mm和从8.03降至1.43 mm。
  ko: Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration
    methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration
    framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact. The inter-foot
    transform from forward ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_robots
- joint_offset_calibration
- contact_constraint
- imu
- kinematic_calibration
- lower_limb
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.02306);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.02306 Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots
  url: https://arxiv.org/abs/2609.02306
  date: '2026-09-02'
  accessed_at: '2026-09-07'
---

## 概述

该研究由Kaixiang Lu等人提出，针对人形机器人下肢关节编码器偏移标定问题，开发了一种自包含方法。核心思想是在静态双足支撑时，两足固定使足间变换保持恒定，通过最小化其位姿相关离散度构建非线性最小二乘问题。Hessian特征结构分析揭示了平行俯仰轴导致的旋转耦合，而方向残差仅观测俯仰偏移之和。在A3和A2机器人上的仿真与实机注入测试验证了方法有效性，独立LiDAR惯性参考确认了俯仰耦合通道的校正效果。

## 核心内容

### 问题背景
人形机器人下肢关节编码器偏移的精确性对运动学一致性至关重要。传统标定方法依赖外部动捕系统或基准靶标，限制了实际应用场景。本文旨在开发一种无需外部设备的自包含标定方案。

### 方法
- 利用静态双足支撑接触约束，此时两足固定，前向运动学计算的足间变换应保持恒定。
- 通过最小化足间变换的位姿相关离散度，构建关于12维偏移向量的非线性最小二乘问题。
- Hessian特征结构分析表明，平行俯仰轴会引发旋转耦合；方向残差仅能观测俯仰偏移之和，平移与位姿多样性决定其余数值可观测性。
- 针对A3的俯仰-横滚-偏航顺序，髋横滚与髋偏航激励可减少髋俯仰耦合；站立姿态的膝部先验用于锚定弱俯仰链分解。

### 实验设置与结果
- 在A3和A2机器人上进行仿真与实机注入测试，结果显示偏移恢复具有一致性。
- 在保留测试集上，标定使足高RMS残差在A3上从4.26 mm降至2.20 mm，在A2上从8.03 mm降至1.43 mm。
- 独立LiDAR惯性参考系统验证了俯仰耦合通道的校正效果；移除注入的俯仰偏移后，腿部里程计垂直漂移回归至LiDAR轨迹附近。

### 结论
少量静态双足支撑姿态即可为激励充分的方向提供接触一致的校正。弱俯仰链中的个别偏移仍依赖先验信息，表明该方法在特定方向上的局限性。

## Overview

Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact. The inter-foot transform from forward kinematics must stay constant when both feet are fixed; minimizing its posture-dependent dispersion yields a nonlinear least-squares problem over the 12-dimensional offset vector. A Hessian eigenstructure analysis shows that parallel pitch axes induce a rotational coupling. Orientation residuals then observe only the pitch-offset sum, while translation and posture diversity set the remaining numerical observability. For the A3 pitch-to-roll-to-yaw ordering, hip-roll and hip-yaw excitation reduce hip-pitch coupling. A standing-posture knee prior then anchors the remaining weak pitch-chain decomposition. Simulation and real-machine injection tests show consistent recovery, and on held-out recordings calibration reduces foot-height RMS residuals from 4.26 to 2.20 mm on A3 and from 8.03 to 1.43 mm on A2. An independent LiDAR-inertial reference checks the pitch-coupled channel. Removing an injected pitch offset moves the leg-odometry vertical drift back toward the LiDAR trajectory. A few static double-support stances thus provide contact-consistent corrections for well-excited directions. Individual offsets in the weak pitch chain remain prior-dependent.

## 参考
- https://arxiv.org/abs/2609.02306
