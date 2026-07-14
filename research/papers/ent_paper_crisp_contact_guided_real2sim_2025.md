---
$id: ent_paper_crisp_contact_guided_real2sim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  zh: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
summary:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- crisp
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.14696v3.
sources:
- id: src_001
  type: paper
  title: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives (arXiv)'
  url: https://arxiv.org/abs/2512.14696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 核心内容
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 参考
- http://arxiv.org/abs/2512.14696v3

