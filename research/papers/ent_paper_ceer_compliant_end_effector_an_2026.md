---
$id: ent_paper_ceer_compliant_end_effector_an_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
  zh: CEER｜兼容的末端执行器和根控制作为分层人形移动操作的统一接口
  ko: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
summary:
  en: 'CEER mainly solves the data closed loop: using ontology state and joint sequence, teleoperation/exoskeleton data, and
    simulation interaction data to collect human operation and robot state, and then transform it into trainable and reusable
    whole-body trajectory/action sequence, end effector/wrist target, and low-level controller target through teacher-student
    knowledge transfer, whole-body controller/WBC/MPC, hierarchical skills/expert strategy. The key point is to train teacher
    strategies with privileged information and then distill the capabilities to the point where only student strategies with
    deployed observations can be used.'
  zh: CEER 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: CEER 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- ceer
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (033). Institution: . Full title: CEER: Compliant End-Effector and Root Control
    as a Unified Interface for Hierarchical Humanoid Loco-Manipulation. English name/summary machine-translated from Chinese
    by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: CEER project page
  url: https://robotproject8.github.io/ceer_page/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
CEER 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
CEER 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、分层技能/专家策略转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

