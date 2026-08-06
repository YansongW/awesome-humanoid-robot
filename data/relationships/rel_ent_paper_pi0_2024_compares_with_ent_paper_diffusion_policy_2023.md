---
$id: rel_ent_paper_pi0_2024_compares_with_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_pi0_2024
  name:
    en: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
    zh: π0：用于通用机器人控制的视觉-语言-动作流模型
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'π0: A Vision-Language-Action Flow Model for General Robot Control compares with Diffusion Policy.'
  zh: π0：用于通用机器人控制的视觉-语言-动作流模型compares_with扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: π0将Diffusion Policy作为此前的主流方案之一进行对比。 | 证据: 机器人学习长期受困于数据稀缺、泛化差和鲁棒性不足，此前的主流方案要么是任务特定的行为克隆（如
    ACT、Diffusion Policy），要么是试图用单一模型覆盖多任务的 VLA（如 OpenVLA、RT-2），但后者受限于自回归离散化动作表示，无法支持高频控制和动作分块，且缺乏大规模预训练数据的支撑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_pi0_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_pi0_2024/
  accessed_at: '2026-08-06'
---
