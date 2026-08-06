---
$id: rel_ent_paper_amo_adaptive_motion_optimizati_2025_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_amo_adaptive_motion_optimizati_2025
  name:
    en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
    zh: AMO｜超灵巧人形全身控制的自适应运动优化
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control uses Action Chunking with Transformers.'
  zh: AMO｜超灵巧人形全身控制的自适应运动优化使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 自主策略使用ACT（Action Chunking with Transformers）作为方法。
    | 证据: - 自主策略：ACT（Action Chunking with Transformers）+ DinoV2视觉编码器，输入双目图像（2×16×22×384 tokens），输出 [q_head, q_dual-arm, q_dual-hand,
    v, rpy, h]。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_amo_adaptive_motion_optimizati_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_amo_adaptive_motion_optimizati_2025/
  accessed_at: '2026-08-06'
---
