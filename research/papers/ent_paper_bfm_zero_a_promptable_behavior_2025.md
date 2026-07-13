---
$id: ent_paper_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using
    Unsupervised Reinforcement Learning'
  zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型
  ko: ''
summary:
  en: ''
  zh: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- bfm_zero
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (003). Institution: Carnegie Mellon University、Meta、aWork
    done during internships at Carnegie Mellon University. The authors are now with
    Tsinghua University. Full title: BFM-Zero: A Promptable Behavioral Foundation
    Model for Humanoid Control Using Unsupervised Reinforcement Learning.'
sources:
- id: src_001
  type: website
  title: BFM-Zero project page
  url: https://lecar-lab.github.io/BFM-Zero/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
