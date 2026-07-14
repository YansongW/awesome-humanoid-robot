---
$id: ent_paper_guided_motion_diffusion_for_co_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Guided Motion Diffusion for Controllable Human Motion Synthesis
  zh: Guided Motion Diffusion for Controllable Human Motion Synthesis
  ko: Guided Motion Diffusion for Controllable Human Motion Synthesis
summary:
  en: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
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
- guided_motion_diffusion_for_co
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.12577v3.
sources:
- id: src_001
  type: paper
  title: Guided Motion Diffusion for Controllable Human Motion Synthesis (arXiv)
  url: https://arxiv.org/abs/2305.12577
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## 核心内容
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## 参考
- http://arxiv.org/abs/2305.12577v3

