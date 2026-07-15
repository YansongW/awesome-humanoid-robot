---
$id: ent_paper_mosaic_bridging_the_sim_to_rea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation'
  zh: MOSAIC｜通过快速残差适应，弥合通用人形运动跟踪和远程操作中的模拟与现实世界的差距
  ko: 'MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation'
summary:
  en: 'MOSAIC mainly solves the data closed loop: it uses the body state and joint sequence, teleoperation/exoskeleton data,
    and simulation interaction data to collect human operation and robot states, and then converts them into trainable and
    reusable whole-body trajectory/action sequences and low-level controller targets through diffusion strategy/flow matching.
    The key point is to view action generation as a conditional generation problem and use diffusion or flow matching to sample
    executable trajectories in a multimodal action distribution.'
  zh: MOSAIC 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: MOSAIC 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- locomotion
- mosaic
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (014). Institution: Technical University of Munich, Munich, Germany、Tsinghua University,
    Beijing, China、Nanjing University, Suzhou, China、IO-AI.TECH, Shenzhen, China. Full title: MOSAIC: Bridging the Sim-to-Real
    Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation. English name/summary machine-translated
    from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: MOSAIC project page
  url: https://baai-humanoid.github.io/MOSAIC/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
MOSAIC 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
MOSAIC 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

