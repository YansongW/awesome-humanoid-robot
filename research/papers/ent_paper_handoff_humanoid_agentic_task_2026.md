---
$id: ent_paper_handoff_humanoid_agentic_task_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary
    Teachers'
  zh: HANDOFF｜通过精炼补充教师进行人形智能体任务空间全身控制
  ko: ''
summary:
  en: HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  zh: HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- handoff
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (037). Institution: California Institute
    of Technology、The Institute for Human & Machine Cognition. Full title: HANDOFF:
    Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers.'
sources:
- id: src_001
  type: website
  title: HANDOFF project page
  url: https://lzyang2000.github.io/HANDOFF/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
