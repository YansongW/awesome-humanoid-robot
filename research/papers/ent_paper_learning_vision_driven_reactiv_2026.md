---
$id: ent_paper_learning_vision_driven_reactiv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots
  zh: 足球任务里，视觉和动作是同一件事
  ko: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots
summary:
  en: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots is a knowledge node related to paper in the humanoid
    robot value chain.
  zh: Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly
    coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses
    and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues.
    In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive
    soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial
    Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded
    dynamic control. We introduce an encoder-decoder architecture comb
  ko: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots is a knowledge node related to paper in the humanoid
    robot value chain.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.03996v1.
sources:
- id: src_001
  type: paper
  title: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2511.03996
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 足球任务里，视觉和动作是同一件事 project page
  url: https://humanoid-kick.github.io
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## 核心内容
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## 参考
- http://arxiv.org/abs/2511.03996v1

