---
$id: ent_paper_lim_mapo_mixture_of_experts_with_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking'
  zh: 'MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking'
  ko: 'MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking'
summary:
  en: Universal humanoid motion tracking is essential for enabling humanoid robots to perform diverse tasks in human environments.
    To capture the wide diversity of human motions, mixture-of-experts (MoE) policies have been widely adopted, leveraging
    dynamic routing to enhance policy expressiveness. However, we identify that divergence between old and updated policies
    can be misestimated during ...
  zh: MAPO（Mixture of Experts with Alternating Policy Optimization）是一种面向通用人形机器人运动跟踪的专家混合策略优化方法，由 Seonghyeon Lim、Hyeonwoo Lee、Mincheol
    Kim、Kimin Lee、Hyun Myung 提出。该方法指出 MoE 策略的动态路由会使策略梯度更新中对新旧策略散度的估计出现偏差，进而导致更新过于保守或过大；为此 MAPO 交替优化路由器与专家网络以规避该问题。实验中 MAPO
    能持续跟踪 182 个 PPO with MoE 无法跟踪的动作，而后者仅能跟踪 1 个 MAPO 无法跟踪的动作。
  ko: Universal humanoid motion tracking is essential for enabling humanoid robots to perform diverse tasks in human environments.
    To capture the wide diversity of human motions, mixture-of-experts (MoE) policies have been widely adopted, leveraging
    dynamic routing to enhance policy expressiveness. However, we identify that divergence between old and updated policies
    can be misestimated during ...
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
- humanoid_motion_tracking
- mixture_of_experts
- policy_optimization
- policy_gradient
- dynamic_routing
- motion_tracking
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.02613);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.02613 MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking'
  url: https://arxiv.org/abs/2611.02613
  date: '2026-11-02'
  accessed_at: '2026-11-09'
---

## 概述

通用人形机器人运动跟踪是让人形机器人在人类环境中执行多样任务的基础能力，而人类动作的多样性促使研究者广泛采用带动态路由的专家混合（MoE）策略来提升策略表达能力。作者发现，由于 MoE 策略存在动态路由，在策略梯度更新过程中，新旧策略之间的散度可能被错误估计；而多数策略梯度算法正是依据该散度来约束更新幅度，因此这种错误估计会造成更新过于保守或步长过大，最终得到次优策略。针对这一问题，作者提出 MAPO，通过交替优化路由器与专家网络来避免散度误估。在对比实验中，MAPO 能持续跟踪 182 个 PPO with MoE 无法跟踪的动作，反向失败仅 1 个，并在所比较方法中取得最高跟踪成功率，且在多数误差指标上取得最低跟踪误差。

## 核心内容

### 问题背景

通用人形机器人运动跟踪使人形机器人能够在人类环境中完成多样任务。为覆盖人类动作的广泛多样性，研究者广泛采用专家混合（MoE）策略，借助动态路由提升策略表达能力。作者指出，MoE 策略的动态路由会导致在策略梯度更新时对新旧策略散度的错误估计；由于多数策略梯度算法依据该散度约束策略更新幅度，这种误估可能造成更新过于保守或步长过大，从而得到次优策略。

### 方法

作者提出 MAPO（Mixture of Experts with Alternating Policy Optimization），其核心是交替优化路由器与专家网络，以规避上述散度误估问题。

### 实验设置与关键结果

- 与 PPO with MoE 的对比：MAPO 能持续跟踪 182 个 PPO with MoE 无法跟踪的动作；而 PPO with MoE 仅能跟踪 1 个 MAPO 无法跟踪的动作。
- 在与其他方法比较中，MAPO 取得最高跟踪成功率，并在多数误差指标上取得最低跟踪误差。

### 结论

实验结果表明，交替优化路由器与专家网络可有效避免 MoE 策略梯度更新中的散度误估，从而在人形机器人通用运动跟踪上取得优于对比方法的性能。项目视频见 https://mapo-corl2026.github.io/MAPO/。

## Overview

Universal humanoid motion tracking is essential for enabling humanoid robots to perform diverse tasks in human environments. To capture the wide diversity of human motions, mixture-of-experts (MoE) policies have been widely adopted, leveraging dynamic routing to enhance policy expressiveness. However, we identify that divergence between old and updated policies can be misestimated during policy-gradient updates of MoE policies, due to their dynamic routing. Because most policy-gradient algorithms regulate policy updates based on the divergence, this misestimation can lead to either overly conservative or excessively large updates, which can yield a suboptimal policy. In this paper, we propose Mixture of Experts with Alternating Policy Optimization (MAPO), which alternately optimizes the router and the experts to avoid the divergence misestimation. MAPO consistently tracks 182 motions that PPO with MoE fails to track, whereas PPO with MoE tracks only one motion that MAPO fails to track. MAPO also attains the highest tracking success rate among the compared methods and the lowest tracking error across most error metrics, demonstrating its superior performance. Videos can be found on the project website: https://mapo-corl2026.github.io/MAPO/

## 参考
- https://arxiv.org/abs/2611.02613
