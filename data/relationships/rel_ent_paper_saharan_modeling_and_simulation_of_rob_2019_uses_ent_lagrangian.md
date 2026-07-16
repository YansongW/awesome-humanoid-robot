---
$id: rel_ent_paper_saharan_modeling_and_simulation_of_rob_2019_uses_ent_lagrangian
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_saharan_modeling_and_simulation_of_rob_2019
  name:
    en: Modeling and Simulation of Robotic Finger Powered by Nylon Artificial Muscles — Equations with Simulink Model
    zh: 尼龙人造肌肉驱动的机器人手指建模与仿真——含Simulink模型的方程
target:
  id: ent_lagrangian
  name:
    en: Lagrangian
    zh: 拉格朗日量
domains:
  source_domain: 06_design_engineering
  target_domain: 00_foundations
description:
  en: Modeling and Simulation of Robotic Finger Powered by Nylon Artificial Muscles — Equations with Simulink Model uses Lagrangian.
  zh: 尼龙人造肌肉驱动的机器人手指建模与仿真——含Simulink模型的方程使用拉格朗日量。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 作者使用欧拉-拉格朗日公式推导手指动力学。 | 证据: The authors derive
    the finger dynamics using an Euler-Lagrangian formulation with velocity Jacobians, simplify the coupled equations by neglecting
    small Coriolis and off-diagonal inertia terms, and add velocity-proportional joint damping to improve n'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_saharan_modeling_and_simulation_of_rob_2019
  url: https://kg.rounds-tech.com/entry/ent_paper_saharan_modeling_and_simulation_of_rob_2019/
  accessed_at: '2026-07-16'
---
