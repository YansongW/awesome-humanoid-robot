---
$id: ent_paper_a_closed_loop_multi_agent_fram_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation
  zh: A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation
  ko: ''
summary:
  en: "arXiv:2607.06990v1 Announce Type: new \nAbstract: Multi-robot systems provide\
    \ the parallelism and redundancy necessary for long-horizon tasks, while Large\
    \ Language Models (LLMs) offer the reasoning capabilities to decompose these objectives\
    \ into actionable plans. However, effectively grounding this high-level reasoning\
    \ in physical multi-robot execution remains an open challenge. Existing LLM-based\
    \ approaches fall mainly into two categories: Single-robot methods achieve robust\
    \ contact-rich manipulation but lack the coordination mechanisms required for\
    \ tasks spanning multiple workspaces. Current multi-robot frameworks focus on\
    \ high-level planning, often treating manipulation as an idealized primitive that\
    \ fails to account for real-world execution uncertainties. To address this, we\
    \ propose a hierarchical closed-loop agentic LLM-based framework to ensure robust\
    \ multi-robot manipulation. Our system consists of three specialized agents: the\
    \ Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation\
    \ Agent for each robot executes actions via adaptive tool use, and the Verification\
    \ Agent closes the loop by monitoring physical outcomes and feeding back semantic\
    \ corrections. Extensive real-world experiments demonstrate that our framework\
    \ achieves superior success rates, ensures robust adaptability ranging from single\
    \ to cross workspace manipulation, and offers a generalizable approach for diverse\
    \ manipulation tasks."
  zh: "arXiv:2607.06990v1 Announce Type: new \nAbstract: Multi-robot systems provide\
    \ the parallelism and redundancy necessary for long-horizon tasks, while Large\
    \ Language Models (LLMs) offer the reasoning capabilities to decompose these objectives\
    \ into actionable plans. However, effectively grounding this high-level reasoning\
    \ in physical multi-robot execution remains an open challenge. Existing LLM-based\
    \ approaches fall mainly into two categories: Single-robot methods achieve robust\
    \ contact-rich manipulation but lack the coordination mechanisms required for\
    \ tasks spanning multiple workspaces. Current multi-robot frameworks focus on\
    \ high-level planning, often treating manipulation as an idealized primitive that\
    \ fails to account for real-world execution uncertainties. To address this, we\
    \ propose a hierarchical closed-loop agentic LLM-based framework to ensure robust\
    \ multi-robot manipulation. Our system consists of three specialized agents: the\
    \ Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation\
    \ Agent for each robot executes actions via adaptive tool use, and the Verification\
    \ Agent closes the loop by monitoring physical outcomes and feeding back semantic\
    \ corrections. Extensive real-world experiments demonstrate that our framework\
    \ achieves superior success rates, ensures robust adaptability ranging from single\
    \ to cross workspace manipulation, and offers a generalizable approach for diverse\
    \ manipulation tasks."
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
- a_closed_loop_multi_agent_fram
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
  title: A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.06990
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06990v1 Announce Type: new 
Abstract: Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms required for tasks spanning multiple workspaces. Current multi-robot frameworks focus on high-level planning, often treating manipulation as an idealized primitive that fails to account for real-world execution uncertainties. To address this, we propose a hierarchical closed-loop agentic LLM-based framework to ensure robust multi-robot manipulation. Our system consists of three specialized agents: the Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation Agent for each robot executes actions via adaptive tool use, and the Verification Agent closes the loop by monitoring physical outcomes and feeding back semantic corrections. Extensive real-world experiments demonstrate that our framework achieves superior success rates, ensures robust adaptability ranging from single to cross workspace manipulation, and offers a generalizable approach for diverse manipulation tasks.
