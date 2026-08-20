---
$id: rel_ent_paper_trajbooster_boosting_humanoid_2026_uses_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_trajbooster_boosting_humanoid_2026
  name:
    en: 'TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning'
    zh: TrajBooster｜通过以轨迹为中心的学习促进人形全身操作
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning uses Action Chunking with Transformers.'
  zh: TrajBooster｜通过以轨迹为中心的学习促进人形全身操作使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文TrajBooster采用ACT（Action Chunking with Transformers）进行行为克隆模仿学习。
    | 证据: 在此基础上，模型采用两种互补的学习路径：一是基于 ACT（Action Chunking with Transformers）的行为克隆模仿学习，用于捕捉示范轨迹中的时序依赖关系；二是引入 VLA（Vision-Language-Action）多模态动作模型，将视觉特征与语言指令融合，直接预测全身轨迹与末端执行器目标。
    | WP4 2026-08-11: endpoint id rewritten (ent_paper_trajbooster_boosting_humanoid_2026→ent_paper_trajbooster_boosting_humanoid_2026,
    ent_method_action_chunking_transformer→ent_method_action_chunking_transformer); original file rel_ent_paper_trajbooster_boosting_humanoid_2026_uses_ent_paper_action_chunking_with_transform_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_trajbooster_boosting_humanoid_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_trajbooster_boosting_humanoid_2026/
  accessed_at: '2026-07-16'
---
