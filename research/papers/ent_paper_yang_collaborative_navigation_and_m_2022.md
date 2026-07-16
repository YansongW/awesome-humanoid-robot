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
  zh: This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while
    avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel
    through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is
    a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load.
    Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.14424v1.
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
This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load. Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In this paper, we introduce a cascaded planning scheme with a parallelized centralized trajectory optimization that deals with hybrid mode switches. We additionally develop a set of decentralized planners per robot, which enables our approach to solve the problem of collaborative load manipulation online. We develop and demonstrate one of the first collaborative autonomy framework that is able to move a cable-towed load, which is too heavy to move by a single robot, through narrow spaces with real-time feedback and reactive planning in experiments.

## 核心内容
This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load. Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In this paper, we introduce a cascaded planning scheme with a parallelized centralized trajectory optimization that deals with hybrid mode switches. We additionally develop a set of decentralized planners per robot, which enables our approach to solve the problem of collaborative load manipulation online. We develop and demonstrate one of the first collaborative autonomy framework that is able to move a cable-towed load, which is too heavy to move by a single robot, through narrow spaces with real-time feedback and reactive planning in experiments.

## 参考
- http://arxiv.org/abs/2206.14424v1

## Overview
This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load. Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In this paper, we introduce a cascaded planning scheme with a parallelized centralized trajectory optimization that deals with hybrid mode switches. We additionally develop a set of decentralized planners per robot, which enables our approach to solve the problem of collaborative load manipulation online. We develop and demonstrate one of the first collaborative autonomy framework that is able to move a cable-towed load, which is too heavy to move by a single robot, through narrow spaces with real-time feedback and reactive planning in experiments.

## Content
This paper tackles the problem of robots collaboratively towing a load with cables to a specified goal location while avoiding collisions in real time. The introduction of cables (as opposed to rigid links) enables the robotic team to travel through narrow spaces by changing its intrinsic dimensions through slack/taut switches of the cable. However, this is a challenging problem because of the hybrid mode switches and the dynamical coupling among multiple robots and the load. Previous attempts at addressing such a problem were performed offline and do not consider avoiding obstacles online. In this paper, we introduce a cascaded planning scheme with a parallelized centralized trajectory optimization that deals with hybrid mode switches. We additionally develop a set of decentralized planners per robot, which enables our approach to solve the problem of collaborative load manipulation online. We develop and demonstrate one of the first collaborative autonomy framework that is able to move a cable-towed load, which is too heavy to move by a single robot, through narrow spaces with real-time feedback and reactive planning in experiments.

## 개요
본 논문은 로봇들이 케이블을 이용해 협력하여 화물을 지정된 목표 위치로 견인하면서 실시간으로 충돌을 회피하는 문제를 다룹니다. 케이블(강체 링크와 달리)을 도입함으로써 로봇 팀은 케이블의 느슨함/팽팽함 전환을 통해 내부 치수를 변경하여 좁은 공간을 통과할 수 있습니다. 그러나 이는 하이브리드 모드 전환과 여러 로봇 및 화물 간의 동적 결합으로 인해 도전적인 문제입니다. 이전의 이러한 문제 해결 시도는 오프라인에서 수행되었으며 온라인 장애물 회피를 고려하지 않았습니다. 본 논문에서는 하이브리드 모드 전환을 처리하는 병렬화된 중앙 집중식 궤적 최적화를 포함한 계층적 계획 방식을 도입합니다. 또한 로봇별 분산 계획기를 추가로 개발하여 협력적 화물 조작 문제를 온라인으로 해결할 수 있게 합니다. 우리는 단일 로봇으로는 이동하기 너무 무거운 케이블 견인 화물을 실시간 피드백과 반응형 계획을 통해 좁은 공간으로 이동할 수 있는 최초의 협력 자율성 프레임워크 중 하나를 개발하고 실험에서 시연합니다.

## 핵심 내용
본 논문은 로봇들이 케이블을 이용해 협력하여 화물을 지정된 목표 위치로 견인하면서 실시간으로 충돌을 회피하는 문제를 다룹니다. 케이블(강체 링크와 달리)을 도입함으로써 로봇 팀은 케이블의 느슨함/팽팽함 전환을 통해 내부 치수를 변경하여 좁은 공간을 통과할 수 있습니다. 그러나 이는 하이브리드 모드 전환과 여러 로봇 및 화물 간의 동적 결합으로 인해 도전적인 문제입니다. 이전의 이러한 문제 해결 시도는 오프라인에서 수행되었으며 온라인 장애물 회피를 고려하지 않았습니다. 본 논문에서는 하이브리드 모드 전환을 처리하는 병렬화된 중앙 집중식 궤적 최적화를 포함한 계층적 계획 방식을 도입합니다. 또한 로봇별 분산 계획기를 추가로 개발하여 협력적 화물 조작 문제를 온라인으로 해결할 수 있게 합니다. 우리는 단일 로봇으로는 이동하기 너무 무거운 케이블 견인 화물을 실시간 피드백과 반응형 계획을 통해 좁은 공간으로 이동할 수 있는 최초의 협력 자율성 프레임워크 중 하나를 개발하고 실험에서 시연합니다.
