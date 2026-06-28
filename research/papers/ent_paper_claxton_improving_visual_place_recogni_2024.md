---
$id: ent_paper_claxton_improving_visual_place_recogni_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Visual Place Recognition Based Robot Navigation By Verifying Localization
    Estimates
  zh: 通过验证定位估计改进基于视觉地点识别的机器人导航
  ko: 위치 추정 검증을 통한 시각적 장소 인식 기반 로봇 내비게이션 개선
summary:
  en: This paper introduces a Multi-Layer Perceptron (MLP) integrity monitor for Visual
    Place Recognition (VPR) that classifies matches as in-tolerance or out-of-tolerance,
    and integrates it into two real-time robot navigation methods tested on a Clearpath
    Jackal in indoor and outdoor environments.
  zh: 本文提出了一种用于视觉地点识别（VPR）的多层感知器（MLP）完整性监控器，将匹配分类为容差内或容差外，并将其集成到两种实时机器人导航方法中，在室内和室外环境中使用Clearpath
    Jackal平台进行了测试。
  ko: 본 논문은 시각적 장소 인식(VPR) 매칭을 허용 오차 내/외로 분류하는 다층 퍼셉트론(MLP) 기반 무결성 모니터를 제안하고, 이를 Clearpath
    Jackal 플랫폼을 이용해 실내 및 실외 환경에서 테스트한 두 가지 실시간 로봇 내비게이션 방법에 통합하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- visual_place_recognition
- vpr_integrity_monitoring
- multi_layer_perceptron
- robot_navigation
- localization_verification
- outdoor_navigation
- indoor_navigation
- ap_gem
- netvlad
- salad
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: Improving Visual Place Recognition Based Robot Navigation By Verifying Localization
    Estimates
  url: https://arxiv.org/abs/2407.08162
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3483045
theoretical_depth:
- method
---

## Overview

Visual Place Recognition (VPR) systems enable robots to localize by matching current camera views against a previously collected reference map, but their matching performance is imperfect and can produce unsafe navigation decisions. This paper proposes a Multi-Layer Perceptron (MLP) integrity monitor that classifies VPR matches as in-tolerance or out-of-tolerance, replacing earlier SVM-based monitors to improve classification performance and cross-environment generalizability. The monitor is integrated into two real-time verification paradigms: a single-query rejection method that prevents bad matches from reaching the navigator, and a history-of-queries method that selects the best verified recent match and extrapolates the current position using wheel encoder odometry.

The authors evaluate the system on a Clearpath Robotics Jackal equipped with an Occam 360 panoramic camera, a Velodyne VLP-16 LiDAR, and wheel encoders, using the VPR descriptors AP-GeM, NetVLAD, and SALAD across the QCR Office, QCR Campus, Nordland, and Oxford RobotCar datasets. Experiment 1 (goal-zone navigation) reduced aggregate mean along-track goal error from approximately 9.8 m to 3.1 m and raised mission completion from approximately 41 % to 55 %. Experiment 2 (history-of-queries localization) reduced aggregate mean along-track localization error from approximately 2.0 m to 0.5 m and increased localization precision from approximately 97 % to 99 %.

A key practical claim is that a single trained MLP monitor can outperform per-environment trained SVMs and fixed-distance thresholds, reducing manual tuning requirements when deploying VPR-based navigation in new environments.

## Key Contributions

- Closed-loop integration of a VPR integrity monitor into active robot navigation for real-time navigational decisions.
- Novel MLP-based VPR integrity monitor that replaces prior SVM approaches and improves performance and cross-environment generalizability.
- History-of-queries method that verifies recent VPR matches and extrapolates the current position from the best verified match using odometry.
- Extensive real-world mobile robot experiments across indoor and outdoor environments using multiple VPR techniques (AP-GeM, NetVLAD, SALAD).
- Demonstration that a single trained MLP monitor outperforms per-environment trained SVMs and fixed-distance thresholds.

## Relevance to Humanoid Robotics

Reliable visual localization is a core requirement for autonomous humanoid robots operating in dynamic, unstructured environments where GNSS may be unavailable or unreliable. The MLP integrity monitor described in this paper addresses the safety-critical problem of detecting incorrect VPR matches before they propagate into navigation decisions, which is directly transferable to humanoid platforms that rely on vision-based localization. Because the monitor removes the need for per-environment training, it could reduce deployment engineering effort for humanoid systems that must adapt quickly to new indoor or outdoor settings. However, the paper's experiments were performed on a wheeled Clearpath Jackal rather than a bipedal humanoid, so humanoid-specific validation—particularly under viewpoint changes caused by camera height variation and gait-induced motion blur—remains to be demonstrated.
