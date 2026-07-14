---
$id: ent_paper_omniretarget_interaction_prese_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget｜人形全身移动操作和场景交互的交互保存数据生成
  ko: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
summary:
  en: A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references
    to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant
    embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.
    More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential
    for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving
    data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact
    relationships between an agent, the terrain, and manipulated objects. By minimiz
  zh: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- motion_tracking
- omniretarget
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OmniRetarget: Interaction-Preserving
    Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction.'
sources:
- id: src_001
  type: website
  title: OmniRetarget project page
  url: https://omniretarget.github.io
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 核心内容
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 参考
- Semantic Scholar search: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

