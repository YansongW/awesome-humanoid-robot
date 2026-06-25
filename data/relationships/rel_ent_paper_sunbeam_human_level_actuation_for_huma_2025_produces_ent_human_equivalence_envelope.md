---
$id: rel_ent_paper_sunbeam_human_level_actuation_for_huma_2025_produces_ent_human_equivalence_envelope
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
  id: ent_human_equivalence_envelope
  name:
    en: Human-Equivalence Envelope (HEE)
    zh: 人等效包络（HEE）
    ko: 인간 등가 영역(HEE)
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 10_evaluation_benchmarks
description:
  en: The paper defines HEE to specify per-joint torque-power requirements at task-relevant
    postures and rates.
  zh: 论文定义了HEE以规定任务相关姿态和速度下的单关节扭矩-功率需求。
  ko: 본 논문은 작업 관련 자세와 속도에서 관절별 토크-전력 요구사항을 규정하기 위해 HEE를 정의한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Second, Human-Equivalence Envelopes
    (HEE) define per-joint requirements by measuring whether a robot meets human torque
    and power simultaneously at the same joint angle and rate (q, ω), weighted by
    positive mechanical work in task-specific bands.'
sources:
- id: src_001
  type: paper
  title: Human-Level Actuation for Humanoids
  url: https://arxiv.org/abs/2511.06796
  date: '2025'
  accessed_at: '2026-06-22'
---

