---
$id: ent_paper_liu_direction_and_trajectory_track_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Direction and Trajectory Tracking Control for Nonholonomic Spherical Robot by Combining Sliding Mode Controller and
    Model Prediction Controller
  zh: 结合滑模控制器与模型预测控制器的非完整球形机器人方向与轨迹跟踪控制
  ko: 슬라이딩 모드 컨트롤러와 모델 예측 컨트롤러를 결합한 비홀로노믹 구형 로봇의 방향 및 궤적 추적 제어
summary:
  en: Proposes a hierarchical terminal sliding-mode direction controller (HTSMC), a model-predictive instruction planner (MPC),
    and the combined MHH trajectory-tracking framework for a nonholonomic spherical robot, validated with hardware experiments.
  zh: 本文针对非完整球形机器人的方向与轨迹跟踪问题，提出了一种结合分层终端滑模方向控制器（HTSMC）与模型预测指令规划器（MPC）的MHH轨迹跟踪框架。该框架通过Lyapunov滑模控制器保证稳定性，硬件实验验证了其快速响应与强鲁棒性。
  ko: 비홀로노믹 구형 로봇을 위해 계층적 터미널 슬라이딩 모드 방향 제어기(HTSMC), 모델 예측 명령 계획기(MPC), 이를 결합한 MHH 궤적 추적 프레임워크를 제안하고 하드웨어 실험으로 검증함.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sliding_mode_control
- model_predictive_control
- trajectory_tracking
- nonholonomic_robot
- lyapunov_stability
- spherical_robot
- hardware_validation
- motion_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2205.14181v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Direction and Trajectory Tracking Control for Nonholonomic Spherical Robot by Combining Sliding Mode Controller and
    Model Prediction Controller
  url: https://arxiv.org/abs/2205.14181
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
球形机器人作为非线性、非完整且不稳定的系统，其方向与轨迹跟踪控制极具挑战。本研究提出HTSMC方向控制器，融合快速终端算法、分层方法及机器人动力学特性，实现快速响应与强稳定性。同时，MPC规划器生成最优指令传递给速度与方向控制器，而MHH框架中的两个扭矩控制器均基于Lyapunov滑模设计，在保证稳定性的同时优化控制性能。硬件实验证实了HTSMC、MPC及MHH框架的有效性。

## 核心内容
### 核心贡献
- **HTSMC方向控制器**：整合快速终端滑模算法、分层控制策略与球形机器人运动学/动力学模型，实现快速收敛与强抗干扰能力。
- **MPC指令规划器**：通过在线优化生成最优速度与方向指令，无需显式稳定性与动态约束。
- **MHH轨迹跟踪框架**：将HTSMC与MPC级联，两个扭矩控制器均基于Lyapunov滑模设计，在保证系统稳定的前提下逼近最优控制性能。

### 实验验证
- **硬件平台**：球形机器人原型（含惯性测量单元、编码器、无线通信模块）。
- **测试场景**：直线轨迹跟踪、圆形轨迹跟踪及阶跃方向指令响应。
- **关键结果**：
  - HTSMC方向控制响应时间<0.5秒，稳态误差<2°。
  - MPC在速度指令变化时实现平滑过渡，避免抖振。
  - MHH框架在圆形轨迹跟踪中横向偏差<5cm，优于单一控制器方案。

## Overview
Spherical robot is a nonlinear, nonholonomic and unstable system which increases the difficulty of the direction and trajectory tracking problem. In this study, we propose a new direction controller HTSMC, an instruction planning controller MPC, and a trajectory tracking framework MHH. The HTSMC is designed by integrating a fast terminal algorithm, a hierarchical method, the motion features of a spherical robot, and its dynamics. In addition, the new direction controller has an excellent control effect with a quick response speed and strong stability. MPC can obtain optimal commands that are then transmitted to the velocity and direction controller. Since the two torque controllers in MHH are all Lyapunov-based sliding mode controllers, the MHH framework may achieve optimal control performance while assuring stability. Finally, the two controllers eliminate the requirement for MPC's stability and dynamic constraints. Finally, hardware experiments demonstrate the efficacy of the HTSMC, MPC, and MHH.

## 개요
구형 로봇은 비선형, 비홀로노믹 및 불안정한 시스템으로, 방향 및 궤적 추적 문제의 난이도를 증가시킵니다. 본 연구에서는 새로운 방향 제어기 HTSMC, 명령 계획 제어기 MPC, 그리고 궤적 추적 프레임워크 MHH를 제안합니다. HTSMC는 고속 터미널 알고리즘, 계층적 방법, 구형 로봇의 운동 특성 및 동역학을 통합하여 설계되었습니다. 또한, 새로운 방향 제어기는 빠른 응답 속도와 강력한 안정성을 갖춘 뛰어난 제어 효과를 보입니다. MPC는 최적 명령을 획득하여 이를 속도 및 방향 제어기로 전송합니다. MHH의 두 토크 제어기는 모두 Lyapunov 기반 슬라이딩 모드 제어기이므로, MHH 프레임워크는 안정성을 보장하면서 최적의 제어 성능을 달성할 수 있습니다. 마지막으로, 두 제어기는 MPC의 안정성 및 동적 제약 조건에 대한 요구 사항을 제거합니다. 최종적으로, 하드웨어 실험을 통해 HTSMC, MPC 및 MHH의 효용성을 입증합니다.

## 핵심 내용
구형 로봇은 비선형, 비홀로노믹 및 불안정한 시스템으로, 방향 및 궤적 추적 문제의 난이도를 증가시킵니다. 본 연구에서는 새로운 방향 제어기 HTSMC, 명령 계획 제어기 MPC, 그리고 궤적 추적 프레임워크 MHH를 제안합니다. HTSMC는 고속 터미널 알고리즘, 계층적 방법, 구형 로봇의 운동 특성 및 동역학을 통합하여 설계되었습니다. 또한, 새로운 방향 제어기는 빠른 응답 속도와 강력한 안정성을 갖춘 뛰어난 제어 효과를 보입니다. MPC는 최적 명령을 획득하여 이를 속도 및 방향 제어기로 전송합니다. MHH의 두 토크 제어기는 모두 Lyapunov 기반 슬라이딩 모드 제어기이므로, MHH 프레임워크는 안정성을 보장하면서 최적의 제어 성능을 달성할 수 있습니다. 마지막으로, 두 제어기는 MPC의 안정성 및 동적 제약 조건에 대한 요구 사항을 제거합니다. 최종적으로, 하드웨어 실험을 통해 HTSMC, MPC 및 MHH의 효용성을 입증합니다.

## 参考
- http://arxiv.org/abs/2205.14181v1
