---
$id: ent_paper_ye_energy_based_policy_orchestrat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Energy-Based Policy Orchestration
  zh: Energy-Based Policy Orchestration
  ko: Energy-Based Policy Orchestration
summary:
  en: Hierarchical control scales robot behavior by separating task-level planning from low-level control. In dynamic, high-dimensional
    tasks, however, a fixed planner-to-policy interface can fail when contacts, balance, or disturbances evolve faster than
    high-level policy updates. Execution therefore requires choosing not only which low-level policy to run, but also which
    policy-specific goal should ...
  zh: EPO 是一种基于能量的策略编排器，由 Weirui Ye、Yen-Jen Wang、Elvis Hsieh、Zhiyang Dou、Shibo Zhao、Pieter Abbeel、Yilun Du、Leslie Pack Kaelbling
    等人提出，用于模块化目标条件策略族。它为每个策略学习一个关于低层目标的复合能量函数，运行时细化各策略目标并执行能量最低的策略-目标对，从而在跟踪规划目标的同时提升可行性。仿真中该方法改善了精度-鲁棒性权衡，并在真实人形机器人 loco-manipulation
    任务上完成了同一套冻结策略与能量模型的 sim-to-real 部署。
  ko: Hierarchical control scales robot behavior by separating task-level planning from low-level control. In dynamic, high-dimensional
    tasks, however, a fixed planner-to-policy interface can fail when contacts, balance, or disturbances evolve faster than
    high-level policy updates. Execution therefore requires choosing not only which low-level policy to run, but also which
    policy-specific goal should ...
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
- policy_orchestration
- energy_based_model
- hierarchical_control
- humanoid_loco_manipulation
- sim_to_real
- goal_conditioned_policy
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.02546);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.02546 Energy-Based Policy Orchestration
  url: https://arxiv.org/abs/2611.02546
  date: '2026-11-02'
  accessed_at: '2026-11-09'
---

## 概述

分层控制通过将任务级规划与低层控制分离来扩展机器人行为规模，但在动态高维任务中，固定的规划器到策略接口容易失效，因为接触、平衡或扰动可能比高层策略更新更快地变化。执行时不仅需要选择运行哪个低层策略，还需要决定给该策略设定哪个策略专属目标。作者将这一问题形式化为策略编排，即运行时选择一个既可能保持可行、又能跟踪规划器目标的策略-目标对。为此提出 EPO，为每个目标条件策略学习一个关于低层目标的复合能量，能量越低表示可行性越高、目标实现越准确。运行时 EPO 细化每个策略的目标并执行能量最低的策略-目标对；由于能量是策略专属的，新策略只需学习自身能量模型即可接入，无需重训已有策略或集中式调度器。

## 核心内容

### 问题背景
分层控制把任务级规划与低层控制分离，是扩展机器人行为规模的常用手段。但在动态、高维任务中，固定的规划器到策略接口可能失效：接触、平衡或扰动变化的速度可能快于高层策略的更新频率。此时执行阶段面临两个耦合决策——运行哪个低层策略，以及向该策略下达哪个策略专属目标。作者将这一运行时选择问题称为 policy orchestration（策略编排），目标是选出既可能保持可行、又能跟踪规划器目标的策略-目标对。

### 方法
- 面向模块化的目标条件策略族，提出 EPO（energy-based policy orchestrator）。
- 为每个策略学习一个关于低层目标的复合能量函数，能量越低对应可行性越高、目标实现越准确。
- 运行时先细化每个策略的目标，再依据能量分数选择并执行能量最低的策略-目标对。
- 能量模型是策略专属的，因此新增策略只需学习自己的能量模型，无需重新训练已有策略，也无需集中式调度器。

### 实验设置与关键结果
- 在仿真中评估，EPO 通过在策略间基于能量分数选择性切换之前细化策略专属目标，改善了经验上的精度-鲁棒性权衡。
- 进一步在真实人形机器人 loco-manipulation 任务上演示了 sim-to-real 部署，使用的是同一套冻结的策略与能量模型。

### 结论
将执行期的策略选择与目标细化统一为基于能量的策略编排，可在不重训已有策略的前提下支持策略族的模块化扩展，并在仿真与真实人形机器人任务上验证了可行性。

## Overview

Hierarchical control scales robot behavior by separating task-level planning from low-level control. In dynamic, high-dimensional tasks, however, a fixed planner-to-policy interface can fail when contacts, balance, or disturbances evolve faster than high-level policy updates. Execution therefore requires choosing not only which low-level policy to run, but also which policy-specific goal should be given to it. We formulate this problem as policy orchestration: runtime selection of a policy-goal pair that is likely to remain feasible while tracking the planner target. We develop EPO, an energy-based policy orchestrator for modular goal-conditioned policy families. For each policy, EPO learns a composite energy over low-level goals, where lower energy corresponds to higher feasibility and more accurate target realization. At runtime, EPO refines each policy's goal and executes the lowest-energy policy-goal pair. Because energies are policy-specific, new policies can be incorporated by learning their own energy models, without retraining the existing policies or a centralized scheduler. In simulation, EPO improves the empirical precision-robustness trade-off by refining policy-specific goals before selectively switching among policies based on energy scores. We further demonstrate sim-to-real deployment of the same frozen policies and energy models on real humanoid loco-manipulation tasks. Project website: https://yewr.github.io/epo

## 参考
- https://arxiv.org/abs/2611.02546
