---
$id: ent_paper_leverb_humanoid_whole_body_con_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
  zh: LeVERB｜具有潜在视觉语言指令的人形全身控制
  ko: ''
summary:
  en: ''
  zh: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作
    token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: ''
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- contact_planning
- leverb
- mobile_manipulation
- task_planning
- visual_closed_loop
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (122). Institution: University of California
    Berkeley、Norwegian University of Science and Technology、Simon Fraser University、Carnegie
    Mellon University. Full title: LeVERB: Humanoid Whole-Body Control with Latent
    Vision-Language Instruction.'
sources:
- id: src_001
  type: website
  title: LeVERB project page
  url: https://github.com/ember-lab-berkeley/LeVERB-Website
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
