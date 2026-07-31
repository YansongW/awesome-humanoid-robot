---
$id: rel_ent_paper_omnicontrol_control_any_joint_2023_evaluates_on_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_omnicontrol_control_any_joint_2023
  name:
    en: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation'
    zh: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation'
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation is evaluated on HumanML3D.'
  zh: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation评测于HumanML3D。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该论文在HumanML3D数据集上进行了实验验证。 | 证据: 实验在 HumanML3D
    和 KIT-ML 数据集上验证，OmniControl 在骨盆控制任务上显著超越现有方法，并在其他关节约束场景中展现出良好效果。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_omnicontrol_control_any_joint_2023
  url: https://kg.rounds-tech.com/entry/ent_paper_omnicontrol_control_any_joint_2023/
  accessed_at: '2026-07-31'
---
