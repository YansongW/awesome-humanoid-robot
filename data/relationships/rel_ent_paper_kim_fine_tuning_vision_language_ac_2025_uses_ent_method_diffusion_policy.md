---
$id: rel_ent_paper_kim_fine_tuning_vision_language_ac_2025_uses_ent_method_diffusion_policy
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_kim_fine_tuning_vision_language_ac_2025
  name:
    en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
    zh: OpenVLA-OFT
target:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success uses Diffusion Policy.'
  zh: OpenVLA-OFT使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文的微调方法使OpenVLA能够执行任务，但证据中未直接提及使用Diffusion Policy。
    | 证据: In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency
    control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes,
    as well a'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_kim_fine_tuning_vision_language_ac_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_kim_fine_tuning_vision_language_ac_2025/
  accessed_at: '2026-07-16'
---
