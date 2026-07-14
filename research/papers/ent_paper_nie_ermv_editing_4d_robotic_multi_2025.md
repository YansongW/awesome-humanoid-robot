---
$id: ent_paper_nie_ermv_editing_4d_robotic_multi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents'
  zh: ERMV
  ko: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents'
summary:
  en: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents (ERMV), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Key Laboratory of System Control and Information
    Processing, Cambridge University.'
  zh: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents (ERMV), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Key Laboratory of System Control and Information
    Processing, Cambridge University.'
  ko: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents (ERMV), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Key Laboratory of System Control and Information
    Processing, Cambridge University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ermv
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.17462v1.
sources:
- id: src_001
  type: paper
  title: 'ERMV: Editing 4D Robotic Multi-view images to enhance embodied agents (arXiv)'
  url: https://arxiv.org/abs/2507.17462
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ERMV source
  url: https://doi.org/10.48550/arXiv.2507.17462
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot imitation learning relies on 4D multi-view sequential images. However, the high cost of data collection and the scarcity of high-quality data severely constrain the generalization and application of embodied intelligence policies like Vision-Language-Action (VLA) models. Data augmentation is a powerful strategy to overcome data scarcity, but methods for editing 4D multi-view sequential images for manipulation tasks are currently lacking. Thus, we propose ERMV (Editing Robotic Multi-View 4D data), a novel data augmentation framework that efficiently edits an entire multi-view sequence based on single-frame editing and robot state conditions. This task presents three core challenges: (1) maintaining geometric and appearance consistency across dynamic views and long time horizons; (2) expanding the working window with low computational costs; and (3) ensuring the semantic integrity of critical objects like the robot arm. ERMV addresses these challenges through a series of innovations. First, to ensure spatio-temporal consistency in motion blur, we introduce a novel Epipolar Motion-Aware Attention (EMA-Attn) mechanism that learns pixel shift caused by movement before applying geometric constraints. Second, to maximize the editing working window, ERMV pioneers a Sparse Spatio-Temporal (STT) module, which decouples the temporal and spatial views and remodels a single-frame multi-view problem through sparse sampling of the views to reduce computational demands. Third, to alleviate error accumulation, we incorporate a feedback intervention Mechanism, which uses a Multimodal Large Language Model (MLLM) to check editing inconsistencies and request targeted expert guidance only when necessary. Extensive experiments demonstrate that ERMV-augmented data significantly boosts the robustness and generalization of VLA models in both simulated and real-world environments.

## 核心内容
Robot imitation learning relies on 4D multi-view sequential images. However, the high cost of data collection and the scarcity of high-quality data severely constrain the generalization and application of embodied intelligence policies like Vision-Language-Action (VLA) models. Data augmentation is a powerful strategy to overcome data scarcity, but methods for editing 4D multi-view sequential images for manipulation tasks are currently lacking. Thus, we propose ERMV (Editing Robotic Multi-View 4D data), a novel data augmentation framework that efficiently edits an entire multi-view sequence based on single-frame editing and robot state conditions. This task presents three core challenges: (1) maintaining geometric and appearance consistency across dynamic views and long time horizons; (2) expanding the working window with low computational costs; and (3) ensuring the semantic integrity of critical objects like the robot arm. ERMV addresses these challenges through a series of innovations. First, to ensure spatio-temporal consistency in motion blur, we introduce a novel Epipolar Motion-Aware Attention (EMA-Attn) mechanism that learns pixel shift caused by movement before applying geometric constraints. Second, to maximize the editing working window, ERMV pioneers a Sparse Spatio-Temporal (STT) module, which decouples the temporal and spatial views and remodels a single-frame multi-view problem through sparse sampling of the views to reduce computational demands. Third, to alleviate error accumulation, we incorporate a feedback intervention Mechanism, which uses a Multimodal Large Language Model (MLLM) to check editing inconsistencies and request targeted expert guidance only when necessary. Extensive experiments demonstrate that ERMV-augmented data significantly boosts the robustness and generalization of VLA models in both simulated and real-world environments.

## 参考
- http://arxiv.org/abs/2507.17462v1

