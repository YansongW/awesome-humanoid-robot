---
$id: ent_paper_chi_impromptu_vla_open_weights_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
  zh: Impromptu VLA
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
summary:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  zh: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- impromptu_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23757v1.
sources:
- id: src_001
  type: paper
  title: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Impromptu VLA source
  url: https://doi.org/10.48550/arXiv.2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 核心内容
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 参考
- http://arxiv.org/abs/2505.23757v1

