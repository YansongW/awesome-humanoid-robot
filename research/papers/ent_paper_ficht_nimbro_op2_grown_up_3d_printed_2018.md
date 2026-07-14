---
$id: ent_paper_ficht_nimbro_op2_grown_up_3d_printed_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  zh: NimbRo-OP2：面向研究的成人尺寸3D打印开源人形机器人平台
  ko: 'NimbRo-OP2: 연구를 위한 성인 크기 3D 프린팅 오픈 소스 휴머노이드 플랫폼'
summary:
  en: NimbRo-OP2 is an affordable, open-source adult-sized humanoid robot approximately 135 cm tall and 18 kg in weight, featuring
    a 3D-printed PA12 exoskeleton and ROS-based software. The paper details its mechanical design, electronics, COTS actuator-based
    actuation with external gearing and parallel kinematics, and validation through victories at RoboCup 2017.
  zh: NimbRo-OP2是一款经济实惠、开源的成人尺寸人形机器人，高约135厘米、重约18千克，采用3D打印PA12外骨骼和基于ROS的软件。论文详细介绍了其机械设计、电子系统、基于商用执行器的外部齿轮传动与并联运动学，以及通过2017年RoboCup获胜进行的验证。
  ko: NimbRo-OP2는 약 135cm 높이와 18kg 무게의 저렴하고 오픈 소스인 성인 크기 휴머노이드 로봇으로, 3D 프린팅 PA12 외골격과 ROS 기반 소프트웨어를 갖추고 있습니다. 본 논문은 기계적 설계,
    전자 시스템, 상용 액추에이터 기반 외부 기어링과 병렬 운동학, 그리고 2017 RoboCup에서의 승리를 통한 검증을 다룹니다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- adult_size_humanoid
- 3d_printed_exoskeleton
- open_source_hardware
- open_source_software
- cots_actuators
- parallel_kinematics
- ros_software
- humanoid_soccer
- lightweight_design
- robocup
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.11144v1.
sources:
- id: src_001
  type: paper
  title: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  url: https://arxiv.org/abs/1809.11144
  date: '2018'
  accessed_at: '2026-06-26'
---
## 概述
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## 核心内容
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## 参考
- http://arxiv.org/abs/1809.11144v1

