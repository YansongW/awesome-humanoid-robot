---
$id: ent_paper_gao_kilvo_kinematic_inertial_lidar_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots'
  zh: 'KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots'
  ko: 'KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots'
summary:
  en: This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the
    platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid
    robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated
    Kalman filter (ESIKF). Specifically, ...
  zh: KILVO 是一种面向人形机器人的运动估计框架，融合关节编码器、IMU、LiDAR 和相机数据，采用异步-顺序混合误差状态迭代卡尔曼滤波器（ESIKF）实现高精度、高效率的位姿估计。该框架由 Jixin Gao、Fucheng Liu、Teng
    Zhang 和 Fusheng Zha 提出，具备多模态自适应能力以应对传感器故障，并在公开数据集和真实场景中验证了其鲁棒性。
  ko: This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the
    platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid
    robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated
    Kalman filter (ESIKF). Specifically, ...
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
- humanoid_odometry
- multimodal_fusion
- state_estimation
- sensor_failure_robustness
- esikf
- contact_estimation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-10'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-10). Bibliographic metadata from arXiv API (2608.05647);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.05647 KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid
    Robots'
  url: https://arxiv.org/abs/2608.05647
  date: '2026-08-06'
  accessed_at: '2026-08-10'
---

## 概述

KILVO 专为人形机器人设计，充分利用其常见传感器配置，通过异步处理腿部运动学数据提供本体感觉约束，并顺序融合 LiDAR 几何先验和相机光度误差。框架内置紧凑的接触估计模块，无需额外传感器即可共享状态估计信息。实验表明，KILVO 在精度、效率和输出频率上优于现有融合方法，且对传感器退化具有强鲁棒性，代码和数据集已开源。

## 核心内容

### 问题背景
人形机器人在复杂环境中需要高精度、高鲁棒性的状态估计，但现有融合方法往往未充分利用平台特有的关节编码器信息，且对传感器故障敏感。KILVO 旨在解决这些问题，通过多模态融合提升适应性和可靠性。

### 方法
- **传感器利用**：整合关节编码器、IMU、LiDAR 和相机，覆盖本体感觉与外部感知。
- **滤波框架**：采用异步-顺序混合误差状态迭代卡尔曼滤波器（ESIKF），惯性数据用于预测，腿部运动学以高频率异步处理并提供本体感觉约束。
- **外部感知更新**：顺序执行，先通过 LiDAR 点云配准获取几何先验，再通过光度误差更新视觉分量。
- **多模态自适应**：设计用于应对传感器故障，确保部分传感器失效时仍能稳定运行。
- **接触估计模块**：紧凑设计，无需额外传感器，与状态估计共享信息。

### 实验设置与结果
- **数据集与场景**：在公开数据集和真实世界中，跨多个人形机器人、多种步态模式和场景进行广泛测试。
- **关键结果**：KILVO 在精度、效率和输出频率上达到高度竞争力，相比最先进的融合方法，对传感器退化和故障表现出强鲁棒性，更适合人形机器人应用。
- **开源**：代码和数据集已在 GitHub 上发布。

### 结论
KILVO 通过充分利用人形机器人平台特性，结合多模态自适应和高效滤波设计，显著提升了状态估计的准确性和可靠性，为复杂环境下的机器人操作提供了实用解决方案。

## Overview

This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated Kalman filter (ESIKF). Specifically, inertial data are used for prediction, leg kinematics are processed asynchronously at a high rate and provide proprioceptive constraints, while exteroception is updated sequentially, first by registering LiDAR points for geometric priors and then by updating the visual component via photometric errors. Moreover, the framework is elaborately designed with multimodal adaptation for resilience to sensor failures. A compact contact estimation module is also developed, sharing information with state estimation without additional sensors. Extensive experiments on public datasets and in the real world across multiple humanoid robots, gait patterns, and scenarios demonstrate that KILVO achieves highly competitive accuracy, efficiency, and output rates, with strong robustness against sensor degradation and failures, making it more suitable for humanoid robots than state-of-the-art fusion methods. Our code and datasets are released on GitHub.

## 参考
- https://arxiv.org/abs/2608.05647
