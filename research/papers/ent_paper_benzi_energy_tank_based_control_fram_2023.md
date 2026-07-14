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
  zh: 该论文提出了一种基于能量罐的被动控制框架，可直接执行 ISO/TS 15066 为协作机器人规定的能量边界，避免保守速度限制，同时在自由运动和人体接触期间保持稳定。该方法在 KUKA LWR 4+ 七自由度力控机械臂的仿真中进行了验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.14059v1.
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
The technical specification ISO/TS 15066 provides the foundational elements for assessing the safety of collaborative human-robot cells, which are the cornerstone of the modern industrial paradigm. The standard implementation of the ISO/TS 15066 procedure, however, often results in conservative motions of the robot, with consequently low performance of the cell. In this paper, we propose an energy tank-based approach that allows to directly satisfy the energetic bounds imposed by the ISO/TS 15066, thus avoiding the introduction of conservative modeling and assumptions. The proposed approach has been successfully validated in simulation.

## 核心内容
The technical specification ISO/TS 15066 provides the foundational elements for assessing the safety of collaborative human-robot cells, which are the cornerstone of the modern industrial paradigm. The standard implementation of the ISO/TS 15066 procedure, however, often results in conservative motions of the robot, with consequently low performance of the cell. In this paper, we propose an energy tank-based approach that allows to directly satisfy the energetic bounds imposed by the ISO/TS 15066, thus avoiding the introduction of conservative modeling and assumptions. The proposed approach has been successfully validated in simulation.

## 参考
- http://arxiv.org/abs/2304.14059v1

