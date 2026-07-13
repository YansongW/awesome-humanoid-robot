---
$id: ent_paper_langwbc_language_directed_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LangWBC: Language-directed Humanoid Whole-Body Control via End-to-end Learning'
  zh: LangWBC｜通过端到端学习进行语言指导的人形全身控制
  ko: ''
summary:
  en: ''
  zh: LangWBC 先从语言指令、本体状态与关节序列、仿真交互数据恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- language_control
- langwbc
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (098). Institution: University of California,
    Berkeley. Full title: LangWBC: Language-directed Humanoid Whole-Body Control via
    End-to-end Learning.'
sources:
- id: src_001
  type: website
  title: LangWBC project page
  url: https://LangWBC.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


LangWBC 先从语言指令、本体状态与关节序列、仿真交互数据恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
