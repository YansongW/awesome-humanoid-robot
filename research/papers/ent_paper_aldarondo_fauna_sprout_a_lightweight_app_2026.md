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

## Overview
Recent advances in learned control, large-scale simulation, and generative models have accelerated progress toward general-purpose robotic controllers, yet the field still lacks platforms suitable for safe, expressive, long-term deployment in human environments. Most existing humanoids are either closed industrial systems or academic prototypes that are difficult to deploy and operate around people, limiting progress in robotics. We introduce Sprout, a developer platform designed to address these limitations through an emphasis on safety, expressivity, and developer accessibility. Sprout adopts a lightweight form factor with compliant control, limited joint torques, and soft exteriors to support safe operation in shared human spaces. The platform integrates whole-body control, manipulation with integrated grippers, and virtual-reality-based teleoperation within a unified hardware-software stack. An expressive head further enables social interaction -- a domain that remains underexplored on most utilitarian humanoids. By lowering physical and technical barriers to deployment, Sprout expands access to capable humanoid platforms and provides a practical basis for developing embodied intelligence in real human environments.

## Content
Recent advances in learned control, large-scale simulation, and generative models have accelerated progress toward general-purpose robotic controllers, yet the field still lacks platforms suitable for safe, expressive, long-term deployment in human environments. Most existing humanoids are either closed industrial systems or academic prototypes that are difficult to deploy and operate around people, limiting progress in robotics. We introduce Sprout, a developer platform designed to address these limitations through an emphasis on safety, expressivity, and developer accessibility. Sprout adopts a lightweight form factor with compliant control, limited joint torques, and soft exteriors to support safe operation in shared human spaces. The platform integrates whole-body control, manipulation with integrated grippers, and virtual-reality-based teleoperation within a unified hardware-software stack. An expressive head further enables social interaction -- a domain that remains underexplored on most utilitarian humanoids. By lowering physical and technical barriers to deployment, Sprout expands access to capable humanoid platforms and provides a practical basis for developing embodied intelligence in real human environments.

## 개요
학습 제어, 대규모 시뮬레이션 및 생성 모델의 최근 발전은 범용 로봇 제어기를 향한 진전을 가속화했지만, 인간 환경에서 안전하고 표현력이 풍부하며 장기간 배포하기에 적합한 플랫폼은 여전히 부족합니다. 대부분의 기존 휴머노이드는 폐쇄형 산업 시스템이거나 사람 주변에서 배포 및 운영이 어려운 학술 프로토타입에 불과하여 로봇 공학의 발전을 제한합니다. 우리는 안전성, 표현력 및 개발자 접근성을 강조하여 이러한 한계를 해결하도록 설계된 개발자 플랫폼인 Sprout을 소개합니다. Sprout은 경량 폼팩터를 채택하여 순응 제어, 제한된 관절 토크 및 부드러운 외관을 통해 공유 인간 공간에서 안전한 작동을 지원합니다. 이 플랫폼은 전신 제어, 통합 그리퍼를 이용한 조작, 가상 현실 기반 원격 조작을 통합 하드웨어-소프트웨어 스택 내에 통합합니다. 표현력이 풍부한 헤드는 대부분의 실용적인 휴머노이드에서 아직 충분히 탐구되지 않은 영역인 사회적 상호작용을 가능하게 합니다. 배포에 대한 물리적 및 기술적 장벽을 낮춤으로써 Sprout은 유능한 휴머노이드 플랫폼에 대한 접근성을 확대하고 실제 인간 환경에서 체화된 지능을 개발하기 위한 실용적인 기반을 제공합니다.

## 핵심 내용
학습 제어, 대규모 시뮬레이션 및 생성 모델의 최근 발전은 범용 로봇 제어기를 향한 진전을 가속화했지만, 인간 환경에서 안전하고 표현력이 풍부하며 장기간 배포하기에 적합한 플랫폼은 여전히 부족합니다. 대부분의 기존 휴머노이드는 폐쇄형 산업 시스템이거나 사람 주변에서 배포 및 운영이 어려운 학술 프로토타입에 불과하여 로봇 공학의 발전을 제한합니다. 우리는 안전성, 표현력 및 개발자 접근성을 강조하여 이러한 한계를 해결하도록 설계된 개발자 플랫폼인 Sprout을 소개합니다. Sprout은 경량 폼팩터를 채택하여 순응 제어, 제한된 관절 토크 및 부드러운 외관을 통해 공유 인간 공간에서 안전한 작동을 지원합니다. 이 플랫폼은 전신 제어, 통합 그리퍼를 이용한 조작, 가상 현실 기반 원격 조작을 통합 하드웨어-소프트웨어 스택 내에 통합합니다. 표현력이 풍부한 헤드는 대부분의 실용적인 휴머노이드에서 아직 충분히 탐구되지 않은 영역인 사회적 상호작용을 가능하게 합니다. 배포에 대한 물리적 및 기술적 장벽을 낮춤으로써 Sprout은 유능한 휴머노이드 플랫폼에 대한 접근성을 확대하고 실제 인간 환경에서 체화된 지능을 개발하기 위한 실용적인 기반을 제공합니다.
