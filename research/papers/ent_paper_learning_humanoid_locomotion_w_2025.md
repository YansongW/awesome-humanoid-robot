---
$id: ent_paper_learning_humanoid_locomotion_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with World Model Reconstruction
  zh: Learning Humanoid Locomotion with World Model Reconstruction
  ko: Learning Humanoid Locomotion with World Model Reconstruction
summary:
  en: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
  zh: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
  ko: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_locomotion_w
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.16230v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with World Model Reconstruction (arXiv)
  url: https://arxiv.org/abs/2502.16230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 核心内容
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 参考
- http://arxiv.org/abs/2502.16230v1

