---
$id: ent_paper_ask_to_clarify_resolving_instr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue'
  zh: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue'
  ko: ''
summary:
  en: "arXiv:2509.15061v3 Announce Type: replace \nAbstract: Embodied agents are intelligent\
    \ systems designed to perceive, reason, and act within the physical world. While\
    \ the robotics community has long strived to build such versatile agents, a fundamental\
    \ limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act''\
    \ paradigm. These systems assume instructions are unambiguous and execute them\
    \ in a passive fashion, preventing them from resolving uncertainty through dialogue.\
    \ To address this, we propose Ask-to-Clarify, a unified end-to-end framework that\
    \ seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor\
    \ control, eliminating the reliance on high-level action primitives or external\
    \ planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner\
    \ with a Diffusion-based Motor Executor. To bridge the disparity between high-level\
    \ disambiguation and low-level execution, we introduce a Semantic-Visual Alignment\
    \ Adapter, which functions as a cross-modal interface to synthesize semantic intent\
    \ with visual perceptual streams. Furthermore, we observe severe catastrophic\
    \ forgetting: visuomotor fine-tuning completely erases dialogue capabilities.\
    \ To overcome this, we propose a two-stage knowledge-insulation training strategy,\
    \ effectively decoupling dialogue logic from physical manipulation. Extensive\
    \ evaluations across 11 real-world tasks demonstrate that \\framework{} significantly\
    \ outperforms existing methods, offering a promising path toward building truly\
    \ collaborative embodied agents."
  zh: "arXiv:2509.15061v3 Announce Type: replace \nAbstract: Embodied agents are intelligent\
    \ systems designed to perceive, reason, and act within the physical world. While\
    \ the robotics community has long strived to build such versatile agents, a fundamental\
    \ limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act''\
    \ paradigm. These systems assume instructions are unambiguous and execute them\
    \ in a passive fashion, preventing them from resolving uncertainty through dialogue.\
    \ To address this, we propose Ask-to-Clarify, a unified end-to-end framework that\
    \ seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor\
    \ control, eliminating the reliance on high-level action primitives or external\
    \ planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner\
    \ with a Diffusion-based Motor Executor. To bridge the disparity between high-level\
    \ disambiguation and low-level execution, we introduce a Semantic-Visual Alignment\
    \ Adapter, which functions as a cross-modal interface to synthesize semantic intent\
    \ with visual perceptual streams. Furthermore, we observe severe catastrophic\
    \ forgetting: visuomotor fine-tuning completely erases dialogue capabilities.\
    \ To overcome this, we propose a two-stage knowledge-insulation training strategy,\
    \ effectively decoupling dialogue logic from physical manipulation. Extensive\
    \ evaluations across 11 real-world tasks demonstrate that \\framework{} significantly\
    \ outperforms existing methods, offering a promising path toward building truly\
    \ collaborative embodied agents."
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
- ask_to_clarify
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue
    (arXiv)'
  url: https://arxiv.org/abs/2509.15061
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2509.15061v3 Announce Type: replace 
Abstract: Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.
