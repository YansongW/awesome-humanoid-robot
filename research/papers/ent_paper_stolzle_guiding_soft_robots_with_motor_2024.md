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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.13441v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (627 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2401.13441v2

## 개요
이 연구는 뇌-컴퓨터 인터페이스 기술을 임상 환경에서 비임상 로봇 제어 분야로 확장하여, 단 세 개의 EEG 채널만을 필요로 하는 운동 상상 알고리즘을 통해 사용자 의도를 해석하고 가상 어트랙터 위치 변화를 구동합니다. 소프트 로봇을 위해 특별히 설계된 데카르트 임피던스 컨트롤러와 결합하여, 시스템은 평면 손가위 보조 팽창 소프트 로봇의 고유한 비선형 제어 문제를 효과적으로 처리할 수 있습니다. 실험 결과, 정밀 조절 작업에서 사용자 단계의 66%가 목표 지점에 근접할 수 있었고, 성공 단계의 평균 응답 시간은 21.5초였으며, 로봇의 유연성에 의존하는 환경 상호작용 작업을 성공적으로 시연했습니다.

## 핵심 내용
### 방법 아키텍처
- 3채널 웨어러블 EEG 장치를 사용하여 운동 상상 뇌파 신호를 수집하고, 강건한 운동 상상 알고리즘을 통해 사용자 의도를 실시간으로 디코딩
- 사용자는 뇌파 신호를 통해 가상 데카르트 어트랙터의 2차원 평면 위치를 제어하며, 소프트 로봇 엔드 이펙터는 새로운 데카르트 임피던스 컨트롤러를 통해 이 가상 지점으로 끌려감
- 컨트롤러는 평면 손가위 보조 팽창 메타물질 소프트 로봇의 비선형 특성(예: 제어 비아핀성)을 위해 특별히 설계됨

### 실험 설정
- 작업 유형: 정밀 조절(setpoint regulation) 정량 평가 + 일상생활 활동(ADL) 환경 상호작용 시연
- 평가 지표: 목표 지점 근접 성공률(66%), 성공 단계 평균 응답 시간(21.5초)

### 주요 발견
- 사용자는 제어 단계의 66%에서 로봇 엔드 이펙터를 사전 설정된 목표 지점에 근접시킬 수 있음
- 목표 지점에 성공적으로 근접한 평균 응답 시간은 21.5초
- 실제 환경 상호작용 시연에서 소프트 로봇의 유연성이 복잡한 작업 완료의 핵심 보장 요소가 됨

### 결론
이 연구는 저채널 EEG 뇌-컴퓨터 인터페이스와 소프트 로봇의 결합을 통한 안전한 제어 가능성을 검증했으며, 뇌 제어 로봇이 임상에서 비임상 응용으로 전환되는 새로운 경로를 제공합니다.
