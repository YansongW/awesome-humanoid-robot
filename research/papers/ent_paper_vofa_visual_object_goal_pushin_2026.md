---
$id: ent_paper_vofa_visual_object_goal_pushin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VOFA: Visual Object Goal Pushing with Force-Adaptive Control for Humanoids'
  zh: VOFA｜通过人形机器人的力自适应控制推动视觉对象目标
  ko: 'VOFA: Visual Object Goal Pushing with Force-Adaptive Control for Humanoids'
summary:
  en: ''
  zh: VOFA 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、导航/到达目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: VOFA 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、导航/到达目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- upper_body_control
- vofa
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (050). Institution: Department of Computer
    Science, The University of Texas at Austin. Full title: VOFA: Visual Object Goal
    Pushing with Force-Adaptive Control for Humanoids.'
sources:
- id: src_001
  type: website
  title: 'VOFA: Visual Object Goal Pushing with Force-Adaptive Control for Humanoids'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
VOFA 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、导航/到达目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
VOFA 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过扩散策略/流匹配、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、导航/到达目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
