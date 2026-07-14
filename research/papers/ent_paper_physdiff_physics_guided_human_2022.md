---
$id: ent_paper_physdiff_physics_guided_human_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  zh: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
summary:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
  zh: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
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
- motion_analysis
- motion_synthesis
- physdiff
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.02500v3.
sources:
- id: src_001
  type: paper
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model (arXiv)'
  url: https://arxiv.org/abs/2212.02500
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model project page'
  url: https://nvlabs.github.io/PhysDiff/
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 核心内容
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 参考
- http://arxiv.org/abs/2212.02500v3

