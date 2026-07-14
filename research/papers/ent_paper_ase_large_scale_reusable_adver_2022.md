---
$id: ent_paper_ase_large_scale_reusable_adver_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
  zh: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
  ko: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
summary:
  en: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  zh: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  ko: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ase
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2205.01906v2.
sources:
- id: src_001
  type: paper
  title: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters (arXiv)'
  url: https://arxiv.org/abs/2205.01906
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters project page'
  url: https://xbpeng.github.io/projects/ASE/index.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## 核心内容
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## 参考
- http://arxiv.org/abs/2205.01906v2

