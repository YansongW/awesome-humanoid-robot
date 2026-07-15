---
$id: ent_paper_wococo_learning_whole_body_hum_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts'
  zh: WoCoCo｜通过顺序接触学习全身人形控制
  ko: 'WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts'
summary:
  en: WoCoCo first recovers scene, target or motion representations from ontology state and joint sequences, human video/motion
    capture trajectories, and simulation interaction data, and then uses PPO/RL strategy training, AMP/motion priors, diffusion
    strategy/flow matching to generate whole-body trajectories/action sequences, end effectors/wrist targets. The key point
    is to view action generation as a conditional generation problem and use diffusion or flow matching to sample executable
    trajectories in a multimodal action distribution.
  zh: WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_video
- interaction_planning
- motion_capture
- motion_retargeting
- wococo
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (116). Institution: ETH Zurich、⋆Work was done at Carnegie Mellon University、Carnegie
    Mellon University. Full title: WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts. English name/summary
    machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: WoCoCo project page
  url: https://lecar-lab.github.io/wococo/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

