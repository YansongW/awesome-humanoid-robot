---
$id: ent_paper_omniretarget_interaction_prese_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body
    Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget｜人形全身移动操作和场景交互的交互保存数据生成
  ko: ''
summary:
  en: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  zh: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- omniretarget
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (017). Institution: Amazon FAR (Frontier
    AI & Robotics)、MIT、UC Berkeley、Stanford University. Full title: OmniRetarget:
    Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation
    and Scene Interaction.'
sources:
- id: src_001
  type: website
  title: OmniRetarget project page
  url: https://omniretarget.github.io
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
