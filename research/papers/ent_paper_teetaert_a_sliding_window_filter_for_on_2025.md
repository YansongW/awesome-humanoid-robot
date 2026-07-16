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

## Overview
Stochastic state estimation methods for continuum robots (CRs) often struggle to balance accuracy and computational efficiency. While several recent works have explored sliding-window formulations for CRs, these methods are limited to simplified, discrete-time approximations and do not provide stochastic representations. In contrast, current stochastic filter methods must run at the speed of measurements, limiting their full potential. Recent works in continuous-time estimation techniques for CRs show a principled approach to addressing this runtime constraint, but are currently restricted to offline operation. In this work, we present a sliding-window filter (SWF) for continuous-time state estimation of CRs that improves upon the accuracy of a filter approach while enabling continuous-time methods to operate online, all while running at faster-than-real-time speeds. This represents the first stochastic SWF specifically designed for CRs, providing a promising direction for future research in this area.

## Content
Stochastic state estimation methods for continuum robots (CRs) often struggle to balance accuracy and computational efficiency. While several recent works have explored sliding-window formulations for CRs, these methods are limited to simplified, discrete-time approximations and do not provide stochastic representations. In contrast, current stochastic filter methods must run at the speed of measurements, limiting their full potential. Recent works in continuous-time estimation techniques for CRs show a principled approach to addressing this runtime constraint, but are currently restricted to offline operation. In this work, we present a sliding-window filter (SWF) for continuous-time state estimation of CRs that improves upon the accuracy of a filter approach while enabling continuous-time methods to operate online, all while running at faster-than-real-time speeds. This represents the first stochastic SWF specifically designed for CRs, providing a promising direction for future research in this area.

## 개요
연속체 로봇(CR)의 확률적 상태 추정 방법은 종종 정확성과 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪습니다. 최근 여러 연구에서 CR을 위한 슬라이딩 윈도우 기법을 탐구했지만, 이러한 방법은 단순화된 이산 시간 근사에 국한되어 확률적 표현을 제공하지 못합니다. 반대로, 현재의 확률적 필터 방법은 측정 속도에 맞춰 실행되어야 하므로 잠재력을 완전히 발휘하지 못합니다. CR을 위한 연속 시간 추정 기법에 대한 최근 연구는 이러한 실행 시간 제약을 해결하는 원칙적인 접근 방식을 보여주지만, 현재는 오프라인 작업으로 제한됩니다. 본 연구에서는 필터 접근 방식의 정확성을 개선하면서 연속 시간 방법이 온라인으로 작동할 수 있도록 하고, 실시간보다 빠른 속도로 실행되는 CR의 연속 시간 상태 추정을 위한 슬라이딩 윈도우 필터(SWF)를 제시합니다. 이는 CR을 위해 특별히 설계된 최초의 확률적 SWF로, 이 분야의 미래 연구에 유망한 방향을 제시합니다.

## 핵심 내용
연속체 로봇(CR)의 확률적 상태 추정 방법은 종종 정확성과 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪습니다. 최근 여러 연구에서 CR을 위한 슬라이딩 윈도우 기법을 탐구했지만, 이러한 방법은 단순화된 이산 시간 근사에 국한되어 확률적 표현을 제공하지 못합니다. 반대로, 현재의 확률적 필터 방법은 측정 속도에 맞춰 실행되어야 하므로 잠재력을 완전히 발휘하지 못합니다. CR을 위한 연속 시간 추정 기법에 대한 최근 연구는 이러한 실행 시간 제약을 해결하는 원칙적인 접근 방식을 보여주지만, 현재는 오프라인 작업으로 제한됩니다. 본 연구에서는 필터 접근 방식의 정확성을 개선하면서 연속 시간 방법이 온라인으로 작동할 수 있도록 하고, 실시간보다 빠른 속도로 실행되는 CR의 연속 시간 상태 추정을 위한 슬라이딩 윈도우 필터(SWF)를 제시합니다. 이는 CR을 위해 특별히 설계된 최초의 확률적 SWF로, 이 분야의 미래 연구에 유망한 방향을 제시합니다.
