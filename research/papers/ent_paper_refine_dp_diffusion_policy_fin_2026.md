---
$id: ent_paper_refine_dp_diffusion_policy_fin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'REFINE-DP: Diffusion Policy Fine-tuning for Humanoid Loco-manipulation via
    Reinforcement Learning'
  zh: REFINE-DP｜通过强化学习对人形移动操作进行扩散策略微调
  ko: ''
summary:
  en: ''
  zh: REFINE-DP 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、扩散策略/流匹配预测关节位置/力矩命令、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- refine_dp
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (157). Institution: IEEE ROBOTICS AND
    AUTOMATION LETTERS. Full title: REFINE-DP: Diffusion Policy Fine-tuning for Humanoid
    Loco-manipulation via Reinforcement Learning.'
sources:
- id: src_001
  type: website
  title: REFINE-DP project page
  url: https://refine-dp.github.io/REFINE-DP/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


REFINE-DP 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、扩散策略/流匹配预测关节位置/力矩命令、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
