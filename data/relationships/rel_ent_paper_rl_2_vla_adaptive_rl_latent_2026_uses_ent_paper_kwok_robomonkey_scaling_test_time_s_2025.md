---
$id: rel_ent_paper_rl_2_vla_adaptive_rl_latent_2026_uses_ent_paper_kwok_robomonkey_scaling_test_time_s_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_rl_2_vla_adaptive_rl_latent_2026
  name:
    en: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models'
    zh: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models'
target:
  id: ent_paper_kwok_robomonkey_scaling_test_time_s_2025
  name:
    en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
    zh: RoboMonkey
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models uses
    RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models.'
  zh: 'RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models使用RoboMonkey。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明RL$^2$-VLA使用RoboMonkey作为验证器来为候选动作打分。 | 证据:
    - 验证器（CoVer 或 RoboMonkey）为每个候选动作打分 r_t^n = V_θ(o_t, â_t^n, l_t)，选择最高分样本 â_t*。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_rl_2_vla_adaptive_rl_latent_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_rl_2_vla_adaptive_rl_latent_2026/
  accessed_at: '2026-08-06'
---
