---
$id: ent_paper_du_learning_universal_policies_vi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Universal Policies via Text-Guided Video Generation
  zh: UniPi
  ko: Learning Universal Policies via Text-Guided Video Generation
summary:
  en: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
  zh: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
  ko: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
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
- unipi
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.00111v3.
sources:
- id: src_001
  type: website
  title: UniPi source
  url: http://papers.nips.cc/paper_files/paper/2023/hash/1d5b9233ad716a43be5c0d3023cb82d0-Abstract-Conference.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 核心内容
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 参考
- http://arxiv.org/abs/2302.00111v3

