---
$id: ent_paper_osmo_open_source_tactile_glove_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
  zh: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
  ko: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
summary:
  en: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
  zh: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
  ko: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- osmo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08920v1.
sources:
- id: src_001
  type: paper
  title: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer (arXiv)'
  url: https://arxiv.org/abs/2512.08920
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 核心内容
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 参考
- http://arxiv.org/abs/2512.08920v1

