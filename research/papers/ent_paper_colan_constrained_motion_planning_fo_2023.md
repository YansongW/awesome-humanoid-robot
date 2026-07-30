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
  zh: 本文提出一种基于分层二次规划的在线优化框架，用于微创手术中机器人内窥镜的视觉伺服控制。该框架优先满足远程运动中心约束以防止组织损伤，同时将视觉特征跟踪作为次要任务。在6自由度Denso VS050机械臂上的实验表明，优化求解时间低于0.4毫秒，RCM最大偏差约0.4毫米。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.09982v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
针对微创手术中视野受限和运动范围受限的挑战，本文提出一种在线分层优化框架，用于内窥镜的视觉伺服控制。该框架通过分层二次规划，将远程运动中心约束作为首要任务，确保内窥镜运动不损伤组织，同时将视觉特征跟踪作为次要任务，实现自主跟踪。在6自由度Denso VS050机械臂上的验证显示，该框架的优化求解时间低于0.4毫秒，RCM最大偏差约0.4毫米，证明了其在精确自主定位和视觉跟踪方面的有效性。

## 核心内容
### 方法
- 提出基于分层二次规划（Hierarchical Quadratic Programming, HQP）的在线优化框架，用于微创手术中内窥镜的视觉伺服控制。
- 框架将远程运动中心（RCM）约束作为首要任务，确保内窥镜运动不损伤组织；视觉特征跟踪作为次要任务，实现自主跟踪。

### 架构
- 采用分层优化结构，优先满足高优先级约束（RCM），再处理低优先级任务（视觉跟踪）。
- 使用二次规划求解器在线求解优化问题，确保实时性。

### 实验设置
- 使用6自由度Denso VS050机械臂进行验证。
- 实验环境模拟微创手术场景，评估RCM约束保持和视觉跟踪性能。

### 关键数字
- 优化求解时间低于0.4毫秒，满足实时控制需求。
- 最大RCM偏差约0.4毫米，表明约束保持精度高。

### 结论
- 该方法有效解决了微创手术中的约束运动规划问题，实现了精确、自主的内窥镜定位和视觉跟踪。
- 实验结果验证了框架在实时性和精度方面的有效性，为机器人辅助内窥镜系统提供了可行方案。

## Overview
Minimally Invasive Surgeries (MIS) are challenging for surgeons due to the limited field of view and constrained range of motion imposed by narrow access ports. These challenges can be addressed by robot-assisted endoscope systems which provide precise and stabilized positioning, as well as constrained and smooth motion control of the endoscope. In this work, we propose an online hierarchical optimization framework for visual servoing control of the endoscope in MIS. The framework prioritizes maintaining a remote-center-of-motion (RCM) constraint to prevent tissue damage, while a visual tracking task is defined as a secondary task to enable autonomous tracking of visual features of interest. We validated our approach using a 6-DOF Denso VS050 manipulator and achieved optimization solving times under 0.4 ms and maximum RCM deviation of approximately 0.4 mm. Our results demonstrate the effectiveness of the proposed approach in addressing the constrained motion planning challenges of MIS, enabling precise and autonomous endoscope positioning and visual tracking.

## 개요
최소 침습 수술(MIS)은 좁은 접근 포트로 인한 제한된 시야와 움직임 범위로 인해 외과의사에게 어려운 과제입니다. 이러한 문제는 로봇 보조 내시경 시스템을 통해 해결할 수 있으며, 이 시스템은 정밀하고 안정적인 위치 지정과 함께 내시경의 제한적이고 부드러운 움직임 제어를 제공합니다. 본 연구에서는 MIS에서 내시경의 시각 서보 제어를 위한 온라인 계층적 최적화 프레임워크를 제안합니다. 이 프레임워크는 조직 손상을 방지하기 위해 원격 중심 움직임(RCM) 제약 조건을 유지하는 것을 우선시하며, 관심 시각 특징의 자율 추적을 가능하게 하기 위해 시각 추적 작업을 보조 작업으로 정의합니다. 우리는 6자유도 Denso VS050 매니퓰레이터를 사용하여 접근 방식을 검증했으며, 최적화 해결 시간이 0.4ms 미만이고 최대 RCM 편차가 약 0.4mm임을 달성했습니다. 결과는 제안된 접근 방식이 MIS의 제한된 움직임 계획 문제를 해결하는 데 효과적임을 보여주며, 정밀하고 자율적인 내시경 위치 지정 및 시각 추적을 가능하게 합니다.

## 핵심 내용
최소 침습 수술(MIS)은 좁은 접근 포트로 인한 제한된 시야와 움직임 범위로 인해 외과의사에게 어려운 과제입니다. 이러한 문제는 로봇 보조 내시경 시스템을 통해 해결할 수 있으며, 이 시스템은 정밀하고 안정적인 위치 지정과 함께 내시경의 제한적이고 부드러운 움직임 제어를 제공합니다. 본 연구에서는 MIS에서 내시경의 시각 서보 제어를 위한 온라인 계층적 최적화 프레임워크를 제안합니다. 이 프레임워크는 조직 손상을 방지하기 위해 원격 중심 움직임(RCM) 제약 조건을 유지하는 것을 우선시하며, 관심 시각 특징의 자율 추적을 가능하게 하기 위해 시각 추적 작업을 보조 작업으로 정의합니다. 우리는 6자유도 Denso VS050 매니퓰레이터를 사용하여 접근 방식을 검증했으며, 최적화 해결 시간이 0.4ms 미만이고 최대 RCM 편차가 약 0.4mm임을 달성했습니다. 결과는 제안된 접근 방식이 MIS의 제한된 움직임 계획 문제를 해결하는 데 효과적임을 보여주며, 정밀하고 자율적인 내시경 위치 지정 및 시각 추적을 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2406.09982v1
