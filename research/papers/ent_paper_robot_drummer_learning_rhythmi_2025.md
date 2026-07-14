---
$id: ent_paper_robot_drummer_learning_rhythmi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
  zh: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
  ko: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
summary:
  en: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming is a 2025 work on manipulation for humanoid robots.'
  zh: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming is a 2025 work on manipulation for humanoid robots.'
  ko: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming is a 2025 work on manipulation for humanoid robots.'
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
- manipulation
- robot_drummer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.11498v2.
sources:
- id: src_001
  type: paper
  title: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming (arXiv)'
  url: https://arxiv.org/abs/2507.11498
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have seen remarkable advances in dexterity, balance, and locomotion, yet their role in expressive domains such as music performance remains largely unexplored. Musical tasks, like drumming, present unique challenges, including split-second timing, rapid contacts, and multi-limb coordination over performances lasting minutes. In this paper, we introduce Robot Drummer, a humanoid capable of expressive, high-precision drumming across a diverse repertoire of songs. We formulate humanoid drumming as sequential fulfillment of timed contacts and transform drum scores into a Rhythmic Contact Chain. To handle the long-horizon nature of musical performance, we decompose each piece into fixed-length segments and train a single policy across all segments in parallel using reinforcement learning. Through extensive experiments on over thirty popular rock, metal, and jazz tracks, our results demonstrate that Robot Drummer consistently achieves high F1 scores. The learned behaviors exhibit emergent human-like drumming strategies, such as cross-arm strikes, and adaptive stick assignments, demonstrating the potential of reinforcement learning to bring humanoid robots into the domain of creative musical performance. Project page: robotdrummer.github.io

## 核心内容
Humanoid robots have seen remarkable advances in dexterity, balance, and locomotion, yet their role in expressive domains such as music performance remains largely unexplored. Musical tasks, like drumming, present unique challenges, including split-second timing, rapid contacts, and multi-limb coordination over performances lasting minutes. In this paper, we introduce Robot Drummer, a humanoid capable of expressive, high-precision drumming across a diverse repertoire of songs. We formulate humanoid drumming as sequential fulfillment of timed contacts and transform drum scores into a Rhythmic Contact Chain. To handle the long-horizon nature of musical performance, we decompose each piece into fixed-length segments and train a single policy across all segments in parallel using reinforcement learning. Through extensive experiments on over thirty popular rock, metal, and jazz tracks, our results demonstrate that Robot Drummer consistently achieves high F1 scores. The learned behaviors exhibit emergent human-like drumming strategies, such as cross-arm strikes, and adaptive stick assignments, demonstrating the potential of reinforcement learning to bring humanoid robots into the domain of creative musical performance. Project page: robotdrummer.github.io

## 参考
- http://arxiv.org/abs/2507.11498v2

