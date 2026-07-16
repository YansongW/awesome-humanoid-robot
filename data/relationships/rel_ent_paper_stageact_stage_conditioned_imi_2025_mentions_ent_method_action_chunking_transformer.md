---
$id: rel_ent_paper_stageact_stage_conditioned_imi_2025_mentions_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_stageact_stage_conditioned_imi_2025
  name:
    en: 'StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening'
    zh: StageACT｜鲁棒的人形开门的阶段条件模仿
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening mentions Action Chunking with Transformers (ACT).'
  zh: StageACT｜鲁棒的人形开门的阶段条件模仿提及动作分块变压器（ACT）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: StageACT mainly solves the data closed loop:
    using camera images/multi-view observation, ontology state and joint sequence, teleoperation/exoskeleton data to collect
    human operation and robot state, and then through ACT/behavioral cloning imitation learning, diffusion strategy/stream
    matching, VLM s'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_stageact_stage_conditioned_imi_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_stageact_stage_conditioned_imi_2025/
  accessed_at: '2026-07-16'
---
