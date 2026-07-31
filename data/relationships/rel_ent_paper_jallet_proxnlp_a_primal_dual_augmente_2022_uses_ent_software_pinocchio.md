---
$id: rel_ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022
  name:
    en: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming in Robotics and beyond'
    zh: ProxNLP：面向机器人及更广领域的非线性规划原始-对偶增广拉格朗日求解器
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming in Robotics and beyond uses Pinocchio.'
  zh: ProxNLP：面向机器人及更广领域的非线性规划原始-对偶增广拉格朗日求解器使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: proxNLP实现利用了Pinocchio库。 | 证据: 此外，他们开发了开源C++实现proxNLP，该实现利用Eigen、Pinocchio和CasADi库，并通过Talos机器人姿态生成等实例验证了其有效性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022
  url: https://kg.rounds-tech.com/entry/ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022/
  accessed_at: '2026-07-31'
---
