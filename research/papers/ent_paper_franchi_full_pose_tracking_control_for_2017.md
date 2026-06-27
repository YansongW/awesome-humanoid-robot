---
$id: ent_paper_franchi_full_pose_tracking_control_for_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Full-Pose Tracking Control for Aerial Robotic Systems with Laterally-Bounded
    Input Force
  zh: 具有侧向有界输入力的空中机器人系统的全位姿跟踪控制
  ko: 측방 제한 입력력을 가진 공중 로봇 시스템의 전체 자세 추적 제어
summary:
  en: This paper introduces Laterally Bounded Force (LBF) vehicles, a class of aerial
    robots whose primary control authority is along a principal thrust direction while
    lateral force is limited, and proposes a geometric SE(3) controller that achieves
    independent position-plus-orientation tracking when feasible and falls back to
    guaranteed position tracking otherwise.
  zh: 本文提出了侧向有界力（LBF）飞行器类，其主要控制力沿主推力方向而侧向力受限，并给出了一种SE(3)几何控制器，在可行时实现位置与姿态的独立跟踪，否则保证位置跟踪。
  ko: 본 논문은 주 추력 방향에 주 제어 권한이 있고 측방 힘이 제한된 LBF(Laterally Bounded Force) 항공기 범주를 제안하며,
    가능한 경우 위치와 자세의 독립적 추적을 달성하고 그렇지 않은 경우 위치 추적을 보장하는 SE(3) 기하학적 제어기를 제시한다.
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
- se3_control
- geometric_control
- full_pose_tracking
- laterally_bounded_force
- bounded_force
- aerial_robotics
- lyapunov_stability
- tilt_hex
- actuator_constraints
- pose_tracking
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full text was not inspected,
    so hardware details and cited relationships require human review before verification.
sources:
- id: src_001
  type: paper
  title: Full-Pose Tracking Control for Aerial Robotic Systems with Laterally-Bounded
    Input Force
  url: https://arxiv.org/abs/1605.06645
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper defines the Laterally Bounded Force (LBF) vehicle class, which models aerial robotic systems whose control authority is concentrated along a principal thrust axis and whose lateral force is limited or zero. By unifying under-actuated and fully-actuated multi-rotor platforms within one abstraction, the work addresses the problem that such platforms cannot independently track arbitrary full 6D pose trajectories once the required lateral force exceeds the available limit. It develops a geometric controller directly on SE(3), avoiding local orientation singularities and enabling independent tracking of position-plus-orientation reference trajectories whenever the force bounds permit.

The control law computes a desired orientation that is compatible with the lateral force bound and then applies a cascaded position/attitude strategy. A Lyapunov argument in SE(3) proves exponential tracking for feasible full-pose trajectories; when the desired orientation is infeasible, the controller at least guarantees positional tracking. The authors also give an analytic/numeric orientation solver for the cylindrical LBF case using a bisection algorithm.

Experimental validation is performed on the Tilt-Hex hexarotor, a tilted-rotor platform that can switch between under-actuated and fully-actuated behaviors. The results demonstrate seamless transitions between the two regimes and improvements over prior state-of-the-art methods.

## Key Contributions

- Introduction of the Laterally Bounded Force (LBF) aerial-vehicle class that unifies under- and fully-actuated multi-rotor platforms.
- Geometric full-pose tracking controller in SE(3) that avoids local orientation singularities.
- Lyapunov-based proof of exponential tracking for feasible trajectories and guaranteed position tracking for infeasible ones.
- Analytic/numerical solution for the desired orientation in a cylindrical LBF case using a bisection algorithm.
- Real experimental validation on the Tilt-Hex hexarotor showing seamless transition between under- and fully-actuated behavior.

## Relevance to Humanoid Robotics

Although the paper focuses on aerial robots, its core methodology—geometric SE(3) full-pose tracking under bounded force—is transferable to humanoid robots. Humanoids must similarly coordinate their position and orientation under strict actuator force/torque limits, and the idea of prioritizing position tracking when a full-pose reference is infeasible is directly relevant to balancing and locomotion. The Lyapunov-style stability argument and the force-compatible orientation construction can inform controllers for humanoid whole-body or centroidal dynamics.
