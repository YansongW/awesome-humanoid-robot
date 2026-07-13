---
$id: ent_paper_learning_versatile_humanoid_ma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Versatile Humanoid Manipulation with Touch Dreaming
  zh: 通过触摸梦学习多样化人形操作
  ko: ''
summary:
  en: ''
  zh: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer
    动作头转成可训练、可复用的末端执行器/腕手目标、动作 chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: ''
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
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (092). Institution: Carnegie Mellon University、UT
    Arlington、Bosch Center for AI、deformable objects (towel folding). B: mixed prehensile
    and non-prehensile manipulation for thin-profile rigid objects with limited grasp.
    Full title: Learning Versatile Humanoid Manipulation with Touch Dreaming.'
sources:
- id: src_001
  type: website
  title: 通过触摸梦学习多样化人形操作 project page
  url: https://humanoid-touch-dream.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过PPO/RL 策略训练、扩散策略/流匹配、MM-DiT/Transformer 动作头转成可训练、可复用的末端执行器/腕手目标、动作 chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
