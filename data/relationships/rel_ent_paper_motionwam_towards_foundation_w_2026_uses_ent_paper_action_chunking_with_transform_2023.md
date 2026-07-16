---
$id: rel_ent_paper_motionwam_towards_foundation_w_2026_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_motionwam_towards_foundation_w_2026
  name:
    en: 'MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation'
    zh: MotionWAM｜迈向实时人形移动操作的基础世界行动模型
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation uses Action Chunking with
    Transformers.'
  zh: MotionWAM｜迈向实时人形移动操作的基础世界行动模型使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: MotionWAM论文使用ACT（Action Chunking with Transformers）作为其混合架构的一部分。
    | 证据: 随后，该表征被送入一个由 ACT（Action Chunking with Transformers）行为克隆模块与扩散策略网络组成的混合架构：ACT 负责捕捉长时程动作序列的时序依赖性，而扩散策略则通过迭代去噪过程生成高自由度全身轨迹，确保运动平滑性与多模态分布建模能力。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_motionwam_towards_foundation_w_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_motionwam_towards_foundation_w_2026/
  accessed_at: '2026-07-16'
---
