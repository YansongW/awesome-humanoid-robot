---
$id: rel_ent_paper_halomi_learning_humanoid_loco_2026_uses_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_halomi_learning_humanoid_loco_2026
  name:
    en: 'HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations'
    zh: HALOMI｜通过人类示范的主动感知学习人形移动操作
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations uses Behavior Cloning.'
  zh: HALOMI｜通过人类示范的主动感知学习人形移动操作使用行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用行为克隆进行动作生成 | 证据: 第二阶段为动作生成：基于第一阶段得到的感知表征，系统采用行为克隆（Behavior
    Cloning）与 ACT（Action Chunking with Transformers）架构，将动作生成视为条件概率建模问题。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_halomi_learning_humanoid_loco_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_halomi_learning_humanoid_loco_2026/
  accessed_at: '2026-07-16'
---
