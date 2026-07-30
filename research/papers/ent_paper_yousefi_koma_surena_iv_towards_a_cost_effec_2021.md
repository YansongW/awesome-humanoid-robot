---
$id: ent_paper_yousefi_koma_surena_iv_towards_a_cost_effec_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world Scenarios'
  zh: SURENA IV：面向真实场景的成本效益型全尺寸人形机器人
  ko: 'SURENA IV: 실제 환경을 위한 비용 효율적인 풀사이즈 휴머노이드 로봇'
summary:
  en: SURENA IV is a 43-DoF, 170 cm, 68 kg anthropomorphic humanoid developed at the University of Tehran using low-cost manufacturing;
    it uses a predictive foot sensor and online swing-foot adaptation to walk on bounded uneven terrain without force/torque
    sensors, and current-feedback hand control for manipulation tasks.
  zh: SURENA IV 是德黑兰大学研发的一款 43 自由度、身高 170 厘米、体重 68 公斤的全尺寸人形机器人，采用低成本制造工艺。其核心贡献在于通过一种新型预测性足部传感器和在线摆动足适应机制，无需力/力矩传感器即可在未知障碍地形上行走，并利用电流反馈手部控制完成操作任务。
  ko: SURENA IV는 테헤란 대학에서 저비용 제조 방식으로 개발된 43자유도, 170 cm, 68 kg 의 인간형 휴머노이드 로봇으로, 예측형 발 센서와 온라인 스윙 발 적응 제어를 통해 힘/토크 센서 없이 제한된
    불규칙 지면을 보행하고 전류 피드백 손 제어로 조작 작업을 수행한다.
domains:
- 05_mass_production
- 06_design_engineering
- 03_manufacturing_processes
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- surena_iv
- full_size_humanoid
- cost_effective_humanoid
- predictive_foot_sensor
- swing_foot_adaptation
- bipedal_locomotion
- anthropomorphic_hand
- current_feedback_grasping
- encoder_based_sensing
- university_manufacturing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2108.13515v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world Scenarios'
  url: https://arxiv.org/abs/2108.13515
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
SURENA IV 机器人拥有 43 个自由度，每条手臂 7 个、每只手 6 个、每条腿 6 个，其形态与质量分布接近普通成年人。该平台旨在实现面向真实场景的低成本类人机器人。研究团队提出了一种基于低成本预测性足部传感器的运动框架，该传感器能补偿因连杆与连接件挠曲累积导致的 7 厘米足部位置误差，使机器人无需任何力反馈即可在线调整足部高度与姿态，在未知障碍物上稳定行走。此外，机器人的手臂与手部设计可抓取不同刚度和几何形状的物体，支持钻孔、移动目标视觉伺服以及在白板上书写名字等操作。

## 核心内容
### 硬件与自由度配置
- SURENA IV 总自由度 43，具体分布为：每条手臂 7 个、每只手 6 个、每条腿 6 个。
- 身高 170 cm，质量 68 kg，形态与质量分布模拟普通成年人。

### 低成本制造与挑战
- 采用大学实验室可用工具进行低成本制造，导致连杆与连接件存在挠曲累积误差，足部位置误差可达 7 cm。

### 运动控制框架
- 核心创新：一种新型低成本预测性足部传感器，无需力/力矩传感器。
- 在线摆动足适应机制：机器人可实时调整足部高度与姿态，在未知障碍地形上行走。
- 该传感器直接补偿结构挠曲引起的定位误差，实现无力反馈的稳定步态。

### 操作能力
- 手臂与手部设计支持抓取不同刚度与几何形状的物体。
- 演示任务包括：钻孔、对移动物体进行视觉伺服、在白板上书写名字。
- 手部控制基于电流反馈，无需额外力传感器。

## Overview
This paper describes the hardware, software framework, and experimental testing of SURENA IV humanoid robotics platform. SURENA IV has 43 degrees of freedom (DoFs), including seven DoFs for each arm, six DoFs for each hand, and six DoFs for each leg, with a height of 170 cm and a mass of 68 kg and morphological and mass properties similar to an average adult human. SURENA IV aims to realize a cost-effective and anthropomorphic humanoid robot for real-world scenarios. In this way, we demonstrate a locomotion framework based on a novel and inexpensive predictive foot sensor that enables walking with 7cm foot position error because of accumulative error of links and connections' deflection(that has been manufactured by the tools which are available in the Universities). Thanks to this sensor, the robot can walk on unknown obstacles without any force feedback, by online adaptation of foot height and orientation. Moreover, the arm and hand of the robot have been designed to grasp the objects with different stiffness and geometries that enable the robot to do drilling, visual servoing of a moving object, and writing his name on the white-board.

