---
$id: rel_ent_method_action_chunking_transformer_mentions_ent_method_openvla
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
target:
  id: ent_method_openvla
  name:
    en: OpenVLA
    zh: OpenVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Action Chunking with Transformers (ACT) mentions OpenVLA.
  zh: 动作分块变压器（ACT）提及OpenVLA。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **局限与后续方向**：原始 ACT 只支持单任务、单场景演示分布，对语言指令与开放物体的泛化能力有限；后续的扩散策略、OpenVLA、π0
    等工作在动作头设计、预训练规模与多任务指令条件化上对其进行了扩展。'
sources:
- id: src_001
  type: other
  title: KG body of ent_method_action_chunking_transformer
  url: https://kg.rounds-tech.com/entry/ent_method_action_chunking_transformer/
  accessed_at: '2026-07-16'
---
