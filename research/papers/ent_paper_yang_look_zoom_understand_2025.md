---
$id: ent_paper_yang_look_zoom_understand_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Look Zoom Understand
  zh: EyeVLA
  ko: Look Zoom Understand
summary:
  en: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
  zh: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
  ko: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eyevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15279v2.
sources:
- id: src_001
  type: paper
  title: Look Zoom Understand (arXiv)
  url: https://arxiv.org/abs/2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EyeVLA source
  url: https://doi.org/10.48550/arXiv.2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 核心内容
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 参考
- http://arxiv.org/abs/2511.15279v2

