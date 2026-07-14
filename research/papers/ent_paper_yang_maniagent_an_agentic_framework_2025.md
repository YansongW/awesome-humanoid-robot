---
$id: ent_paper_yang_maniagent_an_agentic_framework_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiAgent: An Agentic Framework for General Robotic Manipulation'
  zh: ManiAgent
  ko: 'ManiAgent: An Agentic Framework for General Robotic Manipulation'
summary:
  en: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (ManiAgent), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Technology, Nanjing University, University of Science
    and Technology of China.'
  zh: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (ManiAgent), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Technology, Nanjing University, University of Science
    and Technology of China.'
  ko: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (ManiAgent), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Technology, Nanjing University, University of Science
    and Technology of China.'
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
- maniagent
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11660v2.
sources:
- id: src_001
  type: paper
  title: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.11660
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ManiAgent source
  url: https://doi.org/10.48550/arXiv.2510.11660
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While Vision-Language-Action (VLA) models have demonstrated impressive capabilities in robotic manipulation, their performance in complex reasoning and long-horizon task planning is limited by data scarcity and model capacity. To address this, we introduce ManiAgent, an agentic architecture for general manipulation tasks that achieves end-to-end output from task descriptions and environmental inputs to robotic manipulation actions. In this framework, multiple agents involve inter-agent communication to perform environmental perception, sub-task decomposition and action generation, enabling efficient handling of complex manipulation scenarios. Evaluations show ManiAgent achieves an 86.8% success rate on the SimplerEnv benchmark and 95.8% on real-world pick-and-place tasks, enabling efficient data collection that yields VLA models with performance comparable to those trained on human-annotated datasets. The project webpage is available at https://yi-yang929.github.io/ManiAgent/.

## 核心内容
While Vision-Language-Action (VLA) models have demonstrated impressive capabilities in robotic manipulation, their performance in complex reasoning and long-horizon task planning is limited by data scarcity and model capacity. To address this, we introduce ManiAgent, an agentic architecture for general manipulation tasks that achieves end-to-end output from task descriptions and environmental inputs to robotic manipulation actions. In this framework, multiple agents involve inter-agent communication to perform environmental perception, sub-task decomposition and action generation, enabling efficient handling of complex manipulation scenarios. Evaluations show ManiAgent achieves an 86.8% success rate on the SimplerEnv benchmark and 95.8% on real-world pick-and-place tasks, enabling efficient data collection that yields VLA models with performance comparable to those trained on human-annotated datasets. The project webpage is available at https://yi-yang929.github.io/ManiAgent/.

## 参考
- http://arxiv.org/abs/2510.11660v2

