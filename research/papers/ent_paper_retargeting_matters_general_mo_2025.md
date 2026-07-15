---
$id: ent_paper_retargeting_matters_general_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking'
  zh: Retargeting｜Matters 人形机器人的通用运动重定向
  ko: 'Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking'
summary:
  en: 'Retargeting mainly addresses data closed-loop: collecting human operations and robot states with human video/dynamic
    capture trajectories, teleoperation/exoskeleton data, contact force/tactile signals, and data processing, then, PPO/RL
    strategy training, IK/action redirection, hierarchical skill/expert strategy are used to transform the whole body trajectory/action
    sequence and low-level controller target into trainable and reusable ones. The key is to break the task down into routable
    skills or expert strategies, which are then selected and combined in execution using high-level modules.'
  zh: Retargeting 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、IK/动作重定向、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: Retargeting 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、IK/动作重定向、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- retargeting
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (018). Institution: Stanford University. Full title: Retargeting Matters: General
    Motion Retargeting for Humanoid Motion Tracking. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: Retargeting project page
  url: https://jaraujo98.github.io/retargeting_matters
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
Retargeting 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、IK/动作重定向、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

## 개요
Retargeting 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、IK/动作重定向、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

