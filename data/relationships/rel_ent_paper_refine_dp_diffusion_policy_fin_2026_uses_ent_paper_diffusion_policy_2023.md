---
$id: rel_ent_paper_refine_dp_diffusion_policy_fin_2026_uses_ent_paper_diffusion_policy_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_refine_dp_diffusion_policy_fin_2026
  name:
    en: 'REFINE-DP: Diffusion Policy Fine-tuning for Humanoid Loco-manipulation via Reinforcement Learning'
    zh: REFINE-DP｜通过强化学习对人形移动操作进行扩散策略微调
target:
  id: ent_paper_diffusion_policy_2023
  name:
    en: Diffusion Policy
    zh: 扩散策略
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'REFINE-DP: Diffusion Policy Fine-tuning for Humanoid Loco-manipulation via Reinforcement Learning uses Diffusion Policy.'
  zh: REFINE-DP｜通过强化学习对人形移动操作进行扩散策略微调使用扩散策略。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文REFINE-DP在其策略学习层中融合了扩散策略，因此使用了该方法。 | 证据: 其次，策略学习层融合了强化学习（PPO）、行为克隆（ACT）与扩散策略（Diffusion
    Policy）三种范式：PPO 用于探索最优动作分布，ACT 提供高效的模仿学习基线，而扩散策略或流匹配则负责从多模态动作分布中采样出平滑且物理可行的关节位置/力矩命令。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_refine_dp_diffusion_policy_fin_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_refine_dp_diffusion_policy_fin_2026/
  accessed_at: '2026-07-16'
---
