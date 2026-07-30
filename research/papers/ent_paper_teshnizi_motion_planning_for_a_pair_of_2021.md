---
$id: ent_paper_teshnizi_motion_planning_for_a_pair_of_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Planning for a Pair of Tethered Robots
  zh: 一对系留机器人的运动规划
  ko: 테더링된 두 로봇의 동작 계획
summary:
  en: Proposes a reduced-visibility-graph A* planning algorithm for two planar point robots connected by a finite-length cable,
    proving that an optimal solution can always be found on the reduced visibility graph and reducing trajectory existence
    to path search.
  zh: 本文提出了一种针对由有限长度缆绳连接的两个平面点机器人的运动规划算法，基于简化可见图（reduced visibility graph）与A*搜索。核心贡献在于证明了最优解总能在简化可见图上找到，并将轨迹存在性问题简化为路径搜索问题。
  ko: 유한 길이 케이블로 연결된 두 평면 점 로봇을 위해 축소 가시성 그래프 기반 A* 계획 알고리즘을 제안하고, 최적 해가 항상 축소 가시성 그래프 상에서 찾아질 수 있음을 증명하여 궤적 존재 문제를 경로 탐색으로
    환원한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- tethered_robots
- motion_planning
- multi_robot_coordination
- visibility_graph
- a_star
- cable_constrained_planning
- homotopy
- trajectory_planning
- extreme_terrain_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2102.13212v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Motion Planning for a Pair of Tethered Robots
  url: https://arxiv.org/abs/2102.13212
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究针对多边形障碍物环境中，两个通过有限长度缆绳连接的平面点机器人的运动规划问题。与单个机器人通过缆绳连接固定基座的先前工作类似，直线视线可见性在此起关键作用。本文展示了简化可见图如何为双机器人情况提供自然的离散化，并有效捕捉核心拓扑考量。然而，与单机器人情况不同，有限缆绳长度引入了协调（或从集中式规划器角度看，相对时序）方面的考量，使问题复杂化。为此，论文引入了比先前单机器人工作更复杂的形式化方法，以建立核心理论结果——一个允许将问题转化为路径搜索而非轨迹搜索的定理。一旦确认，规划问题简化为直接的图搜索，并带有优雅的缆绳表示，仅需少量额外辅助检查来确保缆绳长度足以保证解的可行性。

## 核心内容
### 问题定义
- 环境：包含多边形障碍物的二维平面。
- 机器人：两个平面点机器人（planar point robots），通过有限长度缆绳连接。
- 目标：规划两个机器人的运动，使其从起始位置移动到目标位置，同时避免与障碍物碰撞，并满足缆绳长度约束。

### 核心方法
- **简化可见图（Reduced Visibility Graph）**：论文证明，最优解总能在简化可见图上找到。该图通过捕捉障碍物顶点间的可见性关系，为问题提供自然离散化。
- **理论定理**：通过引入比单机器人情况更复杂的形式化，建立核心定理，将轨迹存在性问题转化为路径搜索问题。这意味着规划问题从连续时间轨迹规划简化为离散图上的路径搜索。
- **A*搜索实现**：基于简化可见图实现A*搜索算法。搜索过程中，通过优雅的缆绳表示（如缆绳长度作为状态的一部分）和少量辅助检查（如确保缆绳长度足以连接路径上的点），保证解的可行性。

### 实验设置与结果
- 实验环境：包含多边形障碍物的测试场景。
- 算法性能：报告了A*搜索的实验结果，验证了算法在多种障碍物配置下的有效性。
- 最优执行：论文还规定了算法所提供解的最优执行方式，确保实际运动满足缆绳约束。

### 结论
本文成功将双机器人缆绳运动规划问题简化为图搜索，证明了简化可见图在该问题中的有效性，并通过A*搜索实现了高效求解。

