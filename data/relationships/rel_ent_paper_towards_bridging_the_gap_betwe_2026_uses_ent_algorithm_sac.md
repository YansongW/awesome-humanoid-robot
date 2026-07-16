---
$id: rel_ent_paper_towards_bridging_the_gap_betwe_2026_uses_ent_algorithm_sac
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_towards_bridging_the_gap_betwe_2026
  name:
    en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
    zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
target:
  id: ent_algorithm_sac
  name:
    en: Soft Actor-Critic (SAC)
    zh: 软演员-评论家（SAC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control uses Soft Actor-Critic
    (SAC).
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control使用软演员-评论家（SAC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源论文明确说明使用SAC进行大规模预训练。 | 证据: In this paper, we
    find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably
    supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_towards_bridging_the_gap_betwe_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_towards_bridging_the_gap_betwe_2026/
  accessed_at: '2026-07-16'
---
