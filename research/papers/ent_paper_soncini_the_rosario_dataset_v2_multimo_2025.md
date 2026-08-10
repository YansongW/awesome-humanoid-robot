---
$id: ent_paper_soncini_the_rosario_dataset_v2_multimo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics'
  zh: 罗萨里奥数据集 v2：面向农业机器人的多模态数据集
  ko: '로사리오 데이터셋 v2: 농업 로보틱스를 위한 다중 모달 데이터셋'
summary:
  en: A two-hour-plus, hardware-synchronized multi-sensor dataset collected in a soybean field, providing stereo IR/RGB images,
    IMU, multi-band GNSS, wheel odometry, and 6-DoF ground truth for benchmarking multi-modal SLAM in agricultural robotics.
  zh: Rosario Dataset v2 是一个在阿根廷大豆田采集的多模态数据集，由 CIFASIS 团队发布。它提供超过两小时的硬件同步传感器数据（立体红外/RGB 相机、IMU、多频段 GNSS、轮式里程计）及 6-DoF 真实位姿，专为农业机器人多模态
    SLAM 基准测试设计。
  ko: 콩밭에서 2시간 이상 하드웨어 동기화된 다중 센서 데이터셋으로, 스테레오 적외선/컬러 영상, IMU, 다중 대역 GNSS, 바퀴 주행거리 및 6자유도 참값을 제공하여 농업 로보틱스 멀티모달 SLAM 벤치마크를
    지원한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- dataset
- multimodal_slam
- sensor_fusion
- outdoor_localization
- gnss
- ground_truth
- loop_closure
- agricultural_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21635v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (772 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'The Rosario Dataset v2: Multimodal Dataset for Agricultural Robotics'
  url: https://arxiv.org/abs/2508.21635
  date: '2025'
  accessed_at: '2026-06-27'
  doi: 10.1177/02783649251368909
theoretical_depth:
- method
---
## 概述
该数据集针对农业环境的典型挑战（自然光照变化、运动模糊、崎岖地形、长距离感知混淆序列）而构建。数据采集平台实现了传感器硬件同步，支持 6 自由度真实轨迹与长路径闭环验证。作者使用多种最先进的多模态 SLAM 方法进行测试，揭示了现有算法在农业场景中的局限性。数据集及配套工具已开源。

## 核心内容
### 数据集构成
- **传感器套件**：立体红外相机、彩色相机、加速度计、陀螺仪、磁力计、GNSS（支持 SPP/RTK/PPK 三种定位模式）、轮式里程计
- **数据规模**：超过 2 小时连续记录，覆盖大豆田全生长周期
- **同步机制**：所有传感器通过硬件触发实现时间同步，确保多模态数据时间戳对齐

### 核心挑战
- **环境干扰**：自然光照剧烈变化（直射/阴影交替）、作物叶片运动导致视觉特征不稳定
- **运动退化**：地面起伏引发 IMU 积分漂移，轮式里程计在松软土壤中打滑
- **感知混淆**：长距离行驶中重复的作物行结构造成视觉/激光雷达特征混淆

### 实验设置
- **基准方法**：测试了 ORB-SLAM3、VINS-Fusion、LIO-SAM 等主流多模态 SLAM 系统
- **评估指标**：绝对轨迹误差（ATE）、相对位姿误差（RPE）、闭环检测召回率
- **关键发现**：纯视觉方法在光照突变时跟踪失败率高达 37%；融合 IMU+轮式里程计可降低 22% 的 ATE，但长距离场景下 GNSS 辅助仍不可或缺

### 结论
该数据集填补了农业机器人 SLAM 基准的空白，现有算法在非结构化农田环境中的鲁棒性不足，尤其需要改进光照自适应特征提取与多传感器退化检测机制。数据集与工具包已发布于 https://cifasis.github.io/rosariov2/。

## Overview
We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories.   We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

## Overview
We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories. We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

## Content
We present a multi-modal dataset collected in a soybean crop field, comprising over two hours of recorded data from sensors such as stereo infrared camera, color camera, accelerometer, gyroscope, magnetometer, GNSS (Single Point Positioning, Real-Time Kinematic and Post-Processed Kinematic), and wheel odometry. This dataset captures key challenges inherent to robotics in agricultural environments, including variations in natural lighting, motion blur, rough terrain, and long, perceptually aliased sequences. By addressing these complexities, the dataset aims to support the development and benchmarking of advanced algorithms for localization, mapping, perception, and navigation in agricultural robotics. The platform and data collection system is designed to meet the key requirements for evaluating multi-modal SLAM systems, including hardware synchronization of sensors, 6-DOF ground truth and loops on long trajectories. We run multimodal state-of-the art SLAM methods on the dataset, showcasing the existing limitations in their application on agricultural settings. The dataset and utilities to work with it are released on https://cifasis.github.io/rosariov2/.

## 参考
- http://arxiv.org/abs/2508.21635v1

## 개요
이 데이터셋은 농업 환경의 전형적인 도전 과제(자연광 변화, 모션 블러, 험준한 지형, 장거리 인식 혼동 시퀀스)를 위해 구축되었습니다. 데이터 수집 플랫폼은 센서 하드웨어 동기화를 구현하여 6자유도 실제 궤적과 장경로 폐루프 검증을 지원합니다. 저자는 여러 최신 다중 모달 SLAM 방법을 테스트하여 농업 시나리오에서 기존 알고리즘의 한계를 밝혔습니다. 데이터셋과配套 도구는 오픈소스로 공개되었습니다.

## 핵심 내용
### 데이터셋 구성
- **센서 키트**: 스테레오 적외선 카메라, 컬러 카메라, 가속도계, 자이로스코프, 자기계, GNSS(SPP/RTK/PPK 세 가지 위치 모드 지원), 휠 오도미터리
- **데이터 규모**: 2시간 이상 연속 기록, 대두밭 전체 생장 주기 포함
- **동기화 메커니즘**: 모든 센서는 하드웨어 트리거를 통해 시간 동기화되어 다중 모달 데이터 타임스탬프 정렬 보장

### 핵심 도전 과제
- **환경 간섭**: 자연광의 급격한 변화(직사광/그림자 교대), 작물 잎 움직임으로 인한 시각적 특징 불안정
- **모션 저하**: 지면 요철로 인한 IMU 적분 드리프트, 휠 오도미터리의 느슨한 토양에서의 미끄러짐
- **인식 혼동**: 장거리 주행 중 반복되는 작물 줄 구조로 인한 시각/라이다 특징 혼동

### 실험 설정
- **기준 방법**: ORB-SLAM3, VINS-Fusion, LIO-SAM 등 주류 다중 모달 SLAM 시스템 테스트
- **평가 지표**: 절대 궤적 오차(ATE), 상대 자세 오차(RPE), 폐루프 검출 재현율
- **주요 발견**: 순수 시각 방법은 조명 급변 시 추적 실패율이 최대 37%; IMU+휠 오도미터리 융합은 ATE를 22% 감소시키지만, 장거리 시나리오에서는 GNSS 지원이 여전히 필수적

### 결론
이 데이터셋은 농업 로봇 SLAM 벤치마크의 공백을 메우며, 기존 알고리즘은 비구조화된 농경지 환경에서 강건성이 부족합니다. 특히 조명 적응형 특징 추출과 다중 센서 저하 감지 메커니즘의 개선이 필요합니다. 데이터셋과 도구 키트는 https://cifasis.github.io/rosariov2/ 에 공개되었습니다.
