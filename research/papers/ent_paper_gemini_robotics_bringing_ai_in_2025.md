---
$id: ent_paper_gemini_robotics_bringing_ai_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gemini Robotics: Bringing AI into the Physical World'
  zh: Gemini Robotics｜将人工智能带入物理世界
  ko: 'Gemini Robotics: Bringing AI into the Physical World'
summary:
  en: The implementation path of Gemini Robotics is to first encode language instructions, camera images/multi-view observations
    into multimodal representations, and then translate them into visual representations, then, Act/behavior clone imitation
    learning, diffusion strategy/flow matching, VLA multimodal action model were used to predict the whole body trajectory/action
    sequence, and action chunk/token. The key point is to retain the semantic understanding of VLM, while increasing the robot
    state and action head, so as to avoid remaining in the language planning.
  zh: Gemini Robotics 的实现路径是先把语言指令、相机图像/多视角观测编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、动作 chunk/token。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: Gemini Robotics 的实现路径是先把语言指令、相机图像/多视角观测编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、动作 chunk/token。关键点是保留
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
- gemini_robotics
- general_manipulation
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (149). Institution: Gemini Robotics: Bringing AI into the Physical、Gemini Robotics
    Team, Google DeepMind1、designed for robotics and built upon the foundation of Gemini .. We present Gemini Robotics, an、Robotics
    executes smooth and reactive movements to tackle a wide range of complex manipulation tasks. Full title: Gemini Robotics:
    Bringing AI into the Physical World. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: Gemini Robotics project page
  url: https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
Gemini Robotics 的实现路径是先把语言指令、相机图像/多视角观测编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、动作 chunk/token。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
Gemini Robotics 的实现路径是先把语言指令、相机图像/多视角观测编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、动作 chunk/token。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

