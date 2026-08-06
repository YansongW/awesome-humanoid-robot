---
$id: rel_ent_paper_modskill_physical_character_skill_modula_2025_uses_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_modskill_physical_character_skill_modula_2025
  name:
    en: 'ModSkill: Physical Character Skill Modularization'
    zh: 'ModSkill: Physical Character Skill Modularization'
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ModSkill: Physical Character Skill Modularization uses HumanML3D.'
  zh: 'ModSkill: Physical Character Skill Modularization使用HumanML3D。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用HumanML3D的文本描述作为条件来合成新的运动序列。 | 证据: - 对每个失败样本（跟踪误差超阈值），使用现成文本到运动扩散模型，以
    HumanML3D 文本描述为条件，合成 N=3 个新运动序列。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_modskill_physical_character_skill_modula_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_modskill_physical_character_skill_modula_2025/
  accessed_at: '2026-08-06'
---
