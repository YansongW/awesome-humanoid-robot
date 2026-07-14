---
$id: ent_paper_polygmap_a_perceptive_locomoti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
  zh: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
  ko: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
summary:
  en: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- polygmap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12346v1.
sources:
- id: src_001
  type: paper
  title: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing (arXiv)'
  url: https://arxiv.org/abs/2510.12346
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 核心内容
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 参考
- http://arxiv.org/abs/2510.12346v1

