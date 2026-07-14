---
$id: ent_paper_hex_humanoid_aligned_experts_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation'
  zh: HEX｜用于跨实体全身操作的人形对齐专家
  ko: 'HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation'
summary:
  en: ''
  zh: HEX 的实现路径是先把本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: HEX 的实现路径是先把本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- hex
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (038). Institution: Beijing Innovation
    Center of Humanoid Robotics、Xi’an Jiaotong University、Nankai University、Peking
    University. Full title: HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body
    Manipulation.'
sources:
- id: src_001
  type: website
  title: HEX project page
  url: https://hex-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
HEX 的实现路径是先把本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
HEX 的实现路径是先把本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
