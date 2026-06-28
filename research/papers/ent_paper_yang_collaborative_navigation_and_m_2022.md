---
$id: ent_paper_yang_collaborative_navigation_and_m_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collaborative Navigation and Manipulation of a Cable-towed Load by Multiple
    Quadrupedal Robots
  zh: 多四足机器人协同牵引缆绳负载的导航与操作
  ko: 다수의 사족 로봇을 이용한 케이블 견인 하중의 협업 내비게이션 및 조작
summary:
  en: This paper proposes an online cascaded planning framework in which multiple
    quadrupedal robots collaboratively tow a cable-suspended load to a goal while
    avoiding obstacles, combining parallelized centralized hybrid-mode trajectory
    optimization with decentralized per-robot planners.
  zh: 本文提出一种在线级联规划框架，使多台四足机器人协同牵引缆绳负载抵达目标并实时避障，结合并行化的集中式混合模式轨迹优化与单机器人分布式规划器。
  ko: 본 논문은 다수의 사족 로봇이 케이블로 연결된 하중을 목표 지점으로 협업하여 견인하면서 실시간으로 장애물을 회피할 수 있는 온라인 캐스케이드
    계획 프레임워크를 제안하며, 병렬화된 중앙집중식 하이브리드 모드 궤적 최적화와 로봇별 분산 계획기를 결합한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the provided paper metadata and abstract; exact section-level
    citations and hardware details require human review against the PDF.
sources:
- id: src_001
  type: paper
  title: Collaborative Navigation and Manipulation of a Cable-towed Load by Multiple
    Quadrupedal Robots
  url: https://arxiv.org/abs/2206.14424
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper addresses the problem of multiple quadrupedal robots collaboratively towing a cable-attached load to a specified goal while avoiding obstacles in real time. Because the cable can switch between slack and taut modes, the team can reconfigure its effective shape to pass through narrow spaces, but these hybrid transitions together with coupled robot-load dynamics make online planning difficult. The authors introduce a cascaded autonomy architecture that handles these challenges without requiring offline computation.

At the top level, an A* planner generates a global path, while a parallelized centralized trajectory optimizer reasons over hybrid slack/taut cable modes for the team. At the lower level, each robot runs its own decentralized optimization-based planner that tracks the centralized trajectory, avoids obstacles, and maintains safe separation from other robots and the load. The planners share a layered cost-map representation and run onboard the robots using current sensor feedback.

Experiments are conducted with teams of up to three Mini Cheetah and Unitree A1 quadrupeds towing payloads too heavy for a single robot. The demonstrations include traversal of narrow gaps, diagonal gaps, and cluttered environments, validating real-time reactive planning and collaborative transport.

## Key Contributions

- Real-time collaborative autonomy framework for cable-towed load manipulation with multiple quadrupedal robots.
- Parallelized centralized trajectory optimization that explicitly handles hybrid slack/taut cable mode switches online.
- Decentralized optimization-based planners per robot for reactive trajectory tracking, obstacle avoidance, and collision avoidance with teammates and the load.
- Experimental validation on teams of three quadrupedal robots navigating narrow gaps, diagonal gaps, and cluttered spaces with heavy loads.

## Relevance to Humanoid Robotics

Although the paper focuses on quadrupedal platforms, the core capabilities—multi-robot collaborative manipulation, hybrid contact planning, and decentralized reactive control for heavy-payload transport—are directly relevant to future humanoid robot fleets. Humanoid mass production and industrial deployment will likely require teams of legged robots to coordinate material handling, logistics, and load relocation in cluttered or narrow factory and warehouse environments. The cascaded planning approach and the handling of cable-based coupling provide a transferable template for coordinating mixed teams of humanoids and other legged systems in such workflows.
