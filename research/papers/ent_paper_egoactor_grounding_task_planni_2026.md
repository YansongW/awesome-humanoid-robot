---
$id: ent_paper_egoactor_grounding_task_planni_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
  zh: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
  ko: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models'
summary:
  en: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
  zh: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
  ko: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models
    is a 2026 work on navigation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egoactor
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04515v1.
sources:
- id: src_001
  type: paper
  title: 'EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language
    Models (arXiv)'
  url: https://arxiv.org/abs/2602.04515
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 核心内容
Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types. Towards addressing these challenges, we propose a novel task - EgoActing, which requires directly grounding high-level instructions into various, precise, spatially aware humanoid actions. We further instantiate this task by introducing EgoActor, a unified and scalable vision-language model (VLM) that can predict locomotion primitives (e.g., walk, turn, move sideways, change height), head movements, manipulation commands, and human-robot interactions to coordinate perception and execution in real-time. We leverage broad supervision over egocentric RGB-only data from real-world demonstrations, spatial reasoning question-answering, and simulated environment demonstrations, enabling EgoActor to make robust, context-aware decisions and perform fluent action inference (under 1s) with both 8B and 4B parameter models. Extensive evaluations in both simulated and real-world environments demonstrate that EgoActor effectively bridges abstract task planning and concrete motor execution, while generalizing across diverse tasks and unseen environments.

## 参考
- http://arxiv.org/abs/2602.04515v1

