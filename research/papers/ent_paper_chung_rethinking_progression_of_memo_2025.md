---
$id: ent_paper_chung_rethinking_progression_of_memo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
  zh: Embodied-SlotSSM
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
summary:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
  zh: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_slotssm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.11478v3.
sources:
- id: src_001
  type: paper
  title: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (arXiv)'
  url: https://arxiv.org/abs/2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Embodied-SlotSSM source
  url: https://doi.org/10.48550/arXiv.2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 核心内容
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 参考
- http://arxiv.org/abs/2511.11478v3

