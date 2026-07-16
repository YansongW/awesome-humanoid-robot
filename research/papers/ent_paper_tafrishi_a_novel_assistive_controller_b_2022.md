---
$id: ent_paper_tafrishi_a_novel_assistive_controller_b_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Novel Assistive Controller Based on Differential Geometry for Users of the Differential-Drive Wheeled Mobile Robots
  zh: 面向差动轮式移动机器人用户的基于微分几何的新型辅助控制器
  ko: 차동 구동 휠 모바일 로봇 사용자를 위한 미분기하학 기반의 새로운 보조 제어기
summary:
  en: This 2022 arXiv paper presents a differential-geometry-based assistive controller that helps users steer differential-drive
    wheeled mobile robots—particularly electric wheelchairs—using only joystick inputs and current vehicle states, without
    requiring pre-specified desired states.
  zh: 本2022年arXiv论文提出了一种基于微分几何的辅助控制器，仅利用操纵杆输入和当前车辆状态，帮助用户操控差动轮式移动机器人（尤其是电动轮椅），无需预先指定期望状态。
  ko: 이 2022년 arXiv 논문은 조이스틱 입력과 현재 차량 상태만을 사용하여 사용자가 차동 구동 휠 모바일 로봇, 특히 전동 휠체어를 조향할 수 있도록 돕는 미분기하학 기반 보조 제어기를 제안하며, 사전에 지정된
    목표 상태가 필요하지 않다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- assistive_control
- differential_geometry
- darboux_frame
- shared_control
- wheelchair
- joystick
- mobile_robot
- safety_constraints
- human_subject_study
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.01969v1.
sources:
- id: src_001
  type: paper
  title: A Novel Assistive Controller Based on Differential Geometry for Users of the Differential-Drive Wheeled Mobile Robots
  url: https://arxiv.org/abs/2202.01969
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Certain wheeled mobile robots e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## 核心内容
Certain wheeled mobile robots e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## 参考
- http://arxiv.org/abs/2202.01969v1

## Overview
Certain wheeled mobile robots, e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## Content
Certain wheeled mobile robots, e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## 개요
특정 바퀴형 이동 로봇(예: 전동 휠체어)은 사용자의 간접적인 조이스틱 제어를 통해 작동할 수 있습니다. 사용자가 차량의 방향과 속도를 결정해야 할 때, 특히 차량 속도와 방향이 두 개의 구동 바퀴로만 제어되는 차동 바퀴형 차량의 경우 올바른 조향 각도가 필수적입니다. 사용자가 복잡한 곡선을 구현해야 할 때 이 문제는 더욱 어려워집니다. 이러한 문제를 해결하기 위해 안전 제약 조건을 갖춘 새로운 보조 제어기가 필요합니다. 또한, 기존 제어 방법은 대부분 사전에 원하는 상태를 요구하는데, 이는 인간이 가고자 하는 위치에 대한 자발적인 결정과 완전히 상반됩니다. 본 연구에서는 조이스틱 입력과 차량 상태에만 의존하는 미분 기하학 기반의 새로운 보조 제어 전략을 개발하며, 이 제어기는 어떤 원하는 상태도 필요로 하지 않습니다. 먼저 차량 운동학과 가상 바퀴와 평면의 접촉점에서 설계된 다르부 프레임 운동학을 설명합니다. 다음으로, 다르부 프레임 운동학을 사용한 기하학적 제어기를 설계하여 특정 안전 제약 조건 하에서 부드러운 궤적을 얻습니다. 다양한 참가자와 함께 접근 방식을 실험하고 다양한 경로에서 성능을 평가합니다.

## 핵심 내용
특정 바퀴형 이동 로봇(예: 전동 휠체어)은 사용자의 간접적인 조이스틱 제어를 통해 작동할 수 있습니다. 사용자가 차량의 방향과 속도를 결정해야 할 때, 특히 차량 속도와 방향이 두 개의 구동 바퀴로만 제어되는 차동 바퀴형 차량의 경우 올바른 조향 각도가 필수적입니다. 사용자가 복잡한 곡선을 구현해야 할 때 이 문제는 더욱 어려워집니다. 이러한 문제를 해결하기 위해 안전 제약 조건을 갖춘 새로운 보조 제어기가 필요합니다. 또한, 기존 제어 방법은 대부분 사전에 원하는 상태를 요구하는데, 이는 인간이 가고자 하는 위치에 대한 자발적인 결정과 완전히 상반됩니다. 본 연구에서는 조이스틱 입력과 차량 상태에만 의존하는 미분 기하학 기반의 새로운 보조 제어 전략을 개발하며, 이 제어기는 어떤 원하는 상태도 필요로 하지 않습니다. 먼저 차량 운동학과 가상 바퀴와 평면의 접촉점에서 설계된 다르부 프레임 운동학을 설명합니다. 다음으로, 다르부 프레임 운동학을 사용한 기하학적 제어기를 설계하여 특정 안전 제약 조건 하에서 부드러운 궤적을 얻습니다. 다양한 참가자와 함께 접근 방식을 실험하고 다양한 경로에서 성능을 평가합니다.
