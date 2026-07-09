---
$id: ent_paper_mask2real_wm_segmentation_mask_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous
    World Models'
  zh: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous
    World Models'
  ko: ''
summary:
  en: "arXiv:2607.04546v1 Announce Type: new \nAbstract: Action-conditioned world\
    \ models allow robots to predict the future consequences of candidate actions\
    \ without additional physical interaction, supporting policy evaluation, planning,\
    \ and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned\
    \ world model for dexterous manipulation that decouples pixel prediction into\
    \ a dynamics model and a rendering model. The dynamics model predicts future segmentation\
    \ masks from past masks and 23-DoF action sequences. The rendering model maps\
    \ the predicted masks to photorealistic RGB using a ControlNet-augmented Stable\
    \ Video Diffusion backbone. The smaller sim-to-real gap in segmentation space\
    \ enables the dynamics model to benefit from large-scale pretraining on over 50\
    \ h of synthetic simulation data, followed by fine-tuning on fewer than 2.5 h\
    \ of real demonstrations. Experiments on a dexterous pick-and-place benchmark\
    \ show that mask conditioning and simulation pretraining are both required for\
    \ per-DoF action controllability across all 23 degrees of freedom. In contrast,\
    \ monolithic baselines capture broad hand and end-effector trajectories but do\
    \ not reliably reflect fine-grained, per-joint action effects."
  zh: "arXiv:2607.04546v1 Announce Type: new \nAbstract: Action-conditioned world\
    \ models allow robots to predict the future consequences of candidate actions\
    \ without additional physical interaction, supporting policy evaluation, planning,\
    \ and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned\
    \ world model for dexterous manipulation that decouples pixel prediction into\
    \ a dynamics model and a rendering model. The dynamics model predicts future segmentation\
    \ masks from past masks and 23-DoF action sequences. The rendering model maps\
    \ the predicted masks to photorealistic RGB using a ControlNet-augmented Stable\
    \ Video Diffusion backbone. The smaller sim-to-real gap in segmentation space\
    \ enables the dynamics model to benefit from large-scale pretraining on over 50\
    \ h of synthetic simulation data, followed by fine-tuning on fewer than 2.5 h\
    \ of real demonstrations. Experiments on a dexterous pick-and-place benchmark\
    \ show that mask conditioning and simulation pretraining are both required for\
    \ per-DoF action controllability across all 23 degrees of freedom. In contrast,\
    \ monolithic baselines capture broad hand and end-effector trajectories but do\
    \ not reliably reflect fine-grained, per-joint action effects."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- mask2real_wm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable
    Dexterous World Models (arXiv)'
  url: https://arxiv.org/abs/2607.04546
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04546v1 Announce Type: new 
Abstract: Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps the predicted masks to photorealistic RGB using a ControlNet-augmented Stable Video Diffusion backbone. The smaller sim-to-real gap in segmentation space enables the dynamics model to benefit from large-scale pretraining on over 50 h of synthetic simulation data, followed by fine-tuning on fewer than 2.5 h of real demonstrations. Experiments on a dexterous pick-and-place benchmark show that mask conditioning and simulation pretraining are both required for per-DoF action controllability across all 23 degrees of freedom. In contrast, monolithic baselines capture broad hand and end-effector trajectories but do not reliably reflect fine-grained, per-joint action effects.
