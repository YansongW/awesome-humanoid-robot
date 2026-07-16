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

