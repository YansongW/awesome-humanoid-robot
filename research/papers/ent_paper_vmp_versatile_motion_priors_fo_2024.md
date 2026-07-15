---
$id: ent_paper_vmp_versatile_motion_priors_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  zh: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
summary:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- vmp
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/.
sources:
- id: src_001
  type: website
  title: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters project page'
  url: https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 核心内容
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 参考
- https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/

