---
$id: ent_paper_play2perfect_what_matters_in_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?'
  zh: 'Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?'
  ko: ''
summary:
  en: "arXiv:2606.26428v2 Announce Type: replace \nAbstract: Multi-fingered robots\
    \ promise the speed and dexterity of human hands, yet challenging problems such\
    \ as precise assembly have remained out of reach. These tasks are contact-rich,\
    \ making data collection for imitation learning difficult, and sparse-reward,\
    \ making direct exploration with reinforcement learning (RL) intractable. Consequently,\
    \ prior work has made progress by structuring the problem with specialized grippers,\
    \ tool attachments, and environment fixtures. In this work, we argue that before\
    \ a robot can perfect precise assembly, it must first learn to play. We further\
    \ ask the question: what factors in the process of learning to play matter for\
    \ precise assembly? We propose Play2Perfect, an RL framework for task-agnostic\
    \ pretraining through play on diverse objects and goals, which is then perfected\
    \ on precise assembly. The goal of play is to acquire reusable manipulation priors,\
    \ such as grasping, in-hand reorientation and pose reaching. Finetuning then adapts\
    \ this general prior to assembly, focusing exploration on the final contact-rich,\
    \ high-precision interactions needed for success. We systematically study key\
    \ design choices in play pretraining, including object diversity, training objective,\
    \ trajectory diversity, and goal precision. We show that our prior is 33x more\
    \ sample-efficient than RL training from scratch, even when provided with dense,\
    \ multi-stage rewards. We demonstrate zero-shot sim-to-real transfer, achieving\
    \ 60% success on tight insertions with only 0.5 mm contact clearance, and over\
    \ 50% success on long-horizon multi-part assembly and screwing."
  zh: "arXiv:2606.26428v2 Announce Type: replace \nAbstract: Multi-fingered robots\
    \ promise the speed and dexterity of human hands, yet challenging problems such\
    \ as precise assembly have remained out of reach. These tasks are contact-rich,\
    \ making data collection for imitation learning difficult, and sparse-reward,\
    \ making direct exploration with reinforcement learning (RL) intractable. Consequently,\
    \ prior work has made progress by structuring the problem with specialized grippers,\
    \ tool attachments, and environment fixtures. In this work, we argue that before\
    \ a robot can perfect precise assembly, it must first learn to play. We further\
    \ ask the question: what factors in the process of learning to play matter for\
    \ precise assembly? We propose Play2Perfect, an RL framework for task-agnostic\
    \ pretraining through play on diverse objects and goals, which is then perfected\
    \ on precise assembly. The goal of play is to acquire reusable manipulation priors,\
    \ such as grasping, in-hand reorientation and pose reaching. Finetuning then adapts\
    \ this general prior to assembly, focusing exploration on the final contact-rich,\
    \ high-precision interactions needed for success. We systematically study key\
    \ design choices in play pretraining, including object diversity, training objective,\
    \ trajectory diversity, and goal precision. We show that our prior is 33x more\
    \ sample-efficient than RL training from scratch, even when provided with dense,\
    \ multi-stage rewards. We demonstrate zero-shot sim-to-real transfer, achieving\
    \ 60% success on tight insertions with only 0.5 mm contact clearance, and over\
    \ 50% success on long-horizon multi-part assembly and screwing."
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
- play2perfect
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?
    (arXiv)'
  url: https://arxiv.org/abs/2606.26428
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2606.26428v2 Announce Type: replace 
Abstract: Multi-fingered robots promise the speed and dexterity of human hands, yet challenging problems such as precise assembly have remained out of reach. These tasks are contact-rich, making data collection for imitation learning difficult, and sparse-reward, making direct exploration with reinforcement learning (RL) intractable. Consequently, prior work has made progress by structuring the problem with specialized grippers, tool attachments, and environment fixtures. In this work, we argue that before a robot can perfect precise assembly, it must first learn to play. We further ask the question: what factors in the process of learning to play matter for precise assembly? We propose Play2Perfect, an RL framework for task-agnostic pretraining through play on diverse objects and goals, which is then perfected on precise assembly. The goal of play is to acquire reusable manipulation priors, such as grasping, in-hand reorientation and pose reaching. Finetuning then adapts this general prior to assembly, focusing exploration on the final contact-rich, high-precision interactions needed for success. We systematically study key design choices in play pretraining, including object diversity, training objective, trajectory diversity, and goal precision. We show that our prior is 33x more sample-efficient than RL training from scratch, even when provided with dense, multi-stage rewards. We demonstrate zero-shot sim-to-real transfer, achieving 60% success on tight insertions with only 0.5 mm contact clearance, and over 50% success on long-horizon multi-part assembly and screwing.
