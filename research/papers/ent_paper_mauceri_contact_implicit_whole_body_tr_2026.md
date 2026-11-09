---
$id: ent_paper_mauceri_contact_implicit_whole_body_tr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain
  zh: Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain
  ko: Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain
summary:
  en: This letter presents a trajectory planner for humanoid robots to perform dynamic motions on complex, parameterizable
    terrains using a contact-implicit whole-body optimization framework. The planner generates feasible movements without
    predefined contact sequences, considering the robot's full dynamics and kinematics. To plan bipedal locomotion on steps,
    ramps, and other terrains, we propose a ...
  zh: 本文提出一种面向人形机器人的轨迹规划器，采用接触隐式全身优化框架，使机器人能够在复杂且可参数化的地形上完成动态运动。该规划器无需预先给定接触序列，即可在考虑完整动力学与运动学的前提下生成可行运动。作者提出用光滑曲面近似地面几何的数学模型，并通过新的接触约束将刚体交互建模从平坦水平面推广到任意光滑曲面，在仿真与真实机器人
    ErgoCub 上完成了非共面地形上的初步可行性测试。
  ko: This letter presents a trajectory planner for humanoid robots to perform dynamic motions on complex, parameterizable
    terrains using a contact-implicit whole-body optimization framework. The planner generates feasible movements without
    predefined contact sequences, considering the robot's full dynamics and kinematics. To plan bipedal locomotion on steps,
    ramps, and other terrains, we propose a ...
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
- humanoid_locomotion
- contact_implicit_optimization
- whole_body_trajectory_optimization
- uneven_terrain
- nonlinear_programming
- ergocub
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.05585);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.05585 Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable
    Uneven Terrain
  url: https://arxiv.org/abs/2611.05585
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

该工作由 Roberto Mauceri、Stefano Dafarra、Giulio Romualdi、Marco Gabiccini 与 Daniele Pucci 完成，目标是让人形机器人在台阶、斜坡等复杂且可参数化的地形上执行动态运动。其核心是一个接触隐式全身轨迹规划框架，不依赖预先定义的接触序列，同时考虑机器人的完整动力学与运动学。为处理非平坦地面，作者提出以光滑曲面近似地面几何的数学模型，并设计新的接触约束来描述机器人与地面之间的刚性交互，从而把适用域从平坦水平面扩展到任意光滑曲面。规划问题通过非线性规划求解，并在代价函数与初始猜测中嵌入高层需求以生成动态轨迹；初步可行性测试在非共面地形上分别于仿真环境和真实机器人 ErgoCub 上开展。

## 核心内容

### 问题背景

人形机器人在复杂地形上的动态运动规划通常依赖预先指定的接触序列，这限制了规划器对台阶、斜坡等非平坦地形的适应能力。本文旨在构建一个接触隐式的全身轨迹规划器，在未知接触序列的情况下生成满足完整动力学与运动学约束的可行运动。

### 方法

- **地形建模**：提出一种数学模型，用光滑曲面近似地面几何，从而统一描述台阶、斜坡及其他可参数化地形。
- **接触约束**：设计新的接触约束来刻画机器人与地面之间的刚性交互，将原有方法的适用范围从平坦且水平的地面推广到任意光滑曲面。
- **优化框架**：采用接触隐式全身优化，不预设接触序列；通过非线性规划求解双足运动轨迹。
- **动态轨迹生成**：将高层需求嵌入代价函数与初始猜测中，以生成动态轨迹。

### 实验设置

初步可行性测试在非共面地形上开展，分别在仿真环境与真实机器人 ErgoCub 上进行；规划器在多种地形拓扑上用于生成运动。

### 关键结果

摘要报告了该方法在多种地形拓扑上的规划有效性，并完成了非共面地形上的初步可行性验证，涵盖仿真与实机两个层面。摘要未给出具体量化指标。

### 结论

所提出的接触隐式全身轨迹优化框架能够在无需预定义接触序列的条件下，为可参数化复杂地形上的人形机器人动态运动生成可行轨迹，并通过仿真与 ErgoCub 实机测试初步验证了可行性。

## Overview

This letter presents a trajectory planner for humanoid robots to perform dynamic motions on complex, parameterizable terrains using a contact-implicit whole-body optimization framework. The planner generates feasible movements without predefined contact sequences, considering the robot's full dynamics and kinematics. To plan bipedal locomotion on steps, ramps, and other terrains, we propose a mathematical model to approximate ground geometry with a smooth surface. The rigid interaction between the robot and the ground is modeled via novel contact constraints, extending the domain of applicability from flat and horizontal surfaces to any arbitrary smooth surface. Effectiveness is demonstrated using nonlinear programming to plan motions on various terrain topologies. We also explore dynamic trajectory generation by embedding high-level requirements in the cost function and the initial guess. Preliminary feasibility tests were conducted over non-coplanar terrains, both in simulation and on the real robot ErgoCub.

## 参考
- https://arxiv.org/abs/2611.05585
