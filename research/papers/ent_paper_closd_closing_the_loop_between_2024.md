---
$id: ent_paper_closd_closing_the_loop_between_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  zh: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
summary:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
  zh: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- closd
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03441v1.
sources:
- id: src_001
  type: paper
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control (arXiv)'
  url: https://arxiv.org/abs/2410.03441
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control project page'
  url: https://guytevet.github.io/CLoSD-page/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 核心内容
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 参考
- http://arxiv.org/abs/2410.03441v1

