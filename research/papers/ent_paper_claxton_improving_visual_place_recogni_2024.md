---
$id: ent_paper_claxton_improving_visual_place_recogni_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Visual Place Recognition Based Robot Navigation By Verifying Localization Estimates
  zh: 通过验证定位估计改进基于视觉地点识别的机器人导航
  ko: 위치 추정 검증을 통한 시각적 장소 인식 기반 로봇 내비게이션 개선
summary:
  en: This paper introduces a Multi-Layer Perceptron (MLP) integrity monitor for Visual Place Recognition (VPR) that classifies
    matches as in-tolerance or out-of-tolerance, and integrates it into two real-time robot navigation methods tested on a
    Clearpath Jackal in indoor and outdoor environments.
  zh: 本文提出了一种用于视觉地点识别（VPR）的多层感知器（MLP）完整性监控器，将匹配分类为容差内或容差外，并将其集成到两种实时机器人导航方法中，在室内和室外环境中使用Clearpath Jackal平台进行了测试。
  ko: 본 논문은 시각적 장소 인식(VPR) 매칭을 허용 오차 내/외로 분류하는 다층 퍼셉트론(MLP) 기반 무결성 모니터를 제안하고, 이를 Clearpath Jackal 플랫폼을 이용해 실내 및 실외 환경에서 테스트한
    두 가지 실시간 로봇 내비게이션 방법에 통합하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.08162v2.
sources:
- id: src_001
  type: paper
  title: Improving Visual Place Recognition Based Robot Navigation By Verifying Localization Estimates
  url: https://arxiv.org/abs/2407.08162
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3483045
theoretical_depth:
- method
---
## 概述
Visual Place Recognition (VPR) systems often have imperfect performance, affecting the `integrity' of position estimates and subsequent robot navigation decisions. Previously, SVM classifiers have been used to monitor VPR integrity. This research introduces a novel Multi-Layer Perceptron (MLP) integrity monitor which demonstrates improved performance and generalizability, removing per-environment training and reducing manual tuning requirements. We test our proposed system in extensive real-world experiments, presenting two real-time integrity-based VPR verification methods: a single-query rejection method for robot navigation to a goal zone (Experiment 1); and a history-of-queries method that takes a best, verified, match from its recent trajectory and uses an odometer to extrapolate a current position estimate (Experiment 2). Noteworthy results for Experiment 1 include a decrease in aggregate mean along-track goal error from ~9.8m to ~3.1m, and an increase in the aggregate rate of successful mission completion from ~41% to ~55%. Experiment 2 showed a decrease in aggregate mean along-track localization error from ~2.0m to ~0.5m, and an increase in the aggregate localization precision from ~97% to ~99%. Overall, our results demonstrate the practical usefulness of a VPR integrity monitor in real-world robotics to improve VPR localization and consequent navigation performance.

## 核心内容
Visual Place Recognition (VPR) systems often have imperfect performance, affecting the `integrity' of position estimates and subsequent robot navigation decisions. Previously, SVM classifiers have been used to monitor VPR integrity. This research introduces a novel Multi-Layer Perceptron (MLP) integrity monitor which demonstrates improved performance and generalizability, removing per-environment training and reducing manual tuning requirements. We test our proposed system in extensive real-world experiments, presenting two real-time integrity-based VPR verification methods: a single-query rejection method for robot navigation to a goal zone (Experiment 1); and a history-of-queries method that takes a best, verified, match from its recent trajectory and uses an odometer to extrapolate a current position estimate (Experiment 2). Noteworthy results for Experiment 1 include a decrease in aggregate mean along-track goal error from ~9.8m to ~3.1m, and an increase in the aggregate rate of successful mission completion from ~41% to ~55%. Experiment 2 showed a decrease in aggregate mean along-track localization error from ~2.0m to ~0.5m, and an increase in the aggregate localization precision from ~97% to ~99%. Overall, our results demonstrate the practical usefulness of a VPR integrity monitor in real-world robotics to improve VPR localization and consequent navigation performance.

## 参考
- http://arxiv.org/abs/2407.08162v2

