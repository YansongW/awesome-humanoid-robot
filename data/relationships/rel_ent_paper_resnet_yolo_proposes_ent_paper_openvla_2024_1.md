---
$id: rel_ent_paper_resnet_yolo_proposes_ent_paper_openvla_2024_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: proposes
source:
  id: ent_paper_resnet_yolo
  name:
    en: 经典视觉骨干与实时检测文献簇（ResNet + YOLO 及相关）
    zh: 经典视觉骨干与实时检测文献簇（ResNet + YOLO 及相关）
target:
  id: ent_paper_openvla_2024_1
  name:
    en: OpenVLA
    zh: OpenVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 经典视觉骨干与实时检测文献簇（ResNet + YOLO 及相关） proposes OpenVLA.
  zh: 经典视觉骨干与实时检测文献簇（ResNet + YOLO 及相关）提出OpenVLA。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该文献簇包含视觉骨干网络，与OpenVLA等视觉-语言-动作模型相关。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_resnet_yolo
  url: https://kg.rounds-tech.com/entry/ent_paper_resnet_yolo/
  accessed_at: '2026-07-31'
---
