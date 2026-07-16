---
$id: rel_ent_paper_demohlm_from_one_demonstration_2025_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_demohlm_from_one_demonstration_2025
  name:
    en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
    zh: DemoHLM｜从单一示范到通用人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation mentions Model Predictive Control (MPC).'
  zh: DemoHLM｜从单一示范到通用人形移动操作提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中MPC作为全身控制器的一种选项被列出，但未明确说明DemoHLM使用了MPC。 |
    证据: 该框架的核心是一个三阶段流水线：首先，通过相机多视角观测、本体状态与关节序列的同步记录，采集人类操作员在遥操作或外骨骼设备上的动作数据；其次，利用 ACT（Action Chunking Transformer）或行为克隆方法，将连续的示范轨迹压缩为可监督的动作预测问题，即模型学习从当前观测到未来动作序列的映射；最后，通过全身控制器（WBC）或模型预测控制（MPC）将预测的动作转化为低层关节位置或力矩指令，并引入闭环纠错机制以修正执行偏差。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_demohlm_from_one_demonstration_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_demohlm_from_one_demonstration_2025/
  accessed_at: '2026-07-16'
---
