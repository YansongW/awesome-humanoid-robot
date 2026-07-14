---
$id: ent_paper_embrace_collisions_humanoid_sh_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
  zh: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
  ko: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions'
summary:
  en: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embrace_collisions
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.01465v1.
sources:
- id: src_001
  type: paper
  title: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions (arXiv)'
  url: https://arxiv.org/abs/2502.01465
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions project page'
  url: https://project-instinct.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Previous humanoid robot research works treat the robot as a bipedal mobile manipulation platform, where only the feet and hands contact the environment. However, we humans use all body parts to interact with the world, e.g., we sit in chairs, get up from the ground, or roll on the floor. Contacting the environment using body parts other than feet and hands brings significant challenges in both model-predictive control and reinforcement learning-based methods. An unpredictable contact sequence makes it almost impossible for model-predictive control to plan ahead in real time. The success of the zero-shot sim-to-real reinforcement learning method for humanoids heavily depends on the acceleration of GPU-based rigid-body physical simulator and simplification of the collision detection. Lacking extreme torso movement of the humanoid research makes all other components non-trivial to design, such as termination conditions, motion commands and reward designs. To address these potential challenges, we propose a general humanoid motion framework that takes discrete motion commands and controls the robot's motor action in real time. Using a GPU-accelerated rigid-body simulator, we train a humanoid whole-body control policy that follows the high-level motion command in the real world in real time, even with stochastic contacts and extremely large robot base rotation and not-so-feasible motion command. More details at https://project-instinct.github.io

## 核心内容
Previous humanoid robot research works treat the robot as a bipedal mobile manipulation platform, where only the feet and hands contact the environment. However, we humans use all body parts to interact with the world, e.g., we sit in chairs, get up from the ground, or roll on the floor. Contacting the environment using body parts other than feet and hands brings significant challenges in both model-predictive control and reinforcement learning-based methods. An unpredictable contact sequence makes it almost impossible for model-predictive control to plan ahead in real time. The success of the zero-shot sim-to-real reinforcement learning method for humanoids heavily depends on the acceleration of GPU-based rigid-body physical simulator and simplification of the collision detection. Lacking extreme torso movement of the humanoid research makes all other components non-trivial to design, such as termination conditions, motion commands and reward designs. To address these potential challenges, we propose a general humanoid motion framework that takes discrete motion commands and controls the robot's motor action in real time. Using a GPU-accelerated rigid-body simulator, we train a humanoid whole-body control policy that follows the high-level motion command in the real world in real time, even with stochastic contacts and extremely large robot base rotation and not-so-feasible motion command. More details at https://project-instinct.github.io

## 参考
- http://arxiv.org/abs/2502.01465v1

