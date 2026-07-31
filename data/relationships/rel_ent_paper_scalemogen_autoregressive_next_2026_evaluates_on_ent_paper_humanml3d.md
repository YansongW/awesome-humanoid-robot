---
$id: rel_ent_paper_scalemogen_autoregressive_next_2026_evaluates_on_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_scalemogen_autoregressive_next_2026
  name:
    en: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
    zh: 用下一尺度自回归把文本生成的人体动作做成由粗到细
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation is evaluated on HumanML3D.'
  zh: 用下一尺度自回归把文本生成的人体动作做成由粗到细评测于HumanML3D。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在HumanML3D数据集上进行评估。 | 证据: - **数据集**：在 HumanML3D
    和 SnapMoGen 数据集上进行评估。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_scalemogen_autoregressive_next_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_scalemogen_autoregressive_next_2026/
  accessed_at: '2026-07-31'
---
