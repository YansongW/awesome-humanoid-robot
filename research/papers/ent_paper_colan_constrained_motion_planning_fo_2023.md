---
$id: ent_paper_colan_constrained_motion_planning_fo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Constrained Motion Planning for a Robotic Endoscope Holder based on Hierarchical Quadratic Programming
  zh: 基于分层二次规划的机器人内窥镜支架约束运动规划
  ko: 계층적 이차 계획법을 기반으로 한 로봇 내시경 홀더의 구속 운동 계획
summary:
  en: Proposes an online hierarchical quadratic programming framework for visual servoing control of a surgical endoscope,
    prioritizing remote-center-of-motion constraints while tracking visual features as a secondary task.
  zh: 提出了一种用于手术内窥镜视觉伺服控制的在线分层二次规划框架，将远程运动中心约束作为高优先级任务，视觉特征跟踪作为次要任务。
  ko: 수술용 내시경의 비주얼 서보 제어를 위한 온라인 계층적 이차 계획 프레임워크를 제안하며, 원격 운동 중심 제약을 높은 우선순위 작업으로 하고 시각적 특징 추적을 보조 작업으로 수행한다.
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
- hierarchical_quadratic_programming
- null_space_task_prioritization
- visual_servoing
- remote_center_of_motion
- constrained_motion_planning
- surgical_robotics
- real_time_optimization
- whole_body_control_transferable
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.09982v1.
sources:
- id: src_001
  type: paper
  title: Constrained Motion Planning for a Robotic Endoscope Holder based on Hierarchical Quadratic Programming
  url: https://arxiv.org/abs/2406.09982
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1109/ICCRE57112.2023.10155579
theoretical_depth:
- method
---
## 概述
Minimally Invasive Surgeries (MIS) are challenging for surgeons due to the limited field of view and constrained range of motion imposed by narrow access ports. These challenges can be addressed by robot-assisted endoscope systems which provide precise and stabilized positioning, as well as constrained and smooth motion control of the endoscope. In this work, we propose an online hierarchical optimization framework for visual servoing control of the endoscope in MIS. The framework prioritizes maintaining a remote-center-of-motion (RCM) constraint to prevent tissue damage, while a visual tracking task is defined as a secondary task to enable autonomous tracking of visual features of interest. We validated our approach using a 6-DOF Denso VS050 manipulator and achieved optimization solving times under 0.4 ms and maximum RCM deviation of approximately 0.4 mm. Our results demonstrate the effectiveness of the proposed approach in addressing the constrained motion planning challenges of MIS, enabling precise and autonomous endoscope positioning and visual tracking.

## 核心内容
Minimally Invasive Surgeries (MIS) are challenging for surgeons due to the limited field of view and constrained range of motion imposed by narrow access ports. These challenges can be addressed by robot-assisted endoscope systems which provide precise and stabilized positioning, as well as constrained and smooth motion control of the endoscope. In this work, we propose an online hierarchical optimization framework for visual servoing control of the endoscope in MIS. The framework prioritizes maintaining a remote-center-of-motion (RCM) constraint to prevent tissue damage, while a visual tracking task is defined as a secondary task to enable autonomous tracking of visual features of interest. We validated our approach using a 6-DOF Denso VS050 manipulator and achieved optimization solving times under 0.4 ms and maximum RCM deviation of approximately 0.4 mm. Our results demonstrate the effectiveness of the proposed approach in addressing the constrained motion planning challenges of MIS, enabling precise and autonomous endoscope positioning and visual tracking.

## 参考
- http://arxiv.org/abs/2406.09982v1

