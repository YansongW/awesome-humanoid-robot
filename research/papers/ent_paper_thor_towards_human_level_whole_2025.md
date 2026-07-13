---
$id: ent_paper_thor_towards_human_level_whole_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments'
  zh: Thor｜在强烈接触的环境中实现人类水平的全身反应
  ko: ''
summary:
  en: ''
  zh: Thor 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- thor
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (047). Institution: . Full title: Thor:
    Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments.'
sources:
- id: src_001
  type: website
  title: Thor project page
  url: https://baai-aether.github.io/baai-thor/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


Thor 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
