---
$id: rel_ent_paper_openvla_2024_evaluates_on_ent_dataset_bridgedata_v2_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_openvla_2024
  name:
    en: 'OpenVLA: An Open-Source Vision-Language-Action Model'
    zh: OpenVLA：一个开源的视觉-语言-动作模型
target:
  id: ent_dataset_bridgedata_v2_2023
  name:
    en: BridgeData V2
    zh: BridgeData V2
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: 'OpenVLA: An Open-Source Vision-Language-Action Model is evaluated on BridgeData V2.'
  zh: OpenVLA：一个开源的视觉-语言-动作模型评测于BridgeData V2。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: OpenVLA在BridgeData V2评估中与RT-2-X对比，表明其在该数据集上进行了评估。
    | 证据: OpenVLA打破了这一僵局——它证明了开源模型可以在参数少7倍的情况下，在BridgeData V2评估中比RT-2-X绝对成功率高出20个百分点（70.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_openvla_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_openvla_2024/
  accessed_at: '2026-08-06'
---
