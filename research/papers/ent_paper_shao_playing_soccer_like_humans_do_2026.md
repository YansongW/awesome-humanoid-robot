---
$id: ent_paper_shao_playing_soccer_like_humans_do_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors'
  zh: 'Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors'
  ko: 'Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors'
summary:
  en: Humanoid soccer requires a robot to seamlessly combine agile locomotion, ball manipulation, and impact-rich contact
    dynamics across a continuous, dynamic behavioral spectrum. Yet existing approaches either cover only a limited set of
    skills, or forego motion priors entirely and produce unnatural behaviors, leaving the combination of a unified skill set
    and human-like motion quality unaddressed. ...
  zh: soccerbot 是一个分层强化学习框架，由 Haoyu Shao、Yunshen Wang、Jingze Zhang、Shaohang Zhu、Yong-Lu Li、Tianzhu Zhang、Baoxiong Jia、Siyuan
    Huang 提出，利用从大规模人类足球动作捕捉数据中蒸馏出的结构化潜在运动先验，在单一技能条件策略中统一学习移动、带球、停球与踢球等足球技能。该方法将策略学习约束在动力学上合理的运动流形内，从而自然产生类人动作与流畅的技能切换，并零样本迁移至
    Unitree G1 人形机器人。
  ko: Humanoid soccer requires a robot to seamlessly combine agile locomotion, ball manipulation, and impact-rich contact
    dynamics across a continuous, dynamic behavioral spectrum. Yet existing approaches either cover only a limited set of
    skills, or forego motion priors entirely and produce unnatural behaviors, leaving the combination of a unified skill set
    and human-like motion quality unaddressed. ...
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
- humanoid_soccer
- latent_motion_prior
- hierarchical_reinforcement_learning
- motion_capture
- zero_shot_transfer
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.06564);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.06564 Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors'
  url: https://arxiv.org/abs/2611.06564
  date: '2026-11-04'
  accessed_at: '2026-11-09'
---

## 概述

人形机器人足球要求机器人在连续动态的行为谱上同时具备敏捷移动、控球与富含冲击的接触动力学能力，而现有方法要么只覆盖有限技能，要么完全舍弃运动先验导致动作不自然。soccerbot 通过分层强化学习框架应对这一矛盾，其核心是从大规模人类足球动作捕捉数据中蒸馏出结构化的潜在运动先验，并将策略学习约束在该动力学合理的运动流形之内。在这一约束下，单个技能条件策略以统一形式学会移动、带球、停球和踢球，并在技能切换时表现出类人的动作质量与流畅过渡。配合面向鲁棒性的仿真设计，该框架零样本迁移到 Unitree G1 人形机器人，在真实环境中完成全套足球技能。

## 核心内容

### 问题背景

人形机器人足球需要在连续且动态的行为谱上无缝结合敏捷移动、控球操作与富含冲击的接触动力学。现有方法存在两方面局限：一是仅覆盖有限的技能集合；二是完全舍弃运动先验，导致产生不自然的动作。因此，统一技能集合与类人动作质量这两者的结合尚未得到解决。

### 方法

- 提出 **soccerbot**，一个分层强化学习框架。
- 核心组件是结构化的潜在运动先验，从大规模人类足球动作捕捉数据中蒸馏得到。
- 将策略学习约束在该动力学上合理的运动流形之内。
- 采用单一技能条件策略，以统一形式学习移动、带球、停球与踢球。
- 由于策略被限制在合理运动流形中，动作本身即具备类人特征，并在指令技能切换时产生流畅过渡。
- 引入面向鲁棒性的仿真设计。

### 实验设置与结果

- 通过零样本迁移部署到 Unitree G1 人形机器人。
- 在真实世界条件下展示全套足球技能的敏捷、自然且鲁棒的执行。

### 结论

soccerbot 表明，借助从人类足球动作捕捉数据蒸馏的潜在运动先验，可以在单一策略中同时获得统一的足球技能集合与类人动作质量，并成功零样本迁移至真实人形机器人。

## Overview

Humanoid soccer requires a robot to seamlessly combine agile locomotion, ball manipulation, and impact-rich contact dynamics across a continuous, dynamic behavioral spectrum. Yet existing approaches either cover only a limited set of skills, or forego motion priors entirely and produce unnatural behaviors, leaving the combination of a unified skill set and human-like motion quality unaddressed. We present soccerbot, a hierarchical reinforcement learning framework that resolves both limitations through a structured latent motion prior distilled from large-scale human soccer motion capture data. By constraining policy learning within this dynamically plausible motion manifold, a single skill-conditioned policy naturally learns to perform moving, dribbling, trapping, and kicking in a unified formulation, while inherently producing human-like motion and fluid transitions during commanded skill switching. Augmented by robustness-oriented simulation design, soccerbot transfers zero-shot to the Unitree G1 humanoid robot, demonstrating agile, natural, and robust execution of the full soccer skill repertoire under real-world conditions.

## 参考
- https://arxiv.org/abs/2611.06564
