---
$id: ent_rom_test
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: Range of Motion Test
  zh: 活动范围测试
  ko: 가동 범위 테스트
summary:
  en: A benchmark that measures the reachable joint angles of a robot hand or limb,
    used to evaluate workspace coverage and joint flexibility.
  zh: 一种测量机器人手或肢体可达关节角度的基准，用于评估工作空间覆盖范围和关节灵活性。
  ko: 로봇 손이나 사지의 도달 가능한 관절 각도를 측정하여 작업 공간 커버리지와 관절 유연성을 평가하는 벤치마크입니다.
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
- rom
- range_of_motion
- benchmark
- workspace
- dexterous_hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard benchmark referenced in the RUKA paper for joint reachability evaluation.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---

# Range of Motion Test

## 抽象

> **生活实例**：它就像体检时测量你手臂能举多高、膝盖能弯多少——用角度范围来判断关节灵活性和可达工作空间。

> **自然语言逻辑**：活动范围（ROM）测试测量机器人手或肢体每个关节能达到的最小和最大角度；它决定了机器人能覆盖多大比例的人类工作空间，是抓取规划、全身控制和手设计的基础输入之一。

## Overview

The Range of Motion (ROM) Test measures the minimum and maximum angles achievable at each joint. In robot hands, it determines how much of the human hand workspace the robot can cover.

## Relevance to Humanoid Robotics

Workspace coverage is a fundamental requirement for humanoid manipulation. ROM testing allows direct comparison between humanoid hands and provides input for higher-level grasp-planning and control algorithms.
