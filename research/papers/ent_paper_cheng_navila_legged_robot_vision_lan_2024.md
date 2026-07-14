---
$id: ent_paper_cheng_navila_legged_robot_vision_lan_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation'
  zh: NaVILA
  ko: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation'
summary:
  en: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (NaVILA), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, USC, NVIDIA, and published at RSS25.'
  zh: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (NaVILA), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, USC, NVIDIA, and published at RSS25.'
  ko: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (NaVILA), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, USC, NVIDIA, and published at RSS25.'
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
- navila
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04453v2.
sources:
- id: src_001
  type: paper
  title: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (arXiv)'
  url: https://arxiv.org/abs/2412.04453
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NaVILA source
  url: https://doi.org/10.48550/arXiv.2412.04453
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This paper proposes to solve the problem of Vision-and-Language Navigation with legged robots, which not only provides a flexible way for humans to command but also allows the robot to navigate through more challenging and cluttered scenes. However, it is non-trivial to translate human language instructions all the way to low-level leg joint actions. We propose NaVILA, a 2-level framework that unifies a Vision-Language-Action model (VLA) with locomotion skills. Instead of directly predicting low-level actions from VLA, NaVILA first generates mid-level actions with spatial information in the form of language, (e.g., "moving forward 75cm"), which serves as an input for a visual locomotion RL policy for execution. NaVILA substantially improves previous approaches on existing benchmarks. The same advantages are demonstrated in our newly developed benchmarks with IsaacLab, featuring more realistic scenes, low-level controls, and real-world robot experiments. We show more results at https://navila-bot.github.io/

## 核心内容
This paper proposes to solve the problem of Vision-and-Language Navigation with legged robots, which not only provides a flexible way for humans to command but also allows the robot to navigate through more challenging and cluttered scenes. However, it is non-trivial to translate human language instructions all the way to low-level leg joint actions. We propose NaVILA, a 2-level framework that unifies a Vision-Language-Action model (VLA) with locomotion skills. Instead of directly predicting low-level actions from VLA, NaVILA first generates mid-level actions with spatial information in the form of language, (e.g., "moving forward 75cm"), which serves as an input for a visual locomotion RL policy for execution. NaVILA substantially improves previous approaches on existing benchmarks. The same advantages are demonstrated in our newly developed benchmarks with IsaacLab, featuring more realistic scenes, low-level controls, and real-world robot experiments. We show more results at https://navila-bot.github.io/

## 参考
- http://arxiv.org/abs/2412.04453v2

