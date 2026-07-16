---
$id: rel_ent_paper_humanoidmimicgen_data_generati_2026_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_humanoidmimicgen_data_generati_2026
  name:
    en: 'HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning'
    zh: HumanoidMimicGen｜通过全身规划进行移动操作的数据生成
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning uses Action Chunking with Transformers.'
  zh: HumanoidMimicGen｜通过全身规划进行移动操作的数据生成使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用ACT（Action Chunking with Transformers）行为克隆算法来编码动作序列。
    | 证据: 该框架的核心流程分为三个层级：首先，通过多视角相机图像、本体传感器与外骨骼设备采集人类操作数据，获取包含场景语义与关节状态的原始观测；其次，利用 ACT（Action Chunking with Transformers）等行为克隆算法，将原始数据编码为分段的全身动作序列；最后，引入分层技能库与专家策略模块，将复杂任务分解为可路由的子技能（如“抓取”、“行走”、“放置”），并通过高层决策模块动态选择与组合。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_humanoidmimicgen_data_generati_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_humanoidmimicgen_data_generati_2026/
  accessed_at: '2026-07-16'
---
