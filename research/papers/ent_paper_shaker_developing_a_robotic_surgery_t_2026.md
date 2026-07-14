---
$id: ent_paper_shaker_developing_a_robotic_surgery_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing a Robotic Surgery Training System for Wide Accessibility and Research
  zh: 面向广泛可及性与研究的机器人手术训练系统开发
  ko: 넓은 접근성과 연구를 위한 로봇 수술 훈련 시스템 개발
summary:
  en: This paper presents RoboScope, a low-cost master-slave robotic laparoscopy training system that uses a redesigned end-effector,
    a RoboDK-based digital twin, and optimized velocity-control teleoperation with Remote Center of Motion constraints to
    broaden access to surgical training and research.
  zh: 本文提出了RoboScope，一种低成本的主从式机器人腹腔镜训练系统，该系统采用重新设计的末端执行器、基于RoboDK的数字孪生平台以及具有远程运动中心约束的优化速度控制遥操作，以扩大外科手术训练和研究的普及性。
  ko: 본 논문은 재설계된 엔드이펙터, RoboDK 기반 디지털 트윈, 그리고 원격 운동 중심(RCM) 제약이 있는 최적화된 속도 제어 원격 조작을 사용하여 외과 수술 훈련 및 연구의 접근성을 확대하는 저렴한 마스터-슬레이브
    로봇 복강경 훈련 시스템인 RoboScope를 제안한다.
domains:
- 06_design_engineering
- 02_components
- 03_manufacturing_processes
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- tool_equipment
tags:
- teleoperation
- digital_twin
- master_slave_system
- remote_center_of_motion
- low_cost_design
- haptic_interface
- surgical_robotics
- collaborative_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.20562v2.
sources:
- id: src_001
  type: paper
  title: Developing a Robotic Surgery Training System for Wide Accessibility and Research
  url: https://arxiv.org/abs/2505.20562
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Robotic surgery represents a major breakthrough in medical interventions, which has revolutionized surgical procedures. However, the high cost and limited accessibility of robotic surgery systems pose significant challenges for training purposes. This study addresses these issues by developing a cost-effective robotic laparoscopy training system that closely replicates advanced robotic surgery setups to ensure broad access for both on-site and remote users. Key innovations include the design of a low-cost robotic end-effector that effectively mimics high-end laparoscopic instruments. Additionally, a digital twin platform was established, facilitating detailed simulation, testing, and real-time monitoring, which enhances both system development and deployment. Furthermore, teleoperation control was optimized, leading to improved trajectory tracking while maintaining remote center of motion (RCM) constraint, with a RMSE of 5 μm and reduced system latency to 0.01 seconds. As a result, the system provides smooth, continuous motion and incorporates essential safety features, making it a highly effective tool for laparoscopic training.

## 核心内容
Robotic surgery represents a major breakthrough in medical interventions, which has revolutionized surgical procedures. However, the high cost and limited accessibility of robotic surgery systems pose significant challenges for training purposes. This study addresses these issues by developing a cost-effective robotic laparoscopy training system that closely replicates advanced robotic surgery setups to ensure broad access for both on-site and remote users. Key innovations include the design of a low-cost robotic end-effector that effectively mimics high-end laparoscopic instruments. Additionally, a digital twin platform was established, facilitating detailed simulation, testing, and real-time monitoring, which enhances both system development and deployment. Furthermore, teleoperation control was optimized, leading to improved trajectory tracking while maintaining remote center of motion (RCM) constraint, with a RMSE of 5 μm and reduced system latency to 0.01 seconds. As a result, the system provides smooth, continuous motion and incorporates essential safety features, making it a highly effective tool for laparoscopic training.

## 参考
- http://arxiv.org/abs/2505.20562v2

