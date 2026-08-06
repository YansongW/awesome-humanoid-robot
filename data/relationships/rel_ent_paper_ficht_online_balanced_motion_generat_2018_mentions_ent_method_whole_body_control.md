---
$id: rel_ent_paper_ficht_online_balanced_motion_generat_2018_mentions_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_ficht_online_balanced_motion_generat_2018
  name:
    en: Online Balanced Motion Generation for Humanoid Robots
    zh: 人形机器人在线平衡运动生成
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Online Balanced Motion Generation for Humanoid Robots mentions Whole-Body Control (WBC).
  zh: 人形机器人在线平衡运动生成提及全身控制（WBC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 现有 WBC 方法在低成本平台上的失效，本质上是"控制架构与硬件能力"的错配：位置控制关节、无力矩传感器、低扭矩/重量比，这三者叠加使得依赖高频力矩指令与力反馈的优化类方法根本无法闭环。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ficht_online_balanced_motion_generat_2018
  url: https://kg.rounds-tech.com/entry/ent_paper_ficht_online_balanced_motion_generat_2018/
  accessed_at: '2026-08-06'
---
