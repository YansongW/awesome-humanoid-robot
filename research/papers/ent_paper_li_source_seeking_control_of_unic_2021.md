---
$id: ent_paper_li_source_seeking_control_of_unic_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Source Seeking Control of Unicycle Robots with 3D-printed Flexible Piezoresistive Sensors
  zh: 基于3D打印柔性压阻传感器的独轮机器人源搜索控制
  ko: 3D 프린팅된 유연한 압저항 센서를 탑재한 유니사이클 로봇의 신호원 탐색 제어
summary:
  en: Presents projected gradient-ascent and extremum-seeking control laws for a unicycle robot using 3D-printed flexible
    graphene-based piezoresistive airflow sensors, with asymptotic convergence proofs and experimental validation.
  zh: We present the design and experimental validation of source seeking control algorithms for a unicycle mobile robot that
    is equipped with novel 3D-printed flexible graphene-based piezoresistive airflow sensors. Based solely on a local gradient
    measurement from the airflow sensors, we propose and analyze a projected gradient ascent algorithm to solve the source
    seeking problem. In the case of partial sensor failure, we propose a combination of Extremum-Seeking Control with our
    projected gradient ascent algorithm. For both control laws, we prove the asymptotic convergence of the robot to the sour
  ko: 3D 프린팅된 유연한 그래핀 기반 압저항 기류 센서가 장착된 유니사이클 로봇을 위해 투영 경사 상승법 및 극값 탐색 제어 법칙을 제안하고, 점근적 수렴성을 증명하며 실험적으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- component
tags:
- source_seeking
- gradient_ascent
- extremum_seeking_control
- airflow_sensor
- piezoresistive_sensor
- flexible_electronics
- 3d_printed_sensor
- unicycle_robot
- mobile_robot
- gps_denied_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.14267v2.
sources:
- id: src_001
  type: paper
  title: Source Seeking Control of Unicycle Robots with 3D-printed Flexible Piezoresistive Sensors
  url: https://arxiv.org/abs/2104.14267
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
We present the design and experimental validation of source seeking control algorithms for a unicycle mobile robot that is equipped with novel 3D-printed flexible graphene-based piezoresistive airflow sensors. Based solely on a local gradient measurement from the airflow sensors, we propose and analyze a projected gradient ascent algorithm to solve the source seeking problem. In the case of partial sensor failure, we propose a combination of Extremum-Seeking Control with our projected gradient ascent algorithm. For both control laws, we prove the asymptotic convergence of the robot to the source. Numerical simulations were performed to validate the algorithms and experimental validations are presented to demonstrate the efficacy of the proposed methods.

## 核心内容
We present the design and experimental validation of source seeking control algorithms for a unicycle mobile robot that is equipped with novel 3D-printed flexible graphene-based piezoresistive airflow sensors. Based solely on a local gradient measurement from the airflow sensors, we propose and analyze a projected gradient ascent algorithm to solve the source seeking problem. In the case of partial sensor failure, we propose a combination of Extremum-Seeking Control with our projected gradient ascent algorithm. For both control laws, we prove the asymptotic convergence of the robot to the source. Numerical simulations were performed to validate the algorithms and experimental validations are presented to demonstrate the efficacy of the proposed methods.

## 参考
- http://arxiv.org/abs/2104.14267v2


