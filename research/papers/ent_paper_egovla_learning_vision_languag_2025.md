---
$id: ent_paper_egovla_learning_vision_languag_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos'
  zh: EgoVLA｜从第一视角的人类视频中学习视觉语言动作模型
  ko: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos'
summary:
  en: The implementation path of egofla is to first encode language instructions, camera images/multi-view observations, ontological
    states, and joint sequences into multimodal representations, which can be used to generate multimodal representations,
    then the whole-body trajectory/action sequence, end-effector/wrist-hand target were predicted with ACT/behavior clone
    imitation learning, VLA multimodal action model, latent variable/action token. The key point is to retain the semantic
    understanding of VLM, while increasing the robot state and action head, so as to avoid remaining in the language planning.
  zh: EgoVLA 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: EgoVLA 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egocentric_video
- egovla
- first_person_video
- imitation_learning
- vla
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (161). Institution: UC San Diego、MIT、NVIDIA. Full title: EgoVLA: Learning Vision-Language-Action
    Models from Egocentric Human Videos. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: EgoVLA project page
  url: https://rchalyang.github.io/EgoVLA/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
EgoVLA 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
EgoVLA 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

