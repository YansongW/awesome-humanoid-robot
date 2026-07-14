---
$id: ent_paper_gao_vla_os_structuring_and_dissect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
  zh: VLA-OS
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
summary:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
  zh: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
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
- vision_language_action
- vla
- vla_os
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17561v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-OS source
  url: https://doi.org/10.48550/arXiv.2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 核心内容
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 参考
- http://arxiv.org/abs/2506.17561v1

