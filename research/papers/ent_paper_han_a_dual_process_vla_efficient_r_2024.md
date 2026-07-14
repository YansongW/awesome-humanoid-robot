---
$id: ent_paper_han_a_dual_process_vla_efficient_r_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM'
  zh: DP-VLA
  ko: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM'
summary:
  en: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (DP-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by ETRI.'
  zh: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (DP-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by ETRI.'
  ko: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (DP-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by ETRI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dp_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.15549v1.
sources:
- id: src_001
  type: paper
  title: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (arXiv)'
  url: https://arxiv.org/abs/2410.15549
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DP-VLA source
  url: https://doi.org/10.48550/arXiv.2410.15549
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are receiving increasing attention for their ability to enable robots to perform complex tasks by integrating visual context with linguistic commands. However, achieving efficient real-time performance remains challenging due to the high computational demands of existing models. To overcome this, we propose Dual Process VLA (DP-VLA), a hierarchical framework inspired by dual-process theory. DP-VLA utilizes a Large System 2 Model (L-Sys2) for complex reasoning and decision-making, while a Small System 1 Model (S-Sys1) handles real-time motor control and sensory processing. By leveraging Vision-Language Models (VLMs), the L-Sys2 operates at low frequencies, reducing computational overhead, while the S-Sys1 ensures fast and accurate task execution. Experimental results on the RoboCasa dataset demonstrate that DP-VLA achieves faster inference and higher task success rates, providing a scalable solution for advanced robotic applications.

## 核心内容
Vision-Language-Action (VLA) models are receiving increasing attention for their ability to enable robots to perform complex tasks by integrating visual context with linguistic commands. However, achieving efficient real-time performance remains challenging due to the high computational demands of existing models. To overcome this, we propose Dual Process VLA (DP-VLA), a hierarchical framework inspired by dual-process theory. DP-VLA utilizes a Large System 2 Model (L-Sys2) for complex reasoning and decision-making, while a Small System 1 Model (S-Sys1) handles real-time motor control and sensory processing. By leveraging Vision-Language Models (VLMs), the L-Sys2 operates at low frequencies, reducing computational overhead, while the S-Sys1 ensures fast and accurate task execution. Experimental results on the RoboCasa dataset demonstrate that DP-VLA achieves faster inference and higher task success rates, providing a scalable solution for advanced robotic applications.

## 参考
- http://arxiv.org/abs/2410.15549v1

