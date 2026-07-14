---
$id: ent_paper_learning_perceptive_humanoid_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Perceptive Humanoid Locomotion over Challenging Terrain
  zh: Learning Perceptive Humanoid Locomotion over Challenging Terrain
  ko: Learning Perceptive Humanoid Locomotion over Challenging Terrain
summary:
  en: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
  zh: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
  ko: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_perceptive_humanoid_l
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00692v3.
sources:
- id: src_001
  type: paper
  title: Learning Perceptive Humanoid Locomotion over Challenging Terrain (arXiv)
  url: https://arxiv.org/abs/2503.00692
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## 核心内容
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## 参考
- http://arxiv.org/abs/2503.00692v3

