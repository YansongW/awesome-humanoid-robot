---
$id: rel_ent_paper_hitter_a_humanoid_table_tennis_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hitter_a_humanoid_table_tennis_2025
  name:
    en: 'HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning'
    zh: HITTER｜通过分层规划和学习的人形乒乓球机器人
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning uses Model Predictive Control (MPC).'
  zh: HITTER｜通过分层规划和学习的人形乒乓球机器人使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: HITTER论文中明确提到低层控制器使用模型预测控制（MPC）实现关节级别的精确跟踪。
    | 证据: HITTER采用分层架构，将任务自上而下分解为三个层次：高层模块负责根据当前场景状态选择并组合预定义的技能策略；中层模块利用PPO/RL策略训练与ACT行为克隆模仿学习，生成平滑的全身轨迹与动作序列；低层控制器则通过全身控制器（WBC）或模型预测控制（MPC）实现关节级别的精确跟踪。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hitter_a_humanoid_table_tennis_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_hitter_a_humanoid_table_tennis_2025/
  accessed_at: '2026-07-16'
---
