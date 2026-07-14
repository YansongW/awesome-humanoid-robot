---
$id: ent_paper_hiking_in_the_wild_a_scalable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
  zh: 脚落在哪里，比走得多快更重要
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
summary:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: 'Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception
    to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer
    from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches
    often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are
    implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive
    framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms:
    a foothold safety mechanism combining scalable \textit{Terrain Edg'
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.07718v1.
sources:
- id: src_001
  type: paper
  title: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids (arXiv)'
  url: https://arxiv.org/abs/2601.07718
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 脚落在哪里，比走得多快更重要 project page
  url: https://project-instinct.github.io/hiking-in-the-wild
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 核心内容
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 参考
- http://arxiv.org/abs/2601.07718v1

