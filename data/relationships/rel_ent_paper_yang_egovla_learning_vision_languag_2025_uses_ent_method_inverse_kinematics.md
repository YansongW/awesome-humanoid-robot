---
$id: rel_ent_paper_yang_egovla_learning_vision_languag_2025_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_yang_egovla_learning_vision_languag_2025
  name:
    en: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos'
    zh: EgoVLA：从以自我视角人体视频中学习视觉-语言-动作模型
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos uses Inverse Kinematics.'
  zh: EgoVLA：从以自我视角人体视频中学习视觉-语言-动作模型使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: EgoVLA使用逆运动学将人类动作转换为机器人动作。 | 证据: With a VLA
    trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to
    convert the human actions to robot actions.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_yang_egovla_learning_vision_languag_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_yang_egovla_learning_vision_languag_2025/
  accessed_at: '2026-07-16'
---
