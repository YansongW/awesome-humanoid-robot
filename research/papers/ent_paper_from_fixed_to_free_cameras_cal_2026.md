---
$id: ent_paper_from_fixed_to_free_cameras_cal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model'
  zh: 'From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model'
  ko: 'From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model'
summary:
  en: 'arXiv:2607.05396v1 Announce Type: cross Abstract: Real-world robot deployment rarely maintains the training-stage camera
    setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust
    Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided,
    making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be
    told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a
    new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector
    action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic
    geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move
    in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding.
    The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as
    the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show
    that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.'
  zh: CamVLA 是一种无需标定的视角鲁棒视觉-语言-动作模型，由阿里巴巴达摩院提出。其核心创新在于将机械臂控制与相机几何解耦，通过预测相机坐标系下的末端执行器动作和手眼矩阵，实现仅依赖单目 RGB 图像即可适应任意相机视角的机器人操作。
  ko: 'arXiv:2607.05396v1 Announce Type: cross Abstract: Real-world robot deployment rarely maintains the training-stage camera
    setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust
    Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided,
    making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be
    told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a
    new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector
    action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic
    geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move
    in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding.
    The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as
    the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show
    that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- from_fixed_to_free_cameras
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05396v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (746 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.05396
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有视角鲁棒的 VLA 策略在相机外参变化时表现脆弱，因为它们需要显式提供相机位姿才能工作。CamVLA 通过预测两个关键量——相机坐标系中的末端执行器动作和 6 自由度手眼矩阵——来解耦控制与几何信息，再通过确定性几何变换将其转换为机器人基座坐标系动作。这种设计使策略无需相机标定、无需深度信息、仅需单目 RGB 图像即可在部署时适应任意相机视角。在仿真和真实机器人数据上的实验表明，CamVLA 在多种未见过的视角下均能稳定提升任务成功率。

## 核心内容
### 方法架构
- **核心思想**：将操作控制与相机几何解耦，让策略自主推断相机位置而非被告知。
- **双预测模块**：
  - 预测相机坐标系下的末端执行器动作（camera-centric end-effector action）
  - 预测 6-DoF 手眼矩阵（hand-eye matrix），关联相机与机器人基座
- **几何变换**：通过确定性几何变换将上述两个预测组合为机器人基座坐标系动作，实现“如何移动”（姿态无关的相机中心动作生成）与“从何观察”（相机视角几何定位）的分离。

### 实验设置
- **输入**：仅需单目 RGB 图像和任务指令，无需深度信息或相机标定
- **评估场景**：仿真环境与真实机器人数据，覆盖多种未见过的相机视角
- **对比基线**：现有视角鲁棒 VLA 策略（需显式提供相机外参）

### 关键结果
- CamVLA 在多样化的未见视角下持续提升任务成功率
- 无需标定、无需深度、单视图的特性使其在实际部署中更具鲁棒性和易用性
- 项目页面提供更多细节：https://alibaba-damo-academy.github.io/CamVLA/

## Overview
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## Overview
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles *how I should move* in pose-independent camera-centric action generation from *where I am looking from* in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## Content
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles *how I should move* in pose-independent camera-centric action generation from *where I am looking from* in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## 参考
- http://arxiv.org/abs/2607.05396v1

## 개요
기존의 시점 강건 VLA 정책은 카메라 외부 파라미터가 변경될 때 성능이 취약한데, 이는 카메라 포즈를 명시적으로 제공해야만 작동하기 때문입니다. CamVLA는 카메라 좌표계의 엔드 이펙터 동작과 6자유도 핸드-아이 행렬이라는 두 가지 핵심 수량을 예측하여 제어와 기하 정보를 분리하고, 결정적 기하 변환을 통해 이를 로봇 베이스 좌표계 동작으로 변환합니다. 이 설계는 정책이 카메라 캘리브레이션, 깊이 정보 없이 단안 RGB 이미지만으로 배포 시 임의의 카메라 시점에 적응할 수 있게 합니다. 시뮬레이션 및 실제 로봇 데이터 실험에서 CamVLA는 다양한 미경험 시점에서 작업 성공률을 안정적으로 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 조작 제어와 카메라 기하를 분리하여, 정책이 카메라 위치를 통보받는 대신 자율적으로 추론하도록 합니다.
- **이중 예측 모듈**:
  - 카메라 좌표계의 엔드 이펙터 동작(camera-centric end-effector action) 예측
  - 6-DoF 핸드-아이 행렬(hand-eye matrix) 예측, 카메라와 로봇 베이스 연결
- **기하 변환**: 결정적 기하 변환을 통해 위 두 예측을 로봇 베이스 좌표계 동작으로 결합하여, "어떻게 움직일지"(포즈 독립적인 카메라 중심 동작 생성)와 "어디서 관찰할지"(카메라 시점 기하 위치 파악)를 분리합니다.

### 실험 설정
- **입력**: 단안 RGB 이미지와 작업 지시만 필요, 깊이 정보나 카메라 캘리브레이션 불필요
- **평가 시나리오**: 시뮬레이션 환경 및 실제 로봇 데이터, 다양한 미경험 카메라 시점 포함
- **비교 기준선**: 기존 시점 강건 VLA 정책(카메라 외부 파라미터 명시 제공 필요)

### 주요 결과
- CamVLA는 다양한 미경험 시점에서 작업 성공률을 지속적으로 향상시킵니다.
- 캘리브레이션 불필요, 깊이 불필요, 단일 뷰 특성 덕분에 실제 배포에서 더 강건하고 사용하기 쉽습니다.
- 프로젝트 페이지에서 추가 세부 정보 제공: https://alibaba-damo-academy.github.io/CamVLA/
