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

## Overview
We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

## Content
We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

## 개요
본 논문에서는 단일 시점 RGB 스테레오로 촬영된 인간 손 시연 영상을 실행 가능하고 물리적으로 검증된 로봇 팔 궤적으로 변환하는 툴킷인 DemoBridge를 제시합니다. 신체적 차이(embodiment gap)를 넘어선 리타겟팅은 어렵습니다. 로봇 팔은 긴 관절 구조를 가진 몸체로 목표물에 도달하며, 각 링크는 손보다 훨씬 큰 충돌 부피를 지닙니다. 매핑된 엔드 이펙터 자세에 대한 역기구학을 풀면 충돌 없는 해를 찾지 못하는 경우가 많으며, 궤적은 모든 웨이포인트에서 이를 강제합니다. 단일 시점은 노이즈를 추가하여 시연된 기준을 부정확하게 만듭니다. DemoBridge의 핵심은 단일 충돌 인식 플래너입니다. 이 플래너는 전체 관절 궤적을 한 번에 최적화하며, 대체 파지 자세, 전체 팔 및 파지된 물체의 충돌, 시연된 경로에 대한 충실도를 공동으로 고려합니다. 물리 시뮬레이터가 루프 내에서 실행됩니다. 각 단계가 생성될 때 검증하고 실패 시 역추적하므로, 주어진 대로 재현할 수 없는 시연은 폐기되지 않고 재계획됩니다. 결과 동작 시퀀스는 동적으로 안정적이며 시연된 조작에 충실합니다. 또한 정책 학습을 위한 즉시 사용 가능한 시뮬레이션 롤아웃으로도 활용됩니다. 파지 타이밍은 자동으로 추론되며, 인식 백엔드, 로봇 및 파이프라인 단계는 설정에서 교체 가능합니다. 우리는 세 가지 실제 시연 작업에서 전체 파이프라인 리타겟팅을 평가하고, 통제된 합성 벤치마크에서 플래너를 평가합니다. 코드는 https://gitlab.kuleuven.be/u0123974/demo-bridge/ 에서 확인할 수 있습니다.

## 핵심 내용
본 논문에서는 단일 시점 RGB 스테레오로 촬영된 인간 손 시연 영상을 실행 가능하고 물리적으로 검증된 로봇 팔 궤적으로 변환하는 툴킷인 DemoBridge를 제시합니다. 신체적 차이(embodiment gap)를 넘어선 리타겟팅은 어렵습니다. 로봇 팔은 긴 관절 구조를 가진 몸체로 목표물에 도달하며, 각 링크는 손보다 훨씬 큰 충돌 부피를 지닙니다. 매핑된 엔드 이펙터 자세에 대한 역기구학을 풀면 충돌 없는 해를 찾지 못하는 경우가 많으며, 궤적은 모든 웨이포인트에서 이를 강제합니다. 단일 시점은 노이즈를 추가하여 시연된 기준을 부정확하게 만듭니다. DemoBridge의 핵심은 단일 충돌 인식 플래너입니다. 이 플래너는 전체 관절 궤적을 한 번에 최적화하며, 대체 파지 자세, 전체 팔 및 파지된 물체의 충돌, 시연된 경로에 대한 충실도를 공동으로 고려합니다. 물리 시뮬레이터가 루프 내에서 실행됩니다. 각 단계가 생성될 때 검증하고 실패 시 역추적하므로, 주어진 대로 재현할 수 없는 시연은 폐기되지 않고 재계획됩니다. 결과 동작 시퀀스는 동적으로 안정적이며 시연된 조작에 충실합니다. 또한 정책 학습을 위한 즉시 사용 가능한 시뮬레이션 롤아웃으로도 활용됩니다. 파지 타이밍은 자동으로 추론되며, 인식 백엔드, 로봇 및 파이프라인 단계는 설정에서 교체 가능합니다. 우리는 세 가지 실제 시연 작업에서 전체 파이프라인 리타겟팅을 평가하고, 통제된 합성 벤치마크에서 플래너를 평가합니다. 코드는 https://gitlab.kuleuven.be/u0123974/demo-bridge/ 에서 확인할 수 있습니다.
