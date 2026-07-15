---
$id: ent_paper_desai_automatic_design_of_task_speci_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automatic Design of Task-specific Robotic Arms
  zh: 面向特定任务的机械臂自动设计
  ko: 작업별 로봇 팔의 자동 설계
summary:
  en: An interactive computational design system that synthesizes custom robot arms from a library of modular parts by searching
    over combinatorial arrangements to track user-specified end-effector trajectories.
  zh: We present an interactive, computational design system for creating custom robotic arms given high-level task descriptions
    and environmental constraints. Various task requirements can be encoded as desired motion trajectories for the robot arm's
    end-effector. Given such end-effector trajectories, our system enables on-demand design of custom robot arms using a library
    of modular and reconfigurable parts such as actuators and connecting links. By searching through the combinatorial set
    of possible arrangements of these parts, our method generates a functional, as-simple-as-possible robot arm th
  ko: 모듈형 부품 라이브러리의 조합적 배열을 탐색하여 사용자가 지정한 종단 효과기 궤적을 추적할 수 있는 맞춤형 로봇 팔을 합성하는 상호작용형 컴퓨터 설계 시스템이다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- robotic_arm_design
- modular_robotics
- computational_design
- task_specific_design
- kinematic_synthesis
- trajectory_tracking
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1806.07419v1.
sources:
- id: src_001
  type: paper
  title: Automatic Design of Task-specific Robotic Arms
  url: https://arxiv.org/abs/1806.07419
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
We present an interactive, computational design system for creating custom robotic arms given high-level task descriptions and environmental constraints. Various task requirements can be encoded as desired motion trajectories for the robot arm's end-effector. Given such end-effector trajectories, our system enables on-demand design of custom robot arms using a library of modular and reconfigurable parts such as actuators and connecting links. By searching through the combinatorial set of possible arrangements of these parts, our method generates a functional, as-simple-as-possible robot arm that is capable of tracking the desired trajectories. We demonstrate our system's capabilities by creating robot arm designs in simulation, for various trajectory following scenarios.

## 核心内容
We present an interactive, computational design system for creating custom robotic arms given high-level task descriptions and environmental constraints. Various task requirements can be encoded as desired motion trajectories for the robot arm's end-effector. Given such end-effector trajectories, our system enables on-demand design of custom robot arms using a library of modular and reconfigurable parts such as actuators and connecting links. By searching through the combinatorial set of possible arrangements of these parts, our method generates a functional, as-simple-as-possible robot arm that is capable of tracking the desired trajectories. We demonstrate our system's capabilities by creating robot arm designs in simulation, for various trajectory following scenarios.

## 参考
- http://arxiv.org/abs/1806.07419v1


