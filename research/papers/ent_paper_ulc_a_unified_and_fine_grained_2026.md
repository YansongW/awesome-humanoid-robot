---
$id: ent_paper_ulc_a_unified_and_fine_grained_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation'
  zh: ULC｜用于人形移动操作的统一细粒度控制器
  ko: ''
summary:
  en: ''
  zh: ULC 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- manipulation_interface
- mobile_manipulation
- ulc
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (048). Institution: . Full title: ULC:
    A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: ULC project page
  url: https://hellod035.github.io/ULC/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


ULC 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
