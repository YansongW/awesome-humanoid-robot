---
$id: rel_ent_paper_pulse_physically_plausible_uni_2026_evaluates_on_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_pulse_physically_plausible_uni_2026
  name:
    en: 'PULSE: Physically Plausible Universal Latent Skill Extraction'
    zh: 物理可行的通用潜在技能提取
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'PULSE: Physically Plausible Universal Latent Skill Extraction is evaluated on Sim-to-Real Transfer.'
  zh: 物理可行的通用潜在技能提取评测于Sim-to-Real迁移。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文PULSE在真实机器人平台上验证了Sim-to-Real迁移的有效性，因此在该场景下评估了该方法。
    | 证据: 此外，该框架在真实机器人平台上的初步部署验证了其Sim-to-Real迁移的有效性，为家庭服务、灾害救援等场景下的通用人形机器人技能库构建提供了关键技术支撑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_pulse_physically_plausible_uni_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_pulse_physically_plausible_uni_2026/
  accessed_at: '2026-07-16'
---
