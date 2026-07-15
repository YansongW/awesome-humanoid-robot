---
$id: ent_paper_shi_hi_robot_open_ended_instructio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models'
  zh: Hi Robot
  ko: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models'
summary:
  en: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
  zh: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
  ko: 'Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (Hi Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Stanford University, University
    of California, Berkeley, and published at ICML25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hi_robot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19417v2.
sources:
- id: src_001
  type: paper
  title: Hi Robot source
  url: https://openreview.net/forum?id=lNVHg9npif
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 核心内容
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping. Videos are available at https://www.pi.website/research/hirobot

## 参考
- http://arxiv.org/abs/2502.19417v2

