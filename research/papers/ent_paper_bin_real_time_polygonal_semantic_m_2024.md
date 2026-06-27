---
$id: ent_paper_bin_real_time_polygonal_semantic_m_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-Time Polygonal Semantic Mapping for Humanoid Robot Stair Climbing
  zh: 面向人形机器人楼梯攀爬的实时多边形语义建图
  ko: 인간형 로봇 계단 등반을 위한 실시간 다각형 의미 지도 작성
summary:
  en: This paper proposes a real-time polygonal planar semantic mapping system for
    humanoid robot stair climbing, combining GPU-accelerated anisotropic diffusion
    filtering, Sobel-based normal estimation, polygonal contour extraction, RANSAC
    plane fitting, and Kalman-filter vertical drift compensation, achieving single-frame
    processing above 30 Hz.
  zh: 本文提出了一种面向人形机器人楼梯攀爬的实时多边形平面语义建图系统，结合了 GPU 加速的各向异性扩散滤波、Sobel 法向量估计、多边形轮廓提取、RANSAC
    平面拟合以及卡尔曼滤波垂直漂移补偿，单帧处理速度超过 30 Hz。
  ko: 본 논문은 인간형 로봇 계단 등반을 위한 실시간 다각형 평면 의미 지도 작성 시스템을 제안한다. GPU 가속 이방성 확산 필터링, Sobel
    기반 법선 추정, 다각형 윤곽 추출, RANSAC 평면 적합, 그리고 칼만 필터 수직 드리프트 보정을 결합하여 단일 프레임 처리 속도가 30
    Hz 이상이다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- stair_climbing
- semantic_mapping
- polygonal_mapping
- plane_extraction
- anisotropic_diffusion
- ransac
- gpu_acceleration
- real_time
- depth_image
- gait_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Real-Time Polygonal Semantic Mapping for Humanoid Robot Stair Climbing
  url: https://arxiv.org/abs/2411.01919
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Humanoid robots need accurate, real-time planar semantic maps to select stable footholds on complex terrain such as stairs. The paper presents a complete system whose inputs are depth images and robot pose estimates from odometry or SLAM, and whose output is a globally consistent polygonal planar semantic map directly usable for gait planning. The pipeline transfers depth images to the GPU, applies anisotropic diffusion filtering, computes normal vectors with the Sobel operator and camera intrinsics, extracts and simplifies contours into polygons, fits a plane per polygon using RANSAC, and incrementally merges the polygons into a global map while compensating vertical odometric drift with a Kalman filter. Experiments on a staircase model report an average step-height error of about 2.1 mm, a plane normal angle standard deviation near 0.44°, IOU around 0.93, and single-frame runtimes below 15 ms at both 320×240 and 640×480 resolutions. The method is also compared against the GPU elevation-mapping implementation EM cupy and is integrated with a humanoid gait planner for stair-climbing simulation in Choreonoid.

## Key Contributions

- Real-time polygonal planar semantic mapping framework specifically designed for humanoid robot stair climbing.
- GPU-accelerated anisotropic diffusion filtering of depth images for edge-preserving denoising prior to normal-vector calculation.
- GPU-parallelized RANSAC plane extraction and fitting that keeps single-frame processing above 30 Hz.
- Incremental polygon integration with Kalman-filter-based compensation of vertical odometric drift.
- Validation through accuracy benchmarks, runtime profiling, comparison with elevation mapping, and humanoid gait-planning simulation.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it addresses the specific need for large, stable planar foothold regions during stair climbing. By extracting accurate polygonal planes and maintaining a consistent global map in real time, the system supports safe foothold selection and gait planning. The authors integrate the semantic map with a walking-pattern generator and whole-body admittance control to simulate stair climbing, demonstrating the practical application of the mapping output to humanoid locomotion.
