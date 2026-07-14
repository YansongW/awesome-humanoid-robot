---
$id: ent_paper_do_you_have_freestyle_expressi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
  zh: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
  ko: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
summary:
  en: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control is a 2025 work on locomotion for humanoid robots.
  zh: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control is a 2025 work on locomotion for humanoid robots.
  ko: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- do_you_have_freestyle_expressi
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23650v2.
sources:
- id: src_001
  type: paper
  title: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control (arXiv)
  url: https://arxiv.org/abs/2512.23650
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans intuitively move to sound, but current humanoid robots lack expressive improvisational capabilities, confined to predefined motions or sparse commands. Generating motion from audio and then retargeting it to robots relies on explicit motion reconstruction, leading to cascaded errors, high latency, and disjointed acoustic-actuation mapping. We propose RoboPerform, the first unified audio-to-locomotion framework that can directly generate music-driven dance and speech-driven co-speech gestures from audio. Guided by the core principle of "motion = content + style", the framework treats audio as implicit style signals and eliminates the need for explicit motion reconstruction. RoboPerform integrates a ResMoE teacher policy for adapting to diverse motion patterns and a diffusion-based student policy for audio style injection. This retargeting-free design ensures low latency and high fidelity. Experimental validation shows that RoboPerform achieves promising results in physical plausibility and audio alignment, successfully transforming robots into responsive performers capable of reacting to audio.

## 核心内容
Humans intuitively move to sound, but current humanoid robots lack expressive improvisational capabilities, confined to predefined motions or sparse commands. Generating motion from audio and then retargeting it to robots relies on explicit motion reconstruction, leading to cascaded errors, high latency, and disjointed acoustic-actuation mapping. We propose RoboPerform, the first unified audio-to-locomotion framework that can directly generate music-driven dance and speech-driven co-speech gestures from audio. Guided by the core principle of "motion = content + style", the framework treats audio as implicit style signals and eliminates the need for explicit motion reconstruction. RoboPerform integrates a ResMoE teacher policy for adapting to diverse motion patterns and a diffusion-based student policy for audio style injection. This retargeting-free design ensures low latency and high fidelity. Experimental validation shows that RoboPerform achieves promising results in physical plausibility and audio alignment, successfully transforming robots into responsive performers capable of reacting to audio.

## 参考
- http://arxiv.org/abs/2512.23650v2

