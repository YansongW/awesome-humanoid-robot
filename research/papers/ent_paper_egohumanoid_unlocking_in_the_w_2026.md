---
$id: ent_paper_egohumanoid_unlocking_in_the_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric
    Demonstration'
  zh: EgoHumanoid｜通过机器人无关的第一视角示范解锁野外移动操作
  ko: ''
summary:
  en: ''
  zh: EgoHumanoid 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA
    多模态动作模型预测地形/场景表征。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: ''
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- egohumanoid
- mobile_manipulation
- scene_understanding
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (060). Institution: The University of
    Hong Kong、Shanghai Innovation Institute、Beihang University、Robot teleoperation
    data collection is constrained to laboratory environment due to hardware and safety
    limitations, while in-. Full title: EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation
    with Robot-Free Egocentric Demonstration.'
sources:
- id: src_001
  type: website
  title: EgoHumanoid project page
  url: https://github.com/NVlabs/GR00T-WholeBodyControl
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


EgoHumanoid 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型预测地形/场景表征。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
