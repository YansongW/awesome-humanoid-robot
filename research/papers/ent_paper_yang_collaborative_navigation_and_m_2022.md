---
$id: ent_paper_yang_collaborative_navigation_and_m_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collaborative Navigation and Manipulation of a Cable-towed Load by Multiple Quadrupedal Robots
  zh: 多四足机器人协同牵引缆绳负载的导航与操作
  ko: 다수의 사족 로봇을 이용한 케이블 견인 하중의 협업 내비게이션 및 조작
summary:
  en: This paper proposes an online cascaded planning framework in which multiple quadrupedal robots collaboratively tow a
    cable-suspended load to a goal while avoiding obstacles, combining parallelized centralized hybrid-mode trajectory optimization
    with decentralized per-robot planners.
  zh: 本文提出一种在线级联规划框架，使多台四足机器人协作拖拽缆绳悬挂负载到达目标，同时避开障碍物。该框架结合了并行化集中式混合模式轨迹优化与分散式单机器人规划器，首次实现实时反应式规划下的缆绳拖拽负载协同操作。
  ko: 본 논문은 다수의 사족 로봇이 케이블로 연결된 하중을 목표 지점으로 협업하여 견인하면서 실시간으로 장애물을 회피할 수 있는 온라인 캐스케이드 계획 프레임워크를 제안하며, 병렬화된 중앙집중식 하이브리드 모드 궤적
    최적화와 로봇별 분산 계획기를 결합한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_collaboration
- quadruped_robots
- cable_towed_load
- trajectory_optimization
- hybrid_mode_switching
- decentralized_planning
- obstacle_avoidance
- heavy_payload_transport
- online_planning
- reactive_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.14424v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (607 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Collaborative Navigation and Manipulation of a Cable-towed Load by Multiple Quadrupedal Robots
  url: https://arxiv.org/abs/2206.14424
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
针对多机器人通过缆绳协作拖拽负载并实时避障的问题，本文引入缆绳替代刚性连杆，使机器人团队能通过缆绳松弛/绷紧切换改变整体尺寸，从而穿越狭窄空间。为解决混合模式切换与多机器人-负载动态耦合的挑战，作者提出级联规划方案：包含处理混合模式切换的并行化集中式轨迹优化，以及为每台机器人开发的分散式规划器。实验证明，该框架是首个能实时反馈并反应式规划、使单机器人无法移动的重负载通过狭窄空间的协同自主系统。

## 核心内容
### 核心问题与挑战
- 多机器人通过缆绳协作拖拽负载至指定目标，需实时避障
- 缆绳替代刚性连杆的优势：通过松弛/绷紧切换改变系统整体尺寸，可穿越狭窄空间
- 主要挑战：混合模式切换（缆绳状态变化）与多机器人-负载动态耦合

### 方法架构
- **级联规划框架**：包含两层规划器
  - **并行化集中式轨迹优化**：处理混合模式切换，生成全局轨迹
  - **分散式单机器人规划器**：每台机器人独立运行，实现实时反应式避障

### 实验设置与关键结果
- 首次实现多机器人协作拖拽缆绳负载的实时反应式规划
- 负载重量超过单机器人承载能力，需多机器人协同移动
- 实验验证：系统能在实时反馈下通过狭窄空间，并动态调整缆绳状态（松弛/绷紧）

### 结论
本文提出的框架是首个能在线解决多机器人缆绳拖拽负载避障问题的协同自主系统，通过级联规划与混合模式优化实现实时性能。

## Overview
This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load. Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In this paper, we introduce a cascaded planning scheme with a parallelized centralized trajectory optimization that deals with hybrid mode switches. We additionally develop a set of decentralized planners per robot, which enables our approach to solve the problem of collaborative load manipulation online. We develop and demonstrate one of the first collaborative autonomy framework that is able to move a cable-towed load, which is too heavy to move by a single robot, through narrow spaces with real-time feedback and reactive planning in experiments.

## 参考
- http://arxiv.org/abs/2206.14424v1

## 개요
다중 로봇이 케이블을 통해 협력하여 하중을 견인하고 실시간 장애물 회피를 수행하는 문제에 대해, 본 논문은 강성 링크를 대체하는 케이블을 도입하여 로봇 팀이 케이블의 이완/긴장 전환을 통해 전체 크기를 변경하고 좁은 공간을 통과할 수 있게 한다. 혼합 모드 전환과 다중 로봇-하중 동적 결합의 도전을 해결하기 위해, 저자는 계단식 계획 방안을 제안한다: 혼합 모드 전환을 처리하는 병렬화된 중앙 집중식 궤적 최적화와 각 로봇을 위해 개발된 분산형 계획기를 포함한다. 실험은 이 프레임워크가 단일 로봇이 이동할 수 없는 중하중을 좁은 공간을 통해 통과시키는 실시간 피드백 및 반응형 계획을 가능하게 하는 최초의 협력 자율 시스템임을 증명한다.

## 핵심 내용
### 핵심 문제와 도전
- 다중 로봇이 케이블을 통해 협력하여 하중을 지정된 목표로 견인하며 실시간 장애물 회피 필요
- 강성 링크를 대체하는 케이블의 장점: 이완/긴장 전환을 통해 시스템 전체 크기를 변경하여 좁은 공간 통과 가능
- 주요 도전: 혼합 모드 전환(케이블 상태 변화)과 다중 로봇-하중 동적 결합

### 방법 아키텍처
- **계단식 계획 프레임워크**: 두 계층의 계획기 포함
  - **병렬화된 중앙 집중식 궤적 최적화**: 혼합 모드 전환을 처리하고 전역 궤적 생성
  - **분산형 단일 로봇 계획기**: 각 로봇이 독립적으로 실행되어 실시간 반응형 장애물 회피 구현

### 실험 설정과 주요 결과
- 다중 로봇 협력 케이블 하중 견인의 실시간 반응형 계획 최초 구현
- 하중 무게가 단일 로봇의 운반 능력을 초과하여 다중 로봇 협력 이동 필요
- 실험 검증: 시스템이 실시간 피드백 하에 좁은 공간을 통과하고 케이블 상태(이완/긴장)를 동적으로 조정

### 결론
본 논문에서 제안한 프레임워크는 다중 로봇 케이블 견인 하중 장애물 회피 문제를 온라인으로 해결하는 최초의 협력 자율 시스템이며, 계단식 계획과 혼합 모드 최적화를 통해 실시간 성능을 달성한다.
