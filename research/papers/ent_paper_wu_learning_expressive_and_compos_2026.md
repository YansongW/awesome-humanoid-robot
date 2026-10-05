---
$id: ent_paper_wu_learning_expressive_and_compos_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Expressive and Compositional Motion Representation via Spectral Skills
  zh: Learning Expressive and Compositional Motion Representation via Spectral Skills
  ko: Learning Expressive and Compositional Motion Representation via Spectral Skills
summary:
  en: Robotic foundation models offer a promising path toward general-purpose humanoid robot control, often through hierarchical
    architectures. However, their effectiveness depends on the command interface between the planner and the controller, which
    must support accurate execution while remaining easy to predict, and ideally allow new behaviors to be composed from prior
    ones. In this work, we ...
  zh: 本文提出 spectral skills，一种用于人形机器人分层控制中规划器与控制器之间命令接口的潜在动作表示，通过预测式表示学习获得。作者来自 Feiyang Wu、Chenxiao Gao、Chen Yang、Ye Zhao、Bo
    Dai、Anqi Wu 等人。在 29 自由度人形机器人上，以 spectral skills 为条件的控制器将全局跟踪误差相对当前最优方法降低 62%，并支持技能串联与组合。
  ko: Robotic foundation models offer a promising path toward general-purpose humanoid robot control, often through hierarchical
    architectures. However, their effectiveness depends on the command interface between the planner and the controller, which
    must support accurate execution while remaining easy to predict, and ideally allow new behaviors to be composed from prior
    ones. In this work, we ...
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
- humanoid_control
- motion_representation
- spectral_skills
- predictive_representation_learning
- skill_composition
- hierarchical_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.37677);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.37677 Learning Expressive and Compositional Motion Representation via Spectral Skills
  url: https://arxiv.org/abs/2609.37677
  date: '2026-09-29'
  accessed_at: '2026-10-05'
---

## 概述

该工作关注机器人基础模型中的分层架构，其效果高度依赖规划器与控制器之间的命令接口：既要能被准确执行，又要易于预测，还应支持由已有行为组合出新行为。为此作者提出 spectral skills，一种通过预测式表示学习得到的潜在表示，它紧凑地编码短时运动片段，训练目标是预测后续运动而非重建编码器输入。在 29 自由度人形机器人上，以 spectral skills 为条件的控制器将全局跟踪误差相对当前最优方法降低 62%。同一个冻结的控制器无需额外的过渡策略即可串联独立编码的技能，并可通过在任意兼容基础技能上叠加正交方向来组合出训练数据中未出现的新行为。作者在 Unitree G1 硬件上展示了跟踪、串联、组合以及通过语言条件规划器进行的控制。

## 核心内容

### 问题背景
机器人基础模型被视为通向通用人形机器人控制的有前景路径，通常采用分层架构。这类架构的效果取决于规划器与控制器之间的命令接口：接口需支持准确执行，同时保持易于预测，并最好能由已有行为组合出新行为。现有接口表示难以同时满足这些要求。

### 方法
作者提出 spectral skills，一种面向该命令接口的潜在表示，通过预测式表示学习获得。其设计要点包括：
- 紧凑编码短时运动片段；
- 学习目标为预测后续运动，而非重建编码器输入。

### 实验设置
- 平台：29 自由度人形机器人；
- 硬件验证：Unitree G1；
- 对比：与当前最优方法比较全局跟踪误差。

### 关键结果
- 以 spectral skills 为条件的控制器将全局跟踪误差相对当前最优方法降低 62%；
- 同一个冻结的控制器无需单独的过渡策略即可串联独立编码的技能；
- 通过在任意兼容基础技能上叠加正交方向，可组合出训练数据中未出现的新行为；
- 在 Unitree G1 硬件上演示了跟踪、串联与组合，以及通过语言条件规划器进行的控制。

### 结论
spectral skills 作为规划器与控制器之间的潜在命令接口，兼顾了准确执行、可预测性与行为组合能力，并在真实人形硬件上得到验证。项目页面：https://spectral-skill.github.io

## Overview

Robotic foundation models offer a promising path toward general-purpose humanoid robot control, often through hierarchical architectures. However, their effectiveness depends on the command interface between the planner and the controller, which must support accurate execution while remaining easy to predict, and ideally allow new behaviors to be composed from prior ones. In this work, we introduce spectral skills, a latent representation of this interface that meets these requirements through predictive representation learning. By design, spectral skills compactly encode short motion segments and are learned by predicting subsequent motion rather than reconstructing the encoder input. On a 29-DoF humanoid, a controller conditioned on spectral skills reduces global tracking error by 62\% relative to the state of the art. The same frozen controller chains independently encoded skills without a separate transition policy. It also composes new behaviors by adding orthogonal directions to any compatible base skill, producing combinations unseen in the training data. We demonstrate tracking, chaining, and composition, as well as control through a language-conditioned planner, on Unitree G1 hardware. Project page: https://spectral-skill.github.io

## 参考
- https://arxiv.org/abs/2609.37677
