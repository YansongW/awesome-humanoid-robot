---
$id: ent_principle_current_velocity_position_loops
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Current / Velocity / Position Control Loops
  zh: 电流环/速度环/位置环
  ko: 전류·속도·위치 제어 루프
summary:
  en: The nested feedback-control hierarchy for servo drives, where an inner current loop regulates torque, a velocity loop
    regulates speed, and an outer position loop regulates joint angle.
  zh: 伺服驱动的级联反馈控制层级：内环电流环控制转矩，中间速度环控制转速，外环位置环控制关节角度。
  ko: '서보 드라이브의 중첩 피드백 제어 계층: 내측 전류 루프는 토크, 속도 루프는 속도, 외측 위치 루프는 관절 각도를 제어.'
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- principle
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Curated names and summary from data/gap-entity-polish.yaml; placeholder body rewritten. Pending domain-expert final
    review.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
# Current / Velocity / Position Control Loops / 电流环/速度环/位置环 / 전류·속도·위치 제어 루프

## 摘要

伺服驱动的级联反馈控制层级：内环电流环控制转矩，中间速度环控制转速，外环位置环控制关节角度。

## Abstract

The nested feedback-control hierarchy for servo drives, where an inner current loop regulates torque, a velocity loop regulates speed, and an outer position loop regulates joint angle.

## 요약

서보 드라이브의 중첩 피드백 제어 계층: 내측 전류 루프는 토크, 속도 루프는 속도, 외측 위치 루프는 관절 각도를 제어.


> 本词条对应 Wiki 第 4 章，详细论述见项目 Wiki。

