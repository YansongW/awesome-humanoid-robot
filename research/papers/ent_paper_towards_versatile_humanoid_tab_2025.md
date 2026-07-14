---
$id: ent_paper_towards_versatile_humanoid_tab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  zh: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
summary:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- towards_versatile_humanoid_tab
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21690v4.
sources:
- id: src_001
  type: paper
  title: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation (arXiv)'
  url: https://arxiv.org/abs/2509.21690
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing--capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate$\geq$96% and success rate$\geq$92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 核心内容
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing--capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate$\geq$96% and success rate$\geq$92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 参考
- http://arxiv.org/abs/2509.21690v4

