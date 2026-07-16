---
$id: rel_ent_paper__2025_uses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper__2025
  name:
    en: Humanoid Robot Motion and Operation｜Progress and Challenges in Control Planning and Learning
    zh: 人形机器人运动与操作｜控制规划和学习的进展与挑战
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Humanoid Robot Motion and Operation｜Progress and Challenges in Control Planning and Learning uses Diffusion Policy.
  zh: 人形机器人运动与操作｜控制规划和学习的进展与挑战使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文中描述系统采用扩散策略（Diffusion Policy）来生成可执行的动作命令。
    | 证据: 随后，基于恢复的表征，系统采用三种互补的生成策略——ACT（Action Chunking with Transformers）行为克隆模仿学习、扩散策略（Diffusion Policy）以及流匹配（Flow Matching）——来生成可执行的动作命令。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper__2025
  url: https://kg.rounds-tech.com/entry/ent_paper__2025/
  accessed_at: '2026-07-16'
---
