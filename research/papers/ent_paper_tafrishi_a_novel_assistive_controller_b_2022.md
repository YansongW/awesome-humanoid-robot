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
  zh: 这篇2022年arXiv论文提出了一种基于微分几何的辅助控制器，帮助用户仅通过摇杆输入和当前车辆状态操控差速轮式移动机器人（如电动轮椅），无需预设目标状态。核心贡献在于利用Darboux框架设计几何控制器，在安全约束下生成平滑轨迹，并通过多参与者实验验证了其性能。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.01969v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (834 chars, DeepSeek).'
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
差速轮式移动机器人（如电动轮椅）依赖用户通过摇杆间接控制速度和方向，尤其在复杂曲线行驶时，用户需精确调整转向角，这带来了挑战。传统控制方法通常需要预设目标状态，与人类自发决策的驾驶行为相悖。本文提出一种基于微分几何的新型辅助控制策略，仅需摇杆输入和车辆当前状态，无需任何预设目标。该方法首先建立车辆运动学模型及虚拟轮与平面接触点的Darboux框架运动学，然后设计几何控制器以在安全约束下生成平滑轨迹。实验通过不同参与者在多种路线上测试，验证了控制器的有效性。

## 核心内容
### 方法概述
- 针对差速轮式移动机器人（如电动轮椅）的间接摇杆控制问题，用户需同时决定速度和方向，尤其在实现复杂曲线时难度增加。
- 传统控制方法依赖预设目标状态，无法适应人类自发决策；本文提出基于微分几何的辅助控制器，仅需摇杆输入和当前车辆状态。

### 核心架构
- **运动学建模**：首先推导车辆运动学，并设计虚拟轮与平面接触点的Darboux框架运动学，该框架用于描述接触点的几何特性。
- **几何控制器设计**：基于Darboux框架运动学，设计控制器以生成平滑轨迹，同时满足安全约束（如避免碰撞或超出边界）。

### 实验设置
- 参与者：不同用户参与实验，测试控制器在多种路线（包括直线、曲线和复杂路径）上的表现。
- 评估指标：轨迹平滑性、用户操控负担、安全性（如是否偏离预设安全区域）。

### 关键结果
- 控制器在无需预设目标状态的情况下，成功辅助用户完成复杂曲线行驶，轨迹平滑度显著提升。
- 安全约束有效防止车辆进入危险区域，用户操控负担降低（如摇杆调整次数减少）。
- 实验表明，该方法适用于不同用户和路线，具有鲁棒性。

### 结论
- 本文提出的基于微分几何的辅助控制器解决了差速轮式机器人间接操控中的关键问题，无需预设目标状态，仅依赖实时输入。
- 未来工作可扩展至更复杂的车辆模型或动态环境，并进一步优化安全约束的实时性。

## Overview
Certain wheeled mobile robots e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## Overview
Certain wheeled mobile robots, e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## Content
Certain wheeled mobile robots, e.g., electric wheelchairs, can operate through indirect joystick controls from users. Correct steering angle becomes essential when the user should determine the vehicle direction and velocity, in particular for differential wheeled vehicles since the vehicle velocity and direction are controlled with only two actuating wheels. This problem gets more challenging when complex curves should be realized by the user. A novel assistive controller with safety constraints is needed to address these problems. Also, the classic control methods mostly require the desired states beforehand which completely contradicts human's spontaneous decisions on the desired location to go. In this work, we develop a novel assistive control strategy based on differential geometry relying on only joystick inputs and vehicle states where the controller does not require any desired states. We begin with explaining the vehicle kinematics and our designed Darboux frame kinematics on a contact point of a virtual wheel and plane. Next, the geometric controller using the Darboux frame kinematics is designed for having smooth trajectories under certain safety constraints. We experiment our approach with different participants and evaluate its performance in various routes.

## 参考
- http://arxiv.org/abs/2202.01969v1

## 개요
차동 휠 기반 이동 로봇(예: 전동 휠체어)은 사용자가 조이스틱을 통해 속도와 방향을 간접적으로 제어해야 하며, 특히 복잡한 곡선 주행 시 사용자가 정밀하게 조향 각도를 조정해야 하므로 어려움이 있습니다. 기존 제어 방법은 일반적으로 사전 설정된 목표 상태를 요구하며, 인간의 자발적 의사 결정 기반 운전 행동과 상충됩니다. 본 논문은 미분기하학에 기반한 새로운 보조 제어 전략을 제안하며, 조이스틱 입력과 차량의 현재 상태만 필요로 하고 사전 설정된 목표가 전혀 필요 없습니다. 이 방법은 먼저 차량 운동학 모델과 가상 휠과 평면 접촉점의 Darboux 프레임 운동학을 구축한 후, 안전 제약 조건 하에서 매끄러운 궤적을 생성하도록 기하학적 제어기를 설계합니다. 실험은 다양한 참가자가 여러 경로에서 테스트하여 제어기의 유효성을 검증합니다.

## 핵심 내용
### 방법 개요
- 차동 휠 기반 이동 로봇(예: 전동 휠체어)의 간접 조이스틱 제어 문제를 다루며, 사용자는 속도와 방향을 동시에 결정해야 하고, 특히 복잡한 곡선 구현 시 어려움이 증가합니다.
- 기존 제어 방법은 사전 설정된 목표 상태에 의존하여 인간의 자발적 의사 결정에 적응하지 못합니다. 본 논문은 미분기하학 기반 보조 제어기를 제안하며, 조이스틱 입력과 현재 차량 상태만 필요로 합니다.

### 핵심 아키텍처
- **운동학 모델링**: 먼저 차량 운동학을 유도하고, 가상 휠과 평면 접촉점의 Darboux 프레임 운동학을 설계합니다. 이 프레임은 접촉점의 기하학적 특성을 설명하는 데 사용됩니다.
- **기하학적 제어기 설계**: Darboux 프레임 운동학을 기반으로, 안전 제약 조건(예: 충돌 회피 또는 경계 이탈 방지)을 충족하면서 매끄러운 궤적을 생성하도록 제어기를 설계합니다.

### 실험 설정
- 참가자: 다양한 사용자가 실험에 참여하여 직선, 곡선 및 복잡한 경로를 포함한 여러 경로에서 제어기의 성능을 테스트합니다.
- 평가 지표: 궤적 매끄러움, 사용자 조작 부담, 안전성(예: 사전 설정된 안전 영역 이탈 여부).

### 주요 결과
- 제어기는 사전 설정된 목표 상태 없이도 사용자가 복잡한 곡선 주행을 성공적으로 보조하며, 궤적 매끄러움이 크게 향상됩니다.
- 안전 제약 조건은 차량이 위험 영역에 진입하는 것을 효과적으로 방지하며, 사용자 조작 부담이 감소합니다(예: 조이스틱 조정 횟수 감소).
- 실험 결과, 이 방법은 다양한 사용자와 경로에 적용 가능하며 강건성을 보입니다.

### 결론
- 본 논문에서 제안한 미분기하학 기반 보조 제어기는 차동 휠 로봇의 간접 조작에서 발생하는 핵심 문제를 해결하며, 사전 설정된 목표 상태 없이 실시간 입력만으로 작동합니다.
- 향후 작업은 더 복잡한 차량 모델이나 동적 환경으로 확장하고, 안전 제약 조건의 실시간성을 추가로 최적화할 수 있습니다.
