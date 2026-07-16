---
$id: ent_paper_chen_adaptive_robotic_information_g_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Robotic Information Gathering via Non-Stationary Gaussian Processes
  zh: 基于非平稳高斯过程的自适应机器人信息获取
  ko: 비정상 가우시안 프로세스를 통한 적응형 로봇 정보 수집
summary:
  en: This paper proposes the Attentive Kernel (AK), a non-stationary Gaussian Process kernel that uses attention-based input-dependent
    length-scale selection to improve uncertainty quantification for robotic information gathering, validated through elevation
    mapping benchmarks and an autonomous surface vehicle field experiment.
  zh: 本文提出了一种名为Attentive Kernel（AK）的非平稳高斯过程核函数，该函数通过基于注意力的输入相关长度尺度选择来改进机器人信息获取中的不确定性量化，并通过高程映射基准测试和自主水面航行器实地实验进行了验证。
  ko: 본 논문은 주의 기반 입력 의존 길이 척도 선택을 통해 로봇 정보 수집의 불확실성 정량화를 개선하는 비정상 가우시안 프로세스 커널인 Attentive Kernel(AK)을 제안하고, 고도 매핑 벤치마크와 자율
    수상 차량 현장 실험을 통해 검증하였다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gaussian_process
- non_stationary_kernel
- attentive_kernel
- robotic_information_gathering
- uncertainty_quantification
- informative_planning
- elevation_mapping
- autonomous_surface_vehicle
- spatial_modeling
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.01263v3.
sources:
- id: src_001
  type: paper
  title: Adaptive Robotic Information Gathering via Non-Stationary Gaussian Processes
  url: https://arxiv.org/abs/2306.01263
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Robotic Information Gathering (RIG) is a foundational research topic that answers how a robot (team) collects informative data to efficiently build an accurate model of an unknown target function under robot embodiment constraints. RIG has many applications, including but not limited to autonomous exploration and mapping, 3D reconstruction or inspection, search and rescue, and environmental monitoring. A RIG system relies on a probabilistic model's prediction uncertainty to identify critical areas for informative data collection. Gaussian Processes (GPs) with stationary kernels have been widely adopted for spatial modeling. However, real-world spatial data is typically non-stationary -- different locations do not have the same degree of variability. As a result, the prediction uncertainty does not accurately reveal prediction error, limiting the success of RIG algorithms. We propose a family of non-stationary kernels named Attentive Kernel (AK), which is simple, robust, and can extend any existing kernel to a non-stationary one. We evaluate the new kernel in elevation mapping tasks, where AK provides better accuracy and uncertainty quantification over the commonly used stationary kernels and the leading non-stationary kernels. The improved uncertainty quantification guides the downstream informative planner to collect more valuable data around the high-error area, further increasing prediction accuracy. A field experiment demonstrates that the proposed method can guide an Autonomous Surface Vehicle (ASV) to prioritize data collection in locations with significant spatial variations, enabling the model to characterize salient environmental features.

## 核心内容
Robotic Information Gathering (RIG) is a foundational research topic that answers how a robot (team) collects informative data to efficiently build an accurate model of an unknown target function under robot embodiment constraints. RIG has many applications, including but not limited to autonomous exploration and mapping, 3D reconstruction or inspection, search and rescue, and environmental monitoring. A RIG system relies on a probabilistic model's prediction uncertainty to identify critical areas for informative data collection. Gaussian Processes (GPs) with stationary kernels have been widely adopted for spatial modeling. However, real-world spatial data is typically non-stationary -- different locations do not have the same degree of variability. As a result, the prediction uncertainty does not accurately reveal prediction error, limiting the success of RIG algorithms. We propose a family of non-stationary kernels named Attentive Kernel (AK), which is simple, robust, and can extend any existing kernel to a non-stationary one. We evaluate the new kernel in elevation mapping tasks, where AK provides better accuracy and uncertainty quantification over the commonly used stationary kernels and the leading non-stationary kernels. The improved uncertainty quantification guides the downstream informative planner to collect more valuable data around the high-error area, further increasing prediction accuracy. A field experiment demonstrates that the proposed method can guide an Autonomous Surface Vehicle (ASV) to prioritize data collection in locations with significant spatial variations, enabling the model to characterize salient environmental features.

## 参考
- http://arxiv.org/abs/2306.01263v3

## Overview
Robotic Information Gathering (RIG) is a foundational research topic that addresses how a robot (or team of robots) collects informative data to efficiently build an accurate model of an unknown target function under robot embodiment constraints. RIG has numerous applications, including but not limited to autonomous exploration and mapping, 3D reconstruction or inspection, search and rescue, and environmental monitoring. A RIG system relies on the prediction uncertainty of a probabilistic model to identify critical areas for informative data collection. Gaussian Processes (GPs) with stationary kernels have been widely adopted for spatial modeling. However, real-world spatial data is typically non-stationary—different locations do not exhibit the same degree of variability. As a result, prediction uncertainty does not accurately reflect prediction error, limiting the success of RIG algorithms. We propose a family of non-stationary kernels called Attentive Kernel (AK), which is simple, robust, and can extend any existing kernel to a non-stationary one. We evaluate the new kernel in elevation mapping tasks, where AK provides better accuracy and uncertainty quantification compared to commonly used stationary kernels and leading non-stationary kernels. The improved uncertainty quantification guides the downstream informative planner to collect more valuable data around high-error areas, further enhancing prediction accuracy. A field experiment demonstrates that the proposed method can guide an Autonomous Surface Vehicle (ASV) to prioritize data collection in locations with significant spatial variations, enabling the model to characterize salient environmental features.

