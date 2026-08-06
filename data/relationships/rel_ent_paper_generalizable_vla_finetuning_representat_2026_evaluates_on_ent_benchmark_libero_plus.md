---
$id: rel_ent_paper_generalizable_vla_finetuning_representat_2026_evaluates_on_ent_benchmark_libero_plus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_generalizable_vla_finetuning_representat_2026
  name:
    en: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment
    zh: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment
target:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment is evaluated on LIBERO-Plus.
  zh: Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment评测于LIBERO-Plus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该方法在LIBERO-Plus基准上进行了评估。 | 证据: 该方法在 LIBERO-PRO、LIBERO-Plus、CALVIN
    及真实 xArm7 机器人上显著提升分布外泛化与长时程控制，并首次直接量化了联合训练 VLA 中语言-动作错位的程度及其与任务成功的相关性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_generalizable_vla_finetuning_representat_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_generalizable_vla_finetuning_representat_2026/
  accessed_at: '2026-08-06'
---
