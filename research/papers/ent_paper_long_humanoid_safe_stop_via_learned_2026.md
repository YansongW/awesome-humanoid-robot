---
$id: ent_paper_long_humanoid_safe_stop_via_learned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Safe Stop via Learned Stoppability Value
  zh: Humanoid Safe Stop via Learned Stoppability Value
  ko: Humanoid Safe Stop via Learned Stoppability Value
summary:
  en: 'Humanoid robots responding to emergency stop commands typically execute a fixed maneuver, without reasoning about whether
    a safe stop is actually feasible from the current state. We cast emergency stopping as a reach-avoid problem and propose
    Safe-Stop, a task-agnostic framework that pairs a learned stop policy with learned stoppability estimators. The estimators
    are complementary: a ...'
  zh: 本文提出 Safe-Stop，一个面向人形机器人的任务无关紧急停止框架，由学习停止策略与两个互补的可停止性估计器组成。该框架将紧急停止建模为可达-避免问题，通过估计器一致性检查决定是否执行停止或切换至阻尼回退策略，且无需针对上游任务重新训练。
  ko: 'Humanoid robots responding to emergency stop commands typically execute a fixed maneuver, without reasoning about whether
    a safe stop is actually feasible from the current state. We cast emergency stopping as a reach-avoid problem and propose
    Safe-Stop, a task-agnostic framework that pairs a learned stop policy with learned stoppability estimators. The estimators
    are complementary: a ...'
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
- humanoid_robots
- emergency_stop
- reach_avoid
- hamilton_jacobi
- safe_control
- task_agnostic
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.02358);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.02358 Humanoid Safe Stop via Learned Stoppability Value
  url: https://arxiv.org/abs/2609.02358
  date: '2026-09-02'
  accessed_at: '2026-09-07'
---

## 概述

Safe-Stop 由 Junfeng Long 等人提出，旨在解决人形机器人在收到紧急停止命令时无法判断当前状态是否安全可停的问题。其核心创新在于将停止决策转化为可达-避免问题，并训练两个互补的估计器：一个监督学习停止策略的实际结果，另一个基于 Hamilton-Jacobi 备份提供物理状态的可恢复性信号。由于停止策略与估计器不依赖停止命令前的行为策略，因此可跨任务迁移。部署时，仅当两个估计器均认为停止可行时才执行停止，否则切换至阻尼回退策略，从而在保证鲁棒性的同时不牺牲反应速度。

## 核心内容

### 问题背景
传统人形机器人在收到紧急停止命令时，通常执行固定动作，而不考虑从当前状态是否真的能安全停下。这种缺乏推理的做法可能导致危险后果。本文将紧急停止形式化为可达-避免问题，即判断是否存在一条轨迹使机器人达到停止状态并避开障碍。

### 方法
Safe-Stop 框架包含三个核心组件：
- **学习停止策略**：一个任务无关的策略，用于执行停止动作。
- **停止概率估计器**：监督学习自固定停止策略的实际结果，捕捉学习控制器的涌现停止行为。
- **可达-避免估计器**：基于物理状态的 Hamilton-Jacobi 备份进行监督，提供互补的可恢复性信号。

由于停止策略与两个估计器均不依赖停止命令之前的行为策略，它们可以在不同上游任务间直接迁移，无需重新训练。

### 部署决策
在部署时，两个估计器的输出被结合：仅当两者均指示停止仍可行时，Safe-Stop 才执行停止；否则，将控制权交给回退策略，该策略被实例化为阻尼回退。这种一致性检查机制使决策既鲁棒又保持反应性。

### 结论
Safe-Stop 通过将停止可行性显式建模并引入互补估计器，为人形机器人的紧急停止提供了更安全、更智能的决策框架，且具备良好的任务泛化能力。

## Overview

Humanoid robots responding to emergency stop commands typically execute a fixed maneuver, without reasoning about whether a safe stop is actually feasible from the current state. We cast emergency stopping as a reach-avoid problem and propose Safe-Stop, a task-agnostic framework that pairs a learned stop policy with learned stoppability estimators. The estimators are complementary: a stop-probability estimator supervised by the actual outcomes of the fixed stop policy, and a reach-avoidance estimator supervised by a Hamilton-Jacobi backup over physical state. The first captures emergent stopping behavior of the learned controller; the second provides a complementary recoverability signal. Because the stop policy and estimators do not depend on the behavior policy that preceded the stop command, they transfer across diverse upstream tasks without retraining. At deployment, the two estimates are combined: Safe-Stop commits to the stop only when both estimators indicate that stopping remains feasible, otherwise it hands off to a fall policy, instantiated as a damping fallback. This agreement check yields decisions that are robust without sacrificing reactivity.

## 参考
- https://arxiv.org/abs/2609.02358
