---
$id: ent_paper_sumo_dynamic_and_generalizable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation'
  zh: Sumo｜动态且可推广的全身移动操作
  ko: 'Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation'
summary:
  en: ''
  zh: Sumo 把本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: Sumo 把本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- sumo
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (046). Institution: MIT、RAI Institute、Cornell,
    *Equal Contribution、This work was done in part during an internship at the RAI
    Institute. Full title: Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: Sumo project page
  url: https://sumo.rai-inst.com/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
Sumo 把本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
Sumo 把本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
