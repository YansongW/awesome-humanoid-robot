---
$id: ent_paper_ye_actdistill_general_action_guid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
  zh: ActDistill
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
summary:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
  zh: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- actdistill
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18082v3.
sources:
- id: src_001
  type: paper
  title: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ActDistill source
  url: https://doi.org/10.48550/arXiv.2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 核心内容
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 参考
- http://arxiv.org/abs/2511.18082v3

