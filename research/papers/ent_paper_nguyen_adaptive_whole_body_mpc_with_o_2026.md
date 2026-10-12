---
$id: ent_paper_nguyen_adaptive_whole_body_mpc_with_o_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads
  zh: Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads
  ko: Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads
summary:
  en: 'Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads.
    However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We
    propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predictive
    controller (MPC) that generates ...'
  zh: 该论文提出一种面向人形机器人的自适应全身控制架构，用于在负载未知且变化的情况下完成举升与搬运任务。作者为 Manh Cuong Nguyen 等人，核心由质心 MPC、自适应模糊平衡控制器与基于航路点的姿态规划器三部分组成。仿真与硬件实验表明，相比非自适应基线，该框架提升了平衡鲁棒性并减轻了姿态切换与举升过程中的跟踪性能退化。
  ko: 'Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads.
    However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We
    propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predictive
    controller (MPC) that generates ...'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_robotics
- whole_body_control
- model_predictive_control
- adaptive_control
- posture_planning
- payload_uncertainty
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.12972);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.12972 Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads
  url: https://arxiv.org/abs/2610.12972
  date: '2026-10-09'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人在执行举升与物料搬运任务时，必须在负载未知且不断变化的情况下保持平衡，而负载不确定性会显著影响全身动力学，甚至使常规控制器失稳。为此，作者提出一种自适应全身控制架构，将三部分整合在一起：生成动态可行参考运动的质心模型预测控制器、通过支撑腿关节分配修正力矩来补偿负载引起模型失配的自适应模糊平衡控制器，以及基于三重积分模型、满足质心稳定性约束与关节限制的航路点最优姿态规划器。三者协同使机器人能够在显著负载不确定性下稳定完成下放、抓取、举升、搬运与放置等行为。仿真与硬件实验显示，该框架在姿态切换和举升任务中相比非自适应基线具有更好的平衡鲁棒性，并减少了跟踪性能的退化。

## 核心内容

### 问题背景
人形机器人在举升和物料搬运场景中，需要面对未知且变化的负载。负载不确定性会显著改变全身动力学特性，使传统控制器面临失稳风险，因此需要一种能够在线补偿模型失配并保持平衡的控制方案。

### 方法
论文提出的自适应全身控制架构由三个组件构成：

- **质心模型预测控制器（centroidal MPC）**：负责生成动态可行的参考运动。
- **自适应模糊平衡控制器**：针对负载引起的模型失配进行补偿，生成修正力矩，并将其分配到支撑腿的各个关节上。
- **基于航路点的最优姿态规划器**：建立在三重积分模型之上，生成平滑的坐起（sit-to-stand）与坐下（stand-to-sit）轨迹，同时满足质心（CoM）稳定性约束、关节限制以及全身可行性要求。

三个组件协同工作，使机器人能够在显著负载不确定性下稳定执行下放、抓取、举升、搬运和放置等行为。

### 实验与结果
论文通过大量仿真与硬件实验进行验证。结果表明，与非自适应基线相比，所提框架在姿态切换和举升任务中提升了平衡鲁棒性，并减轻了跟踪性能的退化。

### 结论
将质心 MPC、自适应模糊平衡控制与航路点最优姿态规划相结合，可有效应对负载不确定性对人形机器人全身动力学的影响，从而支持稳定的举升与搬运作业。

## Overview

Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predictive controller (MPC) that generates dynamically feasible reference motions, (ii) an adaptive fuzzy balance controller that compensates for payload-induced model mismatch by generating corrective torques distributed across the supporting-leg joints, and (iii) a waypoint-based optimal posture planner built on a triple-integrator model that produces smooth sit-to-stand and stand-to-sit trajectories satisfying center-of-mass (CoM) stability constraints, joint limits, and whole-body feasibility requirements. Together, these components enable stable lowering, grasping, lifting, carrying, and placing behaviors under significant payload uncertainty. Extensive simulation and hardware experiments demonstrate that the proposed framework improves balance robustness and reduces tracking degradation during posture transitions and lifting tasks compared to non-adaptive baselines.

## 参考
- https://arxiv.org/abs/2610.12972
