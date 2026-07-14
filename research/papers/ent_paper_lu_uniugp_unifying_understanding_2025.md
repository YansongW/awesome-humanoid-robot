---
$id: ent_paper_lu_uniugp_unifying_understanding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving'
  zh: UniUGP
  ko: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving'
summary:
  en: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (UniUGP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ByteDance Seed, HKUST-GZ.'
  zh: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (UniUGP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ByteDance Seed, HKUST-GZ.'
  ko: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (UniUGP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ByteDance Seed, HKUST-GZ.'
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
- robotic_manipulation
- uniugp
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09864v1.
sources:
- id: src_001
  type: paper
  title: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2512.09864
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniUGP source
  url: https://doi.org/10.48550/arXiv.2512.09864
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous driving (AD) systems struggle in long-tail scenarios due to limited world knowledge and weak visual dynamic modeling. Existing vision-language-action (VLA)-based methods cannot leverage unlabeled videos for visual causal learning, while world model-based methods lack reasoning capabilities from large language models. In this paper, we construct multiple specialized datasets providing reasoning and planning annotations for complex scenarios. Then, a unified Understanding-Generation-Planning framework, named UniUGP, is proposed to synergize scene reasoning, future video generation, and trajectory planning through a hybrid expert architecture. By integrating pre-trained VLMs and video generation models, UniUGP leverages visual dynamics and semantic reasoning to enhance planning performance. Taking multi-frame observations and language instructions as input, it produces interpretable chain-of-thought reasoning, physically consistent trajectories, and coherent future videos. We introduce a four-stage training strategy that progressively builds these capabilities across multiple existing AD datasets, along with the proposed specialized datasets. Experiments demonstrate state-of-the-art performance in perception, reasoning, and decision-making, with superior generalization to challenging long-tail situations.

## 核心内容
Autonomous driving (AD) systems struggle in long-tail scenarios due to limited world knowledge and weak visual dynamic modeling. Existing vision-language-action (VLA)-based methods cannot leverage unlabeled videos for visual causal learning, while world model-based methods lack reasoning capabilities from large language models. In this paper, we construct multiple specialized datasets providing reasoning and planning annotations for complex scenarios. Then, a unified Understanding-Generation-Planning framework, named UniUGP, is proposed to synergize scene reasoning, future video generation, and trajectory planning through a hybrid expert architecture. By integrating pre-trained VLMs and video generation models, UniUGP leverages visual dynamics and semantic reasoning to enhance planning performance. Taking multi-frame observations and language instructions as input, it produces interpretable chain-of-thought reasoning, physically consistent trajectories, and coherent future videos. We introduce a four-stage training strategy that progressively builds these capabilities across multiple existing AD datasets, along with the proposed specialized datasets. Experiments demonstrate state-of-the-art performance in perception, reasoning, and decision-making, with superior generalization to challenging long-tail situations.

## 参考
- http://arxiv.org/abs/2512.09864v1

