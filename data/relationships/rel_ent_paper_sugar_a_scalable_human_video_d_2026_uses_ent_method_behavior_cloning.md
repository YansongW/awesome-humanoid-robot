---
$id: rel_ent_paper_sugar_a_scalable_human_video_d_2026_uses_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_sugar_a_scalable_human_video_d_2026
  name:
    en: 'SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework'
    zh: SUGAR｜可扩展的人类视频驱动的通用人形移动操作学习框架
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework uses Behavior Cloning.'
  zh: SUGAR｜可扩展的人类视频驱动的通用人形移动操作学习框架使用行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文在上层采用了行为克隆模仿学习（ACT），表明其使用了行为克隆方法。 | 证据: At
    the lower level, it extracts robust motion representations from human videos and motion capture trajectories through AMP
    (Adversarial Motion Prior) and motion prior modules; at the upper level, it employs ACT (Behavior Cloning Imitation Learning) '
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_sugar_a_scalable_human_video_d_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_sugar_a_scalable_human_video_d_2026/
  accessed_at: '2026-07-16'
---
