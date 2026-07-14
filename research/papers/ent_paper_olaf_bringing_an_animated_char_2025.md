---
$id: ent_paper_olaf_bringing_an_animated_char_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Olaf: Bringing an Animated Character to Life in the Physical World'
  zh: 'Olaf: Bringing an Animated Character to Life in the Physical World'
  ko: 'Olaf: Bringing an Animated Character to Life in the Physical World'
summary:
  en: 'Olaf: Bringing an Animated Character to Life in the Physical World is a 2025 work on hardware design for humanoid robots.'
  zh: 'Olaf: Bringing an Animated Character to Life in the Physical World is a 2025 work on hardware design for humanoid robots.'
  ko: 'Olaf: Bringing an Animated Character to Life in the Physical World is a 2025 work on hardware design for humanoid robots.'
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
- olaf
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16705v2.
sources:
- id: src_001
  type: paper
  title: 'Olaf: Bringing an Animated Character to Life in the Physical World (arXiv)'
  url: https://arxiv.org/abs/2512.16705
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Animated characters often move in non-physical ways and have proportions that are far from a typical walking robot. This provides an ideal platform for innovation in both mechanical design and stylized motion control. In this paper, we bring Olaf to life in the physical world, relying on reinforcement learning guided by animation references for control. To create the illusion of Olaf's feet moving along his body, we hide two asymmetric legs under a soft foam skirt. To fit actuators inside the character, we use spherical and planar linkages in the arms, mouth, and eyes. Because the walk cycle results in harsh contact sounds, we introduce additional rewards that noticeably reduce impact noise. The large head, driven by small actuators in the character's slim neck, creates a risk of overheating, amplified by the costume. To keep actuators from overheating, we feed temperature values as additional inputs to policies, introducing new rewards to keep them within bounds. We validate the efficacy of our modeling in simulation and on hardware, demonstrating an unmatched level of believability for a costumed robotic character.

## 核心内容
Animated characters often move in non-physical ways and have proportions that are far from a typical walking robot. This provides an ideal platform for innovation in both mechanical design and stylized motion control. In this paper, we bring Olaf to life in the physical world, relying on reinforcement learning guided by animation references for control. To create the illusion of Olaf's feet moving along his body, we hide two asymmetric legs under a soft foam skirt. To fit actuators inside the character, we use spherical and planar linkages in the arms, mouth, and eyes. Because the walk cycle results in harsh contact sounds, we introduce additional rewards that noticeably reduce impact noise. The large head, driven by small actuators in the character's slim neck, creates a risk of overheating, amplified by the costume. To keep actuators from overheating, we feed temperature values as additional inputs to policies, introducing new rewards to keep them within bounds. We validate the efficacy of our modeling in simulation and on hardware, demonstrating an unmatched level of believability for a costumed robotic character.

## 参考
- http://arxiv.org/abs/2512.16705v2

