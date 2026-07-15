---
$id: ent_paper_shridhar_cliport_what_and_where_pathway_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLIPort: What and Where Pathways for Robotic Manipulation'
  zh: CLIPort
  ko: 'CLIPort: What and Where Pathways for Robotic Manipulation'
summary:
  en: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
  zh: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
  ko: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cliport
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2109.12098v1.
sources:
- id: src_001
  type: paper
  title: CLIPort source
  url: https://proceedings.mlr.press/v164/shridhar22a.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## 核心内容
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## 参考
- http://arxiv.org/abs/2109.12098v1

