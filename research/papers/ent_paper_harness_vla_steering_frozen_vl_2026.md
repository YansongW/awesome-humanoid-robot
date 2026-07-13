---
$id: ent_paper_harness_vla_steering_frozen_vl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via
    Memory-Guided Agents'
  zh: 'Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via
    Memory-Guided Agents'
  ko: ''
summary:
  en: "arXiv:2607.08448v1 Announce Type: new \nAbstract: Language-conditioned manipulation\
    \ requires both precise contact-rich control and robust reasoning over language,\
    \ scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide\
    \ strong local visuomotor skills, but they are trained on in-distribution task\
    \ trajectories and often fail under deployment perturbations such as semantic\
    \ retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts.\
    \ LLM coding agents provide complementary semantic and compositional reasoning,\
    \ but purely analytic primitives struggle with irregular grasping, constrained\
    \ placement, and articulated-object interaction. We present Harness VLA, a memory-augmented\
    \ agentic framework that exposes a frozen VLA as a retryable contact-rich primitive\
    \ and composes it with a small fixed library of analytic primitives for grounding,\
    \ staging, transport, navigation, and release. Rather than expanding the skill\
    \ library, the harness learns the operating range of these fixed primitives from\
    \ task-specific execution traces, global success rules, and failure models. By\
    \ lifting semantic re-grounding, non-contact execution, and VLA re-staging to\
    \ the planner while reserving the frozen VLA for local contact-rich phases, Harness\
    \ VLA extends pretrained VLAs beyond their original trajectory distribution without\
    \ finetuning. Across perturbed tabletop, household kitchen, and clean-to-randomized\
    \ bimanual manipulation, Harness VLA improves over the strongest relevant baselines\
    \ by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively,\
    \ and reaches 58.4% on RoboTwin C2R."
  zh: "arXiv:2607.08448v1 Announce Type: new \nAbstract: Language-conditioned manipulation\
    \ requires both precise contact-rich control and robust reasoning over language,\
    \ scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide\
    \ strong local visuomotor skills, but they are trained on in-distribution task\
    \ trajectories and often fail under deployment perturbations such as semantic\
    \ retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts.\
    \ LLM coding agents provide complementary semantic and compositional reasoning,\
    \ but purely analytic primitives struggle with irregular grasping, constrained\
    \ placement, and articulated-object interaction. We present Harness VLA, a memory-augmented\
    \ agentic framework that exposes a frozen VLA as a retryable contact-rich primitive\
    \ and composes it with a small fixed library of analytic primitives for grounding,\
    \ staging, transport, navigation, and release. Rather than expanding the skill\
    \ library, the harness learns the operating range of these fixed primitives from\
    \ task-specific execution traces, global success rules, and failure models. By\
    \ lifting semantic re-grounding, non-contact execution, and VLA re-staging to\
    \ the planner while reserving the frozen VLA for local contact-rich phases, Harness\
    \ VLA extends pretrained VLAs beyond their original trajectory distribution without\
    \ finetuning. Across perturbed tabletop, household kitchen, and clean-to-randomized\
    \ bimanual manipulation, Harness VLA improves over the strongest relevant baselines\
    \ by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively,\
    \ and reaches 58.4% on RoboTwin C2R."
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
- harness_vla
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
  title: 'Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives
    via Memory-Guided Agents (arXiv)'
  url: https://arxiv.org/abs/2607.08448
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08448v1 Announce Type: new 
Abstract: Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional reasoning, but purely analytic primitives struggle with irregular grasping, constrained placement, and articulated-object interaction. We present Harness VLA, a memory-augmented agentic framework that exposes a frozen VLA as a retryable contact-rich primitive and composes it with a small fixed library of analytic primitives for grounding, staging, transport, navigation, and release. Rather than expanding the skill library, the harness learns the operating range of these fixed primitives from task-specific execution traces, global success rules, and failure models. By lifting semantic re-grounding, non-contact execution, and VLA re-staging to the planner while reserving the frozen VLA for local contact-rich phases, Harness VLA extends pretrained VLAs beyond their original trajectory distribution without finetuning. Across perturbed tabletop, household kitchen, and clean-to-randomized bimanual manipulation, Harness VLA improves over the strongest relevant baselines by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively, and reaches 58.4% on RoboTwin C2R.
