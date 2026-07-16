---
$id: ent_paper_sunbeam_human_level_actuation_for_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Level Actuation for Humanoids
  zh: 人形机器人的类人驱动能力
  ko: 휴머노이드를 위한 인간 수준 구동
summary:
  en: Proposes a reproducible benchmarking framework that makes 'human-level' actuation measurable for humanoids through an
    ISB-based DoF atlas, Human-Equivalence Envelopes (HEE), and the Human-Level Actuation Score (HLAS).
  zh: Claims that humanoid robots achieve ``human-level'' actuation are common but rarely quantified. Peak torque or speed
    specifications tell us little about whether a joint can deliver the right combination of torque, power, and endurance
    at task-relevant postures and rates. We introduce a comprehensive framework that makes ``human-level'' measurable and
    comparable across systems. Our approach has three components. First, a kinematic \emph{DoF atlas} standardizes joint coordinate
    systems and ranges of motion using ISB-based conventions, ensuring that human and robot joints are compared in the same
  ko: ISB 기반 자유도 아틀라스, 인간 등가 영역(HEE) 및 인간 수준 구동 점수(HLAS)를 통해 휴머노이드의 '인간 수준' 구동을 측정 가능하게 하는 재현 가능한 벤치마크 프레임워크를 제안한다.
domains:
- 10_evaluation_benchmarks
- 02_components
- 06_design_engineering
layers:
- validation_markets
- upstream
- midstream
functional_roles:
- knowledge
tags:
- human_level_actuation
- actuation_benchmark
- human_equivalence_envelope
- hlas
- biomechanics
- joint_dynamometry
- torque_power_envelope
- isb_conventions
- de_leva_anthropometry
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06796v1.
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_human_level_actuation_score
  relationship: produces
  description:
    en: The paper introduces the Human-Level Actuation Score (HLAS) as a scalar, decomposable benchmarking metric.
    zh: 本文提出了类人驱动评分（HLAS），作为一个可分解的标量基准指标。
    ko: 본 논문은 스칼라이면서 분해 가능한 벤치마크 지표인 인간 수준 구동 점수(HLAS)를 제안한다.
- id: ent_human_equivalence_envelope
  relationship: produces
  description:
    en: The paper defines Human-Equivalence Envelopes (HEE) to specify per-joint torque-power requirements at task-relevant
      postures and rates.
    zh: 本文定义了人等效包络（HEE），用于规定任务相关姿态和速度下的单关节扭矩-功率需求。
    ko: 본 논문은 작업 관련 자세와 속도에서 관절별 토크-전력 요구사항을 규정하기 위해 인간 등가 영역(HEE)을 정의한다.
- id: ent_isb_conventions
  relationship: is_based_on
  description:
    en: The kinematic DoF atlas in the paper uses ISB-based conventions to standardize joint coordinate systems and ranges
      of motion.
    zh: 论文中的运动自由度图谱采用基于ISB的约定来标准化关节坐标系和活动范围。
    ko: 논문의 운동학적 자유도 아틀라스는 관절 좌표계와 가동 범위를 표준화하기 위해 ISB 기반 관례를 사용한다.
- id: ent_deleva_anthropometry
  relationship: is_based_on
  description:
    en: The paper synthesizes published human biomechanics data into torque, power, and rate targets using de Leva anthropometry
      for a 75 kg reference body.
    zh: 论文使用de Leva人体测量学将已发表的人体生物力学数据综合为75公斤参考人体的扭矩、功率和速率目标。
    ko: 본 논문은 75kg 기준 신체에 대한 de Leva 인체측정법을 사용하여 발표된 인체 생체역학 데이터를 토크, 전력 및 속도 목표로 종합한다.
theoretical_depth:
- system
---

## 概述
Claims that humanoid robots achieve ``human-level'' actuation are common but rarely quantified. Peak torque or speed specifications tell us little about whether a joint can deliver the right combination of torque, power, and endurance at task-relevant postures and rates. We introduce a comprehensive framework that makes ``human-level'' measurable and comparable across systems. Our approach has three components. First, a kinematic \emph{DoF atlas} standardizes joint coordinate systems and ranges of motion using ISB-based conventions, ensuring that human and robot joints are compared in the same reference frames. Second, \emph{Human-Equivalence Envelopes (HEE)} define per-joint requirements by measuring whether a robot meets human torque \emph{and} power simultaneously at the same joint angle and rate $(q,ω)$, weighted by positive mechanical work in task-specific bands (walking, stairs, lifting, reaching, and hand actions). Third, the \emph{Human-Level Actuation Score (HLAS)} aggregates six physically grounded factors: workspace coverage (ROM and DoF), HEE coverage, torque-mode bandwidth, efficiency, and thermal sustainability. We provide detailed measurement protocols using dynamometry, electrical power monitoring, and thermal testing that yield every HLAS input from reproducible experiments. A worked example demonstrates HLAS computation for a multi-joint humanoid, showing how the score exposes actuator trade-offs (gearing ratio versus bandwidth and efficiency) that peak-torque specifications obscure. The framework serves as both a design specification for humanoid development and a benchmarking standard for comparing actuation systems, with all components grounded in published human biomechanics data.

