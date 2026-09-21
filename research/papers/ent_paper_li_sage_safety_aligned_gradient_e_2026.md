---
$id: ent_paper_li_sage_safety_aligned_gradient_e_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration'
  zh: 'SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration'
  ko: 'SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration'
summary:
  en: 'Multi-party human-robot collaboration poses a dual challenge: robot decisions should remain interpretable and auditable,
    while executed actions must satisfy safety constraints during physical interaction. Combining explainable decision-tree
    policies with control-barrier-function (CBF) filtering provides a promising architecture but creates two learning mismatches
    in multi-agent reinforcement ...'
  zh: SAGE（safety-aligned gradient enforcement）是一种面向多方人机协作的安全对齐梯度强化方法，由 Yisen Li、Hao Zhang、Ruize Geng、Yves Tseng、Ding Zhao、H.
    Eric Tseng 提出。它针对可解释决策树策略与控制屏障函数（CBF）过滤结合时出现的两处学习失配，分别用 SAIL 与 TALO 两个组件加以解决。在九个仿真场景中，SAGE 取得 71.0% 的成功率，每千环境步仅 0.5 次碰撞步。
  ko: 'Multi-party human-robot collaboration poses a dual challenge: robot decisions should remain interpretable and auditable,
    while executed actions must satisfy safety constraints during physical interaction. Combining explainable decision-tree
    policies with control-barrier-function (CBF) filtering provides a promising architecture but creates two learning mismatches
    in multi-agent reinforcement ...'
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
- human_robot_collaboration
- control_barrier_function
- multi_agent_reinforcement_learning
- safety_alignment
- humanoid_robots
- lyapunov_optimization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.21130);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.21130 SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration'
  url: https://arxiv.org/abs/2609.21130
  date: '2026-09-17'
  accessed_at: '2026-09-21'
---

## 概述

多方人机协作要求机器人决策既可解释、可审计，又要在物理交互中满足安全约束。将可解释的决策树策略与控制屏障函数（CBF）过滤结合是一种有前景的架构，但在多智能体强化学习中会引入两处学习失配：安全投影会改变实际作用于环境的动作，而耦合的提议图会使各自独立优化的 actor 更新与团队级更新不一致。为此作者提出 safety-aligned gradient enforcement（SAGE），其中 shield-annealed internalization layer（SAIL）在保留精确 CBF 二次规划用于执行的同时，使用可微的有限惩罚提议映射，从而保留约束法向敏感性以内化反复激活的安全约束；team-averaged Lyapunov policy optimization（TALO）则构造团队感知的更新参考，并用 Lyapunov 半空间校正来约束各 actor 的独立更新。作者用两台人形机器人与一名人类伙伴开展物理实验验证部署可行性，并在九个仿真场景中评估方法性能。

## 核心内容

### 问题背景
多方人机协作存在双重挑战：机器人决策需要保持可解释与可审计，同时执行的动作必须在物理交互过程中满足安全约束。把可解释的决策树策略与控制屏障函数（CBF）过滤相结合是一种有前景的架构，但在多智能体强化学习中会产生两处学习失配：
- 安全投影会改变实际施加到环境上的动作；
- 耦合的提议图会使各自独立优化的 actor 更新与团队级更新之间产生错位。

### 方法
作者提出 safety-aligned gradient enforcement（SAGE），同时应对上述两处失配，包含两个组件：
- **shield-annealed internalization layer（SAIL）**：使用可微的有限惩罚提议映射，同时保留精确的 CBF 二次规划用于执行，从而保持约束法向敏感性，以内化反复激活的安全约束。
- **team-averaged Lyapunov policy optimization（TALO）**：构造团队感知的更新参考，并施加 Lyapunov 半空间校正，以规范各 actor 的独立更新。

### 实验设置
- 物理实验：使用两台人形机器人与一名人类伙伴，验证部署可行性。
- 仿真评估：在九个仿真场景中进行。

### 关键结果
- SAGE 在九个仿真场景中取得 71.0% 的成功率，每千环境步的碰撞步数为 0.5。
- 消融实验显示，直接使用 CBF 过滤可将碰撞频率降低 98.5%，但成功率从 67.3% 下降到 59.3%。
- SAIL 将提议违规降低 48.8%，将提议—执行校正降低 85.2%。
- TALO 将更新一致性差距降低 50.8%。

### 结论
SAGE 通过 SAIL 与 TALO 分别缓解安全投影带来的动作改变与团队级更新错位这两处学习失配，在保持安全约束的同时维持了任务成功率，并通过两台人形机器人与人类伙伴的物理实验证明了部署可行性。

## Overview

Multi-party human-robot collaboration poses a dual challenge: robot decisions should remain interpretable and auditable, while executed actions must satisfy safety constraints during physical interaction. Combining explainable decision-tree policies with control-barrier-function (CBF) filtering provides a promising architecture but creates two learning mismatches in multi-agent reinforcement learning. Safety projection changes the action applied to the environment, while the coupled proposal graph can misalign independently optimized actor updates with a team-level update. We present safety-aligned gradient enforcement (SAGE) to address both mismatches. Its shield-annealed internalization layer (SAIL) uses a differentiable finite-penalty proposal map while retaining the exact CBF quadratic program for execution, preserving constraint-normal sensitivity to internalize repeatedly active safety constraints. Team-averaged Lyapunov policy optimization (TALO) constructs a team-aware update reference and applies a Lyapunov half-space correction to regulate independent actor updates. Physical experiments with two humanoid robots and a human partner demonstrate deployment feasibility. Across nine simulation scenarios, SAGE achieves a 71.0% success rate with 0.5 collision steps per thousand environment steps. Ablations show that direct CBF filtering reduces collision frequency by 98.5% but decreases success from 67.3% to 59.3%. SAIL reduces proposal violation by 48.8% and proposal-execution correction by 85.2%, while TALO reduces the update-consistency gap by 50.8%.

## 参考
- https://arxiv.org/abs/2609.21130
