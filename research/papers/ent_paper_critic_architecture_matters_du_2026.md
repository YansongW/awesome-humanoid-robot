---
$id: ent_paper_critic_architecture_matters_du_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation'
  zh: 价值网络结构很重要｜人形移动操作中的双评论家与统一评论家
  ko: 'Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation'
summary:
  en: ''
  zh: 这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: 这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (052). Institution: Department of Computer
    Engineering、C¸ ukurova University. Full title: Critic Architecture Matters: Dual
    vs. Unified Critics for Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: 'Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
这篇工作把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
