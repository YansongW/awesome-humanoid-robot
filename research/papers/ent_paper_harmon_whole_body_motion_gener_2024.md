---
$id: ent_paper_harmon_whole_body_motion_gener_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions'
  zh: Harmon｜从语言描述生成人形机器人的全身运动
  ko: ''
summary:
  en: Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  zh: Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: ''
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- harmon
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (097). Institution: The University of
    Texas at Austin、NVIDIA Research. Full title: HARMON: Whole-Body Motion Generation
    of Humanoid Robots from Language Descriptions.'
sources:
- id: src_001
  type: website
  title: Harmon project page
  url: https://ut-austin-rpl.github.io/Harmon/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
