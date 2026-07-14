---
$id: ent_paper_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型
  ko: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
summary:
  en: Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under
    a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid
    characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective
    shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to
    be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile
    and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot
    motion tracking, goal reaching, and reward optimization, and few-sho
  zh: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
- bfm_zero
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BFM-Zero: A Promptable
    Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning.'
sources:
- id: src_001
  type: website
  title: BFM-Zero project page
  url: https://lecar-lab.github.io/BFM-Zero/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 核心内容
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 参考
- Semantic Scholar search: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning

