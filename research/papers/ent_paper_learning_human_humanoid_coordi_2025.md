---
$id: ent_paper_learning_human_humanoid_coordi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Human-Humanoid Coordination for Collaborative Object Carrying
  zh: COLA｜学习人机协调以协作搬运物体
  ko: ''
summary:
  en: ''
  zh: COLA 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、世界模型/视频预测、闭环纠错/人类干预生成全身轨迹/动作序列、低层控制器目标。关键点是把PPO/RL
    策略训练、世界模型/视频预测放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
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
- cola
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (034). Institution: Department of Electrical
    and Electronic Engineering, the University of Hong Kong、State Key Laboratory of
    General Artificial Intelligence, BIGAI、School of Computer Science and Technology,
    Beijing Institute of Technology、Yuanpei College, Peking University. Full title:
    Learning Human-Humanoid Coordination for Collaborative Object Carrying.'
sources:
- id: src_001
  type: website
  title: COLA project page
  url: https://yushi-du.github.io/COLA/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


COLA 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、世界模型/视频预测、闭环纠错/人类干预生成全身轨迹/动作序列、低层控制器目标。关键点是把PPO/RL 策略训练、世界模型/视频预测放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
