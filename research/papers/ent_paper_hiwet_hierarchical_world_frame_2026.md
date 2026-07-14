---
$id: ent_paper_hiwet_hierarchical_world_frame_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid
    Loco-Manipulation'
  zh: HiWET｜用于长时程人形移动操作的分层世界坐标系末端执行器跟踪
  ko: 'HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid
    Loco-Manipulation'
summary:
  en: ''
  zh: HiWET 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、VLM 语义规划/路由、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: HiWET 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、VLM 语义规划/路由、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- hiwet
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (041). Institution: Shanghai Jiao Tong
    University、Shanghai Innovation Institute、Tongji University、Tsinghua University.
    Full title: HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon
    Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: 'HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid
    Loco-Manipulation'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
HiWET 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、VLM 语义规划/路由、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

## 개요
HiWET 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、VLM 语义规划/路由、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
