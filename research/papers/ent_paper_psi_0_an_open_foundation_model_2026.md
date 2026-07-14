---
$id: ent_paper_psi_0_an_open_foundation_model_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '$\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation'
  zh: Psi0｜面向通用人形移动操作的开放基础模型
  ko: '$\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation'
summary:
  en: ''
  zh: Psi0 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用异构动捕与合成平衡数据、VLM 语义规划/路由、潜变量/动作
    token预测动作 chunk/token。关键点是把异构动捕与合成平衡数据、VLM 语义规划/路由放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: Psi0 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用异构动捕与合成平衡数据、VLM 语义规划/路由、潜变量/动作
    token预测动作 chunk/token。关键点是把异构动捕与合成平衡数据、VLM 语义规划/路由放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- general_manipulation
- psi0
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (156). Institution: NVIDIA. Full title:
    $\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: Psi0 project page
  url: https://psi-lab.ai/Psi0
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
Psi0 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用异构动捕与合成平衡数据、VLM 语义规划/路由、潜变量/动作 token预测动作 chunk/token。关键点是把异构动捕与合成平衡数据、VLM 语义规划/路由放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
Psi0 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用异构动捕与合成平衡数据、VLM 语义规划/路由、潜变量/动作 token预测动作 chunk/token。关键点是把异构动捕与合成平衡数据、VLM 语义规划/路由放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
