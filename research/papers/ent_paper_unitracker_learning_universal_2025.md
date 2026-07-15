---
$id: ent_paper_unitracker_learning_universal_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots'
  zh: UniTracker｜学习仿人机器人通用全身运动跟踪器
  ko: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots'
summary:
  en: UniTracker converts camera images/multi-view observations, ontology state and joint sequences, and simulation interaction
    data into trackable body targets, and finally outputs whole-body trajectories/action sequences and low-level controller
    targets through teacher-student knowledge transfer, PPO/RL policy training, diffusion policy/flow matching training, or
    combined whole-body policies. The key point is to train teacher strategies with privileged information and then distill
    the capabilities to the point where only student strategies with deployed observations can be used.
  zh: UniTracker 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: UniTracker 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- unitracker
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (024). Institution: Shanghai Jiao Tong Univeristy、Shanghai Artificial Intelligence
    Laboratory、Shanghai Innovation Institute、Peking University. Full title: UniTracker: Learning Universal Whole-Body Motion
    Tracker for Humanoid Robots. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: UniTracker project page
  url: https://yinkangning0124.github.io/Humanoid-UniTracker/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
UniTracker 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
UniTracker 把相机图像/多视角观测、本体状态与关节序列、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

