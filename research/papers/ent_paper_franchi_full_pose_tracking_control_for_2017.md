---
$id: ent_paper_franchi_full_pose_tracking_control_for_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Full-Pose Tracking Control for Aerial Robotic Systems with Laterally-Bounded Input Force
  zh: 具有侧向有界输入力的空中机器人系统的全位姿跟踪控制
  ko: 측방 제한 입력력을 가진 공중 로봇 시스템의 전체 자세 추적 제어
summary:
  en: This paper introduces Laterally Bounded Force (LBF) vehicles, a class of aerial robots whose primary control authority
    is along a principal thrust direction while lateral force is limited, and proposes a geometric SE(3) controller that achieves
    independent position-plus-orientation tracking when feasible and falls back to guaranteed position tracking otherwise.
  zh: 本文提出了侧向有界力（LBF）飞行器类，其主要控制力沿主推力方向而侧向力受限，并给出了一种SE(3)几何控制器，在可行时实现位置与姿态的独立跟踪，否则保证位置跟踪。
  ko: 본 논문은 주 추력 방향에 주 제어 권한이 있고 측방 힘이 제한된 LBF(Laterally Bounded Force) 항공기 범주를 제안하며, 가능한 경우 위치와 자세의 독립적 추적을 달성하고 그렇지 않은 경우
    위치 추적을 보장하는 SE(3) 기하학적 제어기를 제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1605.06645v2.
sources:
- id: src_001
  type: paper
  title: Full-Pose Tracking Control for Aerial Robotic Systems with Laterally-Bounded Input Force
  url: https://arxiv.org/abs/1605.06645
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this paper, we define a general class of abstract aerial robotic systems named Laterally Bounded Force (LBF) vehicles, in which most of the control authority is expressed along a principal thrust direction, while in the lateral directions a (smaller and possibly null) force may be exploited to achieve full-pose tracking. This class approximates well platforms endowed with non-coplanar/non-collinear rotors that can use the tilted propellers to slightly change the orientation of the total thrust w.r.t. the body frame. For this broad class of systems, we introduce a new geometric control strategy in SE(3) to achieve, whenever made possible by the force constraints, the independent tracking of position-plus-orientation trajectories. The exponential tracking of a feasible full-pose reference trajectory is proven using a Lyapunov technique in SE(3). The method can deal seamlessly with both under- and fully-actuated LBF platforms. The controller guarantees the tracking of at least the positional part in the case that an unfeasible full-pose reference trajectory is provided. The paper provides several experimental tests clearly showing the practicability of the approach and the sharp improvement with respect to state of-the-art approaches.

## 核心内容
In this paper, we define a general class of abstract aerial robotic systems named Laterally Bounded Force (LBF) vehicles, in which most of the control authority is expressed along a principal thrust direction, while in the lateral directions a (smaller and possibly null) force may be exploited to achieve full-pose tracking. This class approximates well platforms endowed with non-coplanar/non-collinear rotors that can use the tilted propellers to slightly change the orientation of the total thrust w.r.t. the body frame. For this broad class of systems, we introduce a new geometric control strategy in SE(3) to achieve, whenever made possible by the force constraints, the independent tracking of position-plus-orientation trajectories. The exponential tracking of a feasible full-pose reference trajectory is proven using a Lyapunov technique in SE(3). The method can deal seamlessly with both under- and fully-actuated LBF platforms. The controller guarantees the tracking of at least the positional part in the case that an unfeasible full-pose reference trajectory is provided. The paper provides several experimental tests clearly showing the practicability of the approach and the sharp improvement with respect to state of-the-art approaches.

## 参考
- http://arxiv.org/abs/1605.06645v2

