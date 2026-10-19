---
$id: ent_paper_parsuram_compliant_gmt_making_general_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation'
  zh: 'Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation'
  ko: 'Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation'
summary:
  en: We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking.
    As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and
    robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained
    to be stiff, leading to unexpected and ...
  zh: Compliant GMT（C-GMT）是一个模块化框架，用于在通用运动跟踪中实现全身柔顺响应。该工作由 Venki Parsuram、Michelle Wang、Jin-Hyuk Hong 与 Pulkit Agrawal 提出，核心思路是在预训练通用运动跟踪器（GMT）之上引入一个以本体感知历史为条件的残差适配器，从而同时获得通用运动跟踪能力与全身柔顺响应。相比现有通用运动跟踪器与单一动作柔顺策略，C-GMT
    在跟踪精度与柔顺性上均表现出竞争力，并在仿真与真实 G1 实验中展现出更好的安全性、鲁棒性与误差容忍度。
  ko: We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking.
    As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and
    robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained
    to be stiff, leading to unexpected and ...
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
- motion_tracking
- compliant_control
- residual_adaptation
- whole_body_control
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.22119);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.22119 Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation'
  url: https://arxiv.org/abs/2610.22119
  date: '2026-10-15'
  accessed_at: '2026-10-19'
- id: src_002
  type: website
  title: Project page
  url: https://venki1899.github.io/c-gmt/
  accessed_at: '2026-10-19'
---

## 概述

人形机器人走向真实部署后，不仅要能执行各类动作，还需对交互力做出安全、稳健的响应。现有通用运动跟踪策略虽能模仿多样动作，却被训练得僵硬，受扰动时容易产生意外且不安全的行为；而此前的柔顺人形控制工作往往在柔顺性与通用性之间取舍，已有的全身柔顺响应案例多局限于经过大量人工筛选的单一参考策略。C-GMT 的关键洞察是利用预训练 GMT 的通用性来承担运动跟踪，同时由一个以本体感知历史为条件的残差适配器引入柔顺性。该模块化设计使通用运动跟踪与全身柔顺响应得以兼得，并在与最先进通用运动跟踪器和单一动作柔顺策略的对比中，于跟踪精度与柔顺性两方面均表现竞争力。作者进一步在仿真与真实 G1 实验中验证了安全性、鲁棒性与误差容忍度的提升。

## 核心内容

### 问题背景

- 人形机器人进入真实世界部署后，除了执行任意动作，还必须对交互力做出安全且稳健的响应。
- 现有通用运动跟踪策略能够模仿多样动作，但被训练得僵硬，遇到扰动时会产生意外且不安全的行为。
- 此前的柔顺人形控制研究在柔顺性与通用性之间存在取舍：已有的全身柔顺响应案例高度依赖于单一参考策略，且经过大量人工筛选；而通用运动跟踪器（GMT）则是在大规模动作捕捉数据集上被训练为刚性模仿。

### 方法

- 核心思路：利用预训练 GMT 的通用性负责运动跟踪，同时由一个残差适配器引入柔顺性。
- 该残差适配器以本体感知历史为条件，从而生成全身柔顺响应。
- 整体为模块化框架，命名为 Compliant GMT（C-GMT），使通用运动跟踪与全身柔顺响应得以同时实现。

### 实验设置与关键结果

- 对比对象为最先进的通用运动跟踪器与单一动作柔顺策略。
- C-GMT 在运动跟踪精度与柔顺性遵循两方面均表现出竞争力。
- 在仿真与真实 G1 实验中进一步展示了安全性、鲁棒性与误差容忍度的提升。

### 结论

C-GMT 通过残差参考适配的方式，在不牺牲通用运动跟踪能力的前提下赋予策略全身柔顺响应，为真实部署中的人形机器人提供了更安全、更稳健的跟踪行为。

## Overview

We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking. As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained to be stiff, leading to unexpected and unsafe behaviors under disturbance. Prior work in compliant humanoid control trades off compliance and generality. There exist examples of full-body compliant responses, but these are heavily curated to single-reference policies. On the other hand, general motion trackers (GMT) are trained to rigidly imitate massive motion capture datasets. Our key insight is to leverage the generality of pretrained GMTs for motion tracking while introducing compliance from a residual adapter that conditions on a history of proprioception. This enables our approach, C-GMT, to achieve both general motion tracking and whole-body compliant responses. Compared to state-of-the-art general motion trackers and single-motion compliant policies, C-GMT demonstrates competitive performance in both motion tracking accuracy and compliance adherence. We further demonstrate improved safety, robustness, and error tolerance in simulation and real-world G1 experiments.

## 参考
- https://arxiv.org/abs/2610.22119
- https://venki1899.github.io/c-gmt/
