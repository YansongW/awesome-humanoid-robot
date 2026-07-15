---
$id: ent_paper_skillblender_towards_versatile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending'
  zh: SkillBlender｜通过技能混合实现多样化人形全身移动操作
  ko: 'SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending'
summary:
  en: SkillBlender first recovers scene, target, or motion representations from camera images/multi-view observations, ontology
    state and joint sequences, contact force/tactile signals, and then generates whole-body trajectory/action sequences using
    PPO/RL strategy training, diffusion strategy/flow matching, and whole-body controller/WBC/MPC. The key point is to view
    action generation as a conditional generation problem and use diffusion or flow matching to sample executable trajectories
    in a multimodal action distribution.
  zh: SkillBlender 先从相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: SkillBlender 先从相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- scene_understanding
- skillblender
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (077). Institution: University of Southern California、Stanford University、Peking
    University、University of California, Berkeley. Full title: SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation
    via Skill Blending. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: SkillBlender project page
  url: https://usc-gvl.github.io/SkillBlender-web/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
SkillBlender 先从相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
SkillBlender 先从相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