## Overview
This paper describes the hardware, software framework, and experimental testing of the SURENA IV humanoid robotics platform. SURENA IV has 43 degrees of freedom (DoFs), including seven DoFs for each arm, six DoFs for each hand, and six DoFs for each leg, with a height of 170 cm and a mass of 68 kg, and morphological and mass properties similar to an average adult human. SURENA IV aims to realize a cost-effective and anthropomorphic humanoid robot for real-world scenarios. In this way, we demonstrate a locomotion framework based on a novel and inexpensive predictive foot sensor that enables walking with a 7 cm foot position error due to the accumulative error of links and connections' deflection (manufactured using tools available in universities). Thanks to this sensor, the robot can walk on unknown obstacles without any force feedback, by online adaptation of foot height and orientation. Moreover, the arm and hand of the robot have been designed to grasp objects with different stiffness and geometries, enabling the robot to perform drilling, visual servoing of a moving object, and writing its name on a whiteboard.

## Content
This paper describes the hardware, software framework, and experimental testing of the SURENA IV humanoid robotics platform. SURENA IV has 43 degrees of freedom (DoFs), including seven DoFs for each arm, six DoFs for each hand, and six DoFs for each leg, with a height of 170 cm and a mass of 68 kg, and morphological and mass properties similar to an average adult human. SURENA IV aims to realize a cost-effective and anthropomorphic humanoid robot for real-world scenarios. In this way, we demonstrate a locomotion framework based on a novel and inexpensive predictive foot sensor that enables walking with a 7 cm foot position error due to the accumulative error of links and connections' deflection (manufactured using tools available in universities). Thanks to this sensor, the robot can walk on unknown obstacles without any force feedback, by online adaptation of foot height and orientation. Moreover, the arm and hand of the robot have been designed to grasp objects with different stiffness and geometries, enabling the robot to perform drilling, visual servoing of a moving object, and writing its name on a whiteboard.

## 개요
본 논문은 SURENA IV 휴머노이드 로봇 플랫폼의 하드웨어, 소프트웨어 프레임워크 및 실험적 테스트에 대해 설명합니다. SURENA IV는 43개의 자유도(DoF)를 가지며, 각 팔에 7개의 DoF, 각 손에 6개의 DoF, 각 다리에 6개의 DoF로 구성되어 있습니다. 키는 170cm, 질량은 68kg이며, 형태 및 질량 특성이 평균 성인 인간과 유사합니다. SURENA IV는 실제 환경에서 비용 효율적이고 인간형에 가까운 휴머노이드 로봇을 구현하는 것을 목표로 합니다. 이를 위해, 대학에서 사용 가능한 도구로 제작된 링크 및 연결부의 처짐으로 인한 누적 오차로 인해 7cm의 발 위치 오차가 발생하는 상황에서도 보행이 가능하도록 하는, 새롭고 저렴한 예측형 발 센서 기반의 보행 프레임워크를 시연합니다. 이 센서 덕분에 로봇은 힘 피드백 없이도 발 높이와 방향을 온라인으로 조정하여 알려지지 않은 장애물 위를 걸을 수 있습니다. 또한, 로봇의 팔과 손은 다양한 강성과 형상을 가진 물체를 잡을 수 있도록 설계되어, 드릴 작업, 움직이는 물체의 비주얼 서보잉, 화이트보드에 자신의 이름 쓰기 등을 수행할 수 있습니다.

## 핵심 내용
본 논문은 SURENA IV 휴머노이드 로봇 플랫폼의 하드웨어, 소프트웨어 프레임워크 및 실험적 테스트에 대해 설명합니다. SURENA IV는 43개의 자유도(DoF)를 가지며, 각 팔에 7개의 DoF, 각 손에 6개의 DoF, 각 다리에 6개의 DoF로 구성되어 있습니다. 키는 170cm, 질량은 68kg이며, 형태 및 질량 특성이 평균 성인 인간과 유사합니다. SURENA IV는 실제 환경에서 비용 효율적이고 인간형에 가까운 휴머노이드 로봇을 구현하는 것을 목표로 합니다. 이를 위해, 대학에서 사용 가능한 도구로 제작된 링크 및 연결부의 처짐으로 인한 누적 오차로 인해 7cm의 발 위치 오차가 발생하는 상황에서도 보행이 가능하도록 하는, 새롭고 저렴한 예측형 발 센서 기반의 보행 프레임워크를 시연합니다. 이 센서 덕분에 로봇은 힘 피드백 없이도 발 높이와 방향을 온라인으로 조정하여 알려지지 않은 장애물 위를 걸을 수 있습니다. 또한, 로봇의 팔과 손은 다양한 강성과 형상을 가진 물체를 잡을 수 있도록 설계되어, 드릴 작업, 움직이는 물체의 비주얼 서보잉, 화이트보드에 자신의 이름 쓰기 등을 수행할 수 있습니다.

## 参考
- http://arxiv.org/abs/2108.13515v1
