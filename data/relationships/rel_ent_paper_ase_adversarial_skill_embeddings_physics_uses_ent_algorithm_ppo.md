---
$id: rel_ent_paper_ase_adversarial_skill_embeddings_physics_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_ase_adversarial_skill_embeddings_physics
  name:
    en: 'ASE: Adversarial Skill Embeddings for Physics-based Character Control'
    zh: 'ASE: Adversarial Skill Embeddings for Physics-based Character Control'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ASE: Adversarial Skill Embeddings for Physics-based Character Control uses Proximal Policy Optimization (PPO).'
  zh: 'ASE: Adversarial Skill Embeddings for Physics-based Character Control使用近端策略优化（PPO）。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该论文使用强化学习训练物理角色控制，PPO是常用的RL算法。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ase_adversarial_skill_embeddings_physics
  url: https://kg.rounds-tech.com/entry/ent_paper_ase_adversarial_skill_embeddings_physics/
  accessed_at: '2026-07-31'
---
