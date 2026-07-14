---
$id: ent_paper_gaussgym_an_open_source_real_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  zh: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
summary:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
  zh: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gaussgym
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.15352v1.
sources:
- id: src_001
  type: paper
  title: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels (arXiv)'
  url: https://arxiv.org/abs/2510.15352
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 核心内容
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 参考
- http://arxiv.org/abs/2510.15352v1

