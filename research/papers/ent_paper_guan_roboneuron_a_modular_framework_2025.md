---
$id: ent_paper_guan_roboneuron_a_modular_framework_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
  zh: RoboNeuron
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
summary:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
  zh: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
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
- roboneuron
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10394v2.
sources:
- id: src_001
  type: paper
  title: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (arXiv)'
  url: https://arxiv.org/abs/2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboNeuron source
  url: https://doi.org/10.48550/arXiv.2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 核心内容
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 参考
- http://arxiv.org/abs/2512.10394v2

