---
$id: rel_ent_paper_flexible_motion_in_betweening_2024_evaluates_on_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_flexible_motion_in_betweening_2024
  name:
    en: Flexible Motion In-betweening with Diffusion Models
    zh: Flexible Motion In-betweening with Diffusion Models
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Flexible Motion In-betweening with Diffusion Models is evaluated on HumanML3D.
  zh: Flexible Motion In-betweening with Diffusion Models评测于HumanML3D。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该模型在HumanML3D数据集上进行了评估，因此源评估于目标。 | 证据: 该模型在文本条件化的
    HumanML3D 数据集上进行了评估，展示了扩散模型在关键帧插值任务中的通用性和有效性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_flexible_motion_in_betweening_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_flexible_motion_in_betweening_2024/
  accessed_at: '2026-07-31'
---
