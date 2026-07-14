---
$id: ent_paper_robust_humanoid_walking_on_com_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
  zh: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
  ko: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
summary:
  en: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL is a 2025 work on locomotion for humanoid robots.
  zh: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL is a 2025 work on locomotion for humanoid robots.
  ko: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robust_humanoid_walking_on_com
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.13619v1.
sources:
- id: src_001
  type: paper
  title: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL (arXiv)
  url: https://arxiv.org/abs/2504.13619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
For the deployment of legged robots in real-world environments, it is essential to develop robust locomotion control methods for challenging terrains that may exhibit unexpected deformability and irregularity. In this paper, we explore the application of sim-to-real deep reinforcement learning (RL) for the design of bipedal locomotion controllers for humanoid robots on compliant and uneven terrains. Our key contribution is to show that a simple training curriculum for exposing the RL agent to randomized terrains in simulation can achieve robust walking on a real humanoid robot using only proprioceptive feedback. We train an end-to-end bipedal locomotion policy using the proposed approach, and show extensive real-robot demonstration on the HRP-5P humanoid over several difficult terrains inside and outside the lab environment. Further, we argue that the robustness of a bipedal walking policy can be improved if the robot is allowed to exhibit aperiodic motion with variable stepping frequency. We propose a new control policy to enable modification of the observed clock signal, leading to adaptive gait frequencies depending on the terrain and command velocity. Through simulation experiments, we show the effectiveness of this policy specifically for walking over challenging terrains by controlling swing and stance durations. The code for training and evaluation is available online at https://github.com/rohanpsingh/LearningHumanoidWalking. Demo video is available at https://www.youtube.com/watch?v=ZgfNzGAkk2Q.

## 核心内容
For the deployment of legged robots in real-world environments, it is essential to develop robust locomotion control methods for challenging terrains that may exhibit unexpected deformability and irregularity. In this paper, we explore the application of sim-to-real deep reinforcement learning (RL) for the design of bipedal locomotion controllers for humanoid robots on compliant and uneven terrains. Our key contribution is to show that a simple training curriculum for exposing the RL agent to randomized terrains in simulation can achieve robust walking on a real humanoid robot using only proprioceptive feedback. We train an end-to-end bipedal locomotion policy using the proposed approach, and show extensive real-robot demonstration on the HRP-5P humanoid over several difficult terrains inside and outside the lab environment. Further, we argue that the robustness of a bipedal walking policy can be improved if the robot is allowed to exhibit aperiodic motion with variable stepping frequency. We propose a new control policy to enable modification of the observed clock signal, leading to adaptive gait frequencies depending on the terrain and command velocity. Through simulation experiments, we show the effectiveness of this policy specifically for walking over challenging terrains by controlling swing and stance durations. The code for training and evaluation is available online at https://github.com/rohanpsingh/LearningHumanoidWalking. Demo video is available at https://www.youtube.com/watch?v=ZgfNzGAkk2Q.

## 参考
- http://arxiv.org/abs/2504.13619v1

