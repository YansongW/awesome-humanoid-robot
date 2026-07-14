---
$id: ent_paper_wang_physiagent_an_embodied_agent_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysiAgent: An Embodied Agent Framework in Physical World'
  zh: PhysiAgent
  ko: 'PhysiAgent: An Embodied Agent Framework in Physical World'
summary:
  en: 'PhysiAgent: An Embodied Agent Framework in Physical World (PhysiAgent), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua University, Peking University,
    University of California, Berkeley.'
  zh: 'PhysiAgent: An Embodied Agent Framework in Physical World (PhysiAgent), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua University, Peking University,
    University of California, Berkeley.'
  ko: 'PhysiAgent: An Embodied Agent Framework in Physical World (PhysiAgent), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua University, Peking University,
    University of California, Berkeley.'
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
- physiagent
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.24524v1.
sources:
- id: src_001
  type: paper
  title: 'PhysiAgent: An Embodied Agent Framework in Physical World (arXiv)'
  url: https://arxiv.org/abs/2509.24524
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PhysiAgent source
  url: https://doi.org/10.48550/arXiv.2509.24524
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have achieved notable success but often struggle with limited generalizations. To address this, integrating generalized Vision-Language Models (VLMs) as assistants to VLAs has emerged as a popular solution. However, current approaches often combine these models in rigid, sequential structures: using VLMs primarily for high-level scene understanding and task planning, and VLAs merely as executors of lower-level actions, leading to ineffective collaboration and poor grounding challenges. In this paper, we propose an embodied agent framework, PhysiAgent, tailored to operate effectively in physical environments. By incorporating monitor, memory, self-reflection mechanisms, and lightweight off-the-shelf toolboxes, PhysiAgent offers an autonomous scaffolding framework to prompt VLMs to organize different components based on real-time proficiency feedback from VLAs to maximally exploit VLAs' capabilities. Experimental results demonstrate significant improvements in task-solving performance on complex real-world robotic tasks, showcasing effective self-regulation of VLMs, coherent tool collaboration, and adaptive evolution of the framework during execution. PhysiAgent makes practical and pioneering efforts to integrate VLMs and VLAs, effectively grounding embodied agent frameworks in real-world settings.

## 核心内容
Vision-Language-Action (VLA) models have achieved notable success but often struggle with limited generalizations. To address this, integrating generalized Vision-Language Models (VLMs) as assistants to VLAs has emerged as a popular solution. However, current approaches often combine these models in rigid, sequential structures: using VLMs primarily for high-level scene understanding and task planning, and VLAs merely as executors of lower-level actions, leading to ineffective collaboration and poor grounding challenges. In this paper, we propose an embodied agent framework, PhysiAgent, tailored to operate effectively in physical environments. By incorporating monitor, memory, self-reflection mechanisms, and lightweight off-the-shelf toolboxes, PhysiAgent offers an autonomous scaffolding framework to prompt VLMs to organize different components based on real-time proficiency feedback from VLAs to maximally exploit VLAs' capabilities. Experimental results demonstrate significant improvements in task-solving performance on complex real-world robotic tasks, showcasing effective self-regulation of VLMs, coherent tool collaboration, and adaptive evolution of the framework during execution. PhysiAgent makes practical and pioneering efforts to integrate VLMs and VLAs, effectively grounding embodied agent frameworks in real-world settings.

## 参考
- http://arxiv.org/abs/2509.24524v1

