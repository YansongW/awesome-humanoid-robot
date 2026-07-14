---
$id: ent_paper_climbingcap_multi_modal_datase_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
  zh: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
  ko: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
summary:
  en: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  zh: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  ko: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- climbingcap
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.21268v1.
sources:
- id: src_001
  type: paper
  title: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate (arXiv)'
  url: https://arxiv.org/abs/2503.21268
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human Motion Recovery (HMR) research mainly focuses on ground-based motions such as running. The study on capturing climbing motion, an off-ground motion, is sparse. This is partly due to the limited availability of climbing motion datasets, especially large-scale and challenging 3D labeled datasets. To address the insufficiency of climbing motion datasets, we collect AscendMotion, a large-scale well-annotated, and challenging climbing motion dataset. It consists of 412k RGB, LiDAR frames, and IMU measurements, including the challenging climbing motions of 22 skilled climbing coaches across 12 different rock walls. Capturing the climbing motions is challenging as it requires precise recovery of not only the complex pose but also the global position of climbers. Although multiple global HMR methods have been proposed, they cannot faithfully capture climbing motions. To address the limitations of HMR methods for climbing, we propose ClimbingCap, a motion recovery method that reconstructs continuous 3D human climbing motion in a global coordinate system. One key insight is to use the RGB and LiDAR modalities to separately reconstruct motions in camera coordinates and global coordinates and to optimize them jointly. We demonstrate the quality of the AscendMotion dataset and present promising results from ClimbingCap. The AscendMotion dataset and source code release publicly at \href{this link}{http://www.lidarhumanmotion.net/climbingcap/}

## 核心内容
Human Motion Recovery (HMR) research mainly focuses on ground-based motions such as running. The study on capturing climbing motion, an off-ground motion, is sparse. This is partly due to the limited availability of climbing motion datasets, especially large-scale and challenging 3D labeled datasets. To address the insufficiency of climbing motion datasets, we collect AscendMotion, a large-scale well-annotated, and challenging climbing motion dataset. It consists of 412k RGB, LiDAR frames, and IMU measurements, including the challenging climbing motions of 22 skilled climbing coaches across 12 different rock walls. Capturing the climbing motions is challenging as it requires precise recovery of not only the complex pose but also the global position of climbers. Although multiple global HMR methods have been proposed, they cannot faithfully capture climbing motions. To address the limitations of HMR methods for climbing, we propose ClimbingCap, a motion recovery method that reconstructs continuous 3D human climbing motion in a global coordinate system. One key insight is to use the RGB and LiDAR modalities to separately reconstruct motions in camera coordinates and global coordinates and to optimize them jointly. We demonstrate the quality of the AscendMotion dataset and present promising results from ClimbingCap. The AscendMotion dataset and source code release publicly at \href{this link}{http://www.lidarhumanmotion.net/climbingcap/}

## 参考
- http://arxiv.org/abs/2503.21268v1

