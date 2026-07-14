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
  zh: 针对非完整球形机器人提出分层终端滑模方向控制器（HTSMC）、模型预测指令规划器（MPC）以及两者结合的MHH轨迹跟踪框架，并通过硬件实验验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2205.14181v1.
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
Spherical robot is a nonlinear, nonholonomic and unstable system which increases the difficulty of the direction and trajectory tracking problem. In this study, we propose a new direction controller HTSMC, an instruction planning controller MPC, and a trajectory tracking framework MHH. The HTSMC is designed by integrating a fast terminal algorithm, a hierarchical method, the motion features of a spherical robot, and its dynamics. In addition, the new direction controller has an excellent control effect with a quick response speed and strong stability. MPC can obtain optimal commands that are then transmitted to the velocity and direction controller. Since the two torque controllers in MHH are all Lyapunov-based sliding mode controllers, the MHH framework may achieve optimal control performance while assuring stability. Finally, the two controllers eliminate the requirement for MPC's stability and dynamic constraints. Finally, hardware experiments demonstrate the efficacy of the HTSMC, MPC, and MHH.

## 核心内容
Spherical robot is a nonlinear, nonholonomic and unstable system which increases the difficulty of the direction and trajectory tracking problem. In this study, we propose a new direction controller HTSMC, an instruction planning controller MPC, and a trajectory tracking framework MHH. The HTSMC is designed by integrating a fast terminal algorithm, a hierarchical method, the motion features of a spherical robot, and its dynamics. In addition, the new direction controller has an excellent control effect with a quick response speed and strong stability. MPC can obtain optimal commands that are then transmitted to the velocity and direction controller. Since the two torque controllers in MHH are all Lyapunov-based sliding mode controllers, the MHH framework may achieve optimal control performance while assuring stability. Finally, the two controllers eliminate the requirement for MPC's stability and dynamic constraints. Finally, hardware experiments demonstrate the efficacy of the HTSMC, MPC, and MHH.

## 参考
- http://arxiv.org/abs/2205.14181v1

