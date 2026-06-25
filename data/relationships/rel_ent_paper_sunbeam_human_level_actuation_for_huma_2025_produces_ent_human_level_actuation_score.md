---
$id: rel_ent_paper_sunbeam_human_level_actuation_for_huma_2025_produces_ent_human_level_actuation_score
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: produces
source:
  id: ent_paper_sunbeam_human_level_actuation_for_huma_2025
  name:
    en: Human-Level Actuation for Humanoids
    zh: 人形机器人的类人驱动能力
    ko: 휴머노이드를 위한 인간 수준 구동
target:
  id: ent_human_level_actuation_score
  name:
    en: Human-Level Actuation Score (HLAS)
    zh: 类人驱动评分（HLAS）
    ko: 인간 수준 구동 점수(HLAS)
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 10_evaluation_benchmarks
description:
  en: The paper introduces HLAS as a scalar benchmarking metric for humanoid actuation.
  zh: 论文提出了HLAS作为人形机器人驱动的标量基准指标。
  ko: 본 논문은 휴머노이드 구동을 위한 스칼라 벤치마크 지표로 HLAS를 제안한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Third, the Human-Level Actuation
    Score (HLAS) aggregates six physically grounded factors: workspace coverage (ROM
    and DoF), HEE coverage, torque-mode bandwidth, efficiency, and thermal sustainability.'
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-22'
---

