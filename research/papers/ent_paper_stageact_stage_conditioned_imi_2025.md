---
$id: ent_paper_stageact_stage_conditioned_imi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening'
  zh: StageACT｜鲁棒的人形开门的阶段条件模仿
  ko: 'StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening'
summary:
  en: 'StageACT mainly solves the data closed loop: using camera images/multi-view observation, ontology state and joint sequence,
    teleoperation/exoskeleton data to collect human operation and robot state, and then through ACT/behavioral cloning imitation
    learning, diffusion strategy/stream matching, VLM semantic planning/routing to trainable, reusable and executable action
    commands. The key point is to view action generation as a conditional generation problem and use diffusion or flow matching
    to sample executable trajectories in a multimodal action distribution.'
  zh: StageACT 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、VLM 语义规划/路由转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: StageACT 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、VLM 语义规划/路由转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- stageact
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (078). Institution: StageACT: Stage-Conditioned Imitation for Robust. Full title:
    StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening. English name/summary machine-translated from Chinese
    by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: StageACT project page
  url: https://icradooropen.github.io/icradooropen/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
StageACT 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、VLM 语义规划/路由转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
StageACT 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、VLM 语义规划/路由转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

