---
$id: ent_paper_cmr_contractive_mapping_embedd_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
  zh: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
  ko: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
summary:
  en: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains is a 2026 work on locomotion
    for humanoid robots.'
  zh: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains is a 2026 work on locomotion
    for humanoid robots.'
  ko: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains is a 2026 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cmr
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.03511v1.
sources:
- id: src_001
  type: paper
  title: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains (arXiv)'
  url: https://arxiv.org/abs/2602.03511
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Robust disturbance rejection remains a longstanding challenge in humanoid locomotion, particularly on unstructured terrains where sensing is unreliable and model mismatch is pronounced. While perception information, such as height map, enhances terrain awareness, sensor noise and sim-to-real gaps can destabilize policies in practice. In this work, we provide theoretical analysis that bounds the return gap under observation noise, when the induced latent dynamics are contractive. Furthermore, we present Contractive Mapping for Robustness (CMR) framework that maps high-dimensional, disturbance-prone observations into a latent space, where local perturbations are attenuated over time. Specifically, this approach couples contrastive representation learning with Lipschitz regularization to preserve task-relevant geometry while explicitly controlling sensitivity. Notably, the formulation can be incorporated into modern deep reinforcement learning pipelines as an auxiliary loss term with minimal additional technical effort required. Further, our extensive humanoid experiments show that CMR potently outperforms other locomotion algorithms under increased noise.

## 核心内容
Robust disturbance rejection remains a longstanding challenge in humanoid locomotion, particularly on unstructured terrains where sensing is unreliable and model mismatch is pronounced. While perception information, such as height map, enhances terrain awareness, sensor noise and sim-to-real gaps can destabilize policies in practice. In this work, we provide theoretical analysis that bounds the return gap under observation noise, when the induced latent dynamics are contractive. Furthermore, we present Contractive Mapping for Robustness (CMR) framework that maps high-dimensional, disturbance-prone observations into a latent space, where local perturbations are attenuated over time. Specifically, this approach couples contrastive representation learning with Lipschitz regularization to preserve task-relevant geometry while explicitly controlling sensitivity. Notably, the formulation can be incorporated into modern deep reinforcement learning pipelines as an auxiliary loss term with minimal additional technical effort required. Further, our extensive humanoid experiments show that CMR potently outperforms other locomotion algorithms under increased noise.

## 参考
- http://arxiv.org/abs/2602.03511v1

