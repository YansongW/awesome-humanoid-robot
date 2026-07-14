---
$id: ent_paper_egodex_learning_dexterous_mani_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
  zh: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
  ko: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video'
summary:
  en: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
  zh: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
  ko: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video is a 2025 work on manipulation for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egodex
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11709v3.
sources:
- id: src_001
  type: paper
  title: 'EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2505.11709
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 核心内容
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

## 参考
- http://arxiv.org/abs/2505.11709v3

