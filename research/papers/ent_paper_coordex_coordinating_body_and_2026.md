---
$id: ent_paper_coordex_coordinating_body_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation'
  zh: CoorDex｜协调身体和手的优先顺序以实现连续灵巧的人形移动操作
  ko: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation'
summary:
  en: CoorDex converts the body state with joint sequences, contact force/tactile signals into trackable body targets, and
    finally outputs whole-body trajectories/action sequences, low-level controller targets, and terrain/scene representations
    through PPO/RL policy training, diffusion policy/flow matching, MM-DiT/Transformer action head training, or combined whole-body
    policies. The key point is to view action generation as a conditional generation problem and use diffusion or flow matching
    to sample executable trajectories in a multimodal action distribution.
  zh: CoorDex 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: CoorDex 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- coordex
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (035). Institution: University of North Carolina at Chapel Hill、University of
    California, Berkeley. Full title: CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation.
    English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: CoorDex project page
  url: https://skevinci.github.io/coordex/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
CoorDex 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
CoorDex 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

