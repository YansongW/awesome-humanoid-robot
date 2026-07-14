---
$id: ent_paper_stolzle_guiding_soft_robots_with_motor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Guiding Soft Robots with Motor-Imagery Brain Signals and Impedance Control
  zh: 基于运动想象脑信号与阻抗控制的软体机器人导引
  ko: 운동 상상 뇌신호 및 임피던스 제어를 이용한 소프트 로봇 유도
summary:
  en: This paper presents a pipeline that uses a 3-channel wearable EEG motor-imagery brain-machine interface to steer a virtual
    Cartesian attractor for a planar Handed Shearing Auxetic soft robot, tracked by a novel Cartesian impedance controller;
    it reports preliminary quantitative setpoint-regulation results and a real-world activities-of-daily-living demonstration.
  zh: 本文提出了一种利用三通道可穿戴脑电图运动想象脑机接口，为平面手性剪切拉胀软体机器人驱动虚拟笛卡尔吸引子，并通过新型笛卡尔阻抗控制器进行跟踪的流程；报告了初步的定量设定点调节结果和一项日常生活活动演示。
  ko: 본 논문은 3채널 웨어러블 EEG 운동 상상 뇌-기계 인터페이스를 사용하여 평면 Handed Shearing Auxetic 소프트 로봇의 가상 데카르트 어트랙터를 조향하고, 새로운 데카르트 임피던스 제어기로
    추적하는 파이프라인을 제안하며, 예비적인 정량적 설정점 조절 결과와 실제 일상생활 활동 시연을 보고한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- brain_machine_interface
- motor_imagery
- eeg
- wearable_eeg
- soft_robotics
- handed_shearing_auxetic
- continuum_robot
- cartesian_impedance_control
- underactuated_control
- human_robot_interaction
- assistive_robotics
- setpoint_regulation
- activities_of_daily_living
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.13441v2.
sources:
- id: src_001
  type: paper
  title: Guiding Soft Robots with Motor-Imagery Brain Signals and Impedance Control
  url: https://arxiv.org/abs/2401.13441
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Integrating Brain-Machine Interfaces into non-clinical applications like robot motion control remains difficult - despite remarkable advancements in clinical settings. Specifically, EEG-based motor imagery systems are still error-prone, posing safety risks when rigid robots operate near humans. This work presents an alternative pathway towards safe and effective operation by combining wearable EEG with physically embodied safety in soft robots. We introduce and test a pipeline that allows a user to move a soft robot's end effector in real time via brain waves that are measured by as few as three EEG channels. A robust motor imagery algorithm interprets the user's intentions to move the position of a virtual attractor to which the end effector is attracted, thanks to a new Cartesian impedance controller. We specifically focus here on planar soft robot-based architected metamaterials, which require the development of a novel control architecture to deal with the peculiar nonlinearities - e.g., non-affinity in control. We preliminarily but quantitatively evaluate the approach on the task of setpoint regulation. We observe that the user reaches the proximity of the setpoint in 66% of steps and that for successful steps, the average response time is 21.5s. We also demonstrate the execution of simple real-world tasks involving interaction with the environment, which would be extremely hard to perform if it were not for the robot's softness.

## 核心内容
Integrating Brain-Machine Interfaces into non-clinical applications like robot motion control remains difficult - despite remarkable advancements in clinical settings. Specifically, EEG-based motor imagery systems are still error-prone, posing safety risks when rigid robots operate near humans. This work presents an alternative pathway towards safe and effective operation by combining wearable EEG with physically embodied safety in soft robots. We introduce and test a pipeline that allows a user to move a soft robot's end effector in real time via brain waves that are measured by as few as three EEG channels. A robust motor imagery algorithm interprets the user's intentions to move the position of a virtual attractor to which the end effector is attracted, thanks to a new Cartesian impedance controller. We specifically focus here on planar soft robot-based architected metamaterials, which require the development of a novel control architecture to deal with the peculiar nonlinearities - e.g., non-affinity in control. We preliminarily but quantitatively evaluate the approach on the task of setpoint regulation. We observe that the user reaches the proximity of the setpoint in 66% of steps and that for successful steps, the average response time is 21.5s. We also demonstrate the execution of simple real-world tasks involving interaction with the environment, which would be extremely hard to perform if it were not for the robot's softness.

## 参考
- http://arxiv.org/abs/2401.13441v2

