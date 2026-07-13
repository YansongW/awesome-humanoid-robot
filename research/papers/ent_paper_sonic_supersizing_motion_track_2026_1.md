---
$id: ent_paper_sonic_supersizing_motion_track_2026_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  zh: SONIC｜超大运动跟踪，实现自然人形全身控制
  ko: ''
summary:
  en: ''
  zh: SONIC 的实现路径是先把人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用AMP/运动先验、VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- motion_generation
- sonic
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (103). Institution: NVIDIA. Full title:
    SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control.'
sources:
- id: src_001
  type: website
  title: SONIC project page
  url: https://nvlabs.github.io/GEAR-SONIC/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


SONIC 的实现路径是先把人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用AMP/运动先验、VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
