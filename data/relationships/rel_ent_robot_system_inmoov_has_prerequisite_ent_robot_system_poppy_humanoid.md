---
$id: rel_ent_robot_system_inmoov_has_prerequisite_ent_robot_system_poppy_humanoid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_inmoov
  name:
    en: InMoov
    zh: InMoov 3D 打印人形机器人
target:
  id: ent_robot_system_poppy_humanoid
  name:
    en: Poppy Humanoid
    zh: Poppy 人形机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: InMoov has prerequisite Poppy Humanoid.
  zh: InMoov 3D 打印人形机器人前置依赖Poppy 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: InMoov和Poppy都是开源3D打印人形机器人，Poppy提供了更早的技术参考。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
