---
$id: ent_paper_neau_grasp_vla_graph_based_symbolic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies'
  zh: GraSP-VLA
  ko: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies'
summary:
  en: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
  zh: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
  ko: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- grasp_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.04357v1.
sources:
- id: src_001
  type: paper
  title: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (arXiv)'
  url: https://arxiv.org/abs/2511.04357
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GraSP-VLA source
  url: https://doi.org/10.48550/arXiv.2511.04357
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## 核心内容
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## 参考
- http://arxiv.org/abs/2511.04357v1

