---
$id: ent_paper_lu_pose_estimation_for_robot_mani_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Pose Estimation for Robot Manipulators via Keypoint Optimization and Sim-to-Real
    Transfer
  zh: 基于关键点优化与仿真到现实迁移的机器人操纵臂姿态估计
  ko: 키포인트 최적화 및 시뮬레이션-실제 전이를 통한 로봇 매니퓰레이터 자세 추정
summary:
  en: This paper proposes an iterative keypoint optimization algorithm that selects
    3D keypoints on robotic manipulators to maximize 2D detection and 3D localization
    accuracy, trains a DeepLabCut-based detector on synthetic CoppeliaSim data, and
    transfers it to real images via domain randomization for camera-to-robot calibration
    and tool tracking.
  zh: 本文提出了一种迭代式关键点优化算法，用于在机器人操作臂上选择能最大化二维检测和三维定位精度的三维关键点；该算法在 CoppeliaSim 合成数据上训练基于
    DeepLabCut 的检测器，并通过域随机化将其迁移到真实图像，实现相机到机器人标定与工具跟踪。
  ko: 본 논문은 로봇 매니퓰레이터 상에서 2D 검출 및 3D 위치 추정 정확도를 극대화하는 3D 키포인트를 선택하는 반복적 키포인트 최적화 알고리즘을
    제안한다. CoppeliaSim 합성 데이터로 DeepLabCut 기반 검출기를 학습하고 도메인 랜덤화를 통해 실제 이미지로 전이하여 카메라-로봇
    캘리브레이션과 도구 추적을 수행한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- keypoint_optimization
- sim_to_real_transfer
- domain_randomization
- pose_estimation
- robot_calibration
- surgical_tool_tracking
- deeplabcut
- coppeliasim
- visual_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv PDF (2010.08054); requires human review before
    full verification.
sources:
- id: src_001
  type: paper
  title: Pose Estimation for Robot Manipulators via Keypoint Optimization and Sim-to-Real
    Transfer
  url: https://arxiv.org/abs/2010.08054
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the problem of choosing where to place visual keypoints on robotic manipulators so that they can be detected and localized reliably. Instead of relying on manually selected or marker-based keypoints, the authors formulate keypoint selection as an optimization over a set of candidate 3D locations on the robot links. The objective jointly minimizes 2D detection error from a deep neural network and 3D localization error, and an iterative sampling procedure is used to search for the best subset of keypoints. Training and evaluation are performed entirely in simulation using CoppeliaSim and PyRep, which provide automatic ground-truth labels.

The optimized keypoints are then transferred to real images through domain randomization. The authors randomize lighting, distractor objects, background images, robot mesh colors, and sensor noise during synthetic data generation so that the trained detector generalizes to the physical world. The approach is validated on two robotic systems: a Rethink Robotics Baxter arm for camera-to-robot calibration and end-effector pose estimation, and a da Vinci Research Kit (dVRK) surgical tool for real-time tool tracking. Experiments compare multiple backbone architectures (ResNet 50/101, MobileNet v2 1.0/0.5) and show that optimized keypoints outperform hand-picked or random keypoints.

In addition to the algorithmic contribution, the authors release the "Robot Pose" dataset, which contains calibration and tracking sequences with ground-truth annotations. They also leverage existing datasets—the Baxter dataset captured with a Microsoft Azure Kinect, the SuPer tool tracking dataset for dVRK, and background images from the Indoor Scene and Hamlyn Centre Endoscopic Video datasets—to support training and evaluation.

## Key Contributions

- A general keypoint optimization algorithm that finds 3D keypoint locations on manipulators to maximize 2D detection and 3D localization performance.
- Demonstration that optimized keypoints improve real-world robot-to-camera pose estimation through sim-to-real transfer via domain randomization.
- Methodology combining optimized keypoints with a particle filter for surgical tool tracking, evaluated on the dVRK platform.
- Release of the 'Robot Pose' dataset with calibration and tracking ground-truth data.

## Relevance to Humanoid Robotics

Although the experiments focus on a Baxter arm and a surgical tool, the underlying pipeline—automatic keypoint selection, synthetic training, and sim-to-real transfer—is directly applicable to humanoid robot arms and end-effectors. Humanoid platforms often require vision-based calibration, tool tracking, and end-effector pose estimation during deployment, assembly, and mass production. By optimizing keypoint locations rather than hand-picking them, the method can reduce engineering effort and improve robustness to self-occlusion and symmetric structures, which are common in humanoid manipulators. The domain-randomization-based transfer strategy also provides a scalable way to deploy visual perception modules on new humanoid hardware without collecting large real-world labeled datasets.
