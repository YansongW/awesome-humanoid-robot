---
$id: ent_paper_hover_versatile_neural_whole_b_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots'
  zh: HOVER｜用于人形机器人的多样化神经全身控制器
  ko: 'HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots'
summary:
  en: HOVER first recovers scene, goal, or motion representations from ontology states and joint sequences, and then uses
    teacher-student knowledge transfer, whole-body controller/WBC/MPC, hierarchical skills/expert strategies to generate whole-body
    trajectories/action sequences, and low-level controller goals. The key point is to train teacher strategies with privileged
    information and then distill the capabilities to the point where only student strategies with deployed observations can
    be used.
  zh: HOVER 先从本体状态与关节序列恢复场景、目标或运动表征，再用教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: HOVER 先从本体状态与关节序列恢复场景、目标或运动表征，再用教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- hover
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (010). Institution: . Full title: HOVER: Versatile Neural Whole-Body Controller
    for Humanoid Robots. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: HOVER project page
  url: https://hover-versatile-humanoid.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
HOVER 先从本体状态与关节序列恢复场景、目标或运动表征，再用教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
HOVER 先从本体状态与关节序列恢复场景、目标或运动表征，再用教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略生成全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