## Overview
Considering an environment containing polygonal obstacles, we address the problem of planning motions for a pair of planar robots connected to one another via a cable of limited length. Much like prior problems with a single robot connected via a cable to a fixed base, straight line-of-sight visibility plays an important role. The present paper shows how the reduced visibility graph provides a natural discretization and captures the essential topological considerations very effectively for the two robot case as well. Unlike the single robot case, however, the bounded cable length introduces considerations around coordination (or equivalently, when viewed from the point of view of a centralized planner, relative timing) that complicates the matter. Indeed, the paper has to introduce a rather more involved formalization than prior single-robot work in order to establish the core theoretical result -- a theorem permitting the problem to be cast as one of finding paths rather than trajectories. Once affirmed, the planning problem reduces to a straightforward graph search with an elegant representation of the connecting cable, demanding only a few extra ancillary checks that ensure sufficiency of cable to guarantee feasibility of the solution. We describe our implementation of A${}^\star$ search, and report experimental results. Lastly, we prescribe an optimal execution for the solutions provided by the algorithm.

## 개요
다각형 장애물이 포함된 환경에서, 제한된 길이의 케이블로 서로 연결된 두 대의 평면 로봇의 움직임을 계획하는 문제를 다룹니다. 고정된 베이스에 케이블로 연결된 단일 로봇 문제와 마찬가지로, 직선 가시선(line-of-sight) 가시성이 중요한 역할을 합니다. 본 논문은 축소 가시성 그래프(reduced visibility graph)가 자연스러운 이산화를 제공하고, 두 로봇의 경우에도 핵심적인 위상적 고려 사항을 효과적으로 포착함을 보여줍니다. 그러나 단일 로봇의 경우와 달리, 제한된 케이블 길이는 조정(또는 중앙 집중식 계획자의 관점에서 볼 때 상대적 타이밍)에 대한 고려를 도입하여 문제를 복잡하게 만듭니다. 실제로, 본 논문은 핵심 이론적 결과(문제를 궤적(trajectory)이 아닌 경로(path) 찾기로 전환할 수 있게 하는 정리)를 확립하기 위해 이전 단일 로봇 연구보다 훨씬 더 복잡한 형식화를 도입해야 합니다. 이 정리가 확립되면, 계획 문제는 연결 케이블의 우아한 표현과 함께 간단한 그래프 탐색으로 축소되며, 솔루션의 실행 가능성을 보장하기 위해 케이블의 충분성을 확인하는 몇 가지 추가 보조 검사만 필요합니다. 우리는 A${}^\star$ 탐색의 구현을 설명하고 실험 결과를 보고합니다. 마지막으로, 알고리즘이 제공하는 솔루션에 대한 최적 실행을 제시합니다.

## 핵심 내용
다각형 장애물이 포함된 환경에서, 제한된 길이의 케이블로 서로 연결된 두 대의 평면 로봇의 움직임을 계획하는 문제를 다룹니다. 고정된 베이스에 케이블로 연결된 단일 로봇 문제와 마찬가지로, 직선 가시선(line-of-sight) 가시성이 중요한 역할을 합니다. 본 논문은 축소 가시성 그래프(reduced visibility graph)가 자연스러운 이산화를 제공하고, 두 로봇의 경우에도 핵심적인 위상적 고려 사항을 효과적으로 포착함을 보여줍니다. 그러나 단일 로봇의 경우와 달리, 제한된 케이블 길이는 조정(또는 중앙 집중식 계획자의 관점에서 볼 때 상대적 타이밍)에 대한 고려를 도입하여 문제를 복잡하게 만듭니다. 실제로, 본 논문은 핵심 이론적 결과(문제를 궤적(trajectory)이 아닌 경로(path) 찾기로 전환할 수 있게 하는 정리)를 확립하기 위해 이전 단일 로봇 연구보다 훨씬 더 복잡한 형식화를 도입해야 합니다. 이 정리가 확립되면, 계획 문제는 연결 케이블의 우아한 표현과 함께 간단한 그래프 탐색으로 축소되며, 솔루션의 실행 가능성을 보장하기 위해 케이블의 충분성을 확인하는 몇 가지 추가 보조 검사만 필요합니다. 우리는 A${}^\star$ 탐색의 구현을 설명하고 실험 결과를 보고합니다. 마지막으로, 알고리즘이 제공하는 솔루션에 대한 최적 실행을 제시합니다.

## 参考
- http://arxiv.org/abs/2102.13212v1
