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
  zh: 本文提出一种结合三通道可穿戴EEG运动想象脑机接口与新型笛卡尔阻抗控制器的软体机器人操控方案。研究团队通过引导虚拟笛卡尔吸引子，实现了对平面Handed Shearing Auxetic软体机器人的实时控制，并报告了初步的定点调节定量结果与日常生活任务演示。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.13441v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究将脑机接口技术从临床场景拓展至非临床机器人控制领域，通过仅需三个EEG通道的运动想象算法解析用户意图，驱动虚拟吸引子位置变化。配合专为软体机器人设计的笛卡尔阻抗控制器，系统能有效处理平面手剪辅助膨胀软体机器人特有的非线性控制难题。实验表明，在定点调节任务中用户66%的步骤可接近目标点，成功步骤平均响应时间21.5秒，并成功演示了依赖机器人柔顺性的环境交互任务。

## 核心内容
### 方法架构
- 采用三通道可穿戴EEG设备采集运动想象脑电信号，通过鲁棒运动想象算法实时解码用户意图
- 用户通过脑电信号控制虚拟笛卡尔吸引子的二维平面位置，软体机器人末端执行器通过新型笛卡尔阻抗控制器被吸引至该虚拟点
- 控制器专门针对平面手剪辅助膨胀超材料软体机器人的非线性特性（如控制非仿射性）进行设计

### 实验设置
- 任务类型：定点调节（setpoint regulation）定量评估 + 日常生活活动（ADL）环境交互演示
- 评估指标：接近目标点成功率（66%）、成功步骤平均响应时间（21.5s）

### 关键发现
- 用户可在66%的控制步骤中使机器人末端接近预设目标点
- 成功接近目标点的平均响应时间为21.5秒
- 在真实环境交互演示中，软体机器人的柔顺性成为完成复杂任务的关键保障

### 结论
该研究验证了低通道EEG脑机接口与软体机器人结合的安全操控可行性，为脑控机器人从临床向非临床应用过渡提供了新路径。

## Overview
Integrating Brain-Machine Interfaces into non-clinical applications like robot motion control remains difficult - despite remarkable advancements in clinical settings. Specifically, EEG-based motor imagery systems are still error-prone, posing safety risks when rigid robots operate near humans. This work presents an alternative pathway towards safe and effective operation by combining wearable EEG with physically embodied safety in soft robots. We introduce and test a pipeline that allows a user to move a soft robot's end effector in real time via brain waves that are measured by as few as three EEG channels. A robust motor imagery algorithm interprets the user's intentions to move the position of a virtual attractor to which the end effector is attracted, thanks to a new Cartesian impedance controller. We specifically focus here on planar soft robot-based architected metamaterials, which require the development of a novel control architecture to deal with the peculiar nonlinearities - e.g., non-affinity in control. We preliminarily but quantitatively evaluate the approach on the task of setpoint regulation. We observe that the user reaches the proximity of the setpoint in 66% of steps and that for successful steps, the average response time is 21.5s. We also demonstrate the execution of simple real-world tasks involving interaction with the environment, which would be extremely hard to perform if it were not for the robot's softness.

## 개요
뇌-기계 인터페이스를 로봇 동작 제어와 같은 비임상 응용 분야에 통합하는 것은 임상 환경에서의 놀라운 발전에도 불구하고 여전히 어려운 과제로 남아 있습니다. 특히, EEG 기반 운동 상상 시스템은 여전히 오류가 발생하기 쉬우며, 강체 로봇이 인간 근처에서 작동할 때 안전 위험을 초래합니다. 본 연구는 웨어러블 EEG와 소프트 로봇의 물리적 안전성을 결합하여 안전하고 효과적인 작동을 위한 대안적 경로를 제시합니다. 우리는 사용자가 단 3개의 EEG 채널로 측정된 뇌파를 통해 소프트 로봇의 엔드 이펙터를 실시간으로 움직일 수 있는 파이프라인을 소개하고 테스트합니다. 강건한 운동 상상 알고리즘은 사용자의 의도를 해석하여 가상 어트랙터의 위치를 이동시키며, 이 어트랙터로 엔드 이펙터가 끌려가도록 하는 새로운 데카르트 임피던스 컨트롤러를 사용합니다. 특히 본 연구는 평면 소프트 로봇 기반 구조적 메타물질에 초점을 맞추며, 이는 제어의 비선형성(예: 제어의 비친화성)을 처리하기 위한 새로운 제어 아키텍처 개발을 필요로 합니다. 우리는 설정점 조절 작업에서 이 접근법을 예비적이지만 정량적으로 평가합니다. 사용자가 66%의 단계에서 설정점 근처에 도달했으며, 성공적인 단계의 평균 응답 시간은 21.5초임을 관찰했습니다. 또한 로봇의 부드러움이 없다면 수행하기 매우 어려웠을 환경과의 상호작용을 포함한 간단한 실제 작업의 실행을 시연합니다.

## 핵심 내용
뇌-기계 인터페이스를 로봇 동작 제어와 같은 비임상 응용 분야에 통합하는 것은 임상 환경에서의 놀라운 발전에도 불구하고 여전히 어려운 과제로 남아 있습니다. 특히, EEG 기반 운동 상상 시스템은 여전히 오류가 발생하기 쉬우며, 강체 로봇이 인간 근처에서 작동할 때 안전 위험을 초래합니다. 본 연구는 웨어러블 EEG와 소프트 로봇의 물리적 안전성을 결합하여 안전하고 효과적인 작동을 위한 대안적 경로를 제시합니다. 우리는 사용자가 단 3개의 EEG 채널로 측정된 뇌파를 통해 소프트 로봇의 엔드 이펙터를 실시간으로 움직일 수 있는 파이프라인을 소개하고 테스트합니다. 강건한 운동 상상 알고리즘은 사용자의 의도를 해석하여 가상 어트랙터의 위치를 이동시키며, 이 어트랙터로 엔드 이펙터가 끌려가도록 하는 새로운 데카르트 임피던스 컨트롤러를 사용합니다. 특히 본 연구는 평면 소프트 로봇 기반 구조적 메타물질에 초점을 맞추며, 이는 제어의 비선형성(예: 제어의 비친화성)을 처리하기 위한 새로운 제어 아키텍처 개발을 필요로 합니다. 우리는 설정점 조절 작업에서 이 접근법을 예비적이지만 정량적으로 평가합니다. 사용자가 66%의 단계에서 설정점 근처에 도달했으며, 성공적인 단계의 평균 응답 시간은 21.5초임을 관찰했습니다. 또한 로봇의 부드러움이 없다면 수행하기 매우 어려웠을 환경과의 상호작용을 포함한 간단한 실제 작업의 실행을 시연합니다.

## 参考
- http://arxiv.org/abs/2401.13441v2
