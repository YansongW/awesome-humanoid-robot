---
$id: rel_ent_paper_bansal_thermaldiffusion_visual_to_the_2025_uses_ent_paper_ho_denoising_diffusion_probabilis_2020
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_bansal_thermaldiffusion_visual_to_the_2025
  name:
    en: 'ThermalDiffusion: Visual-to-Thermal Image-to-Image Translation for Autonomous Navigation'
    zh: ThermalDiffusion：用于自主导航的视觉到热成像图像转换
target:
  id: ent_paper_ho_denoising_diffusion_probabilis_2020
  name:
    en: Denoising Diffusion Probabilistic Models
    zh: 去噪扩散概率模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ThermalDiffusion: Visual-to-Thermal Image-to-Image Translation for Autonomous Navigation uses Denoising Diffusion Probabilistic
    Models.'
  zh: ThermalDiffusion：用于自主导航的视觉到热成像图像转换使用去噪扩散概率模型。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源论文采用条件去噪扩散概率模型（DDPM）作为核心架构，因此使用该模型。 | 证据:
    - 采用条件去噪扩散概率模型（DDPM）作为核心架构，将 RGB 图像作为条件输入，逐步生成对应的热成像图像。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_bansal_thermaldiffusion_visual_to_the_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_bansal_thermaldiffusion_visual_to_the_2025/
  accessed_at: '2026-07-31'
---
