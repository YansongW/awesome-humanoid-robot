---
$id: rel_ent_paper_omniretarget_interaction_prese_2026_1_uses_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_omniretarget_interaction_prese_2026_1
  name:
    en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
    zh: OmniRetarget｜人形全身移动操作和场景交互的交互保存数据生成
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
    uses Unitree G1 Humanoid Robot.'
  zh: OmniRetarget｜人形全身移动操作和场景交互的交互保存数据生成使用Unitree G1 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该论文使用OmniRetarget生成的数据来训练Unitree G1人形机器人的策略。
    | 证据: - **下游任务**：使用 OmniRetarget 生成的高质量数据训练 Unitree G1 人形机器人的本体感觉强化学习策略，仅需 5 个奖励项和简单的域随机化（所有任务共享），无需学习课程，即可成功执行长达 30 秒的跑酷和移动操作技能（如跳跃、攀爬、搬运物体）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_omniretarget_interaction_prese_2026_1
  url: https://kg.rounds-tech.com/entry/ent_paper_omniretarget_interaction_prese_2026_1/
  accessed_at: '2026-07-31'
---
