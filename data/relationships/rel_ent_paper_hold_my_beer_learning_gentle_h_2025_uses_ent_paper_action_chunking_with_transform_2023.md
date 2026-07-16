---
$id: rel_ent_paper_hold_my_beer_learning_gentle_h_2025_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hold_my_beer_learning_gentle_h_2025
  name:
    en: 'Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control'
    zh: Hold｜My Beer 学习温和的人形运动和末端执行器稳定控制
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control uses Action Chunking with
    Transformers.'
  zh: Hold｜My Beer 学习温和的人形运动和末端执行器稳定控制使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Hold My Beer论文中明确提到采用ACT（Action Chunking with
    Transformers）方法进行行为克隆。 | 证据: 其核心流程是：首先，通过相机图像或多视角观测数据，利用视觉感知模块恢复场景、目标物体或运动表征；随后，采用ACT（Action Chunking with Transformers）或行为克隆（Behavioral
    Cloning）方法，将人类示范的全身轨迹、末端执行器/腕手目标以及低层控制器目标建模为监督学习问题。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hold_my_beer_learning_gentle_h_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_hold_my_beer_learning_gentle_h_2025/
  accessed_at: '2026-07-16'
---
