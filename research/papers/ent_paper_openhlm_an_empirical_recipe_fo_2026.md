---
$id: ent_paper_openhlm_an_empirical_recipe_fo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation'
  zh: OpenHLM｜全身人形移动操作的经验配方
  ko: ''
summary:
  en: ''
  zh: OpenHLM 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA
    多模态动作模型预测全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- openhlm
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (154). Institution: Tsinghua University、Shanghai
    Qi Zhi Institute、Spirit AI. Full title: OpenHLM: An Empirical Recipe for Whole-Body
    Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: OpenHLM project page
  url: https://openhlm-project.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


OpenHLM 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
