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

## Overview
We present the design and experimental validation of source seeking control algorithms for a unicycle mobile robot that is equipped with novel 3D-printed flexible graphene-based piezoresistive airflow sensors. Based solely on a local gradient measurement from the airflow sensors, we propose and analyze a projected gradient ascent algorithm to solve the source seeking problem. In the case of partial sensor failure, we propose a combination of Extremum-Seeking Control with our projected gradient ascent algorithm. For both control laws, we prove the asymptotic convergence of the robot to the source. Numerical simulations were performed to validate the algorithms and experimental validations are presented to demonstrate the efficacy of the proposed methods.

## Content
We present the design and experimental validation of source seeking control algorithms for a unicycle mobile robot that is equipped with novel 3D-printed flexible graphene-based piezoresistive airflow sensors. Based solely on a local gradient measurement from the airflow sensors, we propose and analyze a projected gradient ascent algorithm to solve the source seeking problem. In the case of partial sensor failure, we propose a combination of Extremum-Seeking Control with our projected gradient ascent algorithm. For both control laws, we prove the asymptotic convergence of the robot to the source. Numerical simulations were performed to validate the algorithms and experimental validations are presented to demonstrate the efficacy of the proposed methods.

## 개요
본 논문에서는 새로운 3D 프린팅된 유연한 그래핀 기반 압저항 공기 흐름 센서를 장착한 단륜 모바일 로봇을 위한 소스 탐색 제어 알고리즘의 설계 및 실험적 검증을 제시합니다. 공기 흐름 센서의 국소 기울기 측정만을 기반으로, 투영 경사 상승 알고리즘을 제안하고 분석하여 소스 탐색 문제를 해결합니다. 부분적인 센서 고장이 발생한 경우, 극한 탐색 제어(Extremum-Seeking Control)와 투영 경사 상승 알고리즘을 결합한 방법을 제안합니다. 두 제어 법칙 모두에 대해 로봇이 소스로 점근적으로 수렴함을 증명합니다. 알고리즘 검증을 위한 수치 시뮬레이션을 수행하였으며, 제안된 방법의 효용성을 입증하기 위한 실험적 검증 결과를 제시합니다.

## 핵심 내용
본 논문에서는 새로운 3D 프린팅된 유연한 그래핀 기반 압저항 공기 흐름 센서를 장착한 단륜 모바일 로봇을 위한 소스 탐색 제어 알고리즘의 설계 및 실험적 검증을 제시합니다. 공기 흐름 센서의 국소 기울기 측정만을 기반으로, 투영 경사 상승 알고리즘을 제안하고 분석하여 소스 탐색 문제를 해결합니다. 부분적인 센서 고장이 발생한 경우, 극한 탐색 제어(Extremum-Seeking Control)와 투영 경사 상승 알고리즘을 결합한 방법을 제안합니다. 두 제어 법칙 모두에 대해 로봇이 소스로 점근적으로 수렴함을 증명합니다. 알고리즘 검증을 위한 수치 시뮬레이션을 수행하였으며, 제안된 방법의 효용성을 입증하기 위한 실험적 검증 결과를 제시합니다.
