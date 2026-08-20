---
$id: rel_ent_paper_universal_manipulation_exoskeleton_compl_2026_uses_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_universal_manipulation_exoskeleton_compl_2026
  name:
    en: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback'
    zh: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback'
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback uses Action
    Chunking with Transformers.'
  zh: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback使用基于Transformer的动作分块。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用ACT（Action Chunking with Transformers）作为其策略架构的一部分。
    | 证据: - **学习**：ACT（Action Chunking with Transformers），ResNet18 骨干，力矩数据与关节位置同样处理，嵌入附加到图像嵌入后输入 Transformer 编码器-解码器，输出期望关节位置。
    | WP4 2026-08-11: endpoint id rewritten (ent_paper_universal_manipulation_exoskeleton_compl_2026→ent_paper_universal_manipulation_exoskeleton_compl_2026,
    ent_method_action_chunking_transformer→ent_method_action_chunking_transformer); original file rel_ent_paper_universal_manipulation_exoskeleton_compl_2026_uses_ent_paper_action_chunking_with_transform_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_universal_manipulation_exoskeleton_compl_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_universal_manipulation_exoskeleton_compl_2026/
  accessed_at: '2026-08-06'
---
