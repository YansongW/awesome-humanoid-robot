---
$id: ent_paper_clear_closed_loop_reinforcemen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  zh: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  ko: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
summary:
  en: "arXiv:2607.02841v1 Announce Type: new \nAbstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor\
    \ information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers\
    \ have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,\
    \ language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts\
    \ imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.\
    \ Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop\
    \ planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning\
    \ (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained\
    \ VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL\
    \ for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we\
    \ design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows\
    \ us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention\
    \ and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods\
    \ and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive."
  zh: "arXiv:2607.02841v1 Announce Type: new \nAbstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor\
    \ information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers\
    \ have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,\
    \ language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts\
    \ imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.\
    \ Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop\
    \ planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning\
    \ (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained\
    \ VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL\
    \ for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we\
    \ design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows\
    \ us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention\
    \ and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods\
    \ and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive."
  ko: "arXiv:2607.02841v1 Announce Type: new \nAbstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor\
    \ information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers\
    \ have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,\
    \ language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts\
    \ imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.\
    \ Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop\
    \ planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning\
    \ (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained\
    \ VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL\
    \ for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we\
    \ design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows\
    \ us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention\
    \ and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods\
    \ and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive."
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
- clear
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02841v1.
sources:
- id: src_001
  type: paper
  title: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2607.02841
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 核心内容
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 参考
- http://arxiv.org/abs/2607.02841v1

