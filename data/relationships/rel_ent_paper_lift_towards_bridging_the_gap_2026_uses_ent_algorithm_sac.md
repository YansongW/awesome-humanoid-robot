---
$id: rel_ent_paper_lift_towards_bridging_the_gap_2026_uses_ent_algorithm_sac
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_lift_towards_bridging_the_gap_2026
  name:
    en: 'LIFT: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control'
    zh: LIFT：用大批量 SAC 预训练 + 物理先验世界模型微调，把人形 sim-to-real 压到 1 小时
target:
  id: ent_algorithm_sac
  name:
    en: Soft Actor-Critic (SAC)
    zh: 软演员-评论家（SAC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'LIFT: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control uses Soft
    Actor-Critic (SAC).'
  zh: LIFT：用大批量 SAC 预训练 + 物理先验世界模型微调，把人形 sim-to-real 压到 1 小时使用软演员-评论家（SAC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文提出的LIFT框架结合了大批量Soft Actor-Critic（SAC）预训练，因此使用了SAC算法。
    | 证据: The LIFT framework proposed in this paper aims to bridge this gap by combining large-batch Soft Actor-Critic (SAC)
    pre-training with a physics-prior-based world model for fine-tuning, significantly reducing the cost of transferring from
    simulation to'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_lift_towards_bridging_the_gap_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_lift_towards_bridging_the_gap_2026/
  accessed_at: '2026-07-16'
---
