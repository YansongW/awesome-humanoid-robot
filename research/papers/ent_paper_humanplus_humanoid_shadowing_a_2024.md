---
$id: ent_paper_humanplus_humanoid_shadowing_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanPlus: Humanoid Shadowing and Imitation from Humans'
  zh: HumanPlus｜人形影子和模仿人类
  ko: ''
summary:
  en: ''
  zh: HumanPlus 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过PPO/RL 策略训练、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: ''
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
- humanplus
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (012). Institution: HumanPlus: Humanoid
    Shadowing and Imitation、project co-leads、Stanford University. Full title: HumanPlus:
    Humanoid Shadowing and Imitation from Humans.'
sources:
- id: src_001
  type: website
  title: HumanPlus project page
  url: https://humanoid-ai.github.io
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


HumanPlus 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过PPO/RL 策略训练、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
