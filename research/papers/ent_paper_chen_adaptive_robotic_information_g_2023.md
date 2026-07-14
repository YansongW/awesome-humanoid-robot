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

