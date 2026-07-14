---
$id: ent_paper_ace_agentic_control_for_embodi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
  zh: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
  ko: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
summary:
  en: "arXiv:2607.04162v1 Announce Type: new \nAbstract: Open-ended tabletop manipulation requires agents to not only understand\
    \ natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for\
    \ Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language.\
    \ Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing\
    \ executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning\
    \ and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask\
    \ specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed\
    \ to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale\
    \ memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using\
    \ the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes,\
    \ and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation\
    \ formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization\
    \ on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard\
    \ end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation\
    \ formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning\
    \ and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation."
  zh: "arXiv:2607.04162v1 Announce Type: new \nAbstract: Open-ended tabletop manipulation requires agents to not only understand\
    \ natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for\
    \ Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language.\
    \ Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing\
    \ executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning\
    \ and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask\
    \ specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed\
    \ to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale\
    \ memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using\
    \ the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes,\
    \ and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation\
    \ formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization\
    \ on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard\
    \ end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation\
    \ formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning\
    \ and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation."
  ko: "arXiv:2607.04162v1 Announce Type: new \nAbstract: Open-ended tabletop manipulation requires agents to not only understand\
    \ natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for\
    \ Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language.\
    \ Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing\
    \ executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning\
    \ and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask\
    \ specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed\
    \ to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale\
    \ memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using\
    \ the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes,\
    \ and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation\
    \ formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization\
    \ on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard\
    \ end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation\
    \ formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning\
    \ and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation."
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
- ace
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04162v1.
sources:
- id: src_001
  type: paper
  title: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning (arXiv)'
  url: https://arxiv.org/abs/2607.04162
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Open-ended tabletop manipulation requires agents to not only understand natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation.

## 核心内容
Open-ended tabletop manipulation requires agents to not only understand natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation.

## 参考
- http://arxiv.org/abs/2607.04162v1

