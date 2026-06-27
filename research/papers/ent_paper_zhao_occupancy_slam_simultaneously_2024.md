---
$id: ent_paper_zhao_occupancy_slam_simultaneously_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy
    Map'
  zh: Occupancy-SLAM：同时优化机器人位姿与连续占用地图
  ko: 'Occupancy-SLAM: 로봇 포즈와 연속 점유 지도를 동시에 최적화'
summary:
  en: An optimization-based SLAM approach that jointly optimizes robot trajectory
    and a continuous occupancy map from 2D laser scans and odometry using a Gauss-Newton
    variant.
  zh: 一种基于优化的SLAM方法，使用高斯-牛顿变体从二维激光扫描和里程计数据中联合优化机器人轨迹与连续占用地图。
  ko: 가우스-뉴턴 변형을 사용하여 2D 레이저 스캔과 주행거리계 정보로부터 로봇 궤적과 연속 점유 지도를 동시에 최적화하는 SLAM 접근법.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- slam
- occupancy_mapping
- laser_scan
- gauss_newton
- pose_estimation
- robot_navigation
- indoor_mapping
- batch_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text verification required
    before promotion.
sources:
- id: src_001
  type: paper
  title: 'Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy
    Map'
  url: https://arxiv.org/abs/2405.10743
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Occupancy-SLAM formulates simultaneous localization and mapping as a single nonlinear least-squares problem in which both robot poses and a continuous occupancy map are optimized together. The map is represented by evidence values at selected discrete grid-cell nodes, with continuous occupancy values obtained through bilinear interpolation. The objective incorporates observation constraints from 2D laser scans, odometry constraints, and adaptive smoothing terms, and is solved with a customized Gauss-Newton method. The approach is offline and batch-oriented; experiments on public 2D laser datasets and simulations show improved map and trajectory accuracy relative to Cartographer, GMapping, Hilbert Maps, and a random mapping baseline, given a sufficiently accurate initial guess.

## Key Contributions

- Joint optimization of robot poses and continuous occupancy map within one nonlinear least-squares framework.
- Continuous occupancy representation using bilinear interpolation of grid-cell node evidence values.
- Analytical derivation of Jacobians with respect to both pose variables and map variables.
- Uncertainty estimation for optimized poses and map via the information matrix.
- Experimental validation demonstrating higher accuracy than Cartographer, GMapping, Hilbert Maps, and Random Mapping on standard 2D laser datasets.

## Relevance to Humanoid Robotics

Accurate, globally consistent 2D occupancy mapping and pose estimation is a foundational navigation capability for humanoid robots deployed in structured indoor environments such as factories and warehouses. By jointly optimizing the map and trajectory rather than treating mapping as a post-processing step, Occupancy-SLAM can improve the reliability of localization and path planning for humanoid platforms operating in cluttered or geometrically complex spaces.
