---
$id: ent_paper_agibot_world_colosseo_a_large_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and
    Intelligent Embodied Systems'
  zh: AgiBot World Colosseo｜用于可扩展和智能具身系统的大规模操作平台
  ko: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and
    Intelligent Embodied Systems'
summary:
  en: ''
  zh: AgiBot World Colosseo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用VLM 语义规划/路由、潜变量/动作
    token、MM-DiT/Transformer 动作头预测全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: AgiBot World Colosseo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用VLM 语义规划/路由、潜变量/动作
    token、MM-DiT/Transformer 动作头预测全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- agibot_world_colosseo
- general_manipulation
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (146). Institution: . Full title: AgiBot
    World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent
    Embodied Systems.'
sources:
- id: src_001
  type: website
  title: AgiBot World Colosseo project page
  url: https://github.com/OpenDriveLab/AgiBot-World
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
AgiBot World Colosseo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用VLM 语义规划/路由、潜变量/动作 token、MM-DiT/Transformer 动作头预测全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。

## 개요
AgiBot World Colosseo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用VLM 语义规划/路由、潜变量/动作 token、MM-DiT/Transformer 动作头预测全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
