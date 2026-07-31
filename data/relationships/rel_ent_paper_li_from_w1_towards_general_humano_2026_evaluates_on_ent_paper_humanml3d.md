---
$id: rel_ent_paper_li_from_w1_towards_general_humano_2026_evaluates_on_ent_paper_humanml3d
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_li_from_w1_towards_general_humano_2026
  name:
    en: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
    zh: FRoM-W1：面向自然语言指令的通用人形机器人全身控制
target:
  id: ent_paper_humanml3d
  name:
    en: HumanML3D
    zh: HumanML3D
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions is evaluated on HumanML3D.'
  zh: FRoM-W1：面向自然语言指令的通用人形机器人全身控制评测于HumanML3D。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在HumanML3D-X基准上验证了性能，因此在该基准上进行了评估。 | 证据: 实验在
    Unitree H1 和 G1 上验证，展示了在 HumanML3D-X 基准上的领先性能，且强化学习微调持续提升了运动跟踪精度和任务成功率。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_li_from_w1_towards_general_humano_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_li_from_w1_towards_general_humano_2026/
  accessed_at: '2026-07-31'
---
