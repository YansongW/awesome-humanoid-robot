---
$id: ent_paper_motionwam_towards_foundation_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation'
  zh: MotionWAM｜迈向实时人形移动操作的基础世界行动模型
  ko: ''
summary:
  en: ''
  zh: MotionWAM 的实现路径是先把相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
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
- motionwam
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (100). Institution: Mondo Robotics、HKUST
    (GZ)、HKUST. Full title: MotionWAM: Towards Foundation World Action Models for
    Real-Time Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: MotionWAM project page
  url: https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


MotionWAM 的实现路径是先把相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
