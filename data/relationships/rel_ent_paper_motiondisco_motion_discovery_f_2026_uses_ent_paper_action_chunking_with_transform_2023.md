---
$id: rel_ent_paper_motiondisco_motion_discovery_f_2026_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_motiondisco_motion_discovery_f_2026
  name:
    en: 'MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation'
    zh: MotionDisco｜用于极端人形移动操作的运动发现
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation uses Action Chunking with Transformers.'
  zh: MotionDisco｜用于极端人形移动操作的运动发现使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: MotionDisco论文使用ACT（Action Chunking with Transformers）算法进行模仿学习。
    | 证据: 其次，利用 ACT（Action Chunking with Transformers）等行为克隆算法对示范数据进行模仿学习，并结合逆运动学（IK）将人类运动重定向至机器人运动学约束下，生成全身轨迹。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_motiondisco_motion_discovery_f_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_motiondisco_motion_discovery_f_2026/
  accessed_at: '2026-07-16'
---
