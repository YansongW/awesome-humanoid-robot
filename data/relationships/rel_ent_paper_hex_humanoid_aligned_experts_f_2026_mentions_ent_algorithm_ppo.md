---
$id: rel_ent_paper_hex_humanoid_aligned_experts_f_2026_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_hex_humanoid_aligned_experts_f_2026
  name:
    en: 'HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation'
    zh: HEX｜用于跨实体全身操作的人形对齐专家
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation mentions Proximal Policy Optimization (PPO).'
  zh: HEX｜用于跨实体全身操作的人形对齐专家提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: The implementation path of HEX is to first encode
    the ontology state and joint sequence into multimodal representation, and then use PPO/RL policy training, VLA multimodal
    action model, VLM semantic planning/routing to predict the whole-body trajectory/action sequence, and low-level controller
    targe'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hex_humanoid_aligned_experts_f_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_hex_humanoid_aligned_experts_f_2026/
  accessed_at: '2026-07-16'
---
