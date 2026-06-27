---
$id: ent_paper_splitadapter_load_aware_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation'
  zh: SplitAdapter｜通过因子化适应进行负载感知的人形移动操作
  ko: ''
summary:
  en: SplitAdapter 把仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  zh: SplitAdapter 把仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- manipulation_interface
- mobile_manipulation
- splitadapter
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (045). Institution: . Full title: SplitAdapter:
    Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation.'
sources:
- id: src_001
  type: website
  title: SplitAdapter project page
  url: https://splitadapter.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

SplitAdapter 把仿真交互数据转成可跟踪的身体目标，并通过PPO/RL 策略训练、扩散策略/流匹配、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
