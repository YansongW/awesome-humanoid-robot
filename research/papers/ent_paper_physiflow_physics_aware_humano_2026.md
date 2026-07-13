---
$id: ent_paper_physiflow_physics_aware_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow
    Matching and Robust Tracking'
  zh: PhysiFlow｜通过多脑潜在流匹配和鲁棒跟踪实现物理感知的人形全身VLA
  ko: ''
summary:
  en: ''
  zh: PhysiFlow 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM
    语义规划/路由预测全身轨迹/动作序列、动作 chunk/token。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: ''
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
- physiflow
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (155). Institution: . Full title: PhysiFlow:
    Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and
    Robust Tracking.'
sources:
- id: src_001
  type: website
  title: 'PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent
    Flow Matching and Robust Tracking'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


PhysiFlow 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用扩散策略/流匹配、VLA 多模态动作模型、VLM 语义规划/路由预测全身轨迹/动作序列、动作 chunk/token。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
