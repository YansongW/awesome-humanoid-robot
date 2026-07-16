---
$id: rel_ent_paper_adversarial_locomotion_and_mot_2025_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_adversarial_locomotion_and_mot_2025
  name:
    en: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning
    zh: 用于人形策略学习的对抗性运动和运动模仿
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 06_design_engineering
  target_domain: 00_foundations
description:
  en: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning uses Flow matching.
  zh: 用于人形策略学习的对抗性运动和运动模仿使用流匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文使用流匹配技术来提高采样效率和轨迹平滑度。 | 证据: Flow matching
    techniques further improve sampling efficiency and trajectory smoothness, ensuring that the generated whole-body action
    sequences satisfy physical constraints in both joint space and task space.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_adversarial_locomotion_and_mot_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_adversarial_locomotion_and_mot_2025/
  accessed_at: '2026-07-16'
---
