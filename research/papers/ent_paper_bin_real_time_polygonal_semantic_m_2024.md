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
  en: This paper proposes a real-time polygonal planar semantic mapping system for humanoid robot stair climbing, combining
    GPU-accelerated anisotropic diffusion filtering, Sobel-based normal estimation, polygonal contour extraction, RANSAC plane
    fitting, and Kalman-filter vertical drift compensation, achieving single-frame processing above 30 Hz.
  zh: 本文提出了一种面向人形机器人楼梯攀爬的实时多边形平面语义建图系统，结合了 GPU 加速的各向异性扩散滤波、Sobel 法向量估计、多边形轮廓提取、RANSAC 平面拟合以及卡尔曼滤波垂直漂移补偿，单帧处理速度超过 30 Hz。
  ko: 본 논문은 인간형 로봇 계단 등반을 위한 실시간 다각형 평면 의미 지도 작성 시스템을 제안한다. GPU 가속 이방성 확산 필터링, Sobel 기반 법선 추정, 다각형 윤곽 추출, RANSAC 평면 적합, 그리고
    칼만 필터 수직 드리프트 보정을 결합하여 단일 프레임 처리 속도가 30 Hz 이상이다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.01919v1.
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
## 概述
We present a novel algorithm for real-time planar semantic mapping tailored for humanoid robots navigating complex terrains such as staircases. Our method is adaptable to any odometry input and leverages GPU-accelerated processes for planar extraction, enabling the rapid generation of globally consistent semantic maps. We utilize an anisotropic diffusion filter on depth images to effectively minimize noise from gradient jumps while preserving essential edge details, enhancing normal vector images' accuracy and smoothness. Both the anisotropic diffusion and the RANSAC-based plane extraction processes are optimized for parallel processing on GPUs, significantly enhancing computational efficiency. Our approach achieves real-time performance, processing single frames at rates exceeding $30~Hz$, which facilitates detailed plane extraction and map management swiftly and efficiently. Extensive testing underscores the algorithm's capabilities in real-time scenarios and demonstrates its practical application in humanoid robot gait planning, significantly improving its ability to navigate dynamic environments.

## 核心内容
We present a novel algorithm for real-time planar semantic mapping tailored for humanoid robots navigating complex terrains such as staircases. Our method is adaptable to any odometry input and leverages GPU-accelerated processes for planar extraction, enabling the rapid generation of globally consistent semantic maps. We utilize an anisotropic diffusion filter on depth images to effectively minimize noise from gradient jumps while preserving essential edge details, enhancing normal vector images' accuracy and smoothness. Both the anisotropic diffusion and the RANSAC-based plane extraction processes are optimized for parallel processing on GPUs, significantly enhancing computational efficiency. Our approach achieves real-time performance, processing single frames at rates exceeding $30~Hz$, which facilitates detailed plane extraction and map management swiftly and efficiently. Extensive testing underscores the algorithm's capabilities in real-time scenarios and demonstrates its practical application in humanoid robot gait planning, significantly improving its ability to navigate dynamic environments.

## 参考
- http://arxiv.org/abs/2411.01919v1

