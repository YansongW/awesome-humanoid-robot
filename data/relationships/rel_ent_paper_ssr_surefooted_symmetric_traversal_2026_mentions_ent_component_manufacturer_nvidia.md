---
$id: rel_ent_paper_ssr_surefooted_symmetric_traversal_2026_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_ssr_surefooted_symmetric_traversal_2026
  name:
    en: 'SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World'
    zh: 第一视角视觉驱动的人形机器人开放世界稳健穿越
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World mentions NVIDIA.'
  zh: 第一视角视觉驱动的人形机器人开放世界稳健穿越提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **硬件与部署**：深度渲染用NVIDIA Warp实现（每像素并行，不重建BVH），实机用Jetson
    AGX Orin + ONNX Runtime 50 Hz推理；关节增益（Table 14）需按平台调整，跨平台时保留相同训练流程但需重新收集运动先验数据。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ssr_surefooted_symmetric_traversal_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_ssr_surefooted_symmetric_traversal_2026/
  accessed_at: '2026-08-06'
---
