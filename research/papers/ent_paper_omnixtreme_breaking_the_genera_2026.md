---
$id: ent_paper_omnixtreme_breaking_the_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
  zh: 高动态动作会撞上硬件边界
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
summary:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
  zh: 'High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However,
    current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably
    collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two
    compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints
    that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples
    general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with
    high-capacity architectures to scale representation capacity without i'
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23843v1.
sources:
- id: src_001
  type: paper
  title: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2602.23843
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 高动态动作会撞上硬件边界 project page
  url: https://extreme-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 核心内容
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 参考
- http://arxiv.org/abs/2602.23843v1

