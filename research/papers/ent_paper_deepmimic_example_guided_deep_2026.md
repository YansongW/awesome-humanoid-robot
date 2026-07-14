---
$id: ent_paper_deepmimic_example_guided_deep_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
  zh: 很多人形控制论文的源头问题
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
summary:
  en: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can
    execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental
    variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies
    capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes
    in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such
    as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective,
    we can train characters that react intelligently in interactive settings, e
  ko: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills is a knowledge node related
    to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1804.02717v3.
sources:
- id: src_001
  type: paper
  title: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills (arXiv)'
  url: https://arxiv.org/abs/1804.02717
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 很多人形控制论文的源头问题 project page
  url: https://xbpeng.github.io/projects/DeepMimic/index.html
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 核心内容
A longstanding goal in character animation is to combine data-driven specification of behavior with a system that can execute a similar behavior in a physical simulation, thus enabling realistic responses to perturbations and environmental variation. We show that well-known reinforcement learning (RL) methods can be adapted to learn robust control policies capable of imitating a broad range of example motion clips, while also learning complex recoveries, adapting to changes in morphology, and accomplishing user-specified goals. Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions. By combining a motion-imitation objective with a task objective, we can train characters that react intelligently in interactive settings, e.g., by walking in a desired direction or throwing a ball at a user-specified target. This approach thus combines the convenience and motion quality of using motion clips to define the desired style and appearance, with the flexibility and generality afforded by RL methods and physics-based animation. We further explore a number of methods for integrating multiple clips into the learning process to develop multi-skilled agents capable of performing a rich repertoire of diverse skills. We demonstrate results using multiple characters (human, Atlas robot, bipedal dinosaur, dragon) and a large variety of skills, including locomotion, acrobatics, and martial arts.

## 参考
- http://arxiv.org/abs/1804.02717v3

