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

## Overview
We present a novel algorithm for real-time planar semantic mapping tailored for humanoid robots navigating complex terrains such as staircases. Our method is adaptable to any odometry input and leverages GPU-accelerated processes for planar extraction, enabling the rapid generation of globally consistent semantic maps. We utilize an anisotropic diffusion filter on depth images to effectively minimize noise from gradient jumps while preserving essential edge details, enhancing normal vector images' accuracy and smoothness. Both the anisotropic diffusion and the RANSAC-based plane extraction processes are optimized for parallel processing on GPUs, significantly enhancing computational efficiency. Our approach achieves real-time performance, processing single frames at rates exceeding $30~Hz$, which facilitates detailed plane extraction and map management swiftly and efficiently. Extensive testing underscores the algorithm's capabilities in real-time scenarios and demonstrates its practical application in humanoid robot gait planning, significantly improving its ability to navigate dynamic environments.

## Content
We present a novel algorithm for real-time planar semantic mapping tailored for humanoid robots navigating complex terrains such as staircases. Our method is adaptable to any odometry input and leverages GPU-accelerated processes for planar extraction, enabling the rapid generation of globally consistent semantic maps. We utilize an anisotropic diffusion filter on depth images to effectively minimize noise from gradient jumps while preserving essential edge details, enhancing normal vector images' accuracy and smoothness. Both the anisotropic diffusion and the RANSAC-based plane extraction processes are optimized for parallel processing on GPUs, significantly enhancing computational efficiency. Our approach achieves real-time performance, processing single frames at rates exceeding $30~Hz$, which facilitates detailed plane extraction and map management swiftly and efficiently. Extensive testing underscores the algorithm's capabilities in real-time scenarios and demonstrates its practical application in humanoid robot gait planning, significantly improving its ability to navigate dynamic environments.

## 개요
본 논문에서는 계단과 같은 복잡한 지형을 탐색하는 휴머노이드 로봇을 위한 실시간 평면 의미론적 매핑 알고리즘을 제시합니다. 본 방법은 모든 오도메트리 입력에 적응 가능하며, GPU 가속 프로세스를 활용한 평면 추출을 통해 전역적으로 일관된 의미론적 맵을 신속하게 생성할 수 있습니다. 깊이 이미지에 이방성 확산 필터를 적용하여 그래디언트 점프로 인한 노이즈를 효과적으로 최소화하면서 필수적인 에지 세부 정보를 보존하고, 법선 벡터 이미지의 정확성과 부드러움을 향상시킵니다. 이방성 확산과 RANSAC 기반 평면 추출 프로세스는 모두 GPU에서 병렬 처리를 위해 최적화되어 계산 효율성을 크게 향상시킵니다. 본 접근 방식은 초당 $30~Hz$를 초과하는 속도로 단일 프레임을 처리하는 실시간 성능을 달성하여, 세부 평면 추출과 맵 관리를 신속하고 효율적으로 수행합니다. 광범위한 테스트를 통해 실시간 시나리오에서 알고리즘의 성능을 입증하고, 휴머노이드 로봇 보행 계획에 실용적으로 적용되어 동적 환경 탐색 능력을 크게 개선함을 보여줍니다.

## 핵심 내용
본 논문에서는 계단과 같은 복잡한 지형을 탐색하는 휴머노이드 로봇을 위한 실시간 평면 의미론적 매핑 알고리즘을 제시합니다. 본 방법은 모든 오도메트리 입력에 적응 가능하며, GPU 가속 프로세스를 활용한 평면 추출을 통해 전역적으로 일관된 의미론적 맵을 신속하게 생성할 수 있습니다. 깊이 이미지에 이방성 확산 필터를 적용하여 그래디언트 점프로 인한 노이즈를 효과적으로 최소화하면서 필수적인 에지 세부 정보를 보존하고, 법선 벡터 이미지의 정확성과 부드러움을 향상시킵니다. 이방성 확산과 RANSAC 기반 평면 추출 프로세스는 모두 GPU에서 병렬 처리를 위해 최적화되어 계산 효율성을 크게 향상시킵니다. 본 접근 방식은 초당 $30~Hz$를 초과하는 속도로 단일 프레임을 처리하는 실시간 성능을 달성하여, 세부 평면 추출과 맵 관리를 신속하고 효율적으로 수행합니다. 광범위한 테스트를 통해 실시간 시나리오에서 알고리즘의 성능을 입증하고, 휴머노이드 로봇 보행 계획에 실용적으로 적용되어 동적 환경 탐색 능력을 크게 개선함을 보여줍니다.
