---
$id: ent_paper_handoff_humanoid_agentic_task_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers'
  zh: HANDOFF｜通过精炼补充教师进行人形智能体任务空间全身控制
  ko: 'HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers'
summary:
  en: Handoff transforms ontological states and joint sequences into trackable body targets, and through teacher-student knowledge
    transfer, diffusion strategy/flow matching, VLM semantic planning/routing training, or combined whole-body strategies,
    the HANDOFF can be implemented in the context of multi-agent systems, finally, the whole body trajectory/action sequence
    and low-level controller target are output. The key is to train the teacher's strategy with privileged information and
    distill the ability to use only the student's strategy of deploying observations.
  zh: HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
  notes: 'Imported from WeChat curated list (037). Institution: California Institute of Technology、The Institute for Human
    & Machine Cognition. Full title: HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers.
    English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
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


## 概述
HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
HANDOFF 把本体状态与关节序列转成可跟踪的身体目标，并通过教师-学生知识迁移、扩散策略/流匹配、VLM 语义规划/路由训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

