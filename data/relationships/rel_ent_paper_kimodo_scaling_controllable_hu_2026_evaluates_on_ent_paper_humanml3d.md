---
$id: rel_ent_paper_kimodo_scaling_controllable_hu_2026_evaluates_on_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_kimodo_scaling_controllable_hu_2026
  name:
    en: 'Kimodo: Scaling Controllable Human Motion Generation'
    zh: 'Kimodo: Scaling Controllable Human Motion Generation'
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Kimodo: Scaling Controllable Human Motion Generation is evaluated on HumanML3D.'
  zh: 'Kimodo: Scaling Controllable Human Motion Generation评测于HumanML3D。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Kimodo很可能在HumanML3D基准上进行了评估。 | 证据: （d）实验/验证或应用价值：尽管论文未提供具体实验数据，但基于其领域标签与摘要推断，Kimodo很可能在标准运动生成基准（如HumanML3D、KIT
    Motion-Language）上进行了评估，并与现有方法（如MDM、MotionDiffuse）进行了对比。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_kimodo_scaling_controllable_hu_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_kimodo_scaling_controllable_hu_2026/
  accessed_at: '2026-07-31'
---
