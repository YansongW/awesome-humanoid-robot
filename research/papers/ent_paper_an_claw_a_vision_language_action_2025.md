---
$id: ent_paper_an_claw_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
  zh: CLAW
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
summary:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
  zh: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- claw
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14143v2.
sources:
- id: src_001
  type: paper
  title: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (arXiv)'
  url: https://arxiv.org/abs/2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLAW source
  url: https://doi.org/10.48550/arXiv.2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 核心内容
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 参考
- http://arxiv.org/abs/2509.14143v2

