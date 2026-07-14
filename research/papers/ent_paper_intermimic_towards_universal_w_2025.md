---
$id: ent_paper_intermimic_towards_universal_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
  zh: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
  ko: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
summary:
  en: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  zh: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  ko: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- intermimic
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.20390v2.
sources:
- id: src_001
  type: paper
  title: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions (arXiv)'
  url: https://arxiv.org/abs/2502.20390
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions project page'
  url: https://sirui-xu.github.io/InterMimic/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## 核心内容
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## 参考
- http://arxiv.org/abs/2502.20390v2

