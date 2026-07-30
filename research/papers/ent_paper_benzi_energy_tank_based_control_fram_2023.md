---
$id: ent_paper_benzi_energy_tank_based_control_fram_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Energy Tank-based Control Framework for Satisfying the ISO/TS 15066 Constraint
  zh: 满足 ISO/TS 15066 约束的能量罐控制框架
  ko: ISO/TS 15066 제약을 만족시키는 에너지 탱크 기반 제어 프레임워크
summary:
  en: This paper proposes an energy tank-based, passivity-based control framework that directly enforces the energetic bounds
    defined by ISO/TS 15066 for collaborative robots, avoiding conservative velocity limits while preserving stability during
    free motion and human contact. The approach was validated in simulation on a KUKA LWR 4+ 7-DOF force-controlled manipulator.
  zh: 本文提出一种基于能量罐的被动控制框架，用于直接满足ISO/TS 15066对协作机器人的能量约束，避免保守的速度限制，同时保持自由运动与人机接触时的稳定性。该方法在KUKA LWR 4+七自由度力控机械臂上进行了仿真验证。
  ko: 본 논문은 협업 로봇을 위해 ISO/TS 15066에서 정의한 에너지 경계를 직접 적용하는 에너지 탱크 기반 수동성 기반 제어 프레임워크를 제안하여 보수적인 속도 제한을 피하면서 자유 운동 및 인간 접촉 시
    안정성을 유지합니다. 이 접근법은 KUKA LWR 4+ 7자유도 힘 제어 매니퓰레이터 시뮬레이션에서 검증되었습니다.
domains:
- 07_ai_models_algorithms
- 12_policy_regulation_ethics
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- energy_tank_control
- passivity_based_control
- iso_ts_15066
- power_force_limiting
- collaborative_robots
- human_robot_interaction
- safety_constraints
- kinetic_energy_bounds
- force_control
- industrial_humanoids
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.14059v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Energy Tank-based Control Framework for Satisfying the ISO/TS 15066 Constraint
  url: https://arxiv.org/abs/2304.14059
  date: '2023'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
针对ISO/TS 15066标准实施中常导致机器人运动保守、单元性能低下的问题，本文提出一种能量罐控制框架。该框架基于被动性理论，直接强制执行标准定义的能界，无需引入保守建模或假设。仿真实验在KUKA LWR 4+七自由度力控机械臂上完成，验证了该方法在自由运动和人机接触场景下均能保持稳定性。

## 核心内容
### 核心问题
- ISO/TS 15066是协作机器人安全评估的基础技术规范，但标准实施常导致机器人运动保守，降低单元性能。
- 现有方法通过引入保守的速度限制来满足安全约束，牺牲了机器人的运动效率。

### 方法架构
- 提出基于能量罐（energy tank）的被动控制框架，直接强制执行ISO/TS 15066定义的能界。
- 能量罐机制确保系统被动性，在自由运动和人机接触时均能保持稳定性，无需保守建模或假设。

### 实验设置
- 仿真平台：KUKA LWR 4+七自由度力控机械臂。
- 验证场景：自由运动与人机接触两种工况。

### 关键结果
- 成功验证了该方法在满足ISO/TS 15066能量约束的同时，避免了保守速度限制。
- 在两种工况下均保持了系统稳定性，未出现失稳或性能下降。

### 结论
- 该框架为协作机器人安全控制提供了直接满足标准约束的可行方案，兼顾安全性与运动性能。

## Overview
The technical specification ISO/TS 15066 provides the foundational elements for assessing the safety of collaborative human-robot cells, which are the cornerstone of the modern industrial paradigm. The standard implementation of the ISO/TS 15066 procedure, however, often results in conservative motions of the robot, with consequently low performance of the cell. In this paper, we propose an energy tank-based approach that allows to directly satisfy the energetic bounds imposed by the ISO/TS 15066, thus avoiding the introduction of conservative modeling and assumptions. The proposed approach has been successfully validated in simulation.

## 개요
기술 사양 ISO/TS 15066은 현대 산업 패러다임의 초석인 협업형 인간-로봇 셀의 안전성을 평가하기 위한 기본 요소를 제공합니다. 그러나 ISO/TS 15066 절차의 표준 구현은 종종 로봇의 보수적인 움직임을 초래하여 결과적으로 셀의 성능이 저하됩니다. 본 논문에서는 ISO/TS 15066이 부과하는 에너지적 제약을 직접 충족할 수 있는 에너지 탱크 기반 접근법을 제안하여 보수적인 모델링과 가정의 도입을 피합니다. 제안된 접근법은 시뮬레이션에서 성공적으로 검증되었습니다.

## 핵심 내용
기술 사양 ISO/TS 15066은 현대 산업 패러다임의 초석인 협업형 인간-로봇 셀의 안전성을 평가하기 위한 기본 요소를 제공합니다. 그러나 ISO/TS 15066 절차의 표준 구현은 종종 로봇의 보수적인 움직임을 초래하여 결과적으로 셀의 성능이 저하됩니다. 본 논문에서는 ISO/TS 15066이 부과하는 에너지적 제약을 직접 충족할 수 있는 에너지 탱크 기반 접근법을 제안하여 보수적인 모델링과 가정의 도입을 피합니다. 제안된 접근법은 시뮬레이션에서 성공적으로 검증되었습니다.

## 参考
- http://arxiv.org/abs/2304.14059v1
