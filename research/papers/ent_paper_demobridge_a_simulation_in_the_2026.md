---
$id: ent_paper_demobridge_a_simulation_in_the_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
  zh: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
  ko: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
summary:
  en: 'arXiv:2607.09519v1 Announce Type: new Abstract: We present DemoBridge, an toolkit that turns a single-view RGB stereo
    recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across
    the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision
    volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution,
    and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate.
    At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning
    jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A
    physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration
    that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable
    and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning.
    Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration.
    We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark.
    Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .'
  zh: 'arXiv:2607.09519v1 Announce Type: new Abstract: We present DemoBridge, an toolkit that turns a single-view RGB stereo
    recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across
    the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision
    volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution,
    and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate.
    At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning
    jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A
    physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration
    that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable
    and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning.
    Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration.
    We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark.
    Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .'
  ko: 'arXiv:2607.09519v1 Announce Type: new Abstract: We present DemoBridge, an toolkit that turns a single-view RGB stereo
    recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across
    the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision
    volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution,
    and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate.
    At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning
    jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A
    physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration
    that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable
    and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning.
    Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration.
    We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark.
    Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- demobridge
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09519v1.
sources:
- id: src_001
  type: paper
  title: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting (arXiv)'
  url: https://arxiv.org/abs/2607.09519
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

## 核心内容
We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

## 参考
- http://arxiv.org/abs/2607.09519v1

