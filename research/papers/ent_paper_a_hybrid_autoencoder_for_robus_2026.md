---
$id: ent_paper_a_hybrid_autoencoder_for_robus_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
  zh: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
  ko: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
summary:
  en: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
  zh: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
  ko: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion is
    a 2026 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hybrid_autoencoder_for_robus
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05855v1.
sources:
- id: src_001
  type: paper
  title: A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion
    (arXiv)
  url: https://arxiv.org/abs/2602.05855
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## 核心内容
Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments. While traditional systems often rely on manually engineered, single-sensor pipelines, this paper presents a learning-based framework that uses an intermediate, robot-centric heightmap representation. A hybrid Encoder-Decoder Structure (EDS) is introduced, utilizing a Convolutional Neural Network (CNN) for spatial feature extraction fused with a Gated Recurrent Unit (GRU) core for temporal consistency. The architecture integrates multimodal data from an Intel RealSense depth camera, a LIVOX MID-360 LiDAR processed via efficient spherical projection, and an onboard IMU. Quantitative results demonstrate that multimodal fusion improves reconstruction accuracy by 7.2% over depth-only and 9.9% over LiDAR-only configurations. Furthermore, the integration of a 3.2 s temporal context reduces mapping drift.

## 参考
- http://arxiv.org/abs/2602.05855v1

