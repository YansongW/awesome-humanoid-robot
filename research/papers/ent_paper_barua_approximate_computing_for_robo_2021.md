---
$id: ent_paper_barua_approximate_computing_for_robo_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Approximate Computing for Robotic Path Planning: Experimentation, Case Study
    and Practical Implications'
  zh: 机器人路径规划中的近似计算：实验、案例研究与实际意义
  ko: '로봇 경로 계획을 위한 근사 컴퓨팅: 실험, 사례 연구 및 실용적 함의'
summary:
  en: This paper applies loop perforation to approximate the A* path planning algorithm
    for battery-driven mobile warehouse robots, and demonstrates that individually
    safe approximations can cause inter-robot collisions in collaborative multi-robot
    fleets.
  zh: 本文将循环穿孔应用于电池供电的移动仓库机器人A*路径规划算法的近似化，并证明在单机器人层面安全的近似在多机器人协同环境中可能引发机器人间碰撞。
  ko: 본 논문은 배터리 구동의 이동식 창고 로봇을 위한 A* 경로 계획 알고리즘을 근사화하기 위해 루프 퍼포레이션을 적용하고, 개별 로봇에게는
    안전한 근사가 협업 다중 로봇 군집에서 로봇 간 충돌을 유발할 수 있음을 보여준다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- approximate_computing
- loop_perforation
- a_star
- path_planning
- multi_robot_coordination
- energy_aware_control
- warehouse_robots
- safety
- graph_search
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata, abstract, and supplied paper summary; requires
    human review of the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Approximate Computing for Robotic path planning - Experimentation, Case Study
    and Practical Implications
  url: https://arxiv.org/abs/2104.05773
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Approximate computing trades time and energy for output quality, making it attractive for battery-driven embedded systems such as robots. The paper investigates whether this trade-off remains safe when multiple robots share a workspace and each robot's path planner is individually approximated. The authors apply loop perforation to the A* search algorithm and measure the resulting speedup, path-length deviation, and collision behavior in simulated warehouse and room scenarios.

The experiments show that, although each approximated path avoids static obstacles (e.g., warehouse racks), the fleet can still suffer inter-robot collisions. For the selected perforation rates, the authors report speedups of roughly 2.7–3.2× and collision rates of 5–20% in warehouse scenarios. Task assignment is handled by the Hungarian Method under a simplified single-task single-robot model.

The central takeaway is that per-subsystem approximation is insufficient in collaborative robotics: a system-aware, controlled approximation strategy is needed to harness energy savings without compromising fleet-wide safety.

## Key Contributions

- Demonstrates that approximate computing in multi-robot path planning can cause collisions even when each robot's planned path avoids static obstacles.
- Applies loop perforation to A* and empirically selects perforation rates that balance speedup against path-quality degradation.
- Quantifies collision rates of 5–20% and speedups of approximately 2.7–3.2× for chosen perforation rates in warehouse scenarios.
- Argues for controlled, system-aware approximation rather than isolated per-subsystem approximation in collaborative robotics.

## Relevance to Humanoid Robotics

Although the experiments use mobile warehouse robots on 2-D grids, the safety argument generalizes to any collaborative multi-robot fleet, including humanoid robot swarms. Humanoid platforms are especially likely to use approximate computing to extend battery life for perception, planning, and control, but this work warns that locally safe approximations can combine into globally unsafe behavior. The paper therefore supports the knowledge-base goal of capturing energy-aware control and safe coordination methods for humanoid systems.
