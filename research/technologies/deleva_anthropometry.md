---
$id: ent_deleva_anthropometry
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: de Leva Anthropometry
  zh: de Leva人体测量学
  ko: 드 레바 인체측정학
summary:
  en: A widely used anthropometric dataset and set of body-segment parameter estimates
    for biomechanical modeling, commonly used to define reference human body mass,
    center-of-mass locations, and moments of inertia.
  zh: 一种广泛应用于生物力学建模的人体测量数据集和身体环节参数估计方法，常用于定义参考人体质量、质心位置和转动惯量。
  ko: 생체역학 모델링에 널리 사용되는 인체측정 데이터 세트 및 신체 부분 매개변수 추정 집합으로, 기준 인체 질량, 질량 중심 위치 및 관성 모멘트를 정의하는 데 사용됩니다.
domains:
- 06_design_engineering
- 10_evaluation_benchmarks
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- anthropometry
- biomechanics
- de_leva
- human_reference
- mass_properties
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Well-established biomechanics reference; application to humanoid actuation benchmarking
    is sourced from the Human-Level Actuation for Humanoids paper.
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-25'
---

# de Leva Anthropometry

## 抽象

> **生活实例**：它就像汽车碰撞测试中使用的“标准假人”——有标准的身高、体重、四肢长度和质心位置，用来作为衡量真人和机器人的共同参照。

> **自然语言逻辑**：de Leva 人体测量学提供了一套标准化的身体环节参数（质量、质心、转动惯量等），广泛应用于生物力学建模；在人形机器人领域，它被用来定义参考人体，使机器人驱动系统和运动能力可以与真实的人类生物力学目标进行直接比较。

## Overview

de Leva anthropometry provides standardized body-segment parameters used to build biomechanical models of humans. It is frequently used as the reference human body in robotics benchmarking.

## Relevance to Humanoid Robotics

The Human-Level Actuation for Humanoids paper uses de Leva anthropometry to define a 75 kg reference body, enabling robot actuation requirements to be compared against realistic human biomechanical targets.
