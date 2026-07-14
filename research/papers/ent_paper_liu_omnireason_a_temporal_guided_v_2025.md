---
$id: ent_paper_liu_omnireason_a_temporal_guided_v_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving'
  zh: OmniReason
  ko: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving'
summary:
  en: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (OmniReason), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and Technology
    (Guangzhou), The Hong Kong University of Science and Technology.'
  zh: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (OmniReason), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and Technology
    (Guangzhou), The Hong Kong University of Science and Technology.'
  ko: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (OmniReason), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and Technology
    (Guangzhou), The Hong Kong University of Science and Technology.'
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
- omnireason
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.00789v2.
sources:
- id: src_001
  type: paper
  title: 'OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2509.00789
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniReason source
  url: https://doi.org/10.48550/arXiv.2509.00789
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The pursuit of autonomous agents capable of temporally coherent planning is hindered by a fundamental flaw in current vision-language models (VLMs): they lack cognitive inertia. Operating on isolated snapshots, these models cannot form a continuous understanding of the environment, leading to erratic decision jitter and a failure to execute complex, multi-step maneuvers. To remedy this, we introduce CogDriver, a framework designed to build a stable internal representation by instilling this crucial cognitive property. Our work makes two key contributions: (1) We present CogDriver-Data, a large-scale vision-language-action dataset whose narrative annotations provide the supervisory signal for learning temporal dynamics and persistent intent. (2) We develop the CogDriver-Agent, an architecture featuring a sparse temporal memory to maintain a stable internal state. This is enabled by a spatiotemporal knowledge distillation approach that explicitly teaches decision coherence. Comprehensive experiments validate our paradigm: CogDriver-Agent achieves a 22% increase in the closed-loop Driving Score on Bench2Drive and a 21% reduction in mean L2 error on nuScenes, establishing a new state-of-the-art. These significant gains in both long-term decision-making and imitation accuracy provide strong evidence that our agent successfully maintains a temporally coherent internal state, bridging the gap toward more reliable autonomous driving. Project link: https://ocean-luna.github.io/CogDriver.github.io/.

## 核心内容
The pursuit of autonomous agents capable of temporally coherent planning is hindered by a fundamental flaw in current vision-language models (VLMs): they lack cognitive inertia. Operating on isolated snapshots, these models cannot form a continuous understanding of the environment, leading to erratic decision jitter and a failure to execute complex, multi-step maneuvers. To remedy this, we introduce CogDriver, a framework designed to build a stable internal representation by instilling this crucial cognitive property. Our work makes two key contributions: (1) We present CogDriver-Data, a large-scale vision-language-action dataset whose narrative annotations provide the supervisory signal for learning temporal dynamics and persistent intent. (2) We develop the CogDriver-Agent, an architecture featuring a sparse temporal memory to maintain a stable internal state. This is enabled by a spatiotemporal knowledge distillation approach that explicitly teaches decision coherence. Comprehensive experiments validate our paradigm: CogDriver-Agent achieves a 22% increase in the closed-loop Driving Score on Bench2Drive and a 21% reduction in mean L2 error on nuScenes, establishing a new state-of-the-art. These significant gains in both long-term decision-making and imitation accuracy provide strong evidence that our agent successfully maintains a temporally coherent internal state, bridging the gap toward more reliable autonomous driving. Project link: https://ocean-luna.github.io/CogDriver.github.io/.

## 参考
- http://arxiv.org/abs/2509.00789v2

