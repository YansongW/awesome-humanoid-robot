---
$id: ent_paper_chasing_stability_humanoid_run_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
  zh: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
  ko: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
summary:
  en: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chasing_stability
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19573v1.
sources:
- id: src_001
  type: paper
  title: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL (arXiv)'
  url: https://arxiv.org/abs/2509.19573
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 核心内容
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 参考
- http://arxiv.org/abs/2509.19573v1