## 核心内容
Claims that humanoid robots achieve ``human-level'' actuation are common but rarely quantified. Peak torque or speed specifications tell us little about whether a joint can deliver the right combination of torque, power, and endurance at task-relevant postures and rates. We introduce a comprehensive framework that makes ``human-level'' measurable and comparable across systems. Our approach has three components. First, a kinematic \emph{DoF atlas} standardizes joint coordinate systems and ranges of motion using ISB-based conventions, ensuring that human and robot joints are compared in the same reference frames. Second, \emph{Human-Equivalence Envelopes (HEE)} define per-joint requirements by measuring whether a robot meets human torque \emph{and} power simultaneously at the same joint angle and rate $(q,ω)$, weighted by positive mechanical work in task-specific bands (walking, stairs, lifting, reaching, and hand actions). Third, the \emph{Human-Level Actuation Score (HLAS)} aggregates six physically grounded factors: workspace coverage (ROM and DoF), HEE coverage, torque-mode bandwidth, efficiency, and thermal sustainability. We provide detailed measurement protocols using dynamometry, electrical power monitoring, and thermal testing that yield every HLAS input from reproducible experiments. A worked example demonstrates HLAS computation for a multi-joint humanoid, showing how the score exposes actuator trade-offs (gearing ratio versus bandwidth and efficiency) that peak-torque specifications obscure. The framework serves as both a design specification for humanoid development and a benchmarking standard for comparing actuation systems, with all components grounded in published human biomechanics data.

## 参考
- http://arxiv.org/abs/2511.06796v1

## Overview
Claims that humanoid robots achieve ``human-level'' actuation are common but rarely quantified. Peak torque or speed specifications tell us little about whether a joint can deliver the right combination of torque, power, and endurance at task-relevant postures and rates. We introduce a comprehensive framework that makes ``human-level'' measurable and comparable across systems. Our approach has three components. First, a kinematic \emph{DoF atlas} standardizes joint coordinate systems and ranges of motion using ISB-based conventions, ensuring that human and robot joints are compared in the same reference frames. Second, \emph{Human-Equivalence Envelopes (HEE)} define per-joint requirements by measuring whether a robot meets human torque \emph{and} power simultaneously at the same joint angle and rate $(q,ω)$, weighted by positive mechanical work in task-specific bands (walking, stairs, lifting, reaching, and hand actions). Third, the \emph{Human-Level Actuation Score (HLAS)} aggregates six physically grounded factors: workspace coverage (ROM and DoF), HEE coverage, torque-mode bandwidth, efficiency, and thermal sustainability. We provide detailed measurement protocols using dynamometry, electrical power monitoring, and thermal testing that yield every HLAS input from reproducible experiments. A worked example demonstrates HLAS computation for a multi-joint humanoid, showing how the score exposes actuator trade-offs (gearing ratio versus bandwidth and efficiency) that peak-torque specifications obscure. The framework serves as both a design specification for humanoid development and a benchmarking standard for comparing actuation systems, with all components grounded in published human biomechanics data.

## Content
Claims that humanoid robots achieve ``human-level'' actuation are common but rarely quantified. Peak torque or speed specifications tell us little about whether a joint can deliver the right combination of torque, power, and endurance at task-relevant postures and rates. We introduce a comprehensive framework that makes ``human-level'' measurable and comparable across systems. Our approach has three components. First, a kinematic \emph{DoF atlas} standardizes joint coordinate systems and ranges of motion using ISB-based conventions, ensuring that human and robot joints are compared in the same reference frames. Second, \emph{Human-Equivalence Envelopes (HEE)} define per-joint requirements by measuring whether a robot meets human torque \emph{and} power simultaneously at the same joint angle and rate $(q,ω)$, weighted by positive mechanical work in task-specific bands (walking, stairs, lifting, reaching, and hand actions). Third, the \emph{Human-Level Actuation Score (HLAS)} aggregates six physically grounded factors: workspace coverage (ROM and DoF), HEE coverage, torque-mode bandwidth, efficiency, and thermal sustainability. We provide detailed measurement protocols using dynamometry, electrical power monitoring, and thermal testing that yield every HLAS input from reproducible experiments. A worked example demonstrates HLAS computation for a multi-joint humanoid, showing how the score exposes actuator trade-offs (gearing ratio versus bandwidth and efficiency) that peak-torque specifications obscure. The framework serves as both a design specification for humanoid development and a benchmarking standard for comparing actuation systems, with all components grounded in published human biomechanics data.

