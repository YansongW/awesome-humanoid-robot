---
$id: ent_paper_from_w1_towards_general_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
  zh: FRoM-W1｜通过语言指令实现通用人形全身控制
  ko: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
summary:
  en: ''
  zh: FRoM-W1 把语言指令、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
  ko: FRoM-W1 把语言指令、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
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
- from_w1
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (008). Institution: Fudan University、Shanghai
    Innovation Institute. Full title: FRoM-W1: Towards General Humanoid Whole-Body
    Control with Language Instructions.'
sources:
- id: src_001
  type: website
  title: FRoM-W1 project page
  url: https://openmoss.github.io/FRoM-W1
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
FRoM-W1 把语言指令、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。

## 개요
FRoM-W1 把语言指令、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
