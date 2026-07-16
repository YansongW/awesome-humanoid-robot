---
$id: rel_ent_paper_roboomni_2025_serves_ent_benchmark_libero_plus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: serves
source:
  id: ent_paper_roboomni_2025
  name:
    en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
    zh: RoboOmni：全模态上下文中的主动式机器人操作
target:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context serves LIBERO-Plus.'
  zh: RoboOmni：全模态上下文中的主动式机器人操作服务LIBERO-Plus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: RoboOmni 与更广泛的 LIBERO 鲁棒性评测生态相关，尽管其主要评估使用标准
    LIBERO。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_paper_roboomni_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_roboomni_2025/
  accessed_at: '2026-07-16'
---
