---
$id: ent_paper_learning_visuotactile_skills_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Visuotactile Skills with Two Multifingered Hands
  zh: Learning Visuotactile Skills with Two Multifingered Hands
  ko: Learning Visuotactile Skills with Two Multifingered Hands
summary:
  en: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
  zh: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
  ko: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_visuotactile_skills_w
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.16823v2.
sources:
- id: src_001
  type: paper
  title: Learning Visuotactile Skills with Two Multifingered Hands (arXiv)
  url: https://arxiv.org/abs/2404.16823
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Visuotactile Skills with Two Multifingered Hands project page
  url: https://toruowo.github.io/hato/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 核心内容
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 参考
- http://arxiv.org/abs/2404.16823v2

