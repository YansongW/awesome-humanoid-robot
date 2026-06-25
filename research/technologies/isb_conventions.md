---
$id: ent_isb_conventions
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: ISB Conventions for Joint Coordinate Systems
  zh: ISB关节坐标系约定
  ko: ISB 관절 좌표계 관례
summary:
  en: Standardized conventions from the International Society of Biomechanics for defining
    joint coordinate systems, sign conventions, and functional ranges of motion in human
    biomechanics.
  zh: 国际生物力学学会（ISB）制定的标准化约定，用于定义人体生物力学中的关节坐标系、符号约定和功能活动范围。
  ko: 인체 생체역학에서 관절 좌표계, 부호 규칙 및 기능적 가동 범위를 정의하기 위한 국제생체역학회(ISB)의 표준화된 관례입니다.
domains:
- 10_evaluation_benchmarks
- 06_design_engineering
layers:
- validation_markets
- midstream
functional_roles:
- knowledge
- policy
tags:
- isb
- biomechanics
- standard
- joint_coordinates
- range_of_motion
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Widely cited biomechanics standard.
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-25'
---

## Overview

ISB conventions provide a common reference frame for describing human joint kinematics. They standardize coordinate axes, rotation sequences, and sign conventions so that studies and robot designs can be compared directly.

## Relevance to Humanoid Robotics

Humanoid robot benchmarking and design benefit from ISB conventions because they allow direct comparison between human joint capabilities and robot joint capabilities using the same coordinate systems.
