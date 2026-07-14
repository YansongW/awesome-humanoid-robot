---
$id: ent_paper_perceptive_humanoid_parkour_ch_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
  zh: 跑酷的难点不是单技能，而是长程组合
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
summary:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility
    and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments
    demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and
    perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that
    enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses.
    Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted
    atomic human skills into long-horizon kinematic trajectories. This frame
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15827v2.
sources:
- id: src_001
  type: paper
  title: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching (arXiv)'
  url: https://arxiv.org/abs/2602.15827
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 跑酷的难点不是单技能，而是长程组合 project page
  url: https://php-parkour.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 核心内容
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 参考
- http://arxiv.org/abs/2602.15827v2

