---
$id: ent_paper_perpetual_humanoid_control_for_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perpetual Humanoid Control for Real-time Simulated Avatars
  zh: Perpetual Humanoid Control for Real-time Simulated Avatars
  ko: Perpetual Humanoid Control for Real-time Simulated Avatars
summary:
  en: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
  zh: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
  ko: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- perpetual_humanoid_control_for
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.06456v3.
sources:
- id: src_001
  type: paper
  title: Perpetual Humanoid Control for Real-time Simulated Avatars (arXiv)
  url: https://arxiv.org/abs/2305.06456
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## 核心内容
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## 参考
- http://arxiv.org/abs/2305.06456v3

