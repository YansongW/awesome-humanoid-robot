---
$id: rel_ent_paper_demohlm_from_one_demonstration_2025_uses_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_demohlm_from_one_demonstration_2025
  name:
    en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
    zh: DemoHLM｜从单一示范到通用人形移动操作
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation uses Action Chunking with Transformers.'
  zh: DemoHLM｜从单一示范到通用人形移动操作使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明系统采用ACT等模仿学习算法将示范轨迹转化为监督学习问题。 | 证据: 随后，系统采用行为克隆（Behavioral
    Cloning）与 ACT（Action Chunking with Transformers）等模仿学习算法，将采集到的示范轨迹转化为可训练的监督学习问题。 | WP1 2026-08-06: endpoint rewritten (ent_paper_demohlm_from_one_demonstration_2025→ent_paper_demohlm_from_one_demonstration_2025,
    ent_method_action_chunking_transformer→ent_method_action_chunking_transformer) after duplicate merge; original
    file rel_ent_paper_demohlm_from_one_demonstration_2025_1_uses_ent_paper_action_chunking_with_transform_2023. | WP4 2026-08-11:
    endpoint id rewritten (ent_paper_demohlm_from_one_demonstration_2025→ent_paper_demohlm_from_one_demonstration_2025, ent_method_action_chunking_transformer→ent_method_action_chunking_transformer);
    original file rel_ent_paper_demohlm_from_one_demonstration_2025_uses_ent_paper_action_chunking_with_transform_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_demohlm_from_one_demonstration_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_demohlm_from_one_demonstration_2025/
  accessed_at: '2026-07-16'
---
