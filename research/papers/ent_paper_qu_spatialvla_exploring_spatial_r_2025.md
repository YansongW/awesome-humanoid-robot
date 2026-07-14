---
$id: ent_paper_qu_spatialvla_exploring_spatial_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model'
  zh: SpatialVLA
  ko: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model'
summary:
  en: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
  zh: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
  ko: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- spatialvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.15830v5.
sources:
- id: src_001
  type: paper
  title: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2501.15830
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SpatialVLA source
  url: https://doi.org/10.48550/arXiv.2501.15830
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## 核心内容
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## 参考
- http://arxiv.org/abs/2501.15830v5

