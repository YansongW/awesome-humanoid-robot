---
$id: rel_ent_paper_prism_personalized_robotic_dat_2026_evaluates_on_ent_benchmark_libero_plus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_prism_personalized_robotic_dat_2026
  name:
    en: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis'
    zh: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis'
target:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis is evaluated on LIBERO-Plus.'
  zh: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis评测于LIBERO-Plus。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: PRISM生成的策略在LIBERO和LIBERO-Plus基准上进行了评估，LIBERO-Plus是评估基准之一。
    | 证据: Extensive experiments show that policies trained on PRISM-generated datasets outperform those trained on baseline-generated
    datasets on LIBERO and LIBERO-Plus, achieve up to 100\% success rate on three real-world manipulation tasks, and maintain
    stro'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_prism_personalized_robotic_dat_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_prism_personalized_robotic_dat_2026/
  accessed_at: '2026-07-16'
---
