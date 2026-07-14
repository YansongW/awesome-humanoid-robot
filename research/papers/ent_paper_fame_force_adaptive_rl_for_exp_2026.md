---
$id: ent_paper_fame_force_adaptive_rl_for_exp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
  zh: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
  ko: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid'
summary:
  en: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid is a 2026 work on loco-manipulation
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
- fame
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.08961v1.
sources:
- id: src_001
  type: paper
  title: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid (arXiv)'
  url: https://arxiv.org/abs/2603.08961v1
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid project page'
  url: https://fame10.github.io/Fame/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Maintaining balance under external hand forces is critical for humanoid bimanual manipulation, where interaction forces propagate through the kinematic chain and constrain the feasible manipulation envelope. We propose \textbf{FAME}, a force-adaptive reinforcement learning framework that conditions a standing policy on a learned latent context encoding upper-body joint configuration and bimanual interaction forces. During training, we apply diverse, spherically sampled 3D forces on each hand to inject disturbances in simulation together with an upper-body pose curriculum, exposing the policy to manipulation-induced perturbations across continuously varying arm configurations. At deployment, interaction forces are estimated from the robot dynamics and fed to the same encoder, enabling online adaptation without wrist force/torque sensors. In simulation across five fixed arm configurations with randomized hand forces and commanded base heights, FAME improves mean standing success to 73.84%, compared to 51.40% for the curriculum-only baseline and 29.44% for the base policy. We further deploy the learned policy on a full-scale Unitree H12 humanoid and evaluate robustness in representative load-interaction scenarios, including asymmetric single-arm load and symmetric bimanual load. Code and videos are available on https://fame10.github.io/Fame/

## 核心内容
Maintaining balance under external hand forces is critical for humanoid bimanual manipulation, where interaction forces propagate through the kinematic chain and constrain the feasible manipulation envelope. We propose \textbf{FAME}, a force-adaptive reinforcement learning framework that conditions a standing policy on a learned latent context encoding upper-body joint configuration and bimanual interaction forces. During training, we apply diverse, spherically sampled 3D forces on each hand to inject disturbances in simulation together with an upper-body pose curriculum, exposing the policy to manipulation-induced perturbations across continuously varying arm configurations. At deployment, interaction forces are estimated from the robot dynamics and fed to the same encoder, enabling online adaptation without wrist force/torque sensors. In simulation across five fixed arm configurations with randomized hand forces and commanded base heights, FAME improves mean standing success to 73.84%, compared to 51.40% for the curriculum-only baseline and 29.44% for the base policy. We further deploy the learned policy on a full-scale Unitree H12 humanoid and evaluate robustness in representative load-interaction scenarios, including asymmetric single-arm load and symmetric bimanual load. Code and videos are available on https://fame10.github.io/Fame/

## 参考
- http://arxiv.org/abs/2603.08961v1

