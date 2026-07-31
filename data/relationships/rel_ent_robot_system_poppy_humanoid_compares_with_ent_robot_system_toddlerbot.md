---
$id: rel_ent_robot_system_poppy_humanoid_compares_with_ent_robot_system_toddlerbot
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_robot_system_poppy_humanoid
  name:
    en: Poppy Humanoid
    zh: Poppy 人形机器人
target:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Poppy Humanoid compares with ToddlerBot.
  zh: Poppy 人形机器人compares_withToddlerBot 幼儿机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据建议新手转看ToddlerBot等新一代平台，隐含Poppy Humanoid与ToddlerBot的对比。
    | 证据: - 门槛：约 €9,000 的套件价格远超当代替代品；主仓库停更意味着新系统/新 Python 版本兼容性要自己踩坑；25 台 Dynamixel 的采购与维护成本高；想做行走/RL 的新手建议转看 ToddlerBot 等新一代平台。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_poppy_humanoid
  url: https://kg.rounds-tech.com/entry/ent_robot_system_poppy_humanoid/
  accessed_at: '2026-07-31'
---
