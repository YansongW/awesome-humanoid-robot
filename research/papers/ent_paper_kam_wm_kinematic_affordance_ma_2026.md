---
$id: ent_paper_kam_wm_kinematic_affordance_ma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  zh: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  ko: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
summary:
  en: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
  zh: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
  ko: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
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
- kam_wm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04652v1.
sources:
- id: src_001
  type: paper
  title: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04652
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 核心内容
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 参考
- http://arxiv.org/abs/2607.04652v1

