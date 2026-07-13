---
$id: ent_paper_chip_adaptive_compliance_for_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation'
  zh: CHIP｜通过事后扰动实现人形控制的自适应合规性
  ko: ''
summary:
  en: ''
  zh: CHIP 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过扩散策略/流匹配、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: ''
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
- balance
- behavioral_foundation_model
- chip
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (005). Institution: NVIDIA、Stanford University.
    Full title: CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation.'
sources:
- id: src_001
  type: website
  title: CHIP project page
  url: https://nvlabs.github.io/CHIP/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


CHIP 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过扩散策略/流匹配、分层技能/专家策略训练或组合全身策略，最终输出全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
