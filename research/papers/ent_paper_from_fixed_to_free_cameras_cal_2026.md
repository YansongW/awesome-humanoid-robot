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
  zh: 'arXiv:2607.05396v1 Announce Type: cross Abstract: Real-world robot deployment rarely maintains the training-stage camera
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05396v1.
sources:
- id: src_001
  type: paper
  title: 'From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.05396
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## 核心内容
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## 参考
- http://arxiv.org/abs/2607.05396v1

## Overview
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles *how I should move* in pose-independent camera-centric action generation from *where I am looking from* in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## Content
Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles *how I should move* in pose-independent camera-centric action generation from *where I am looking from* in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

## 개요
실제 로봇 배포 환경에서는 훈련 단계의 카메라 설정이 유지되는 경우가 드물며, 실제 시나리오에 따라 카메라가 재배치되거나 재장착되는 경우가 많습니다. 기존의 시점 강건 비전-언어-행동(VLA) 정책은 카메라 외부 파라미터가 명시적으로 제공될 때만 이러한 카메라 변화를 허용하므로, 특히 시점 강건성이 중요한 경우 취약하고 사용하기 어렵습니다. 우리는 정책이 카메라의 위치를 알려받는 것이 아니라 스스로 파악해야 한다고 주장합니다. 이를 위해, 우리는 조작 제어를 카메라 기하학으로부터 분리하는 새로운 VLA 모델인 Camera-Centric VLA(CamVLA)를 소개합니다. 이 모델은 (i) 로컬 카메라 프레임으로 표현된 카메라 중심 엔드 이펙터 동작과 (ii) 카메라와 로봇 베이스를 연결하는 6-DoF 핸드-아이 행렬을 예측합니다. 결정론적 기하 변환을 통해 두 예측을 로봇 베이스 프레임 동작으로 구성합니다. 이는 자세 독립적인 카메라 중심 동작 생성에서 '어떻게 움직여야 하는지'와 카메라 관점의 기하학적 기반에서 '어디를 보고 있는지'를 분리합니다. 결과 정책은 캘리브레이션, 깊이 정보, 단일 시점이 필요 없으며, 배포 시 시각적 관찰과 작업 명령으로 단일 모노 RGB 이미지만 필요로 합니다. 시뮬레이션과 실제 로봇 데이터 모두에서의 평가는 CamVLA가 다양한 미지의 시점에서 성공률을 일관되게 향상시킴을 보여줍니다. 프로젝트 페이지: https://alibaba-damo-academy.github.io/CamVLA/.

## 핵심 내용
실제 로봇 배포 환경에서는 훈련 단계의 카메라 설정이 유지되는 경우가 드물며, 실제 시나리오에 따라 카메라가 재배치되거나 재장착되는 경우가 많습니다. 기존의 시점 강건 비전-언어-행동(VLA) 정책은 카메라 외부 파라미터가 명시적으로 제공될 때만 이러한 카메라 변화를 허용하므로, 특히 시점 강건성이 중요한 경우 취약하고 사용하기 어렵습니다. 우리는 정책이 카메라의 위치를 알려받는 것이 아니라 스스로 파악해야 한다고 주장합니다. 이를 위해, 우리는 조작 제어를 카메라 기하학으로부터 분리하는 새로운 VLA 모델인 Camera-Centric VLA(CamVLA)를 소개합니다. 이 모델은 (i) 로컬 카메라 프레임으로 표현된 카메라 중심 엔드 이펙터 동작과 (ii) 카메라와 로봇 베이스를 연결하는 6-DoF 핸드-아이 행렬을 예측합니다. 결정론적 기하 변환을 통해 두 예측을 로봇 베이스 프레임 동작으로 구성합니다. 이는 자세 독립적인 카메라 중심 동작 생성에서 '어떻게 움직여야 하는지'와 카메라 관점의 기하학적 기반에서 '어디를 보고 있는지'를 분리합니다. 결과 정책은 캘리브레이션, 깊이 정보, 단일 시점이 필요 없으며, 배포 시 시각적 관찰과 작업 명령으로 단일 모노 RGB 이미지만 필요로 합니다. 시뮬레이션과 실제 로봇 데이터 모두에서의 평가는 CamVLA가 다양한 미지의 시점에서 성공률을 일관되게 향상시킴을 보여줍니다. 프로젝트 페이지: https://alibaba-damo-academy.github.io/CamVLA/.
