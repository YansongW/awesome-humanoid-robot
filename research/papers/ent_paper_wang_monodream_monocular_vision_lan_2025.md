---
$id: ent_paper_wang_monodream_monocular_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming'
  zh: MonoDream
  ko: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming'
summary:
  en: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
  zh: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
  ko: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
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
- monodream
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.02549v4.
sources:
- id: src_001
  type: paper
  title: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (arXiv)'
  url: https://arxiv.org/abs/2508.02549
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MonoDream source
  url: https://doi.org/10.48550/arXiv.2508.02549
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## 核心内容
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## 参考
- http://arxiv.org/abs/2508.02549v4

