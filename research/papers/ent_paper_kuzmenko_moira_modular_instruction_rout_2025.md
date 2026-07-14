---
$id: ent_paper_kuzmenko_moira_modular_instruction_rout_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics'
  zh: MoIRA
  ko: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics'
summary:
  en: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
  zh: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
  ko: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
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
- moira
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01843v2.
sources:
- id: src_001
  type: paper
  title: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (arXiv)'
  url: https://arxiv.org/abs/2507.01843
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoIRA source
  url: https://doi.org/10.48550/arXiv.2507.01843
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 核心内容
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 参考
- http://arxiv.org/abs/2507.01843v2

