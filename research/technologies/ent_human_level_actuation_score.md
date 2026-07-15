---
$id: ent_human_level_actuation_score
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: Human-Level Actuation Score
  zh: 类人驱动评分
  ko: 인간 수준 구동 점수
summary:
  en: A scalar, decomposable benchmarking metric that aggregates workspace coverage, torque-power requirements, bandwidth,
    efficiency, and thermal sustainability to quantify how close a humanoid robot's actuation is to human-level performance.
  zh: 一种标量、可分解的基准指标，综合工作空间覆盖、扭矩-功率需求、带宽、效率和热可持续性，以量化人形机器人驱动能力接近类人水平的程度。
  ko: 작업 공간 커버리지, 토크-전력 요구사항, 대역폭, 효율 및 열 지속성을 종합하여 휴인oid 로봇의 구동이 인간 수준에 얼마나 가까운지 정량화하는 스칼라 분해 가능 벤치마크 지표입니다.
domains:
- 10_evaluation_benchmarks
- 06_design_engineering
layers:
- validation_markets
- midstream
functional_roles:
- knowledge
- tool_equipment
tags:
- hlas
- human_level_actuation
- benchmark
- actuation
- torque
- power
- biomechanics
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Definition sourced from the Human-Level Actuation for Humanoids paper; detailed measurement protocols require full-text
    review. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---


## 概述
一种标量、可分解的基准指标，综合工作空间覆盖、扭矩-功率需求、带宽、效率和热可持续性，以量化人形机器人驱动能力接近类人水平的程度。

## 核心内容
### 类人驱动评分的定义与定位
类人驱动评分属于 **benchmark** 类型，英文名称为 *Human-Level Actuation Score*。
一种标量、可分解的基准指标，综合工作空间覆盖、扭矩-功率需求、带宽、效率和热可持续性，以量化人形机器人驱动能力接近类人水平的程度。

### 类人驱动评分的关键信息
以下整理了关于类人驱动评分的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像一个综合信用评分——不是只看收入，而是把储蓄、负债、还款记录、消费习惯等合并成一个数字，来衡量一个人的财务健康度。

> **自然语言逻辑**：类人驱动评分（HLAS）是一个标量、可分解的基准指标，把工作空间覆盖、扭矩-功率包络、带宽、效率和热可持续性汇总起来；它以参考人体为 1.0，量化不同机器人驱动系统距离“类人水平”有多远，便于在统一尺度上比较各类执行器技术。

## Overview

The Human-Level Actuation Score (HLAS) is introduced as a way to make the often-vague claim of "human-level" actuation measurable and reproducible. It normalizes performance so that a human reference body scores 1.0, and decomposes the score into physically grounded factors.

## Components

- **Workspace coverage**: Range of motion and degrees of freedom relative to human joints.
- **Human-Equivalence Envelope coverage**: Ability to meet human torque and power simultaneously at task-relevant postures and rates.
- **Torque-mode bandwidth**: Dynamic response of the actuator.
- **Efficiency**: Mechanical and electrical energy conversion.
- **Thermal sustainability**: Ability to sustain operation without overheating.

## Relevance to Humanoid Robotics

HLAS provides a design specification and benchmarking standard for actuation systems, helping compare competing actuator technologies on a common, human-referenced scale.

## 参考
- [Human-Level Actuation for Humanoids](https://arxiv.org/abs/2511.06796)

类人驱动评分的相关技术仍在快速发展。从系统科学角度看，它与其他benchmark相互耦合，共同决定了人形机器人的整体性能。深入理解其原理、边界条件与工程约束，是将实验室样机转化为可量产产品的必要环节。



