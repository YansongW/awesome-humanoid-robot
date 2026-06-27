---
$id: ent_paper_egoprimo_egocentric_motion_gen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control'
  zh: EgoPriMo｜用于交互式人形控制的第一视角运动生成
  ko: ''
summary:
  en: EgoPriMo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用AMP/运动先验、ACT/行为克隆模仿学习、扩散策略/流匹配预测全身轨迹/动作序列。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  zh: EgoPriMo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用AMP/运动先验、ACT/行为克隆模仿学习、扩散策略/流匹配预测全身轨迹/动作序列。关键点是保留
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
- egoprimo
- generative_motion
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (095). Institution: Tianjin University,
    Tianjin, China、Beihang University, Beijing, China、Zhongguancun Institute of Artificial
    Intelligence, Beijing, China. Full title: EgoPriMo: Egocentric Motion Generation
    for Interactive Humanoid Control.'
sources:
- id: src_001
  type: website
  title: 'EgoPriMo: Egocentric Motion Generation for Interactive Humanoid Control'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

EgoPriMo 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用AMP/运动先验、ACT/行为克隆模仿学习、扩散策略/流匹配预测全身轨迹/动作序列。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
