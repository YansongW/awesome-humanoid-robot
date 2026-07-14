---
$id: ent_paper_rove_unlocking_human_intervent_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement
    Learning'
  zh: ROVE｜通过强化学习解锁人形操作的人类干预
  ko: 'ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement
    Learning'
summary:
  en: ''
  zh: ROVE 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、扩散策略/流匹配、VLA 多模态动作模型预测可执行动作命令。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: ROVE 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、扩散策略/流匹配、VLA 多模态动作模型预测可执行动作命令。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- rove
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (158). Institution: XPENG Robotics、Fudan
    University、The Chinese University of Hong Kong、Shanghai Jiao Tong University.
    Full title: ROVE: Unlocking Human Interventions for Humanoid Manipulation via
    Reinforcement Learning.'
sources:
- id: src_001
  type: website
  title: ROVE project page
  url: https://xpeng-robotics.github.io/rove
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
ROVE 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、扩散策略/流匹配、VLA 多模态动作模型预测可执行动作命令。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
ROVE 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、扩散策略/流匹配、VLA 多模态动作模型预测可执行动作命令。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
