---
$id: ent_paper_learning_agile_quadrotor_fligh_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Agile Quadrotor Flight in the Real World
  zh: Learning Agile Quadrotor Flight in the Real World
  ko: Learning Agile Quadrotor Flight in the Real World
summary:
  en: "arXiv:2602.10111v2 Announce Type: replace \nAbstract: Learning-based controllers have achieved impressive performance\
    \ in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification\
    \ for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution\
    \ scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these\
    \ evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining\
    \ their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical\
    \ limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive\
    \ framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive\
    \ Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment\
    \ a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation\
    \ Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate\
    \ that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative\
    \ base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings\
    \ underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism\
    \ for sustained performance improvement in aggressive flight regimes."
  zh: "arXiv:2602.10111v2 Announce Type: replace \nAbstract: Learning-based controllers have achieved impressive performance\
    \ in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification\
    \ for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution\
    \ scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these\
    \ evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining\
    \ their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical\
    \ limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive\
    \ framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive\
    \ Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment\
    \ a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation\
    \ Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate\
    \ that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative\
    \ base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings\
    \ underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism\
    \ for sustained performance improvement in aggressive flight regimes."
  ko: "arXiv:2602.10111v2 Announce Type: replace \nAbstract: Learning-based controllers have achieved impressive performance\
    \ in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification\
    \ for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution\
    \ scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these\
    \ evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining\
    \ their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical\
    \ limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive\
    \ framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive\
    \ Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment\
    \ a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation\
    \ Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate\
    \ that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative\
    \ base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings\
    \ underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism\
    \ for sustained performance improvement in aggressive flight regimes."
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
- learning_agile_quadrotor_fligh
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.10111v2.
sources:
- id: src_001
  type: paper
  title: Learning Agile Quadrotor Flight in the Real World (arXiv)
  url: https://arxiv.org/abs/2602.10111
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 核心内容
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 参考
- http://arxiv.org/abs/2602.10111v2

