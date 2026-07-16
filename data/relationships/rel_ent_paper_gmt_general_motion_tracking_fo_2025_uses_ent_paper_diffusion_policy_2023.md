---
$id: rel_ent_paper_gmt_general_motion_tracking_fo_2025_uses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_gmt_general_motion_tracking_fo_2025
  name:
    en: 'GMT: General Motion Tracking for Humanoid Whole-Body Control'
    zh: GMT｜用于人形全身控制的通用运动跟踪
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'GMT: General Motion Tracking for Humanoid Whole-Body Control uses Diffusion Policy.'
  zh: GMT｜用于人形全身控制的通用运动跟踪使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用扩散策略作为生成模型层的一部分 | 证据: 随后，生成模型层采用扩散策略（Diffusion
    Policy）或流匹配（Flow Matching）技术，将动作生成建模为从噪声到可执行轨迹的逆向扩散过程，能够在多模态动作分布中高效采样。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gmt_general_motion_tracking_fo_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_gmt_general_motion_tracking_fo_2025/
  accessed_at: '2026-07-16'
---
