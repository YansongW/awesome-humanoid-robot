---
$id: ent_paper_embedding_classical_balance_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  zh: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
summary:
  en: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embedding_classical_balance_co
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.08619v1.
sources:
- id: src_001
  type: paper
  title: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery (arXiv)
  url: https://arxiv.org/abs/2603.08619
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots remain vulnerable to falls and unrecoverable failure states, limiting their practical utility in unstructured environments. While reinforcement learning has demonstrated stand-up behaviors, existing approaches treat recovery as a pure task-reward problem without an explicit representation of the balance state. We present a unified RL policy that addresses this limitation by embedding classical balance metrics: capture point, center-of-mass state, and centroidal momentum, as privileged critic inputs and shaping rewards directly around these quantities during training, while the actor relies solely on proprioception for zero-shot hardware transfer. Without reference trajectories or scripted contacts, a single policy spans the full recovery spectrum: ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up using the hands, elbows, and knees. Trained on the Unitree H1-2 in Isaac Lab, the policy achieves a 93.4% recovery rate across randomized initial poses and unscripted fall configurations. An ablation study shows that removing the balance-informed structure causes stand-up learning to fail entirely, confirming that these metrics provide a meaningful learning signal rather than incidental structure. Sim-to-sim transfer to MuJoCo and preliminary hardware experiments further demonstrate cross-environment generalization. These results show that embedding interpretable balance structure into the learning framework substantially reduces time spent in failure states and broadens the envelope of autonomous recovery.

## 核心内容
Humanoid robots remain vulnerable to falls and unrecoverable failure states, limiting their practical utility in unstructured environments. While reinforcement learning has demonstrated stand-up behaviors, existing approaches treat recovery as a pure task-reward problem without an explicit representation of the balance state. We present a unified RL policy that addresses this limitation by embedding classical balance metrics: capture point, center-of-mass state, and centroidal momentum, as privileged critic inputs and shaping rewards directly around these quantities during training, while the actor relies solely on proprioception for zero-shot hardware transfer. Without reference trajectories or scripted contacts, a single policy spans the full recovery spectrum: ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up using the hands, elbows, and knees. Trained on the Unitree H1-2 in Isaac Lab, the policy achieves a 93.4% recovery rate across randomized initial poses and unscripted fall configurations. An ablation study shows that removing the balance-informed structure causes stand-up learning to fail entirely, confirming that these metrics provide a meaningful learning signal rather than incidental structure. Sim-to-sim transfer to MuJoCo and preliminary hardware experiments further demonstrate cross-environment generalization. These results show that embedding interpretable balance structure into the learning framework substantially reduces time spent in failure states and broadens the envelope of autonomous recovery.

## 参考
- http://arxiv.org/abs/2603.08619v1

