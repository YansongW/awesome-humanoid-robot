---
$id: ent_paper_implicit_bezier_motion_model_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  zh: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
summary:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- implicit_bezier_motion_model_f
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/.
sources:
- id: src_001
  type: website
  title: Implicit Bézier Motion Model for Precise Spatial and Temporal Control project page
  url: https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 核心内容
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 参考
- https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/

