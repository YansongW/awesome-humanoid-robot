---
$id: ent_paper_vote_vision_language_action_op_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting'
  zh: 'VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting'
  ko: ''
summary:
  en: "arXiv:2507.05116v5 Announce Type: replace-cross \nAbstract: Recent large-scale\
    \ Vision Language Action (VLA) models have shown superior performance in robotic\
    \ manipulation tasks guided by natural language. However, current VLA models suffer\
    \ from two drawbacks: (i) generation of massive tokens leading to high inference\
    \ latency and increased training cost, and (ii) insufficient utilization of generated\
    \ actions resulting in potential performance loss. To address these issues, we\
    \ develop a training framework to finetune VLA models for generating significantly\
    \ fewer action tokens with high parallelism, effectively reducing inference latency\
    \ and training cost. Furthermore, we introduce an inference optimization technique\
    \ with a novel voting-based ensemble strategy to combine current and previous\
    \ action predictions, improving the utilization of generated actions and overall\
    \ performance. Our results demonstrate that we achieve superior performance compared\
    \ with state-of-the-art VLA models, achieving significantly higher success rates\
    \ and 39$\\times$ faster inference than OpenVLA with 46 Hz throughput on edge\
    \ platforms, demonstrating practical deployability. The code is available at https://github.com/LukeLIN-web/VOTE."
  zh: "arXiv:2507.05116v5 Announce Type: replace-cross \nAbstract: Recent large-scale\
    \ Vision Language Action (VLA) models have shown superior performance in robotic\
    \ manipulation tasks guided by natural language. However, current VLA models suffer\
    \ from two drawbacks: (i) generation of massive tokens leading to high inference\
    \ latency and increased training cost, and (ii) insufficient utilization of generated\
    \ actions resulting in potential performance loss. To address these issues, we\
    \ develop a training framework to finetune VLA models for generating significantly\
    \ fewer action tokens with high parallelism, effectively reducing inference latency\
    \ and training cost. Furthermore, we introduce an inference optimization technique\
    \ with a novel voting-based ensemble strategy to combine current and previous\
    \ action predictions, improving the utilization of generated actions and overall\
    \ performance. Our results demonstrate that we achieve superior performance compared\
    \ with state-of-the-art VLA models, achieving significantly higher success rates\
    \ and 39$\\times$ faster inference than OpenVLA with 46 Hz throughput on edge\
    \ platforms, demonstrating practical deployability. The code is available at https://github.com/LukeLIN-web/VOTE."
  ko: ''
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
- robotics
- vote
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting
    (arXiv)'
  url: https://arxiv.org/abs/2507.05116
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2507.05116v5 Announce Type: replace-cross 
Abstract: Recent large-scale Vision Language Action (VLA) models have shown superior performance in robotic manipulation tasks guided by natural language. However, current VLA models suffer from two drawbacks: (i) generation of massive tokens leading to high inference latency and increased training cost, and (ii) insufficient utilization of generated actions resulting in potential performance loss. To address these issues, we develop a training framework to finetune VLA models for generating significantly fewer action tokens with high parallelism, effectively reducing inference latency and training cost. Furthermore, we introduce an inference optimization technique with a novel voting-based ensemble strategy to combine current and previous action predictions, improving the utilization of generated actions and overall performance. Our results demonstrate that we achieve superior performance compared with state-of-the-art VLA models, achieving significantly higher success rates and 39$\times$ faster inference than OpenVLA with 46 Hz throughput on edge platforms, demonstrating practical deployability. The code is available at https://github.com/LukeLIN-web/VOTE.
