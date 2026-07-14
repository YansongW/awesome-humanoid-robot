---
$id: ent_paper_implicit_kinodynamic_motion_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  zh: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
summary:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
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
- humanoid
- implicit_kinodynamic_motion_re
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15443v2.
sources:
- id: src_001
  type: paper
  title: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning (arXiv)
  url: https://arxiv.org/abs/2509.15443
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 核心内容
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 参考
- http://arxiv.org/abs/2509.15443v2

