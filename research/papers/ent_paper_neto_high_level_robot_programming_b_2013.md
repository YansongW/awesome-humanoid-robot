---
$id: ent_paper_neto_high_level_robot_programming_b_2013
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'High-level robot programming based on CAD: dealing with unpredictable environments'
  zh: 基于CAD的高级机器人编程：应对不可预测环境
  ko: 'CAD 기반 고수준 로봇 프로그래밍: 예측 불가능한 환경 대응'
summary:
  en: This paper presents a CAD-based human-robot interface that lets non-expert users program industrial robots by drawing
    paths in Autodesk Inventor, and compensates for environmental uncertainty using online feedback from a laser camera and
    a force/torque sensor.
  zh: 本文提出一种基于CAD的人机交互界面，允许非专业用户在Autodesk Inventor中绘制路径来编程工业机器人，并通过激光相机和力/力矩传感器的在线反馈补偿环境不确定性。
  ko: 본 논문은 Autodesk Inventor에서 경로를 그려 비전문 사용자가 산업용 로봇을 프로그래밍할 수 있는 CAD 기반 인간-로봇 인터페이스를 제안하며, 레이저 카메라와 힘/토크 센서의 온라인 피드백을 통해
    환경 불확실성을 보상한다.
domains:
- 08_software_middleware
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cad_based_programming
- robot_programming
- teach_by_demonstration
- sensory_feedback
- online_path_correction
- seam_tracking
- force_controlled_profile_following
- industrial_robot
- autodesk_inventor
- laser_camera
- force_torque_sensor
- human_robot_interface
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1309.2086v1.
sources:
- id: src_001
  type: paper
  title: 'High-level robot programming based on CAD: dealing with unpredictable environments'
  url: https://arxiv.org/abs/1309.2086
  date: '2013'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Purpose - The purpose of this paper is to present a CAD-based human-robot interface that allows non-expert users to teach a robot in a manner similar to that used by human beings to teach each other.   Design/methodology/approach - Intuitive robot programming is achieved by using CAD drawings to generate robot programs off-line. Sensory feedback allows minimization of the effects of uncertainty, providing information to adjust the robot paths during robot operation.   Findings - It was found that it is possible to generate a robot program from a common CAD drawing and run it without any major concerns about calibration or CAD model accuracy.   Research limitations/implications - A limitation of the proposed system has to do with the fact that it was designed to be used for particular technological applications.   Practical implications - Since most manufacturing companies have CAD packages in their facilities today, CAD-based robot programming may be a good option to program robots without the need for skilled robot programmers.   Originality/value - The paper proposes a new CAD-based robot programming system. Robot programs are directly generated from a CAD drawing running on a commonly available 3D CAD package (Autodesk Inventor) and not from a commercial, computer aided robotics (CAR) software, making it a simple CAD integrated solution. This is a low-cost and low-setup time system where no advanced robot programming skills are required to operate it. In summary, robot programs are generated with a high-level of abstraction from the robot language.

## 核心内容
Purpose - The purpose of this paper is to present a CAD-based human-robot interface that allows non-expert users to teach a robot in a manner similar to that used by human beings to teach each other.   Design/methodology/approach - Intuitive robot programming is achieved by using CAD drawings to generate robot programs off-line. Sensory feedback allows minimization of the effects of uncertainty, providing information to adjust the robot paths during robot operation.   Findings - It was found that it is possible to generate a robot program from a common CAD drawing and run it without any major concerns about calibration or CAD model accuracy.   Research limitations/implications - A limitation of the proposed system has to do with the fact that it was designed to be used for particular technological applications.   Practical implications - Since most manufacturing companies have CAD packages in their facilities today, CAD-based robot programming may be a good option to program robots without the need for skilled robot programmers.   Originality/value - The paper proposes a new CAD-based robot programming system. Robot programs are directly generated from a CAD drawing running on a commonly available 3D CAD package (Autodesk Inventor) and not from a commercial, computer aided robotics (CAR) software, making it a simple CAD integrated solution. This is a low-cost and low-setup time system where no advanced robot programming skills are required to operate it. In summary, robot programs are generated with a high-level of abstraction from the robot language.

## 参考
- http://arxiv.org/abs/1309.2086v1

## Overview
Purpose - The purpose of this paper is to present a CAD-based human-robot interface that allows non-expert users to teach a robot in a manner similar to that used by human beings to teach each other. Design/methodology/approach - Intuitive robot programming is achieved by using CAD drawings to generate robot programs off-line. Sensory feedback allows minimization of the effects of uncertainty, providing information to adjust the robot paths during robot operation. Findings - It was found that it is possible to generate a robot program from a common CAD drawing and run it without any major concerns about calibration or CAD model accuracy. Research limitations/implications - A limitation of the proposed system has to do with the fact that it was designed to be used for particular technological applications. Practical implications - Since most manufacturing companies have CAD packages in their facilities today, CAD-based robot programming may be a good option to program robots without the need for skilled robot programmers. Originality/value - The paper proposes a new CAD-based robot programming system. Robot programs are directly generated from a CAD drawing running on a commonly available 3D CAD package (Autodesk Inventor) and not from a commercial, computer aided robotics (CAR) software, making it a simple CAD integrated solution. This is a low-cost and low-setup time system where no advanced robot programming skills are required to operate it. In summary, robot programs are generated with a high-level of abstraction from the robot language.

