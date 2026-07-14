---
$id: ent_paper_aldarondo_fauna_sprout_a_lightweight_app_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot'
  zh: Fauna Sprout：一种轻量、易用、面向开发者的人形机器人
  ko: 'Fauna Sprout: 가벼운 접근성 높은 개발자용 휴머노이드 로봇'
summary:
  en: This paper introduces Sprout, a 1.07 m, 22.7 kg developer-ready humanoid robot platform from Fauna Robotics, designed
    for safe, expressive, long-term deployment in human environments through compliant hardware, a modular ROS 2 stack, VR
    teleoperation, dense SLAM, and expressive human-robot interaction.
  zh: 本文介绍了Fauna Robotics公司的Sprout人形机器人平台，身高1.07米、体重22.7千克，面向开发者设计，通过柔顺硬件、模块化ROS 2软件栈、VR遥操作、稠密SLAM以及富有表现力的人机交互，实现安全、富有表现力且可长期部署于人类环境的目标。
  ko: 본 논문은 Fauna Robotics의 개발자용 휴머노이드 로봇 플랫폼인 Sprout을 소개한다. 키 1.07m, 무게 22.7kg로, 순응형 하드웨어, 모듈형 ROS 2 소프트웨어 스택, VR 텔레오퍼레이션,
    밀집 SLAM, 표현력 높은 인간-로봇 상호작용을 통해 인간 환경에서 안전하고 표현력 있으며 장기적인 배치를 목표로 한다.
domains:
- 06_design_engineering
- 05_mass_production
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- system
- knowledge
- intelligence
tags:
- humanoid_robot
- sprout
- fauna_robotics
- developer_platform
- whole_body_control
- vr_teleoperation
- dense_slam
- human_robot_interaction
- compliant_actuation
- ros_2
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.18963v1.
sources:
- id: src_001
  type: paper
  title: 'Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot'
  url: https://arxiv.org/abs/2601.18963
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---
## 概述
Recent advances in learned control, large-scale simulation, and generative models have accelerated progress toward general-purpose robotic controllers, yet the field still lacks platforms suitable for safe, expressive, long-term deployment in human environments. Most existing humanoids are either closed industrial systems or academic prototypes that are difficult to deploy and operate around people, limiting progress in robotics. We introduce Sprout, a developer platform designed to address these limitations through an emphasis on safety, expressivity, and developer accessibility. Sprout adopts a lightweight form factor with compliant control, limited joint torques, and soft exteriors to support safe operation in shared human spaces. The platform integrates whole-body control, manipulation with integrated grippers, and virtual-reality-based teleoperation within a unified hardware-software stack. An expressive head further enables social interaction -- a domain that remains underexplored on most utilitarian humanoids. By lowering physical and technical barriers to deployment, Sprout expands access to capable humanoid platforms and provides a practical basis for developing embodied intelligence in real human environments.

## 核心内容
Recent advances in learned control, large-scale simulation, and generative models have accelerated progress toward general-purpose robotic controllers, yet the field still lacks platforms suitable for safe, expressive, long-term deployment in human environments. Most existing humanoids are either closed industrial systems or academic prototypes that are difficult to deploy and operate around people, limiting progress in robotics. We introduce Sprout, a developer platform designed to address these limitations through an emphasis on safety, expressivity, and developer accessibility. Sprout adopts a lightweight form factor with compliant control, limited joint torques, and soft exteriors to support safe operation in shared human spaces. The platform integrates whole-body control, manipulation with integrated grippers, and virtual-reality-based teleoperation within a unified hardware-software stack. An expressive head further enables social interaction -- a domain that remains underexplored on most utilitarian humanoids. By lowering physical and technical barriers to deployment, Sprout expands access to capable humanoid platforms and provides a practical basis for developing embodied intelligence in real human environments.

## 参考
- http://arxiv.org/abs/2601.18963v1

