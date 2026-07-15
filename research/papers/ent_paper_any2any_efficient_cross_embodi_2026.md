---
$id: ent_paper_any2any_efficient_cross_embodi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking'
  zh: Any2Any｜用于人形全身跟踪的高效跨实体传输
  ko: 'Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking'
summary:
  en: Any2Any converts visual, state, and action data into trackable body targets and outputs full-body trajectories/action
    sequences, low-level controller targets, through source/target robot kinematic alignment, PEFT dynamic adaptation, full-body
    controller/WBC/MPC training, or combined full-body strategies. The key point is to first align the state and action space
    of the source/target robot, and then only fine-tune the dynamics-sensitive module, trying to preserve the motion prior
    of the original strategy.
  zh: Any2Any 把视觉、状态和动作数据转成可跟踪的身体目标，并通过源/目标机器人运动学对齐、PEFT 动力学适配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是先对齐源/目标机器人的状态和动作空间，再只微调动力学敏感模块，尽量保留原策略的运动先验。
  ko: Any2Any 把视觉、状态和动作数据转成可跟踪的身体目标，并通过源/目标机器人运动学对齐、PEFT 动力学适配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是先对齐源/目标机器人的状态和动作空间，再只微调动力学敏感模块，尽量保留原策略的运动先验。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- any2any
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (002). Institution: . Full title: Any2Any: Efficient Cross-Embodiment Transfer
    for Humanoid Whole-Body Tracking. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: Any2Any project page
  url: https://any2any.top/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
Any2Any 把视觉、状态和动作数据转成可跟踪的身体目标，并通过源/目标机器人运动学对齐、PEFT 动力学适配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是先对齐源/目标机器人的状态和动作空间，再只微调动力学敏感模块，尽量保留原策略的运动先验。

## 개요
Any2Any 把视觉、状态和动作数据转成可跟踪的身体目标，并通过源/目标机器人运动学对齐、PEFT 动力学适配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是先对齐源/目标机器人的状态和动作空间，再只微调动力学敏感模块，尽量保留原策略的运动先验。

