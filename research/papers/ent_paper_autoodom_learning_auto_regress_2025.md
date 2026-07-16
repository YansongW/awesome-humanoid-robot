---
$id: ent_paper_autoodom_learning_auto_regress_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  zh: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
summary:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
  zh: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autoodom
- humanoid
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18857v1.
sources:
- id: src_001
  type: paper
  title: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2511.18857
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 核心内容
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 参考
- http://arxiv.org/abs/2511.18857v1

## Overview
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## Content
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 개요
정확한 고유수용성 오도메트리는 GPS가 차단되고 시각 정보가 저하된 환경에서 기존의 시각 오도메트리 시스템이 실패하는 상황에서 보행 로봇의 항법에 필수적입니다. 현재 접근 방식은 중요한 한계에 직면해 있습니다. 분석적 필터링 방법은 모델링 불확실성과 누적 드리프트로 어려움을 겪고, 하이브리드 학습-필터링 접근 방식은 분석적 구성 요소에 의해 제약을 받으며, 순수 학습 기반 방법은 시뮬레이션-현실 전환에 어려움을 겪고 광범위한 실제 데이터 수집을 요구합니다. 본 논문은 혁신적인 2단계 훈련 패러다임을 통해 이러한 문제를 극복하는 새로운 자기회귀 고유수용성 오도메트리 시스템인 AutoOdom을 소개합니다. 1단계는 대규모 시뮬레이션 데이터를 사용하여 보행 운동에 내재된 복잡한 비선형 동역학과 빠르게 변화하는 접촉 상태를 학습하고, 2단계는 제한된 실제 데이터를 사용하여 자기회귀 향상 메커니즘을 도입하여 시뮬레이션-현실 간극을 효과적으로 연결합니다. 핵심 혁신은 모델이 자체 예측으로부터 학습하여 센서 잡음에 대한 탄력성을 개발하고 고도로 동적인 환경에서 견고성을 향상시키는 자기회귀 훈련 접근 방식에 있습니다. Booster T1 휴머노이드 로봇에 대한 포괄적인 실험 검증을 통해 AutoOdom이 모든 평가 지표에서 최첨단 방법을 크게 능가하며, Legolas 기준선 대비 절대 궤적 오차에서 57.2%, Umeyama 정렬 오차에서 59.2%, 상대 자세 오차에서 36.2%의 개선을 달성함을 입증했습니다. 광범위한 절제 연구는 센서 모달리티 선택과 시간적 모델링에 대한 중요한 통찰력을 제공하며, IMU 가속도 데이터에 대한 반직관적인 발견을 밝혀내고 까다로운 보행 시나리오에서 강력한 고유수용성 오도메트리를 위한 체계적인 설계 선택을 검증합니다.

## 핵심 내용
정확한 고유수용성 오도메트리는 GPS가 차단되고 시각 정보가 저하된 환경에서 기존의 시각 오도메트리 시스템이 실패하는 상황에서 보행 로봇의 항법에 필수적입니다. 현재 접근 방식은 중요한 한계에 직면해 있습니다. 분석적 필터링 방법은 모델링 불확실성과 누적 드리프트로 어려움을 겪고, 하이브리드 학습-필터링 접근 방식은 분석적 구성 요소에 의해 제약을 받으며, 순수 학습 기반 방법은 시뮬레이션-현실 전환에 어려움을 겪고 광범위한 실제 데이터 수집을 요구합니다. 본 논문은 혁신적인 2단계 훈련 패러다임을 통해 이러한 문제를 극복하는 새로운 자기회귀 고유수용성 오도메트리 시스템인 AutoOdom을 소개합니다. 1단계는 대규모 시뮬레이션 데이터를 사용하여 보행 운동에 내재된 복잡한 비선형 동역학과 빠르게 변화하는 접촉 상태를 학습하고, 2단계는 제한된 실제 데이터를 사용하여 자기회귀 향상 메커니즘을 도입하여 시뮬레이션-현실 간극을 효과적으로 연결합니다. 핵심 혁신은 모델이 자체 예측으로부터 학습하여 센서 잡음에 대한 탄력성을 개발하고 고도로 동적인 환경에서 견고성을 향상시키는 자기회귀 훈련 접근 방식에 있습니다. Booster T1 휴머노이드 로봇에 대한 포괄적인 실험 검증을 통해 AutoOdom이 모든 평가 지표에서 최첨단 방법을 크게 능가하며, Legolas 기준선 대비 절대 궤적 오차에서 57.2%, Umeyama 정렬 오차에서 59.2%, 상대 자세 오차에서 36.2%의 개선을 달성함을 입증했습니다. 광범위한 절제 연구는 센서 모달리티 선택과 시간적 모델링에 대한 중요한 통찰력을 제공하며, IMU 가속도 데이터에 대한 반직관적인 발견을 밝혀내고 까다로운 보행 시나리오에서 강력한 고유수용성 오도메트리를 위한 체계적인 설계 선택을 검증합니다.
