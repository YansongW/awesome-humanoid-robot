---
$id: ent_human_equivalence_envelope
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: Human-Equivalence Envelope
  zh: 人等效包络
  ko: 인간 등가 영역
summary:
  en: A per-joint operating-requirement definition that requires a robot to meet human
    torque and power simultaneously at the same joint angle and angular rate within
    task-specific bands.
  zh: 一种单关节运行需求定义，要求机器人在任务特定区间内，于相同关节角度和角速度下同时达到人类的扭矩和功率。
  ko: 작업별 구간에서 동일한 관절 각도와 각속도에서 인간의 토크와 전력을 동시에 충족해야 하는 관절별 작동 요구사항 정의입니다.
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
- hee
- human_equivalence
- torque_power
- benchmark
- biomechanics
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Definition sourced from the Human-Level Actuation for Humanoids paper.
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-25'
---

# Human-Equivalence Envelope

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像汽车的动力性能包络——不是只看最大马力或最大扭矩，而是要求在某个转速下同时有足够的马力和扭矩，才能真正爬上陡坡。

> **自然语言逻辑**：人等效包络（HEE）为机器人关节定义了任务相关的运行区间，要求在相同关节角度和角速度下同时达到人类的扭矩和功率；它把“类人水平”这种模糊目标转化为具体的单关节指标，帮助设计者判断执行器能否完成行走、爬楼梯、举物等真实任务。

## Overview

Human-Equivalence Envelopes (HEE) define task-relevant operating bands for robot joints by requiring simultaneous satisfaction of human torque and power at matching joint angles and rates. They translate abstract "human-level" requirements into concrete, per-joint specifications.

## Relevance to Humanoid Robotics

HEE helps designers determine whether an actuator can perform real tasks such as walking, stairs, lifting, reaching, and hand actions, rather than relying only on peak torque or speed specifications.
