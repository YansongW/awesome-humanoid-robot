---
$id: ent_paper_learning_with_pycub_a_simulati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
  zh: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
  ko: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics'
summary:
  en: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics is a 2025 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- learning_with_pycub
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01756v3.
sources:
- id: src_001
  type: paper
  title: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01756
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 核心内容
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 参考
- http://arxiv.org/abs/2506.01756v3

## Overview
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## Content
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 개요
본 논문에서는 휴머노이드 로봇 iCub의 오픈소스 물리 기반 시뮬레이션인 pyCub과 학생들에게 휴머노이드 로봇공학 기초를 가르치기 위한 연습 문제를 제시합니다. C++ 코드와 미들웨어 YARP가 필요한 기존 iCub 시뮬레이터(iCub SIM, iCub Gazebo)와 달리, pyCub은 YARP 없이 Python 코드로 작동합니다. 모든 관절을 갖춘 완전한 로봇이 시뮬레이션되었으며, 눈에는 두 대의 카메라가, iCub의 독특한 민감 피부에는 신체 표면에 4000개의 수용체가 포함되어 있습니다. 연습 문제는 속도, 관절, 데카르트 공간에서의 기본 로봇 제어부터 응시, 파지, 반응 제어와 같은 더 복잡한 작업까지 다양합니다. 전체 프레임워크는 Python으로 작성 및 제어되므로 프로그래밍 경험이 거의 없거나 전혀 없는 사람도 사용할 수 있습니다. 연습 문제는 다양한 난이도로 조정 가능합니다. 우리는 휴머노이드 로봇공학 과정의 두 차례 운영에서 이 프레임워크를 테스트했습니다. 시뮬레이션, 연습 문제, 문서, Docker 이미지, 예제 비디오는 https://rustlluk.github.io/pyCub에서 공개적으로 제공됩니다.

## 핵심 내용
본 논문에서는 휴머노이드 로봇 iCub의 오픈소스 물리 기반 시뮬레이션인 pyCub과 학생들에게 휴머노이드 로봇공학 기초를 가르치기 위한 연습 문제를 제시합니다. C++ 코드와 미들웨어 YARP가 필요한 기존 iCub 시뮬레이터(iCub SIM, iCub Gazebo)와 달리, pyCub은 YARP 없이 Python 코드로 작동합니다. 모든 관절을 갖춘 완전한 로봇이 시뮬레이션되었으며, 눈에는 두 대의 카메라가, iCub의 독특한 민감 피부에는 신체 표면에 4000개의 수용체가 포함되어 있습니다. 연습 문제는 속도, 관절, 데카르트 공간에서의 기본 로봇 제어부터 응시, 파지, 반응 제어와 같은 더 복잡한 작업까지 다양합니다. 전체 프레임워크는 Python으로 작성 및 제어되므로 프로그래밍 경험이 거의 없거나 전혀 없는 사람도 사용할 수 있습니다. 연습 문제는 다양한 난이도로 조정 가능합니다. 우리는 휴머노이드 로봇공학 과정의 두 차례 운영에서 이 프레임워크를 테스트했습니다. 시뮬레이션, 연습 문제, 문서, Docker 이미지, 예제 비디오는 https://rustlluk.github.io/pyCub에서 공개적으로 제공됩니다.
