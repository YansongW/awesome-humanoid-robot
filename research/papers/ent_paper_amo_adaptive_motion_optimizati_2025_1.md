---
$id: ent_paper_amo_adaptive_motion_optimizati_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  zh: AMO｜超灵巧人形全身控制的自适应运动优化
  ko: ''
summary:
  en: ''
  zh: AMO 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
  ko: ''
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
- amo
- deployment
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (135). Institution: UC San Diego. Full
    title: AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body
    Control.'
sources:
- id: src_001
  type: website
  title: AMO project page
  url: https://amo-humanoid.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


AMO 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
