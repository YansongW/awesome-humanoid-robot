---
$id: rel_ent_paper_sunbeam_human_level_actuation_for_huma_2025_is_based_on_ent_isb_conventions
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_paper_sunbeam_human_level_actuation_for_huma_2025
  name:
    en: Human-Level Actuation for Humanoids
    zh: 人形机器人的类人驱动能力
    ko: 휴머노이드를 위한 인간 수준 구동
target:
  id: ent_isb_conventions
  name:
    en: ISB Biomechanics Conventions
    zh: ISB生物力学约定
    ko: ISB 생체역학 관례
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 06_design_engineering
description:
  en: The paper's DoF atlas standardizes joint coordinates and ranges of motion using
    ISB-based conventions.
  zh: 论文中的自由度图谱使用基于ISB的约定来标准化关节坐标和活动范围。
  ko: 논문의 자유도 아틀라스는 ISB 기반 관례를 사용하여 관절 좌표와 가동 범위를 표준화한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: First, a kinematic DoF atlas
    standardizes joint coordinate systems and ranges of motion using ISB-based conventions,
    ensuring that human and robot joints are compared in the same reference frames.'
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-22'
---

