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
  zh: 本文提出一种面向人形机器人爬楼梯场景的实时多边形平面语义建图系统，通过GPU加速的各向异性扩散滤波、Sobel法线估计、多边形轮廓提取、RANSAC平面拟合及卡尔曼滤波垂直漂移补偿，实现单帧处理频率超过30 Hz。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.01919v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (625 chars, DeepSeek).'
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
该系统专为人形机器人在楼梯等复杂地形中导航设计，可适配任意里程计输入。核心创新在于利用GPU并行加速各向异性扩散滤波与RANSAC平面提取，在抑制深度图像梯度跳变噪声的同时保留边缘细节，从而提升法线图像的精度与平滑度。通过卡尔曼滤波补偿垂直方向漂移，系统能快速生成全局一致的语义地图，并在实时场景测试中验证了其在步态规划中的实用价值。

## 核心内容
### 方法架构
- **预处理阶段**：对深度图像应用各向异性扩散滤波，有效抑制梯度跳变噪声，同时保留关键边缘细节，为后续法线估计提供高质量输入。
- **法线估计**：采用Sobel算子进行法线计算，结合滤波后的深度数据生成平滑的法线图像。
- **平面提取**：通过多边形轮廓提取与RANSAC平面拟合，从法线图像中识别平面区域，所有计算均在GPU上并行加速。
- **漂移补偿**：引入卡尔曼滤波器对垂直方向漂移进行实时补偿，确保地图的全局一致性。

### 实验设置与关键数字
- **性能指标**：单帧处理频率超过30 Hz，满足实时性要求。
- **硬件平台**：依赖GPU加速，具体型号未明确，但强调并行优化对计算效率的提升。
- **测试场景**：在楼梯等复杂地形中验证，重点评估平面提取的准确性与地图更新的速度。

### 结论
该系统在实时性（>30 Hz）与鲁棒性上表现突出，能有效支持人形机器人在动态环境中的步态规划。未来可进一步扩展至更复杂的非结构化地形。

## Overview
We present a novel algorithm for real-time planar semantic mapping tailored for humanoid robots navigating complex terrains such as staircases. Our method is adaptable to any odometry input and leverages GPU-accelerated processes for planar extraction, enabling the rapid generation of globally consistent semantic maps. We utilize an anisotropic diffusion filter on depth images to effectively minimize noise from gradient jumps while preserving essential edge details, enhancing normal vector images' accuracy and smoothness. Both the anisotropic diffusion and the RANSAC-based plane extraction processes are optimized for parallel processing on GPUs, significantly enhancing computational efficiency. Our approach achieves real-time performance, processing single frames at rates exceeding $30~Hz$, which facilitates detailed plane extraction and map management swiftly and efficiently. Extensive testing underscores the algorithm's capabilities in real-time scenarios and demonstrates its practical application in humanoid robot gait planning, significantly improving its ability to navigate dynamic environments.

## 参考
- http://arxiv.org/abs/2411.01919v1

## 개요
이 시스템은 인간형 로봇이 계단과 같은 복잡한 지형에서 내비게이션할 수 있도록 설계되었으며, 임의의 오도메트리 입력에 적응할 수 있습니다. 핵심 혁신은 GPU 병렬 가속을 활용한 이방성 확산 필터링과 RANSAC 평면 추출로, 깊이 이미지의 그래디언트 점프 노이즈를 억제하면서도 가장자리 세부 정보를 보존하여 법선 이미지의 정밀도와 평활도를 향상시키는 데 있습니다. 칼만 필터를 통해 수직 방향 드리프트를 보정함으로써, 시스템은 전역적으로 일관된 의미론적 지도를 빠르게 생성할 수 있으며, 실시간 시나리오 테스트에서 보행 계획에 대한 실용적 가치를 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **전처리 단계**: 깊이 이미지에 이방성 확산 필터링을 적용하여 그래디언트 점프 노이즈를 효과적으로 억제하면서도 핵심 가장자리 세부 정보를 보존하여, 이후의 법선 추정에 고품질 입력을 제공합니다.
- **법선 추정**: Sobel 연산자를 사용하여 법선을 계산하고, 필터링된 깊이 데이터를 결합하여 평활한 법선 이미지를 생성합니다.
- **평면 추출**: 다각형 윤곽 추출과 RANSAC 평면 피팅을 통해 법선 이미지에서 평면 영역을 식별하며, 모든 계산은 GPU에서 병렬로 가속화됩니다.
- **드리프트 보정**: 칼만 필터를 도입하여 수직 방향 드리프트를 실시간으로 보정하여 지도의 전역적 일관성을 보장합니다.

### 실험 설정 및 주요 수치
- **성능 지표**: 단일 프레임 처리 주파수가 30 Hz를 초과하여 실시간 요구 사항을 충족합니다.
- **하드웨어 플랫폼**: GPU 가속에 의존하며, 구체적인 모델은 명시되지 않았지만 병렬 최적화가 계산 효율성 향상에 미치는 영향을 강조합니다.
- **테스트 시나리오**: 계단과 같은 복잡한 지형에서 검증되었으며, 평면 추출의 정확성과 지도 업데이트 속도를 중점적으로 평가합니다.

### 결론
이 시스템은 실시간성(>30 Hz)과 견고성에서 뛰어난 성능을 보여주며, 동적 환경에서 인간형 로봇의 보행 계획을 효과적으로 지원할 수 있습니다. 향후 더 복잡한 비구조적 지형으로 확장할 수 있습니다.
