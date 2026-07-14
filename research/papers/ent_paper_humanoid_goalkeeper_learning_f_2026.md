---
$id: ent_paper_humanoid_goalkeeper_learning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
  zh: Humanoid｜Goalkeeper 从位置条件任务运动约束中学习
  ko: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
summary:
  en: 'We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios.
    While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical
    challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent
    response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body
    control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object
    interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL
    training via an adversarial scheme. We demonstrate the effective'
  zh: Humanoid 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: Humanoid 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_video
- humanoid
- interaction_planning
- motion_capture
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Humanoid Goalkeeper: Learning
    from Position Conditioned Task-Motion Constraints.'
sources:
- id: src_001
  type: website
  title: Humanoid project page
  url: https://github.com/InternRobotics/Humanoid-Goalkeeper
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 核心内容
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 参考
- Semantic Scholar search: Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints

