---
$id: ent_paper_mobile_television_predictive_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control'
  zh: Mobile-TeleVision｜用于人形全身控制的预测运动先验
  ko: 'Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control'
summary:
  en: Mobile-TeleVision converts body states and joint sequences, human video/motion capture trajectories, contact force/tactile
    signals into trackable body targets, and finally outputs joint position/torque commands, whole-body trajectories/action
    sequences, and terrain/scene representations through PPO/RL strategy training, AMP/motion priors, diffusion strategy/flow
    matching training, or combined whole-body strategies. The key point is to view action generation as a conditional generation
    problem and use diffusion or flow matching to sample executable trajectories in a multimodal action distribution.
  zh: Mobile-TeleVision 把本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: Mobile-TeleVision 把本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- deployment
- hardware_platform
- mobile_television
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (138). Institution: UC San Diego、MIT. Full title: Mobile-TeleVision: Predictive
    Motion Priors for Humanoid Whole-Body Control. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: Mobile-TeleVision project page
  url: https://mobile-tv.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
Mobile-TeleVision 把本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
Mobile-TeleVision 把本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

