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

