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
  zh: pyCub 是一个基于 iCub 人形机器人的开源物理仿真框架，由研究团队于 2025 年发布。其核心贡献在于完全使用 Python 编写，无需 YARP 中间件，并提供了从基础控制到复杂任务的可扩展练习，降低了人形机器人学的教学门槛。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01756v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01756
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
pyCub 框架完整模拟了 iCub 人形机器人的所有关节，并集成了眼部双摄像头和体表 4000 个触觉传感器。与需要 C++ 和 YARP 的现有 iCub 仿真器不同，pyCub 完全基于 Python 实现，使编程经验较少的学生也能使用。该框架提供了速度控制、关节空间控制、笛卡尔空间控制等基础练习，以及注视、抓取和反应控制等高级任务，难度可灵活调整。研究团队已在两轮人形机器人课程中测试了该框架。

## 核心内容
### 框架设计
- **仿真环境**：基于物理引擎的开源仿真，完整模拟 iCub 人形机器人的所有关节自由度。
- **传感器系统**：眼部配备两个摄像头，体表集成 iCub 特有的敏感皮肤（含 4000 个触觉受体）。
- **技术架构**：完全使用 Python 编写和控制，无需 YARP 中间件，与需要 C++ 和 YARP 的 iCub SIM 及 iCub Gazebo 形成对比。

### 练习内容
- **基础控制**：涵盖速度控制、关节空间控制和笛卡尔空间控制。
- **高级任务**：包括注视控制、抓取操作和反应控制。
- **难度分级**：所有练习均可按不同难度级别进行缩放，适应不同水平的学习者。

### 实验与可用性
- **教学验证**：在两轮人形机器人课程中完成测试。
- **资源开放**：仿真代码、练习、文档、Docker 镜像和示例视频均公开于 https://rustlluk.github.io/pyCub。

## Overview
We present pyCub, an open-source physics-based simulation of the humanoid robot iCub, along with exercises to teach students the basics of humanoid robotics. Compared to existing iCub simulators (iCub SIM, iCub Gazebo), which require C++ code and YARP as middleware, pyCub works without YARP and with Python code. The complete robot with all articulations has been simulated, with two cameras in the eyes and the unique sensitive skin of the iCub comprising 4000 receptors on its body surface. The exercises range from basic control of the robot in velocity, joint, and Cartesian space to more complex tasks like gazing, grasping, or reactive control. The whole framework is written and controlled with Python, thus allowing to be used even by people with small or almost no programming practice. The exercises can be scaled to different difficulty levels. We tested the framework in two runs of a course on humanoid robotics. The simulation, exercises, documentation, Docker images, and example videos are publicly available at https://rustlluk.github.io/pyCub.

## 개요
본 논문에서는 휴머노이드 로봇 iCub의 오픈소스 물리 기반 시뮬레이션인 pyCub과 학생들에게 휴머노이드 로봇공학 기초를 가르치기 위한 연습 문제를 제시합니다. C++ 코드와 미들웨어 YARP가 필요한 기존 iCub 시뮬레이터(iCub SIM, iCub Gazebo)와 달리, pyCub은 YARP 없이 Python 코드로 작동합니다. 모든 관절을 갖춘 완전한 로봇이 시뮬레이션되었으며, 눈에는 두 대의 카메라가, iCub의 독특한 민감 피부에는 신체 표면에 4000개의 수용체가 포함되어 있습니다. 연습 문제는 속도, 관절, 데카르트 공간에서의 기본 로봇 제어부터 응시, 파지, 반응 제어와 같은 더 복잡한 작업까지 다양합니다. 전체 프레임워크는 Python으로 작성 및 제어되므로 프로그래밍 경험이 거의 없거나 전혀 없는 사람도 사용할 수 있습니다. 연습 문제는 다양한 난이도로 조정 가능합니다. 우리는 휴머노이드 로봇공학 과정의 두 차례 운영에서 이 프레임워크를 테스트했습니다. 시뮬레이션, 연습 문제, 문서, Docker 이미지, 예제 비디오는 https://rustlluk.github.io/pyCub에서 공개적으로 제공됩니다.

## 핵심 내용
본 논문에서는 휴머노이드 로봇 iCub의 오픈소스 물리 기반 시뮬레이션인 pyCub과 학생들에게 휴머노이드 로봇공학 기초를 가르치기 위한 연습 문제를 제시합니다. C++ 코드와 미들웨어 YARP가 필요한 기존 iCub 시뮬레이터(iCub SIM, iCub Gazebo)와 달리, pyCub은 YARP 없이 Python 코드로 작동합니다. 모든 관절을 갖춘 완전한 로봇이 시뮬레이션되었으며, 눈에는 두 대의 카메라가, iCub의 독특한 민감 피부에는 신체 표면에 4000개의 수용체가 포함되어 있습니다. 연습 문제는 속도, 관절, 데카르트 공간에서의 기본 로봇 제어부터 응시, 파지, 반응 제어와 같은 더 복잡한 작업까지 다양합니다. 전체 프레임워크는 Python으로 작성 및 제어되므로 프로그래밍 경험이 거의 없거나 전혀 없는 사람도 사용할 수 있습니다. 연습 문제는 다양한 난이도로 조정 가능합니다. 우리는 휴머노이드 로봇공학 과정의 두 차례 운영에서 이 프레임워크를 테스트했습니다. 시뮬레이션, 연습 문제, 문서, Docker 이미지, 예제 비디오는 https://rustlluk.github.io/pyCub에서 공개적으로 제공됩니다.

## 参考
- http://arxiv.org/abs/2506.01756v3
