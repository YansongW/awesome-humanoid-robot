---
$id: ent_paper_huang_voxposer_composable_3d_value_m_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
  zh: VoxPoser
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
summary:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
  zh: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
- voxposer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.05973v2.
sources:
- id: src_001
  type: paper
  title: VoxPoser source
  url: https://proceedings.mlr.press/v229/huang23b.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 核心内容
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 参考
- http://arxiv.org/abs/2307.05973v2

