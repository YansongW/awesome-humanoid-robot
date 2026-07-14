---
$id: ent_paper_li_discrete_diffusion_for_reflect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
  zh: ReflectDrive
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
summary:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
  zh: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- reflectdrive
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20109v1.
sources:
- id: src_001
  type: paper
  title: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ReflectDrive source
  url: https://doi.org/10.48550/arXiv.2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 核心内容
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 参考
- http://arxiv.org/abs/2509.20109v1

