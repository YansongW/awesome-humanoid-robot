---
$id: ent_paper_dial_decoupling_intent_and_act_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA'
  zh: DIAL｜通过端到端VLA的潜在世界建模解耦意图和行动
  ko: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA'
summary:
  en: The implementation path of DIAL is to first encode language instructions, camera images/multi-view observations, ontology
    states and joint sequences into multimodal representations, and then use diffusion strategy/flow matching, VLA multimodal
    action model, VLM semantic planning/routing to predict whole-body trajectories/action sequences, action chunk/token, and
    terrain/scene representations. The key point is to let the video/world model provide predictable physical priors, and
    then the action head turns the semantic goal into continuous control.
  zh: DIAL 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、动作 chunk/token、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
  ko: DIAL 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、动作 chunk/token、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dial
- general_manipulation
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (147). Institution: The University of Hong Kong、XPENG Robotics、University of North
    Carolina at Chapel Hill、Limited Robot Data. Full title: DIAL: Decoupling Intent and Action via Latent World Modeling for
    End-to-End VLA. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: DIAL project page
  url: https://xpeng-robotics.github.io/dial
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
DIAL 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、动作 chunk/token、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

## 개요
DIAL 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、动作 chunk/token、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

