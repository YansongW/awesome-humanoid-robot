---
$id: rel_ent_paper_amo_adaptive_motion_optimizati_2025_mentions_ent_paper_amass
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_amo_adaptive_motion_optimizati_2025
  name:
    en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
    zh: AMO｜超灵巧人形全身控制的自适应运动优化
target:
  id: ent_paper_amass
  name:
    en: AMASS
    zh: AMASS
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control mentions AMASS.'
  zh: AMO｜超灵巧人形全身控制的自适应运动优化提及AMASS。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: **AMO数据集生成**：随机采样AMASS上半身运动 + 随机躯干命令（rpy, h），用Crocoddyl的BoxFDDP求解多接触最优控制问题（MCOP），生成满足动力学约束的全身参考运动。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_amo_adaptive_motion_optimizati_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_amo_adaptive_motion_optimizati_2025/
  accessed_at: '2026-08-06'
---
