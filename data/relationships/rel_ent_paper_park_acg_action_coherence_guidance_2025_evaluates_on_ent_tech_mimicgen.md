---
$id: rel_ent_paper_park_acg_action_coherence_guidance_2025_evaluates_on_ent_tech_mimicgen
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_park_acg_action_coherence_guidance_2025
  name:
    en: 'ACG: Action Coherence Guidance for Flow-based VLA models'
    zh: ACG
target:
  id: ent_tech_mimicgen
  name:
    en: MimicGen
    zh: MimicGen
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models is evaluated on MimicGen.'
  zh: ACG评测于MimicGen。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: ACG在RoboCasa、DexMimicGen和真实世界SO-101任务上进行了评估，MimicGen是评估环境之一。
    | 证据: Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and
    boosts success rates across diverse manipulation tasks.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_park_acg_action_coherence_guidance_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_park_acg_action_coherence_guidance_2025/
  accessed_at: '2026-07-16'
---
