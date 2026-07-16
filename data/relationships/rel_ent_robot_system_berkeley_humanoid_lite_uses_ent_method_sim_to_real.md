---
$id: rel_ent_robot_system_berkeley_humanoid_lite_uses_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Berkeley Humanoid Lite's RL locomotion policies achieve zero-shot sim-to-real transfer to the real
    robot.
  zh: Berkeley Humanoid Lite 的 RL 运动控制策略实现零样本 sim-to-real 迁移上真机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/berkeley-humanoid-lite.md 确认零样本 sim-to-real（论文口径）。
sources:
- id: src_001
  type: website
  title: Berkeley Humanoid Lite paper arXiv:2504.17249
  url: https://arxiv.org/abs/2504.17249
  accessed_at: '2026-07-01'
---
