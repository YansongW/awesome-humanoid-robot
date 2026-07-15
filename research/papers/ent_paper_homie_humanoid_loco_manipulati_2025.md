---
$id: ent_paper_homie_humanoid_loco_manipulati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
  zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作
  ko: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
summary:
  en: 'HOMIE mainly solves the data closed loop: using ontology state and joint sequence, teleoperation/exoskeleton data,
    and simulation interaction data to collect human operation and robot state, and then train through PPO/RL strategy, transform
    the whole-body controller/WBC/MPC into trainable and reusable whole-body trajectory/action sequence, low-level controller
    target, and terrain/scene representation. The key point is to put PPO/RL strategy training, full body controller/WBC/MPC
    in the same training/deployment chain to reduce the breakpoints between high-level goals and low-level actions.'
  zh: HOMIE 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把PPO/RL
    策略训练、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: HOMIE 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把PPO/RL
    策略训练、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
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
- homie
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (040). Institution: Shanghai AI Laboratory、Multimedia Laboratory, The Chinese
    University of Hong Kong. Full title: HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit. English name/summary
    machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: HOMIE project page
  url: https://homietele.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
HOMIE 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把PPO/RL 策略训练、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
HOMIE 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、全身控制器/WBC/MPC转成可训练、可复用的全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把PPO/RL 策略训练、全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

