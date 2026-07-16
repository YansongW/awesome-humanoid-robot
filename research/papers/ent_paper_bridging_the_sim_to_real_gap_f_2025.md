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

## Overview
Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance. However, training solely with task rewards introduces two major challenges: these rewards are prone to exploitation (reward hacking), and the exploration process can lack sufficient direction. To address these issues, we propose a two-stage training pipeline. First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world data to bridge the sim-to-real gap for complex actuation mechanisms without requiring access to torque sensing. UAN mitigates reward hacking by ensuring that the learned behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning strategy that leverages reference trajectories as initial hints to guide exploration. With these innovations, our robot athlete learns to lift, throw, and drag with remarkable fidelity from simulation to reality.

## Content
Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance. However, training solely with task rewards introduces two major challenges: these rewards are prone to exploitation (reward hacking), and the exploration process can lack sufficient direction. To address these issues, we propose a two-stage training pipeline. First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world data to bridge the sim-to-real gap for complex actuation mechanisms without requiring access to torque sensing. UAN mitigates reward hacking by ensuring that the learned behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning strategy that leverages reference trajectories as initial hints to guide exploration. With these innovations, our robot athlete learns to lift, throw, and drag with remarkable fidelity from simulation to reality.

## 개요
로봇에서 운동적 위치-조작(loco-manipulation)을 구현하려면 단순히 기준 궤적을 따라 로봇을 안내하는 전통적인 추적 보상(tracking rewards)을 넘어, 진정으로 역동적이고 목표 지향적인 행동을 유도하는 작업 보상(task rewards)으로 전환해야 합니다. "공을 최대한 멀리 던져라" 또는 "무게를 가능한 한 빨리 들어 올려라"와 같은 명령은 로봇이 운동 성능에 내재된 민첩성과 힘을 발휘하도록 강제합니다. 그러나 작업 보상만으로 훈련하면 두 가지 주요 문제가 발생합니다: 이러한 보상은 악용(보상 해킹)되기 쉬우며, 탐색 과정이 충분한 방향성을 갖지 못할 수 있습니다. 이러한 문제를 해결하기 위해 우리는 2단계 훈련 파이프라인을 제안합니다. 첫째, Unsupervised Actuator Net(UAN)을 도입하여 토크 감지에 접근할 필요 없이 실제 데이터를 활용해 복잡한 구동 메커니즘에 대한 시뮬레이션-현실 격차(sim-to-real gap)를 해소합니다. UAN은 학습된 행동이 견고하고 전이 가능하도록 보장하여 보상 해킹을 완화합니다. 둘째, 기준 궤적을 초기 힌트로 활용하여 탐색을 안내하는 사전 훈련 및 미세 조정 전략을 사용합니다. 이러한 혁신을 통해 우리의 로봇 운동선수는 시뮬레이션에서 현실로 놀라운 충실도로 들어 올리기, 던지기, 끌기를 학습합니다.

## 핵심 내용
로봇에서 운동적 위치-조작(loco-manipulation)을 구현하려면 단순히 기준 궤적을 따라 로봇을 안내하는 전통적인 추적 보상(tracking rewards)을 넘어, 진정으로 역동적이고 목표 지향적인 행동을 유도하는 작업 보상(task rewards)으로 전환해야 합니다. "공을 최대한 멀리 던져라" 또는 "무게를 가능한 한 빨리 들어 올려라"와 같은 명령은 로봇이 운동 성능에 내재된 민첩성과 힘을 발휘하도록 강제합니다. 그러나 작업 보상만으로 훈련하면 두 가지 주요 문제가 발생합니다: 이러한 보상은 악용(보상 해킹)되기 쉬우며, 탐색 과정이 충분한 방향성을 갖지 못할 수 있습니다. 이러한 문제를 해결하기 위해 우리는 2단계 훈련 파이프라인을 제안합니다. 첫째, Unsupervised Actuator Net(UAN)을 도입하여 토크 감지에 접근할 필요 없이 실제 데이터를 활용해 복잡한 구동 메커니즘에 대한 시뮬레이션-현실 격차(sim-to-real gap)를 해소합니다. UAN은 학습된 행동이 견고하고 전이 가능하도록 보장하여 보상 해킹을 완화합니다. 둘째, 기준 궤적을 초기 힌트로 활용하여 탐색을 안내하는 사전 훈련 및 미세 조정 전략을 사용합니다. 이러한 혁신을 통해 우리의 로봇 운동선수는 시뮬레이션에서 현실로 놀라운 충실도로 들어 올리기, 던지기, 끌기를 학습합니다.
