---
$id: ent_paper_teetaert_a_sliding_window_filter_for_on_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Sliding-Window Filter for Online Continuous-Time Continuum Robot State Estimation
  zh: 用于在线连续时间连续体机器人状态估计的滑动窗口滤波器
  ko: 온라인 연속시간 연속체 로봇 상태 추정을 위한 슬라이딩 윈도우 필터
summary:
  en: This paper proposes a continuous-time sliding-window filter for probabilistic online state estimation of continuum robots,
    using factor-graph marginalization and Gauss-Newton optimization to achieve faster-than-real-time accuracy comparable
    to batch smoothers on a tendon-driven continuum robot.
  zh: 本文提出了一种用于连续体机器人概率在线状态估计的连续时间滑动窗口滤波器，利用因子图边缘化和高斯-牛顿优化，在肌腱驱动连续体机器人上实现了比实时更快且接近批量平滑器精度的估计。
  ko: 본 논문은 인대 구동 연속체 로봇에서 실시간보다 빠르고 배치 스무더에 필적하는 정확도를 달성하기 위해 요인 그래프 주변화와 가우스-뉴턴 최적화를 활용한 연속시간 슬라이딩 윈도우 필터를 제안한다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- state_estimation
- continuum_robot
- sliding_window_filter
- factor_graph
- tendon_driven_robot
- online_estimation
- gauss_newton
- marginalization
- uncertainty_quantification
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26623v1.
sources:
- id: src_001
  type: paper
  title: A Sliding-Window Filter for Online Continuous-Time Continuum Robot State Estimation
  url: https://arxiv.org/abs/2510.26623
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Stochastic state estimation methods for continuum robots (CRs) often struggle to balance accuracy and computational efficiency. While several recent works have explored sliding-window formulations for CRs, these methods are limited to simplified, discrete-time approximations and do not provide stochastic representations. In contrast, current stochastic filter methods must run at the speed of measurements, limiting their full potential. Recent works in continuous-time estimation techniques for CRs show a principled approach to addressing this runtime constraint, but are currently restricted to offline operation. In this work, we present a sliding-window filter (SWF) for continuous-time state estimation of CRs that improves upon the accuracy of a filter approach while enabling continuous-time methods to operate online, all while running at faster-than-real-time speeds. This represents the first stochastic SWF specifically designed for CRs, providing a promising direction for future research in this area.

## 核心内容
Stochastic state estimation methods for continuum robots (CRs) often struggle to balance accuracy and computational efficiency. While several recent works have explored sliding-window formulations for CRs, these methods are limited to simplified, discrete-time approximations and do not provide stochastic representations. In contrast, current stochastic filter methods must run at the speed of measurements, limiting their full potential. Recent works in continuous-time estimation techniques for CRs show a principled approach to addressing this runtime constraint, but are currently restricted to offline operation. In this work, we present a sliding-window filter (SWF) for continuous-time state estimation of CRs that improves upon the accuracy of a filter approach while enabling continuous-time methods to operate online, all while running at faster-than-real-time speeds. This represents the first stochastic SWF specifically designed for CRs, providing a promising direction for future research in this area.

## 参考
- http://arxiv.org/abs/2510.26623v1

