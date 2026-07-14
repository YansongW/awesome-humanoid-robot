---
$id: ent_paper_torne_reconciling_reality_through_si_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation'
  zh: 通过仿真调和现实：面向稳健操作的实到仿再到实方法
  ko: '시뮬레이션을 통한 현실 조화: 견고한 조작을 위한 Real-to-Sim-to-Real 접근법'
summary:
  en: RialTo builds on-the-fly digital-twin simulations from real-world scans and transfers real-world demonstrations into
    simulation via a novel inverse-distillation procedure, then uses reinforcement learning to robustify imitation-learning
    policies with minimal human supervision.
  zh: RialTo 从真实世界扫描即时构建数字孪生仿真环境，通过一种新颖的逆蒸馏过程将真实世界演示迁移到仿真中，并利用强化学习在最小人类监督下增强模仿学习策略的鲁棒性。
  ko: RialTo는 실제 세계 스캔에서 즉석에서 디지털 트윈 시뮬레이션을 구축하고, 새로운 역증류 절차를 통해 실제 세계 시연을 시뮬레이션으로 전달한 다음, 최소한의 인간 감독으로 모방 학습 정책을 강화하기 위해
    강화 학습을 사용합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- digital_twin
- real_to_sim_to_real
- sim_to_real
- inverse_distillation
- imitation_learning
- reinforcement_learning
- visuomotor_policy
- robust_manipulation
- isaac_sim
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03949v3.
sources:
- id: src_001
  type: paper
  title: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation'
  url: https://arxiv.org/abs/2403.03949
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## 核心内容
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## 参考
- http://arxiv.org/abs/2403.03949v3

