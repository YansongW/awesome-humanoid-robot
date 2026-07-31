---
$id: rel_ent_paper_robot_simulation_tools_core_papers_evaluates_on_ent_benchmark_humanoidbench
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_robot_simulation_tools_core_papers
  name:
    en: 机器人仿真工具核心论文
    zh: 机器人仿真工具核心论文
target:
  id: ent_benchmark_humanoidbench
  name:
    en: HumanoidBench
    zh: HumanoidBench
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 机器人仿真工具核心论文 is evaluated on HumanoidBench.
  zh: 机器人仿真工具核心论文评测于HumanoidBench。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: HumanoidBench是评估仿真工具性能的基准。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_robot_simulation_tools_core_papers
  url: https://kg.rounds-tech.com/entry/ent_paper_robot_simulation_tools_core_papers/
  accessed_at: '2026-07-31'
---
