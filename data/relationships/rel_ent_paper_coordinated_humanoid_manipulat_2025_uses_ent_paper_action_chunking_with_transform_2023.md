---
$id: rel_ent_paper_coordinated_humanoid_manipulat_2025_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_coordinated_humanoid_manipulat_2025
  name:
    en: Coordinated Humanoid Manipulation with Choice Policies
    zh: 具有选择策略的协调人形操作
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Coordinated Humanoid Manipulation with Choice Policies uses Action Chunking with Transformers.
  zh: 具有选择策略的协调人形操作使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用ACT方法对数据进行预处理。 | 证据: 随后，采用ACT（Action Chunking
    with Transformers）或行为克隆方法对数据进行预处理，将连续动作序列离散化为可训练的“动作块”。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_coordinated_humanoid_manipulat_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_coordinated_humanoid_manipulat_2025/
  accessed_at: '2026-07-16'
---
