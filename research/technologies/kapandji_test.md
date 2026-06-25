---
$id: ent_kapandji_test
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: Kapandji Test
  zh: Kapandji测试
  ko: Kapandji 테스트
summary:
  en: A clinical test of thumb opposability and digital dexterity, adapted in robotics
    to evaluate thumb range of motion and opposition quality in dexterous robot hands.
  zh: 一种临床拇指对掌能力和手指灵活性测试，在机器人学中被改编用于评估灵巧机器人手的拇指活动范围和对掌质量。
  ko: 임상적으로 엄지 대립 능력과 손가락 재주를 측정하는 테스트로, 로봇공학에서 능숙한 로봇 손의 엄지 가동 범위와 대립 품질을 평가하기 위해 채택되었습니다.
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
- kapandji
- thumb
- opposition
- benchmark
- dexterous_hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard clinical test referenced in the RUKA paper for thumb opposability evaluation.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-25'
---

## Overview

The Kapandji Test scores thumb opposition by asking a subject to touch successive points on the hand, from the index distal phalanx to the hypothenar eminence. In robotics, it is used as a simple, interpretable benchmark for thumb dexterity in humanoid hands.

## Relevance to Humanoid Robotics

Thumb opposition is essential for many human-like grasps and in-hand manipulations. The Kapandji Test provides a standardized way to compare this capability across robot hand designs.
