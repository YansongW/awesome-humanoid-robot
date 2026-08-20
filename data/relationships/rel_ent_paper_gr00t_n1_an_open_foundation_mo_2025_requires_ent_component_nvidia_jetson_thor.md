---
$id: rel_ent_paper_gr00t_n1_an_open_foundation_mo_2025_requires_ent_component_nvidia_jetson_thor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_paper_gr00t_n1_an_open_foundation_mo_2025
  name:
    en: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
    zh: GR00T N1｜通用人形机器人的开放基础模型
target:
  id: ent_component_nvidia_jetson_thor
  name:
    en: NVIDIA Jetson Thor
    zh: NVIDIA Jetson Thor
domains:
  source:
  - 07_ai_models_algorithms
  target:
  - 02_components
  - 07_ai_models_algorithms
  - 08_software_middleware
description:
  en: GR00T N1 requires Jetson Thor-class compute for real-time onboard inference.
  zh: GR00T N1需要Jetson Thor级计算进行实时 onboard 推理。
  ko: GR00T N1은 실시간 온보드 추론을 위해 Jetson Thor급 컴퓨팅이 필요합니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_paper_gr00t_n1_an_open_foundation_mo_2025→ent_paper_gr00t_n1_an_open_foundation_mo_2025, ent_component_nvidia_jetson_thor→ent_component_nvidia_jetson_thor);
    original file rel_ent_paper_nvidia_gr00t_n1_2025_requires_ent_component_nvidia_jetson_thor.'
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---
