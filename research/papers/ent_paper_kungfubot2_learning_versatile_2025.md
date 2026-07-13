---
$id: ent_paper_kungfubot2_learning_versatile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
  zh: KungfuBot2｜学习人形全身控制的多样化运动技能
  ko: ''
summary:
  en: ''
  zh: KungfuBot2 把本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、ACT/行为克隆模仿学习、IK/动作重定向训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- kungfubot2
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (013). Institution: . Full title: KungfuBot2:
    Learning Versatile Motion Skills for Humanoid Whole-Body Control.'
sources:
- id: src_001
  type: website
  title: KungfuBot2 project page
  url: https://kungfubot2-humanoid.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


KungfuBot2 把本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据转成可跟踪的身体目标，并通过教师-学生知识迁移、ACT/行为克隆模仿学习、IK/动作重定向训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
