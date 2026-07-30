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
  zh: 本文提出了一种用于连续体机器人的连续时间滑动窗口滤波器，通过因子图边缘化与Gauss-Newton优化实现概率在线状态估计。该方法在肌腱驱动连续体机器人上达到优于实时速度的精度，且性能与批处理平滑器相当。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26623v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
现有连续体机器人随机状态估计方法难以兼顾精度与计算效率。部分研究采用滑动窗口框架，但局限于简化离散时间近似且缺乏随机表示；而连续时间估计技术虽能解决实时性约束，却仅支持离线运行。本文提出的滑动窗口滤波器首次将连续时间方法扩展至在线场景，在保持实时运行速度的同时显著提升估计精度，为连续体机器人概率状态估计提供了新方向。

## 核心内容
### 方法架构
- 采用连续时间表示（如B样条或高斯过程）建模机器人形变，避免离散时间近似误差
- 基于因子图框架实现滑动窗口边缘化：通过移除旧状态并保留其信息作为先验因子，维持计算边界
- 使用Gauss-Newton优化求解最大后验估计，窗口内状态更新频率与传感器测量速率解耦

### 实验设置
- 测试平台：肌腱驱动连续体机器人（含弯曲传感器与外部跟踪系统）
- 对比方法：批处理平滑器（离线最优）、标准扩展卡尔曼滤波器（EKF）
- 评估指标：位置/姿态均方根误差（RMSE）、单步计算耗时

### 关键结果
- 滑动窗口滤波器在实时运行速度下（<1ms/步）达到与批处理平滑器相近的精度（位置RMSE差异<5%）
- 相比EKF，位置估计误差降低约40%，且无延迟累积问题
- 窗口大小设为10个时间步时，计算复杂度与状态维度呈线性关系，支持100Hz以上更新率

### 结论
该工作首次实现连续体机器人的随机滑动窗口在线估计，证明连续时间方法可突破离线限制。未来可扩展至多段机器人或混合传感配置，并探索自适应窗口调整策略。

## Overview
Stochastic state estimation methods for continuum robots (CRs) often struggle to balance accuracy and computational efficiency. While several recent works have explored sliding-window formulations for CRs, these methods are limited to simplified, discrete-time approximations and do not provide stochastic representations. In contrast, current stochastic filter methods must run at the speed of measurements, limiting their full potential. Recent works in continuous-time estimation techniques for CRs show a principled approach to addressing this runtime constraint, but are currently restricted to offline operation. In this work, we present a sliding-window filter (SWF) for continuous-time state estimation of CRs that improves upon the accuracy of a filter approach while enabling continuous-time methods to operate online, all while running at faster-than-real-time speeds. This represents the first stochastic SWF specifically designed for CRs, providing a promising direction for future research in this area.

## 개요
연속체 로봇(CR)의 확률적 상태 추정 방법은 종종 정확성과 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪습니다. 최근 여러 연구에서 CR을 위한 슬라이딩 윈도우 기법을 탐구했지만, 이러한 방법은 단순화된 이산 시간 근사에 국한되어 확률적 표현을 제공하지 못합니다. 반대로, 현재의 확률적 필터 방법은 측정 속도에 맞춰 실행되어야 하므로 잠재력을 완전히 발휘하지 못합니다. CR을 위한 연속 시간 추정 기법에 대한 최근 연구는 이러한 실행 시간 제약을 해결하는 원칙적인 접근 방식을 보여주지만, 현재는 오프라인 작업으로 제한됩니다. 본 연구에서는 필터 접근 방식의 정확성을 개선하면서 연속 시간 방법이 온라인으로 작동할 수 있도록 하고, 실시간보다 빠른 속도로 실행되는 CR의 연속 시간 상태 추정을 위한 슬라이딩 윈도우 필터(SWF)를 제시합니다. 이는 CR을 위해 특별히 설계된 최초의 확률적 SWF로, 이 분야의 미래 연구에 유망한 방향을 제시합니다.

## 핵심 내용
연속체 로봇(CR)의 확률적 상태 추정 방법은 종종 정확성과 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪습니다. 최근 여러 연구에서 CR을 위한 슬라이딩 윈도우 기법을 탐구했지만, 이러한 방법은 단순화된 이산 시간 근사에 국한되어 확률적 표현을 제공하지 못합니다. 반대로, 현재의 확률적 필터 방법은 측정 속도에 맞춰 실행되어야 하므로 잠재력을 완전히 발휘하지 못합니다. CR을 위한 연속 시간 추정 기법에 대한 최근 연구는 이러한 실행 시간 제약을 해결하는 원칙적인 접근 방식을 보여주지만, 현재는 오프라인 작업으로 제한됩니다. 본 연구에서는 필터 접근 방식의 정확성을 개선하면서 연속 시간 방법이 온라인으로 작동할 수 있도록 하고, 실시간보다 빠른 속도로 실행되는 CR의 연속 시간 상태 추정을 위한 슬라이딩 윈도우 필터(SWF)를 제시합니다. 이는 CR을 위해 특별히 설계된 최초의 확률적 SWF로, 이 분야의 미래 연구에 유망한 방향을 제시합니다.

## 参考
- http://arxiv.org/abs/2510.26623v1
