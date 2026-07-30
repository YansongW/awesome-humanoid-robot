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
  zh: 本文提出一种基于多层感知机（MLP）的完整性监视器，用于视觉地点识别（VPR）系统，将匹配结果分类为可容忍或不可容忍，并集成到两种实时机器人导航方法中。该方法在Clearpath Jackal平台上于室内外环境测试，显著降低了导航误差并提升了任务成功率。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.08162v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
针对VPR系统定位估计完整性不足影响导航决策的问题，本文引入MLP完整性监视器替代传统SVM分类器，无需逐环境训练且减少手动调参。通过两种实时验证方法进行实验：单查询拒绝法（实验1）将沿轨迹目标误差从约9.8米降至约3.1米，任务完成率从约41%提升至55%；历史查询法（实验2）将沿轨迹定位误差从约2.0米降至0.5米，定位精度从约97%提升至99%。结果证明VPR完整性监视器在实际机器人导航中具有实用价值。

## 核心内容
### 方法架构
- 提出MLP完整性监视器，输入VPR匹配特征，输出二分类结果（in-tolerance/out-of-tolerance），替代传统SVM分类器。
- 优势：无需针对不同环境重新训练，减少手动调参，提升泛化能力。

### 实验设置
- 平台：Clearpath Jackal机器人，在室内外混合环境进行真实世界实验。
- 两种导航方法：
  - **实验1（单查询拒绝法）**：机器人导航至目标区域时，若当前VPR匹配被判定为out-of-tolerance则拒绝该估计，仅采用in-tolerance匹配进行导航。
  - **实验2（历史查询法）**：从近期轨迹中选取最佳已验证匹配，结合里程计外推当前位姿估计。

### 关键结果
- **实验1**：
  - 沿轨迹目标误差均值：从~9.8米降至~3.1米（降低68%）。
  - 任务完成率：从~41%提升至~55%（提升34%）。
- **实验2**：
  - 沿轨迹定位误差均值：从~2.0米降至~0.5米（降低75%）。
  - 定位精度：从~97%提升至~99%（提升2个百分点）。

### 结论
- MLP完整性监视器在实际机器人导航中有效提升VPR定位可靠性，减少导航失败风险。
- 方法无需环境特定训练，具备良好可迁移性，适用于动态场景。

## Overview
Visual Place Recognition (VPR) systems often have imperfect performance, affecting the `integrity' of position estimates and subsequent robot navigation decisions. Previously, SVM classifiers have been used to monitor VPR integrity. This research introduces a novel Multi-Layer Perceptron (MLP) integrity monitor which demonstrates improved performance and generalizability, removing per-environment training and reducing manual tuning requirements. We test our proposed system in extensive real-world experiments, presenting two real-time integrity-based VPR verification methods: a single-query rejection method for robot navigation to a goal zone (Experiment 1); and a history-of-queries method that takes a best, verified, match from its recent trajectory and uses an odometer to extrapolate a current position estimate (Experiment 2). Noteworthy results for Experiment 1 include a decrease in aggregate mean along-track goal error from ~9.8m to ~3.1m, and an increase in the aggregate rate of successful mission completion from ~41% to ~55%. Experiment 2 showed a decrease in aggregate mean along-track localization error from ~2.0m to ~0.5m, and an increase in the aggregate localization precision from ~97% to ~99%. Overall, our results demonstrate the practical usefulness of a VPR integrity monitor in real-world robotics to improve VPR localization and consequent navigation performance.

## 개요
Visual Place Recognition (VPR) 시스템은 종종 불완전한 성능을 보여 위치 추정의 '무결성'과 이후 로봇 내비게이션 결정에 영향을 미칩니다. 이전에는 SVM 분류기가 VPR 무결성을 모니터링하는 데 사용되었습니다. 본 연구는 환경별 학습을 제거하고 수동 튜닝 요구 사항을 줄여 개선된 성능과 일반화 능력을 보여주는 새로운 Multi-Layer Perceptron (MLP) 무결성 모니터를 소개합니다. 제안된 시스템을 광범위한 실제 실험에서 테스트하며, 두 가지 실시간 무결성 기반 VPR 검증 방법을 제시합니다: 목표 구역으로의 로봇 내비게이션을 위한 단일 쿼리 거부 방법 (실험 1); 그리고 최근 궤적에서 최적의 검증된 매칭을 취하고 주행 거리계를 사용하여 현재 위치 추정을 외삽하는 쿼리 이력 방법 (실험 2). 실험 1의 주목할 만한 결과로는 집계 평균 경로 목표 오차가 약 9.8m에서 약 3.1m로 감소하고, 집계 성공 임무 완료율이 약 41%에서 약 55%로 증가한 점이 포함됩니다. 실험 2는 집계 평균 경로 위치 추정 오차가 약 2.0m에서 약 0.5m로 감소하고, 집계 위치 추정 정밀도가 약 97%에서 약 99%로 증가한 것을 보여주었습니다. 전반적으로, 본 연구 결과는 실제 로봇 공학에서 VPR 무결성 모니터가 VPR 위치 추정 및 결과적인 내비게이션 성능을 개선하는 실용적 유용성을 입증합니다.

## 핵심 내용
Visual Place Recognition (VPR) 시스템은 종종 불완전한 성능을 보여 위치 추정의 '무결성'과 이후 로봇 내비게이션 결정에 영향을 미칩니다. 이전에는 SVM 분류기가 VPR 무결성을 모니터링하는 데 사용되었습니다. 본 연구는 환경별 학습을 제거하고 수동 튜닝 요구 사항을 줄여 개선된 성능과 일반화 능력을 보여주는 새로운 Multi-Layer Perceptron (MLP) 무결성 모니터를 소개합니다. 제안된 시스템을 광범위한 실제 실험에서 테스트하며, 두 가지 실시간 무결성 기반 VPR 검증 방법을 제시합니다: 목표 구역으로의 로봇 내비게이션을 위한 단일 쿼리 거부 방법 (실험 1); 그리고 최근 궤적에서 최적의 검증된 매칭을 취하고 주행 거리계를 사용하여 현재 위치 추정을 외삽하는 쿼리 이력 방법 (실험 2). 실험 1의 주목할 만한 결과로는 집계 평균 경로 목표 오차가 약 9.8m에서 약 3.1m로 감소하고, 집계 성공 임무 완료율이 약 41%에서 약 55%로 증가한 점이 포함됩니다. 실험 2는 집계 평균 경로 위치 추정 오차가 약 2.0m에서 약 0.5m로 감소하고, 집계 위치 추정 정밀도가 약 97%에서 약 99%로 증가한 것을 보여주었습니다. 전반적으로, 본 연구 결과는 실제 로봇 공학에서 VPR 무결성 모니터가 VPR 위치 추정 및 결과적인 내비게이션 성능을 개선하는 실용적 유용성을 입증합니다.

## 参考
- http://arxiv.org/abs/2407.08162v2
