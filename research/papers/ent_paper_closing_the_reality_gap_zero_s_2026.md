---
$id: ent_paper_closing_the_reality_gap_zero_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
  zh: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
  ko: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
summary:
  en: 'arXiv:2607.04940v1 Announce Type: new Abstract: Human-like dexterous hands with multiple fingers offer human-level
    manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich
    physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback
    combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer,
    we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units
    and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii)
    a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current
    to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects
    and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation
    and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1)
    command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly
    executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing
    and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge,
    this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation
    and transferred zero-shot on real hardware.'
  zh: 'arXiv:2607.04940v1 Announce Type: new Abstract: Human-like dexterous hands with multiple fingers offer human-level
    manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich
    physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback
    combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer,
    we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units
    and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii)
    a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current
    to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects
    and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation
    and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1)
    command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly
    executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing
    and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge,
    this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation
    and transferred zero-shot on real hardware.'
  ko: 'arXiv:2607.04940v1 Announce Type: new Abstract: Human-like dexterous hands with multiple fingers offer human-level
    manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich
    physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback
    combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer,
    we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units
    and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii)
    a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current
    to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects
    and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation
    and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1)
    command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly
    executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing
    and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge,
    this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation
    and transferred zero-shot on real hardware.'
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
- closing_the_reality_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04940v1.
sources:
- id: src_001
  type: paper
  title: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04940
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## 核心内容
Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## 参考
- http://arxiv.org/abs/2607.04940v1

## Overview
Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## Content
Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## 개요
인간과 유사한 다지(dexterous) 손은 인간 수준의 조작 능력을 제공하지만, 접촉이 많은 물리적 상호작용과 불완전한 구동(actuation)으로 인해 실제 하드웨어에 배포 가능한 제어 정책을 훈련시키는 것은 여전히 어렵습니다. 우리는 밀집 촉각 피드백과 관절 토크 감지를 결합하여 물리적 상호작용을 명시적으로 조절하는 시뮬레이션-실제(sim-to-real) 강화 학습 방법을 제시합니다. 효과적인 시뮬레이션-실제 전이를 위해 다음을 도입합니다: (i) 병렬 순기구학(parallel forward kinematics)을 통해 밀집 가상 촉각 유닛과 객체 간 거리를 계산하여 강화 학습에 필요한 고속, 고해상도 촉각 신호를 제공하는 계산적으로 빠른 촉각 시뮬레이션; (ii) 모터 전류를 관절 토크로 매핑하여 다지 손의 토크 센서 필요성을 없애는 전류-토크 보정; (iii) 비이상적 토크-속도 효과를 고려하고 구동 격차를 해소하기 위한 무작위화가 포함된 액추에이터 동역학 모델링. 비대칭 액터-크리틱 PPO(asymmetric actor-critic PPO) 파이프라인을 사용하여 정책을 전적으로 시뮬레이션에서 훈련하고 이를 다섯 손가락 손에 직접 배포합니다. 결과 정책은 두 가지 필수 인간 손 기술을 보여줍니다: (1) 명령 기반 제어 가능한 파지력 추적 및 (2) 손 안에서 객체의 방향 재조정, 이 두 가지 모두 로봇에서 미세 조정 없이 강건하게 실행됩니다. 관찰 공간에서 촉각과 토크를 확장 가능한 감지 및 구동 모델링과 결합함으로써, 우리 시스템은 신뢰할 수 있는 정밀 조작을 달성하기 위한 실용적인 솔루션을 제공합니다. 우리가 아는 한, 이는 전적으로 시뮬레이션에서 훈련되고 실제 하드웨어에서 제로샷(zero-shot)으로 전이된 다지 손에서 제어 가능한 파지를 최초로 시연한 것입니다.

## 핵심 내용
인간과 유사한 다지 손은 인간 수준의 조작 능력을 제공하지만, 접촉이 많은 물리적 상호작용과 불완전한 구동으로 인해 실제 하드웨어에 배포 가능한 제어 정책을 훈련시키는 것은 여전히 어렵습니다. 우리는 밀집 촉각 피드백과 관절 토크 감지를 결합하여 물리적 상호작용을 명시적으로 조절하는 시뮬레이션-실제 강화 학습 방법을 제시합니다. 효과적인 시뮬레이션-실제 전이를 위해 다음을 도입합니다: (i) 병렬 순기구학을 통해 밀집 가상 촉각 유닛과 객체 간 거리를 계산하여 강화 학습에 필요한 고속, 고해상도 촉각 신호를 제공하는 계산적으로 빠른 촉각 시뮬레이션; (ii) 모터 전류를 관절 토크로 매핑하여 다지 손의 토크 센서 필요성을 없애는 전류-토크 보정; (iii) 비이상적 토크-속도 효과를 고려하고 구동 격차를 해소하기 위한 무작위화가 포함된 액추에이터 동역학 모델링. 비대칭 액터-크리틱 PPO 파이프라인을 사용하여 정책을 전적으로 시뮬레이션에서 훈련하고 이를 다섯 손가락 손에 직접 배포합니다. 결과 정책은 두 가지 필수 인간 손 기술을 보여줍니다: (1) 명령 기반 제어 가능한 파지력 추적 및 (2) 손 안에서 객체의 방향 재조정, 이 두 가지 모두 로봇에서 미세 조정 없이 강건하게 실행됩니다. 관찰 공간에서 촉각과 토크를 확장 가능한 감지 및 구동 모델링과 결합함으로써, 우리 시스템은 신뢰할 수 있는 정밀 조작을 달성하기 위한 실용적인 솔루션을 제공합니다. 우리가 아는 한, 이는 전적으로 시뮬레이션에서 훈련되고 실제 하드웨어에서 제로샷으로 전이된 다지 손에서 제어 가능한 파지를 최초로 시연한 것입니다.
