---
$id: rel_ent_paper_jetson_pi_onboard_real_time_robot_2026_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_jetson_pi_onboard_real_time_robot_2026
  name:
    en: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference'
    zh: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference'
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference uses Flow matching.'
  zh: 'Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference使用流匹配。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用Flow matching展开技术来减少图调用次数。 | 证据: - **Flow
    matching 展开**：将 10 步去噪迭代融合为统一计算图，减少图调用次数。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jetson_pi_onboard_real_time_robot_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_jetson_pi_onboard_real_time_robot_2026/
  accessed_at: '2026-08-06'
---
