---
$id: ent_paper_active_stereo_camera_outperfor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Active Stereo-Camera Outperforms Multi-Sensor Setup in ACT Imitation Learning
    for Humanoid Manipulation
  zh: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置
  ko: ''
summary:
  en: ''
  zh: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过ACT/行为克隆模仿学习、MM-DiT/Transformer
    动作头训练或组合全身策略，最终输出动作 chunk/token。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
  ko: ''
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- act
- deployment
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (143). Institution: Imitation Learning
    for Humanoid Manipulation. Full title: Active Stereo-Camera Outperforms Multi-Sensor
    Setup in ACT Imitation Learning for Humanoid Manipulation.'
sources:
- id: src_001
  type: website
  title: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 project page
  url: http://github.com/kuehnrobin/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过ACT/行为克隆模仿学习、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出动作 chunk/token。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
