---
$id: ent_paper_adversarial_locomotion_and_mot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning
  zh: 用于人形策略学习的对抗性运动和运动模仿
  ko: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning
summary:
  en: ''
  zh: 这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: 这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (054). Institution: Adversarial Locomotion
    and Motion Imitation for、Institute of Artificial Intelligence (TeleAI), China
    Telecom、ShanghaiTech University、University of Science and Technology of China.
    Full title: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning.'
sources:
- id: src_001
  type: website
  title: 用于人形策略学习的对抗性运动和运动模仿 project page
  url: https://almi-humanoid.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
这篇工作主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配、全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
