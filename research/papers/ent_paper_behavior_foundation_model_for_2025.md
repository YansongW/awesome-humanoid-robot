---
$id: ent_paper_behavior_foundation_model_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Behavior Foundation Model for Humanoid Robots
  zh: 人形机器人行为基础模型
  ko: Behavior Foundation Model for Humanoid Robots
summary:
  en: 'This work mainly addresses the data closed loop: collecting human operation and robot states using ontology state and
    joint sequences, teleoperation/exoskeleton data, and simulation interaction data, and then transforming the whole-body
    controller/WBC/MPC into trainable and reusable whole-body trajectory/action sequences and low-level controller targets
    through teacher-student knowledge transfer, diffusion strategy/flow matching, whole-body controller/WBC/MPC. The key point
    is to train teacher strategies with privileged information and then distill the capabilities to the point where only student
    strategies with deployed observations can be used.'
  zh: 这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: 这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
  notes: 'Imported from WeChat curated list (027). Institution: Peking University、The Chinese University of Hong Kong, Shenzhen、Shanghai
    Jiaotong University、Fudan University. Full title: Behavior Foundation Model for Humanoid Robots. English name/summary
    machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 人形机器人行为基础模型 project page
  url: https://bfm4humanoid.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

