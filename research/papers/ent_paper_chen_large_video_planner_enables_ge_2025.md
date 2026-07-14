---
$id: ent_paper_chen_large_video_planner_enables_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Large Video Planner Enables Generalizable Robot Control
  zh: LVP
  ko: Large Video Planner Enables Generalizable Robot Control
summary:
  en: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
  zh: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
  ko: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
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
- lvp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15840v2.
sources:
- id: src_001
  type: paper
  title: Large Video Planner Enables Generalizable Robot Control (arXiv)
  url: https://arxiv.org/abs/2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LVP source
  url: https://doi.org/10.48550/arXiv.2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 核心内容
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 参考
- http://arxiv.org/abs/2512.15840v2

