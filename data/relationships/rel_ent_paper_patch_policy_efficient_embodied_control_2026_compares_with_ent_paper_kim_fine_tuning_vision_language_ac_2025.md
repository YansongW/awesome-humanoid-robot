---
$id: rel_ent_paper_patch_policy_efficient_embodied_control_2026_compares_with_ent_paper_kim_fine_tuning_vision_language_ac_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_patch_policy_efficient_embodied_control_2026
  name:
    en: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
    zh: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations'
target:
  id: ent_paper_kim_fine_tuning_vision_language_ac_2025
  name:
    en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
    zh: OpenVLA-OFT
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Patch Policy: Efficient Embodied Control via Dense Visual Representations compares with Fine-Tuning Vision-Language-Action
    Models: Optimizing Speed and Success.'
  zh: 'Patch Policy: Efficient Embodied Control via Dense Visual Representationscompares_withOpenVLA-OFT。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文与Fine-Tuning Vision-Language-Action Models的GPU训练时间进行对比。
    | 证据: 5 GPU-hours（1xL40S），对比 OpenVLA-OFT 的 16 GPU-hours 与 ACT 的 24 GPU-hours，同时保留 DINOv2/WebSSL 等大规模预训练的表征收益。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_patch_policy_efficient_embodied_control_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_patch_policy_efficient_embodied_control_2026/
  accessed_at: '2026-08-06'
---
