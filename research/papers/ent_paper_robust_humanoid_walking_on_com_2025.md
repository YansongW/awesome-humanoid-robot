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

## Overview
For the deployment of legged robots in real-world environments, it is essential to develop robust locomotion control methods for challenging terrains that may exhibit unexpected deformability and irregularity. In this paper, we explore the application of sim-to-real deep reinforcement learning (RL) for the design of bipedal locomotion controllers for humanoid robots on compliant and uneven terrains. Our key contribution is to show that a simple training curriculum for exposing the RL agent to randomized terrains in simulation can achieve robust walking on a real humanoid robot using only proprioceptive feedback. We train an end-to-end bipedal locomotion policy using the proposed approach, and show extensive real-robot demonstration on the HRP-5P humanoid over several difficult terrains inside and outside the lab environment. Further, we argue that the robustness of a bipedal walking policy can be improved if the robot is allowed to exhibit aperiodic motion with variable stepping frequency. We propose a new control policy to enable modification of the observed clock signal, leading to adaptive gait frequencies depending on the terrain and command velocity. Through simulation experiments, we show the effectiveness of this policy specifically for walking over challenging terrains by controlling swing and stance durations. The code for training and evaluation is available online at https://github.com/rohanpsingh/LearningHumanoidWalking. Demo video is available at https://www.youtube.com/watch?v=ZgfNzGAkk2Q.

## Content
For the deployment of legged robots in real-world environments, it is essential to develop robust locomotion control methods for challenging terrains that may exhibit unexpected deformability and irregularity. In this paper, we explore the application of sim-to-real deep reinforcement learning (RL) for the design of bipedal locomotion controllers for humanoid robots on compliant and uneven terrains. Our key contribution is to show that a simple training curriculum for exposing the RL agent to randomized terrains in simulation can achieve robust walking on a real humanoid robot using only proprioceptive feedback. We train an end-to-end bipedal locomotion policy using the proposed approach, and show extensive real-robot demonstration on the HRP-5P humanoid over several difficult terrains inside and outside the lab environment. Further, we argue that the robustness of a bipedal walking policy can be improved if the robot is allowed to exhibit aperiodic motion with variable stepping frequency. We propose a new control policy to enable modification of the observed clock signal, leading to adaptive gait frequencies depending on the terrain and command velocity. Through simulation experiments, we show the effectiveness of this policy specifically for walking over challenging terrains by controlling swing and stance durations. The code for training and evaluation is available online at https://github.com/rohanpsingh/LearningHumanoidWalking. Demo video is available at https://www.youtube.com/watch?v=ZgfNzGAkk2Q.

## 개요
실제 환경에서 보행 로봇을 배치하려면 예상치 못한 변형성과 불규칙성을 보일 수 있는 까다로운 지형에 대한 강건한 보행 제어 방법을 개발하는 것이 필수적입니다. 본 논문에서는 시뮬레이션-실제 심층 강화 학습(RL)을 적용하여 유연하고 고르지 않은 지형에서 휴머노이드 로봇의 이족 보행 제어기를 설계하는 방법을 탐구합니다. 주요 기여는 시뮬레이션에서 RL 에이전트를 무작위 지형에 노출시키는 간단한 훈련 커리큘럼이 고유 감각 피드백만을 사용하여 실제 휴머노이드 로봇에서 강건한 보행을 달성할 수 있음을 보여주는 것입니다. 제안된 접근 방식을 사용하여 종단 간 이족 보행 정책을 훈련하고, 실험실 내외의 여러 까다로운 지형에서 HRP-5P 휴머노이드를 통해 광범위한 실제 로봇 시연을 보여줍니다. 또한, 로봇이 가변 보폭 주파수를 가진 비주기적 움직임을 보일 수 있도록 허용하면 이족 보행 정책의 강건성이 향상될 수 있다고 주장합니다. 관찰된 클록 신호를 수정할 수 있는 새로운 제어 정책을 제안하여 지형과 명령 속도에 따라 적응형 보행 주파수를 구현합니다. 시뮬레이션 실험을 통해 스윙 및 스탠스 지속 시간을 제어함으로써 까다로운 지형에서의 보행에 특히 효과적인 이 정책의 효용성을 입증합니다. 훈련 및 평가를 위한 코드는 https://github.com/rohanpsingh/LearningHumanoidWalking 에서 온라인으로 제공됩니다. 데모 비디오는 https://www.youtube.com/watch?v=ZgfNzGAkk2Q 에서 확인할 수 있습니다.

## 핵심 내용
실제 환경에서 보행 로봇을 배치하려면 예상치 못한 변형성과 불규칙성을 보일 수 있는 까다로운 지형에 대한 강건한 보행 제어 방법을 개발하는 것이 필수적입니다. 본 논문에서는 시뮬레이션-실제 심층 강화 학습(RL)을 적용하여 유연하고 고르지 않은 지형에서 휴머노이드 로봇의 이족 보행 제어기를 설계하는 방법을 탐구합니다. 주요 기여는 시뮬레이션에서 RL 에이전트를 무작위 지형에 노출시키는 간단한 훈련 커리큘럼이 고유 감각 피드백만을 사용하여 실제 휴머노이드 로봇에서 강건한 보행을 달성할 수 있음을 보여주는 것입니다. 제안된 접근 방식을 사용하여 종단 간 이족 보행 정책을 훈련하고, 실험실 내외의 여러 까다로운 지형에서 HRP-5P 휴머노이드를 통해 광범위한 실제 로봇 시연을 보여줍니다. 또한, 로봇이 가변 보폭 주파수를 가진 비주기적 움직임을 보일 수 있도록 허용하면 이족 보행 정책의 강건성이 향상될 수 있다고 주장합니다. 관찰된 클록 신호를 수정할 수 있는 새로운 제어 정책을 제안하여 지형과 명령 속도에 따라 적응형 보행 주파수를 구현합니다. 시뮬레이션 실험을 통해 스윙 및 스탠스 지속 시간을 제어함으로써 까다로운 지형에서의 보행에 특히 효과적인 이 정책의 효용성을 입증합니다. 훈련 및 평가를 위한 코드는 https://github.com/rohanpsingh/LearningHumanoidWalking 에서 온라인으로 제공됩니다. 데모 비디오는 https://www.youtube.com/watch?v=ZgfNzGAkk2Q 에서 확인할 수 있습니다.
