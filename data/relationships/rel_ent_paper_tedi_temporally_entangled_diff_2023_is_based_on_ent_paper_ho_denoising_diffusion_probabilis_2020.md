---
$id: rel_ent_paper_tedi_temporally_entangled_diff_2023_is_based_on_ent_paper_ho_denoising_diffusion_probabilis_2020
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_paper_tedi_temporally_entangled_diff_2023
  name:
    en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
    zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
target:
  id: ent_paper_ho_denoising_diffusion_probabilis_2020
  name:
    en: Denoising Diffusion Probabilistic Models
    zh: 去噪扩散概率模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is based on Denoising Diffusion Probabilistic Models.'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis基于去噪扩散概率模型。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源论文TEDi指出扩散过程的渐进性质是DDPM的关键成分，表明其工作基于DDPM。 |
    证据: The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient
    of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and
    been recently ex'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_tedi_temporally_entangled_diff_2023
  url: https://kg.rounds-tech.com/entry/ent_paper_tedi_temporally_entangled_diff_2023/
  accessed_at: '2026-07-16'
---
