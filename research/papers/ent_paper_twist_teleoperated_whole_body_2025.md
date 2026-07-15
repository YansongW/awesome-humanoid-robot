---
$id: ent_paper_twist_teleoperated_whole_body_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWIST: Teleoperated Whole-Body Imitation System'
  zh: TWIST｜遥控全身模仿系统
  ko: 'TWIST: Teleoperated Whole-Body Imitation System'
summary:
  en: 'TWIST mainly solves the data closed loop: using human video/kinetrap trajectories, teleoperation/exoskeleton data,
    contact force/tactile signals to collect human operation and robot states, and then transforming them into trainable and
    reusable whole-body trajectories/action sequences through heterogeneous kinetrap and synthetic balance data, PPO/RL strategy
    training, ACT/behavioral cloning imitation learning, and low-level controller targets. The key is to break down tasks
    into routable skills or expert strategies, which are then selected and combined in execution using high-level modules.'
  zh: TWIST 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: TWIST 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- twist
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (021). Institution: TWIST: Teleoperated Whole-Body Imitation System、Stanford University、Simon
    Fraser University ∗Equal Contribution †Equal Advising. Full title: TWIST: Teleoperated Whole-Body Imitation System. English
    name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: TWIST project page
  url: https://humanoid-teleop.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
TWIST 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

## 개요
TWIST 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