## Content
Purpose - The purpose of this paper is to present a CAD-based human-robot interface that allows non-expert users to teach a robot in a manner similar to that used by human beings to teach each other. Design/methodology/approach - Intuitive robot programming is achieved by using CAD drawings to generate robot programs off-line. Sensory feedback allows minimization of the effects of uncertainty, providing information to adjust the robot paths during robot operation. Findings - It was found that it is possible to generate a robot program from a common CAD drawing and run it without any major concerns about calibration or CAD model accuracy. Research limitations/implications - A limitation of the proposed system has to do with the fact that it was designed to be used for particular technological applications. Practical implications - Since most manufacturing companies have CAD packages in their facilities today, CAD-based robot programming may be a good option to program robots without the need for skilled robot programmers. Originality/value - The paper proposes a new CAD-based robot programming system. Robot programs are directly generated from a CAD drawing running on a commonly available 3D CAD package (Autodesk Inventor) and not from a commercial, computer aided robotics (CAR) software, making it a simple CAD integrated solution. This is a low-cost and low-setup time system where no advanced robot programming skills are required to operate it. In summary, robot programs are generated with a high-level of abstraction from the robot language.

## 개요
목적 - 본 논문의 목적은 비전문가 사용자가 인간이 서로 가르치는 방식과 유사한 방식으로 로봇을 교육할 수 있도록 하는 CAD 기반 인간-로봇 인터페이스를 제시하는 것입니다.  
설계/방법론/접근법 - CAD 도면을 사용하여 오프라인으로 로봇 프로그램을 생성함으로써 직관적인 로봇 프로그래밍이 가능합니다. 감각 피드백은 불확실성의 영향을 최소화하여 로봇 작동 중 로봇 경로를 조정하는 정보를 제공합니다.  
결과 - 일반적인 CAD 도면에서 로봇 프로그램을 생성하고, 캘리브레이션이나 CAD 모델 정확도에 대한 주요 우려 없이 실행할 수 있음을 발견했습니다.  
연구 한계/의의 - 제안된 시스템의 한계는 특정 기술 응용 분야에 사용되도록 설계되었다는 사실과 관련이 있습니다.  
실용적 의의 - 오늘날 대부분의 제조 회사가 시설에 CAD 패키지를 보유하고 있기 때문에, CAD 기반 로봇 프로그래밍은 숙련된 로봇 프로그래머 없이도 로봇을 프로그래밍할 수 있는 좋은 옵션이 될 수 있습니다.  
독창성/가치 - 본 논문은 새로운 CAD 기반 로봇 프로그래밍 시스템을 제안합니다. 로봇 프로그램은 상용 컴퓨터 지원 로봇공학(CAR) 소프트웨어가 아닌, 일반적으로 사용 가능한 3D CAD 패키지(Autodesk Inventor)에서 실행되는 CAD 도면에서 직접 생성되어 간단한 CAD 통합 솔루션을 제공합니다. 이는 저비용 및 짧은 설정 시간을 가진 시스템으로, 작동에 고급 로봇 프로그래밍 기술이 필요하지 않습니다. 요약하면, 로봇 프로그램은 로봇 언어로부터 높은 수준의 추상화를 통해 생성됩니다.

## 핵심 내용
목적 - 본 논문의 목적은 비전문가 사용자가 인간이 서로 가르치는 방식과 유사한 방식으로 로봇을 교육할 수 있도록 하는 CAD 기반 인간-로봇 인터페이스를 제시하는 것입니다.  
설계/방법론/접근법 - CAD 도면을 사용하여 오프라인으로 로봇 프로그램을 생성함으로써 직관적인 로봇 프로그래밍이 가능합니다. 감각 피드백은 불확실성의 영향을 최소화하여 로봇 작동 중 로봇 경로를 조정하는 정보를 제공합니다.  
결과 - 일반적인 CAD 도면에서 로봇 프로그램을 생성하고, 캘리브레이션이나 CAD 모델 정확도에 대한 주요 우려 없이 실행할 수 있음을 발견했습니다.  
연구 한계/의의 - 제안된 시스템의 한계는 특정 기술 응용 분야에 사용되도록 설계되었다는 사실과 관련이 있습니다.  
실용적 의의 - 오늘날 대부분의 제조 회사가 시설에 CAD 패키지를 보유하고 있기 때문에, CAD 기반 로봇 프로그래밍은 숙련된 로봇 프로그래머 없이도 로봇을 프로그래밍할 수 있는 좋은 옵션이 될 수 있습니다.  
독창성/가치 - 본 논문은 새로운 CAD 기반 로봇 프로그래밍 시스템을 제안합니다. 로봇 프로그램은 상용 컴퓨터 지원 로봇공학(CAR) 소프트웨어가 아닌, 일반적으로 사용 가능한 3D CAD 패키지(Autodesk Inventor)에서 실행되는 CAD 도면에서 직접 생성되어 간단한 CAD 통합 솔루션을 제공합니다. 이는 저비용 및 짧은 설정 시간을 가진 시스템으로, 작동에 고급 로봇 프로그래밍 기술이 필요하지 않습니다. 요약하면, 로봇 프로그램은 로봇 언어로부터 높은 수준의 추상화를 통해 생성됩니다.
