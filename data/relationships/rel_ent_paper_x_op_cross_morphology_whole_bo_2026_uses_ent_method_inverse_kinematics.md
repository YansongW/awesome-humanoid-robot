---
$id: rel_ent_paper_x_op_cross_morphology_whole_bo_2026_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_x_op_cross_morphology_whole_bo_2026
  name:
    en: 'X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting'
    zh: 单台 Apple Vision Pro 驱动、跨形态免重训的分层全身遥操作：MPC 重定向器兼顾操作者意图与动力学可行性
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: 'X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting uses Inverse Kinematics.'
  zh: 单台 Apple Vision Pro 驱动、跨形态免重训的分层全身遥操作：MPC 重定向器兼顾操作者意图与动力学可行性使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 上层系统通过轻量逆运动学分析生成参考关节轨迹。 | 证据: 상위 계층은 Apple Vision
    Pro가 조작자의 머리, 양손 및 몸통의 6D 자세를 실시간으로 포착하고, 경량 역기구학(Inverse Kinematics) 해석을 통해 참조 관절 궤적을 생성합니다.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_x_op_cross_morphology_whole_bo_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_x_op_cross_morphology_whole_bo_2026/
  accessed_at: '2026-07-16'
---
