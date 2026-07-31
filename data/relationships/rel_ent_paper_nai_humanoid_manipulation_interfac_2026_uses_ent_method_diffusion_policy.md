---
$id: rel_ent_paper_nai_humanoid_manipulation_interfac_2026_uses_ent_method_diffusion_policy
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_nai_humanoid_manipulation_interfac_2026
  name:
    en: 'Humanoid Manipulation Interface (HuMI): Humanoid Whole-Body Manipulation from Robot-Free Demonstrations'
    zh: 人形机器人操作接口（HuMI）：无需机器人演示的全身操作
target:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Humanoid Manipulation Interface (HuMI): Humanoid Whole-Body Manipulation from Robot-Free Demonstrations uses Diffusion
    Policy.'
  zh: 人形机器人操作接口（HuMI）：无需机器人演示的全身操作使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 高层策略使用Diffusion Policy从人类演示中学习预测关键点轨迹。 | 证据:
    - **高层策略**：使用 Diffusion Policy 从人类演示中学习预测关键点轨迹（如手部、躯干、脚部位置），作为任务规划层。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_nai_humanoid_manipulation_interfac_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_nai_humanoid_manipulation_interfac_2026/
  accessed_at: '2026-07-31'
---
