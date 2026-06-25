---
$id: rel_ent_paper_sunbeam_human_level_actuation_for_huma_2025_is_based_on_ent_deleva_anthropometry
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
  id: ent_deleva_anthropometry
  name:
    en: de Leva Anthropometry
    zh: de Leva人体测量学
    ko: de Leva 인체측정법
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 10_evaluation_benchmarks
description:
  en: The paper uses de Leva anthropometry to derive torque, power, and rate targets
    for a 75 kg reference body.
  zh: 论文使用de Leva人体测量学推导出75公斤参考人体的扭矩、功率和速率目标。
  ko: 본 논문은 75kg 기준 신체에 대한 토크, 전력 및 속도 목표를 도출하기 위해 de Leva 인체측정법을 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: A synthesis of published human
    biomechanics data into absolute torque, power, and rate targets for a 75 kg reference
    body using de Leva anthropometry.'
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-22'
---

