---
$id: ent_paper_holomotion_1_technical_report_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: HoloMotion-1 Technical Report
  zh: HoloMotion｜全身人形控制的基础模型
  ko: ''
summary:
  en: HoloMotion 把人类视频/动捕轨迹转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  zh: HoloMotion 把人类视频/动捕轨迹转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- balance
- behavioral_foundation_model
- holomotion
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (011). Institution: Horizon Robotics.
    Full title: HoloMotion-1 Technical Report.'
sources:
- id: src_001
  type: website
  title: HoloMotion project page
  url: https://horizonrobotics.github.io/robot_lab/holomotion
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

HoloMotion 把人类视频/动捕轨迹转成可跟踪的身体目标，并通过异构动捕与合成平衡数据、扩散策略/流匹配、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
