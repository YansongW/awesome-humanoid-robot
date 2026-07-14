---
$id: ent_paper_bridging_the_sim_to_real_gap_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
  zh: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
  ko: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
summary:
  en: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation is a 2025 work on sim-to-real for humanoid robots.
  zh: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation is a 2025 work on sim-to-real for humanoid robots.
  ko: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation is a 2025 work on sim-to-real for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridging_the_sim_to_real_gap_f
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10894v1.
sources:
- id: src_001
  type: paper
  title: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2502.10894
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance. However, training solely with task rewards introduces two major challenges: these rewards are prone to exploitation (reward hacking), and the exploration process can lack sufficient direction. To address these issues, we propose a two-stage training pipeline. First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world data to bridge the sim-to-real gap for complex actuation mechanisms without requiring access to torque sensing. UAN mitigates reward hacking by ensuring that the learned behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning strategy that leverages reference trajectories as initial hints to guide exploration. With these innovations, our robot athlete learns to lift, throw, and drag with remarkable fidelity from simulation to reality.

## 核心内容
Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance. However, training solely with task rewards introduces two major challenges: these rewards are prone to exploitation (reward hacking), and the exploration process can lack sufficient direction. To address these issues, we propose a two-stage training pipeline. First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world data to bridge the sim-to-real gap for complex actuation mechanisms without requiring access to torque sensing. UAN mitigates reward hacking by ensuring that the learned behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning strategy that leverages reference trajectories as initial hints to guide exploration. With these innovations, our robot athlete learns to lift, throw, and drag with remarkable fidelity from simulation to reality.

## 参考
- http://arxiv.org/abs/2502.10894v1

