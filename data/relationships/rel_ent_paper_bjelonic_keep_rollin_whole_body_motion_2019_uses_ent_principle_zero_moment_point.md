---
$id: rel_ent_paper_bjelonic_keep_rollin_whole_body_motion_2019_uses_ent_principle_zero_moment_point
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_bjelonic_keep_rollin_whole_body_motion_2019
  name:
    en: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots
    zh: Keep Rollin'——轮腿四足机器人的全身运动控制与规划
target:
  id: ent_principle_zero_moment_point
  name:
    en: Zero Moment Point (ZMP)
    zh: 零力矩点（ZMP）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots uses Zero Moment Point (ZMP).
  zh: Keep Rollin'——轮腿四足机器人的全身运动控制与规划使用零力矩点（ZMP）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该论文使用基于ZMP的在线优化框架。 | 证据: - **运动优化器**：基于零力矩点（ZMP）的在线优化框架，持续更新全身参考轨迹，将车轮的非完整滚动约束作为关键优化条件。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_bjelonic_keep_rollin_whole_body_motion_2019
  url: https://kg.rounds-tech.com/entry/ent_paper_bjelonic_keep_rollin_whole_body_motion_2019/
  accessed_at: '2026-07-31'
---
