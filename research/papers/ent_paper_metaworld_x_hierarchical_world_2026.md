---
$id: ent_paper_metaworld_x_hierarchical_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid
    Loco-Manipulation'
  zh: MetaWorld-X｜通过VLM协调的专家进行分层世界建模，用于人形移动操作
  ko: ''
summary:
  en: ''
  zh: MetaWorld-X 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、AMP/运动先验、VLM
    语义规划/路由预测地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- metaworld_x
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (153). Institution: MetaWorld-X: Hierarchical
    World Modeling via VLM-Orchestrated、tasks into human-motion-informed primitives
    and dynamically composes them via semantic routing. Full title: MetaWorld-X: Hierarchical
    World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: MetaWorld-X project page
  url: https://syt2004.github.io/metaworldX/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


MetaWorld-X 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、AMP/运动先验、VLM 语义规划/路由预测地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