## 개요
휴머노이드 로봇이 "인간 수준"의 구동을 달성했다는 주장은 흔하지만, 정량화되는 경우는 드뭅니다. 최대 토크나 속도 사양만으로는 관절이 작업 관련 자세와 속도에서 적절한 토크, 출력, 내구성의 조합을 제공할 수 있는지 알 수 없습니다. 우리는 "인간 수준"을 측정 가능하게 하고 시스템 간 비교를 가능하게 하는 포괄적인 프레임워크를 소개합니다. 우리의 접근 방식은 세 가지 구성 요소로 이루어져 있습니다. 첫째, 운동학적 \emph{DoF 아틀라스}는 ISB 기반 관례를 사용하여 관절 좌표계와 운동 범위를 표준화하여 인간과 로봇 관절이 동일한 기준 좌표계에서 비교되도록 보장합니다. 둘째, \emph{인간 등가 포락선(HEE)}은 동일한 관절 각도와 속도 $(q,ω)$에서 로봇이 인간의 토크 \emph{및} 출력을 동시에 충족하는지 측정하여 관절별 요구 사항을 정의하며, 작업별 대역(보행, 계단, 들어올리기, 뻗기, 손 동작)에서 양의 기계적 일로 가중치를 부여합니다. 셋째, \emph{인간 수준 구동 점수(HLAS)}는 여섯 가지 물리적 기반 요소(작업 공간 범위(ROM 및 DoF), HEE 범위, 토크 모드 대역폭, 효율성, 열 지속 가능성)를 통합합니다. 우리는 동력계, 전력 모니터링, 열 테스트를 사용한 상세한 측정 프로토콜을 제공하여 재현 가능한 실험에서 모든 HLAS 입력을 도출합니다. 실제 예제를 통해 다중 관절 휴머노이드에 대한 HLAS 계산을 보여주며, 점수가 최대 토크 사양이 가리는 구동기 트레이드오프(기어비 대 대역폭 및 효율성)를 어떻게 드러내는지 설명합니다. 이 프레임워크는 휴머노이드 개발을 위한 설계 사양이자 구동 시스템 비교를 위한 벤치마킹 표준 역할을 하며, 모든 구성 요소는 발표된 인간 생체역학 데이터에 기반합니다.

## 핵심 내용
휴머노이드 로봇이 "인간 수준"의 구동을 달성했다는 주장은 흔하지만, 정량화되는 경우는 드뭅니다. 최대 토크나 속도 사양만으로는 관절이 작업 관련 자세와 속도에서 적절한 토크, 출력, 내구성의 조합을 제공할 수 있는지 알 수 없습니다. 우리는 "인간 수준"을 측정 가능하게 하고 시스템 간 비교를 가능하게 하는 포괄적인 프레임워크를 소개합니다. 우리의 접근 방식은 세 가지 구성 요소로 이루어져 있습니다. 첫째, 운동학적 \emph{DoF 아틀라스}는 ISB 기반 관례를 사용하여 관절 좌표계와 운동 범위를 표준화하여 인간과 로봇 관절이 동일한 기준 좌표계에서 비교되도록 보장합니다. 둘째, \emph{인간 등가 포락선(HEE)}은 동일한 관절 각도와 속도 $(q,ω)$에서 로봇이 인간의 토크 \emph{및} 출력을 동시에 충족하는지 측정하여 관절별 요구 사항을 정의하며, 작업별 대역(보행, 계단, 들어올리기, 뻗기, 손 동작)에서 양의 기계적 일로 가중치를 부여합니다. 셋째, \emph{인간 수준 구동 점수(HLAS)}는 여섯 가지 물리적 기반 요소(작업 공간 범위(ROM 및 DoF), HEE 범위, 토크 모드 대역폭, 효율성, 열 지속 가능성)를 통합합니다. 우리는 동력계, 전력 모니터링, 열 테스트를 사용한 상세한 측정 프로토콜을 제공하여 재현 가능한 실험에서 모든 HLAS 입력을 도출합니다. 실제 예제를 통해 다중 관절 휴머노이드에 대한 HLAS 계산을 보여주며, 점수가 최대 토크 사양이 가리는 구동기 트레이드오프(기어비 대 대역폭 및 효율성)를 어떻게 드러내는지 설명합니다. 이 프레임워크는 휴머노이드 개발을 위한 설계 사양이자 구동 시스템 비교를 위한 벤치마킹 표준 역할을 하며, 모든 구성 요소는 발표된 인간 생체역학 데이터에 기반합니다.
