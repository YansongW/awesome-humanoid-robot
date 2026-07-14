---
$id: ent_paper_bendikas_focusing_on_what_matters_objec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
  zh: Oat-VLA
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
summary:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
  zh: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
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
- oat_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23655v1.
sources:
- id: src_001
  type: paper
  title: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (arXiv)'
  url: https://arxiv.org/abs/2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Oat-VLA source
  url: https://doi.org/10.48550/arXiv.2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 核心内容
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 参考
- http://arxiv.org/abs/2509.23655v1

