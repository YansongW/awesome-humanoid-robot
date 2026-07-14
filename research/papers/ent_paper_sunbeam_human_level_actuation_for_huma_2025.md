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
  zh: 提出一个可复现的基准框架，通过基于ISB的自由度图谱、人等效包络（HEE）和类人驱动评分（HLAS），使人形机器人的“类人级”驱动能力可量化。
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

