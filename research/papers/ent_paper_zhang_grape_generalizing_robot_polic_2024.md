---
$id: ent_paper_zhang_grape_generalizing_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
  zh: GRAPE
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
summary:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
  zh: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- grape
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.19309v2.
sources:
- id: src_001
  type: paper
  title: 'GRAPE: Generalizing Robot Policy via Preference Alignment (arXiv)'
  url: https://arxiv.org/abs/2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GRAPE source
  url: https://doi.org/10.48550/arXiv.2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 核心内容
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 参考
- http://arxiv.org/abs/2411.19309v2

