---
$id: ent_paper_smap_self_supervised_motion_ad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
  zh: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
  ko: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
summary:
  en: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
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
- smap
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19463v1.
sources:
- id: src_001
  type: paper
  title: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control (arXiv)'
  url: https://arxiv.org/abs/2505.19463
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## 核心内容
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## 参考
- http://arxiv.org/abs/2505.19463v1

