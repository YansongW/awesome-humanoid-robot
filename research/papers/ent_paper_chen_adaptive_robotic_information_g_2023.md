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
  en: This paper proposes the Attentive Kernel (AK), a non-stationary Gaussian Process
    kernel that uses attention-based input-dependent length-scale selection to improve
    uncertainty quantification for robotic information gathering, validated through
    elevation mapping benchmarks and an autonomous surface vehicle field experiment.
  zh: 本文提出了一种名为Attentive Kernel（AK）的非平稳高斯过程核函数，该函数通过基于注意力的输入相关长度尺度选择来改进机器人信息获取中的不确定性量化，并通过高程映射基准测试和自主水面航行器实地实验进行了验证。
  ko: 본 논문은 주의 기반 입력 의존 길이 척도 선택을 통해 로봇 정보 수집의 불확실성 정량화를 개선하는 비정상 가우시안 프로세스 커널인 Attentive
    Kernel(AK)을 제안하고, 고도 매핑 벤치마크와 자율 수상 차량 현장 실험을 통해 검증하였다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full PDF before final verification.
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

## Overview

Robotic Information Gathering (RIG) asks how robots can collect informative data to build accurate models of unknown target functions while respecting embodiment constraints. A central challenge is that real-world spatial data is typically non-stationary, meaning variability differs across locations. Stationary Gaussian Process (GP) kernels, commonly used for spatial modeling, therefore produce poorly calibrated prediction uncertainties that fail to reveal high-error regions. This paper proposes the Attentive Kernel (AK), a non-stationary GP kernel that extends any base kernel by learning input-dependent length scales and applying instance-selection masking through attention mechanisms.

The authors evaluate AK on multiple elevation mapping datasets, including N17E073, N43W080, N45W123, N47W124, Mount St. Helens, and a quarry lake bathymetric field dataset. AK is reported to provide better accuracy and uncertainty quantification than commonly used stationary kernels and leading non-stationary alternatives. The improved uncertainty estimates guide an informative planner to collect more valuable data around high-error areas, further improving prediction accuracy. A field experiment with an Autonomous Surface Vehicle (ASV) demonstrates that the method can prioritize data collection in regions with significant spatial variation.

The paper also announces the release of PyPolo, an open-source Python library intended to support learning, research, and benchmarking of RIG algorithms.

## Key Contributions

- Design of the Attentive Kernel (AK), a non-stationary GP kernel that composes primitive base kernels via input-dependent length-scale selection and attention-based instance-selection masking.
- Extensive evaluation of AK against stationary and leading non-stationary kernels on elevation mapping tasks, showing improved accuracy and uncertainty quantification.
- Field experiment demonstrating AK-guided informative planning on an Autonomous Surface Vehicle in a quarry lake environment.
- Release of PyPolo, an open-source library for learning, researching, and benchmarking robotic information gathering algorithms.

## Relevance to Humanoid Robotics

Although the experiments focus on an Autonomous Surface Vehicle, the core contribution—better uncertainty quantification in non-stationary GP regression—is directly transferable to humanoid robots. Humanoids operating in complex, partially known environments must adaptively gather spatial and contact information to plan footholds, manipulation strategies, and safe navigation routes. The Attentive Kernel's ability to flag high-error regions could improve exploration and decision-making in these scenarios, supporting adaptive behavior during mass deployment. However, the paper does not validate AK on humanoid hardware or tasks, so its practical effectiveness for humanoids remains to be demonstrated.
