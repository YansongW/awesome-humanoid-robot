---
$id: ent_paper_pilot_a_perceptive_integrated_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PILOT: A Perceptive Integrated Low-level Controller for Loco-manipulation over Unstructured Scenes'
  zh: PILOT｜用于非结构化场景移动操作的感知集成低级控制器
  ko: 'PILOT: A Perceptive Integrated Low-level Controller for Loco-manipulation over Unstructured Scenes'
summary:
  en: Pilot first recovers the scene, target, or motion representation from ontological states and joint sequences, simulated
    interaction data, contact force/tactile signals, and visual cues, then, PPO/RL Strategy Training, whole-body Controller/WBC/MPC,
    hierarchical skills/expert strategy were used to generate whole-body trajectory/action sequence, low-level controller
    target, terrain/scene representation. The key is to break the task down into routable skills or expert strategies, which
    are then selected and combined in execution using high-level modules.
  zh: PILOT 先从本体状态与关节序列、仿真交互数据、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: PILOT 先从本体状态与关节序列、仿真交互数据、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- pilot
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (043). Institution: . Full title: PILOT: A Perceptive Integrated Low-level Controller
    for Loco-manipulation over Unstructured Scenes. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 'PILOT: A Perceptive Integrated Low-level Controller for Loco-manipulation over Unstructured Scenes'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
PILOT 先从本体状态与关节序列、仿真交互数据、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

## 개요
PILOT 先从本体状态与关节序列、仿真交互数据、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

