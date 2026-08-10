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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.09982v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (668 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2406.09982v1

## 개요
최소 침습 수술에서 시야 제한과 운동 범위 제한이라는 도전 과제를 해결하기 위해, 본 논문은 내시경의 시각 서보 제어를 위한 온라인 계층적 최적화 프레임워크를 제안한다. 이 프레임워크는 계층적 이차 계획법을 통해 원격 운동 중심 제약을 최우선 과제로 설정하여 내시경 운동이 조직을 손상시키지 않도록 보장하고, 동시에 시각 특징 추적을 부차적 과제로 설정하여 자율 추적을 구현한다. 6자유도 Denso VS050 로봇 팔에서의 검증 결과, 이 프레임워크의 최적화 해석 시간은 0.4밀리초 미만이며, RCM 최대 편차는 약 0.4밀리미터로, 정밀한 자율 위치 결정 및 시각 추적에서의 효과성을 입증한다.

## 핵심 내용
### 방법
- 최소 침습 수술에서 내시경의 시각 서보 제어를 위한 계층적 이차 계획법(Hierarchical Quadratic Programming, HQP) 기반 온라인 최적화 프레임워크를 제안한다.
- 프레임워크는 원격 운동 중심(RCM) 제약을 최우선 과제로 설정하여 내시경 운동이 조직을 손상시키지 않도록 보장하고, 시각 특징 추적을 부차적 과제로 설정하여 자율 추적을 구현한다.

### 아키텍처
- 계층적 최적화 구조를 채택하여 높은 우선순위 제약(RCM)을 먼저 충족시키고, 낮은 우선순위 작업(시각 추적)을 처리한다.
- 이차 계획법 솔버를 사용하여 최적화 문제를 온라인으로 해석하여 실시간성을 보장한다.

### 실험 설정
- 6자유도 Denso VS050 로봇 팔을 사용하여 검증한다.
- 실험 환경은 최소 침습 수술 시나리오를 모사하며, RCM 제약 유지 및 시각 추적 성능을 평가한다.

### 주요 수치
- 최적화 해석 시간은 0.4밀리초 미만으로 실시간 제어 요구를 충족한다.
- 최대 RCM 편차는 약 0.4밀리미터로 제약 유지 정밀도가 높음을 나타낸다.

### 결론
- 이 방법은 최소 침습 수술에서의 제약 운동 계획 문제를 효과적으로 해결하여 정밀하고 자율적인 내시경 위치 결정 및 시각 추적을 구현한다.
- 실험 결과는 프레임워크의 실시간성과 정밀도에서의 효과성을 검증하며, 로봇 보조 내시경 시스템에 실행 가능한 솔루션을 제공한다.
