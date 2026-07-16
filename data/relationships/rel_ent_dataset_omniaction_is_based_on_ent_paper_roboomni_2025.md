---
$id: rel_ent_dataset_omniaction_is_based_on_ent_paper_roboomni_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_dataset_omniaction
  name:
    en: OmniAction Dataset
    zh: OmniAction 数据集
target:
  id: ent_paper_roboomni_2025
  name:
    en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
    zh: RoboOmni：全模态上下文中的主动式机器人操作
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'OmniAction Dataset is based on RoboOmni: Proactive Robot Manipulation in Omni-modal Context.'
  zh: OmniAction 数据集基于RoboOmni：全模态上下文中的主动式机器人操作。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: OmniAction 被引入并用于训练 RoboOmni 模型。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_dataset_omniaction
  url: https://kg.rounds-tech.com/entry/ent_dataset_omniaction/
  accessed_at: '2026-07-16'
---
