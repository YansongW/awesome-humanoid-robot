---
$id: ent_paper_magne_nitrogen_an_open_foundation_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents'
  zh: NitroGen
  ko: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents'
summary:
  en: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (NitroGen), is a 2026 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford, Caltech, UChicago, UT Austin.'
  zh: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (NitroGen), is a 2026 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford, Caltech, UChicago, UT Austin.'
  ko: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (NitroGen), is a 2026 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford, Caltech, UChicago, UT Austin.'
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
- nitrogen
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.02427v1.
sources:
- id: src_001
  type: paper
  title: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (arXiv)'
  url: https://arxiv.org/abs/2601.02427
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We introduce NitroGen, a vision-action foundation model for generalist gaming agents that is trained on 40,000 hours of gameplay videos across more than 1,000 games. We incorporate three key ingredients: 1) an internet-scale video-action dataset constructed by automatically extracting player actions from publicly available gameplay videos, 2) a multi-game benchmark environment that can measure cross-game generalization, and 3) a unified vision-action model trained with large-scale behavior cloning. NitroGen exhibits strong competence across diverse domains, including combat encounters in 3D action games, high-precision control in 2D platformers, and exploration in procedurally generated worlds. It transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch. We release the dataset, evaluation suite, and model weights to advance research on generalist embodied agents.

## 核心内容
We introduce NitroGen, a vision-action foundation model for generalist gaming agents that is trained on 40,000 hours of gameplay videos across more than 1,000 games. We incorporate three key ingredients: 1) an internet-scale video-action dataset constructed by automatically extracting player actions from publicly available gameplay videos, 2) a multi-game benchmark environment that can measure cross-game generalization, and 3) a unified vision-action model trained with large-scale behavior cloning. NitroGen exhibits strong competence across diverse domains, including combat encounters in 3D action games, high-precision control in 2D platformers, and exploration in procedurally generated worlds. It transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch. We release the dataset, evaluation suite, and model weights to advance research on generalist embodied agents.

## 参考
- http://arxiv.org/abs/2601.02427v1