## Content
Robotic Information Gathering (RIG) is a foundational research topic that addresses how a robot (or team of robots) collects informative data to efficiently build an accurate model of an unknown target function under robot embodiment constraints. RIG has numerous applications, including but not limited to autonomous exploration and mapping, 3D reconstruction or inspection, search and rescue, and environmental monitoring. A RIG system relies on the prediction uncertainty of a probabilistic model to identify critical areas for informative data collection. Gaussian Processes (GPs) with stationary kernels have been widely adopted for spatial modeling. However, real-world spatial data is typically non-stationary—different locations do not exhibit the same degree of variability. As a result, prediction uncertainty does not accurately reflect prediction error, limiting the success of RIG algorithms. We propose a family of non-stationary kernels called Attentive Kernel (AK), which is simple, robust, and can extend any existing kernel to a non-stationary one. We evaluate the new kernel in elevation mapping tasks, where AK provides better accuracy and uncertainty quantification compared to commonly used stationary kernels and leading non-stationary kernels. The improved uncertainty quantification guides the downstream informative planner to collect more valuable data around high-error areas, further enhancing prediction accuracy. A field experiment demonstrates that the proposed method can guide an Autonomous Surface Vehicle (ASV) to prioritize data collection in locations with significant spatial variations, enabling the model to characterize salient environmental features.

## 개요
로봇 정보 수집(RIG)은 로봇(팀)이 로봇 구현 제약 조건 하에서 알려지지 않은 목표 함수의 정확한 모델을 효율적으로 구축하기 위해 정보성 데이터를 수집하는 방법을 다루는 기초 연구 주제입니다. RIG는 자율 탐사 및 매핑, 3D 재구성 또는 검사, 수색 및 구조, 환경 모니터링 등 다양한 응용 분야를 포함합니다. RIG 시스템은 확률적 모델의 예측 불확실성에 의존하여 정보성 데이터 수집을 위한 중요한 영역을 식별합니다. 고정 커널을 사용하는 가우시안 프로세스(GP)는 공간 모델링에 널리 채택되어 왔습니다. 그러나 실제 공간 데이터는 일반적으로 비고정적입니다. 즉, 위치에 따라 변동성이 동일하지 않습니다. 그 결과, 예측 불확실성이 예측 오차를 정확히 나타내지 못하여 RIG 알고리즘의 성공을 제한합니다. 우리는 간단하고 강건하며 기존의 모든 커널을 비고정 커널로 확장할 수 있는 Attentive Kernel(AK)이라는 비고정 커널 패밀리를 제안합니다. 새로운 커널을 고도 매핑 작업에서 평가한 결과, AK는 일반적으로 사용되는 고정 커널 및 주요 비고정 커널보다 더 나은 정확도와 불확실성 정량화를 제공합니다. 개선된 불확실성 정량화는 하류 정보성 플래너가 오차가 큰 영역 주변에서 더 가치 있는 데이터를 수집하도록 유도하여 예측 정확도를 더욱 향상시킵니다. 현장 실험을 통해 제안된 방법이 자율 수상 선박(ASV)이 공간 변동이 큰 위치에서 데이터 수집을 우선시하도록 안내하여 모델이 두드러진 환경 특징을 특성화할 수 있음을 입증했습니다.

## 핵심 내용
로봇 정보 수집(RIG)은 로봇(팀)이 로봇 구현 제약 조건 하에서 알려지지 않은 목표 함수의 정확한 모델을 효율적으로 구축하기 위해 정보성 데이터를 수집하는 방법을 다루는 기초 연구 주제입니다. RIG는 자율 탐사 및 매핑, 3D 재구성 또는 검사, 수색 및 구조, 환경 모니터링 등 다양한 응용 분야를 포함합니다. RIG 시스템은 확률적 모델의 예측 불확실성에 의존하여 정보성 데이터 수집을 위한 중요한 영역을 식별합니다. 고정 커널을 사용하는 가우시안 프로세스(GP)는 공간 모델링에 널리 채택되어 왔습니다. 그러나 실제 공간 데이터는 일반적으로 비고정적입니다. 즉, 위치에 따라 변동성이 동일하지 않습니다. 그 결과, 예측 불확실성이 예측 오차를 정확히 나타내지 못하여 RIG 알고리즘의 성공을 제한합니다. 우리는 간단하고 강건하며 기존의 모든 커널을 비고정 커널로 확장할 수 있는 Attentive Kernel(AK)이라는 비고정 커널 패밀리를 제안합니다. 새로운 커널을 고도 매핑 작업에서 평가한 결과, AK는 일반적으로 사용되는 고정 커널 및 주요 비고정 커널보다 더 나은 정확도와 불확실성 정량화를 제공합니다. 개선된 불확실성 정량화는 하류 정보성 플래너가 오차가 큰 영역 주변에서 더 가치 있는 데이터를 수집하도록 유도하여 예측 정확도를 더욱 향상시킵니다. 현장 실험을 통해 제안된 방법이 자율 수상 선박(ASV)이 공간 변동이 큰 위치에서 데이터 수집을 우선시하도록 안내하여 모델이 두드러진 환경 특징을 특성화할 수 있음을 입증했습니다.
