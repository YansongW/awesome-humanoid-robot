---
$id: ent_paper_wococo_learning_whole_body_hum_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts'
  zh: WoCoCo｜通过顺序接触学习全身人形控制
  ko: ''
summary:
  en: ''
  zh: WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: ''
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_video
- interaction_planning
- motion_capture
- motion_retargeting
- wococo
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (116). Institution: ETH Zurich、⋆Work was
    done at Carnegie Mellon University、Carnegie Mellon University. Full title: WoCoCo:
    Learning Whole-Body Humanoid Control with Sequential Contacts.'
sources:
- id: src_001
  type: website
  title: WoCoCo project page
  url: https://lecar-lab.github.io/wococo/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


WoCoCo 先从本体状态与关节序列、人类视频/动捕轨迹、仿真交互数据恢复场景、目标或运动表征，再用PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配生成全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
