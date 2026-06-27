---
$id: ent_paper_gr00t_n1_an_open_foundation_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
  zh: GR00T N1｜通用人形机器人的开放基础模型
  ko: ''
summary:
  en: GR00T N1 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA
    多模态动作模型预测可执行动作命令。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  zh: GR00T N1 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA
    多模态动作模型预测可执行动作命令。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- general_manipulation
- gr00t_n1
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (148). Institution: NVIDIA1. Full title:
    GR00T N1: An Open Foundation Model for Generalist Humanoid Robots.'
sources:
- id: src_001
  type: website
  title: GR00T N1 project page
  url: https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

GR00T N1 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、扩散策略/流匹配、VLA 多模态动作模型预测可执行动作命令。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
