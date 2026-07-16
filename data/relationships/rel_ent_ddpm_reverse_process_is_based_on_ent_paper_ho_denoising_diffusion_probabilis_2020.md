---
$id: rel_ent_ddpm_reverse_process_is_based_on_ent_paper_ho_denoising_diffusion_probabilis_2020
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_ddpm_reverse_process
  name:
    en: DDPM reverse process
    zh: DDPM 逆过程
target:
  id: ent_paper_ho_denoising_diffusion_probabilis_2020
  name:
    en: Denoising Diffusion Probabilistic Models
    zh: 去噪扩散概率模型
domains:
  source_domain: 00_foundations
  target_domain: 07_ai_models_algorithms
description:
  en: DDPM reverse process is based on Denoising Diffusion Probabilistic Models.
  zh: DDPM 逆过程基于去噪扩散概率模型。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: DDPM反向过程是基于去噪扩散概率模型论文中描述的方法。 | 证据: 去噪扩散概率模型（DDPM）中学习的反向马尔可夫链，逐步将高斯噪声转化为类数据样本。'
sources:
- id: src_001
  type: other
  title: KG body of ent_ddpm_reverse_process
  url: https://kg.rounds-tech.com/entry/ent_ddpm_reverse_process/
  accessed_at: '2026-07-16'
---
