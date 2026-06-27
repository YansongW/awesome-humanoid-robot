---
$id: ent_paper_expressive_whole_body_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Expressive Whole-Body Control for Humanoid Robots
  zh: 人形机器人富有表现力的全身控制
  ko: ''
summary:
  en: 这篇工作把本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
  zh: 这篇工作把本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
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
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (026). Institution: UC San Diego. Full
    title: Expressive Whole-Body Control for Humanoid Robots.'
sources:
- id: src_001
  type: website
  title: 人形机器人富有表现力的全身控制 project page
  url: https://expressive-humanoid.github.io
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

这篇工作把本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、PPO/RL 策略训练、ACT/行为克隆模仿学习训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
